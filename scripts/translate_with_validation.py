#!/usr/bin/env python3
"""
PDDL → Python 转换 + LLM 验证（独立版本）
针对 floor 15 的10个任务，输出到 plan_to_code_validated/

用法:
  python scripts/translate_with_validation.py \
    --translate-model deepseek-ai/DeepSeek-V3 \
    --validate-model moonshotai/Kimi-K2.7-Code \
    --task-dir logs/Put_apple_in_fridge_and_switch_off_the_light_plans_09-09-2026-18-53-56 \
    --output-dir plan_to_code_validated

  # 批量跑所有 floor15 任务
  python scripts/translate_with_validation.py --batch --floor 15
"""

import os
import sys
import re
import json
import time
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# 添加项目根目录到 path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import openai


# ============================================================
# 1. API 初始化
# ============================================================

def init_client(api_key_file: str = "api_key.txt"):
    """初始化 OpenAI 兼容客户端（SiliconFlow）"""
    key_path = PROJECT_ROOT / api_key_file
    if not key_path.exists():
        # 尝试当前目录
        key_path = Path(api_key_file)
    if not key_path.exists():
        raise FileNotFoundError(f"API key file not found: {api_key_file}")
    api_key = key_path.read_text().strip()
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.siliconflow.cn/v1"
    )
    return client


def query_llm(client, model: str, prompt: str, system: str = "",
               max_tokens: int = 2048, temperature: float = 0.1,
               timeout: int = 120) -> str:
    """调用 LLM，返回文本内容"""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        timeout=timeout
    )
    return response.choices[0].message.content.strip()


# ============================================================
# 2. 场景物体列表提取
# ============================================================

def extract_objects_from_log(log_file: Path) -> str:
    """从 log.txt 提取场景物体列表"""
    if not log_file.exists():
        return ""
    content = log_file.read_text(encoding='utf-8', errors='ignore')
    match = re.search(r'objects\s*=\s*(\[.*?\])', content, re.DOTALL)
    if not match:
        return ""
    try:
        import ast
        objs = ast.literal_eval(match.group(1))
        names = list(set(o['name'] for o in objs if 'name' in o))
        return ', '.join(sorted(names))
    except Exception:
        return ""


# ============================================================
# 3. PDDL → Python 转换 Prompt
# ============================================================

TRANSLATE_SYSTEM = """You are a Robot PDDL to Mimic Format Translator. 
Your task is to translate complete PDDL plans into executable Python code 
following the AI2-THOR controller format. 
Translate the entire plan as a single coherent function."""


def build_translate_prompt(task_description: str, combined_plan: str,
                           objects_list: str) -> str:
    """构建转换 Prompt（复用 plantocode 的12条规则 + few-shot）"""
    return f"""# CRITICAL INSTRUCTION: DO NOT REDEFINE AI2-THOR FUNCTIONS
# The following AI2-THOR functions are ALREADY DEFINED and available:
# - GoToObject(robot, object_name)
# - PickupObject(robot, object_name)
# - PutObject(robot, object_name, target_location)
# - SwitchOn(robot, object_name)
# - SwitchOff(robot, object_name)
# - SliceObject(robot, object_name)
# - BreakObject(robot, object_name)
# - CleanObject(robot, object_name)
# - ThrowObject(robot, object_name)
# - OpenObject(robot, object_name)
# - CloseObject(robot, object_name)
# - time.sleep(seconds)
#
# Available objects in this scene (use ONLY these exact names):
# {objects_list}
#
# === STRICT RULES ===
# 1. Output ONLY executable Python code. NO comments, NO explanations, NO markdown.
# 2. Use ONLY the function names listed above.
# 3. Use ONLY object names from the available objects list above.
# 4. NEVER use time.sleep to simulate actions - use the actual action functions.
# 5. DO NOT redefine any function. Use them directly.
# 6. SINGLE-HAND RULE: An agent can hold only ONE object at a time. PickupObject fails if hand is not empty. Put down current object first if needed.
# 7. SliceObject/BreakObject/CleanObject act on objects IN THE SCENE - do NOT PickupObject first. Just GoToObject then SliceObject/BreakObject/CleanObject directly.
# 8. PutObject requires the agent to be HOLDING that object. Only put down what you picked up.
# 9. FIXED objects (CounterTop, Floor, Wall, SinkBasin, StoveBurner, Faucet, LightSwitch, Window) CANNOT be picked up.
# 10. Always GoToObject before PickupObject/PutObject/SliceObject/SwitchOn/OpenObject.
# 11. PutObject target must be a receptacle (CounterTop, Sink, Fridge, Drawer, Plate, Bowl, Box, GarbageCan, Microwave, CoffeeMachine, etc.).
# 12. After SliceObject, the sliced object stays in place - do NOT try to pick it up and put it down again.
# 13. OPEN-BEFORE-PUT RULE: If target is an openable receptacle (Fridge, Microwave, Drawer, Cabinet), you MUST OpenObject first, then PutObject, then CloseObject.
# 14. ROBOT PARAMETER RULE: Always use robots[0], robots[1], etc. NEVER pass the raw 'robots' list to action functions.

# Example: Complete PDDL Plan Translation with Multi-Robot Coordination
Task: Wash multiple vegetables (apple, tomato, lettuce, potato)
Complete PDDL Plan: (define (problem wash_vegetables) ... )

def wash_apple(robots):
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'Sink')
    PutObject(robots[0], 'Apple', 'Sink')
    SwitchOn(robots[0], 'Faucet')
    time.sleep(5)
    SwitchOff(robots[0], 'Faucet')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Apple', 'CounterTop')

def wash_tomato(robots):
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Sink')
    PutObject(robots[1], 'Tomato', 'Sink')
    SwitchOn(robots[1], 'Faucet')
    time.sleep(5)
    SwitchOff(robots[1], 'Faucet')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Tomato', 'CounterTop')

task1_thread = threading.Thread(target=wash_apple, args=(robots,))
task2_thread = threading.Thread(target=wash_tomato, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()
action_queue.append({{'action':'Done'}})
action_queue.append({{'action':'Done'}})
task_over = True
time.sleep(5)

# Now translate the following complete plan:
Task: {task_description}
Complete PDDL Plan: {combined_plan}

# IMPORTANT: Generate code that follows the EXACT structure above
def execute_task():
    # Complete plan execution for: {task_description}
"""


# ============================================================
# 4. LLM 验证 Prompt
# ============================================================

VALIDATE_SYSTEM = """You are a strict Python code validator for AI2-THOR robot execution.
You check if generated code would actually run without errors and without logical mistakes.
Be thorough and unforgiving — missing any issue means the robot will crash in simulation."""


def build_validate_prompt(code: str, task_description: str,
                          objects_list: str) -> str:
    """构建验证 Prompt —— 比原 plantocode 的验证更严格"""
    return f"""You are validating Python code generated from a PDDL plan for AI2-THOR simulation.

Task: "{task_description}"

Scene objects (only these exist): {objects_list}

Available AI2-THOR functions (these are already imported, DO NOT redefine):
- GoToObject(robot, object_name)
- PickupObject(robot, object_name)
- PutObject(robot, object_name, target_location)
- SwitchOn(robot, object_name)
- SwitchOff(robot, object_name)
- SliceObject(robot, object_name)
- BreakObject(robot, object_name)
- CleanObject(robot, object_name)
- ThrowObject(robot, object_name)
- OpenObject(robot, object_name)
- CloseObject(robot, object_name)
- time.sleep(seconds)

Available variables (already defined):
- robots: list of robot objects, access as robots[0], robots[1], robots[2]
- action_queue: list, append {{'action':'Done'}} when done
- task_over: boolean, set to True when all tasks done

=== CHECKLIST (go through EVERY item) ===

【语法检查】
1. Python 语法是否正确？有无缩进错误、括号不匹配？
2. 是否引用了未定义的变量或函数？
3. 是否重新定义了 AI2-THOR 函数（def GoToObject 等）？

【参数检查 —— 最常见错误】
4. 所有动作函数的第一个参数是否是 robots[0]/robots[1]/robots[2]？
   ❌ 错误: GoToObject(robots, 'Apple')  ← 传了列表
   ✅ 正确: GoToObject(robots[0], 'Apple')
5. threading.Thread 的 args 是否是 (robots,) 而不是 (robots[0],)？
6. 函数定义的参数名是否是 robots（不是 robot）？

【物体检查】
7. 所有物体名是否在场景物体列表中？有无编造不存在的物体？
8. 固定物体（CounterTop, Floor, Wall, SinkBasin, StoveBurner, Faucet, LightSwitch, Window）是否被 PickupObject 了？

【物理约束检查】
9. 单手规则：PickupObject 之前手上是否为空？有无连续 PickupObject 不 PutObject？
10. 容器规则：往 Fridge/Microwave/Drawer/Cabinet 放东西前是否 OpenObject 了？放完是否 CloseObject？
11. PutObject 之前是否 PickupObject 了该物体？
12. SliceObject/BreakObject/CleanObject 之前是否错误地 PickupObject 了目标物体？（应该直接切，不需先拿）

【线程检查】
13. 是否所有线程都 start() 了？
14. 是否所有线程都 join() 了？
15. 是否在所有线程 join() 之后才设置 task_over = True？
16. action_queue.append 的数量是否等于线程数？

【逻辑检查】
17. 动作顺序是否合理？（GoTo → Pickup → GoTo → Put）
18. 是否有死循环或不可能完成的动作序列？

Code to validate:
```python
{code}
```

Respond in EXACTLY this format:
VALID: true/false
ISSUE_COUNT: N
ISSUES:
- [Category] Issue 1 description (line: approximate location)
- [Category] Issue 2 description
SUGGESTIONS:
- Fix 1: specific code change
- Fix 2: specific code change

If no issues:
VALID: true
ISSUE_COUNT: 0
ISSUES:
SUGGESTIONS:
"""


def parse_validation_response(response: str) -> Tuple[bool, int, List[str], List[str]]:
    """解析验证响应"""
    is_valid = False
    issue_count = 0
    issues = []
    suggestions = []

    lines = response.strip().split('\n')
    section = None
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('VALID:'):
            is_valid = stripped.split(':', 1)[1].strip().lower() == 'true'
        elif stripped.startswith('ISSUE_COUNT:'):
            try:
                issue_count = int(stripped.split(':', 1)[1].strip())
            except ValueError:
                pass
        elif stripped.startswith('ISSUES:'):
            section = 'issues'
            continue
        elif stripped.startswith('SUGGESTIONS:'):
            section = 'suggestions'
            continue
        elif stripped.startswith('-') and section:
            item = stripped[1:].strip()
            if section == 'issues':
                issues.append(item)
            elif section == 'suggestions':
                suggestions.append(item)

    return is_valid, issue_count, issues, suggestions


# ============================================================
# 5. 修复 Prompt
# ============================================================

FIX_SYSTEM = """You are a Python code fixer for AI2-THOR robot execution.
Fix the code based on the validation issues. Return ONLY the corrected code."""


def build_fix_prompt(code: str, issues: List[str], suggestions: List[str],
                     task_description: str, objects_list: str) -> str:
    """构建修复 Prompt"""
    issues_text = '\n'.join(f'- {i}' for i in issues) if issues else '(none)'
    suggestions_text = '\n'.join(f'- {s}' for s in suggestions) if suggestions else '(none)'

    return f"""Fix the following AI2-THOR Python code based on validation issues.

Task: {task_description}
Scene objects: {objects_list}

Issues found:
{issues_text}

Suggestions:
{suggestions_text}

Rules:
- Use robots[0], robots[1], etc. NEVER pass raw 'robots' list to action functions
- OpenObject before PutObject into Fridge/Microwave/Drawer/Cabinet, then CloseObject
- Single hand: only hold one object at a time
- Only use objects from the scene list
- Do NOT redefine AI2-THOR functions
- Return ONLY the corrected Python code, no explanations, no markdown

Original code:
```python
{code}
```

Corrected code:
"""


# ============================================================
# 6. 确定性代码检查（补充 LLM 验证）
# ============================================================

def deterministic_check(code: str, objects_list: str) -> List[str]:
    """确定性检查，补充 LLM 验证可能漏检的问题"""
    issues = []

    # 检查1: GoToObject(robots,  传列表
    if re.search(r'GoToObject\(\s*robots\s*,', code):
        issues.append("[Deterministic] GoToObject 传了 robots 列表，应为 robots[0]/robots[1]")
    if re.search(r'PickupObject\(\s*robots\s*,', code):
        issues.append("[Deterministic] PickupObject 传了 robots 列表，应为 robots[0]/robots[1]")
    if re.search(r'PutObject\(\s*robots\s*,', code):
        issues.append("[Deterministic] PutObject 传了 robots 列表，应为 robots[0]/robots[1]")
    if re.search(r'SwitchOn\(\s*robots\s*,', code):
        issues.append("[Deterministic] SwitchOn 传了 robots 列表，应为 robots[0]/robots[1]")
    if re.search(r'SwitchOff\(\s*robots\s*,', code):
        issues.append("[Deterministic] SwitchOff 传了 robots 列表，应为 robots[0]/robots[1]")
    if re.search(r'SliceObject\(\s*robots\s*,', code):
        issues.append("[Deterministic] SliceObject 传了 robots 列表，应为 robots[0]/robots[1]")
    if re.search(r'OpenObject\(\s*robots\s*,', code):
        issues.append("[Deterministic] OpenObject 传了 robots 列表，应为 robots[0]/robots[1]")
    if re.search(r'CloseObject\(\s*robots\s*,', code):
        issues.append("[Deterministic] CloseObject 传了 robots 列表，应为 robots[0]/robots[1]")

    # 检查2: 重新定义了 AI2-THOR 函数
    for func in ['GoToObject', 'PickupObject', 'PutObject', 'SwitchOn', 'SwitchOff',
                 'SliceObject', 'BreakObject', 'CleanObject', 'ThrowObject',
                 'OpenObject', 'CloseObject']:
        if re.search(rf'def\s+{func}\s*\(', code):
            issues.append(f"[Deterministic] 重新定义了 {func}，该函数已导入")

    # 检查3: 物体名是否在场景列表中
    if objects_list:
        scene_objects = set(o.strip() for o in objects_list.split(','))
        # 提取代码中引用的物体名（字符串字面量）
        code_objects = set(re.findall(r"['\"]([A-Z][a-zA-Z]+)['\"]", code))
        fixed_objects = {'CounterTop', 'Floor', 'Wall', 'SinkBasin', 'StoveBurner',
                         'Faucet', 'LightSwitch', 'Window', 'Sink', 'Fridge',
                         'Microwave', 'Drawer', 'Cabinet', 'GarbageCan', 'Plate',
                         'Bowl', 'Box', 'CoffeeMachine', 'StoveKnob', 'Toaster',
                         'Kettle', 'Pan', 'Pot'}
        for obj in code_objects:
            if obj not in scene_objects and obj not in fixed_objects:
                issues.append(f"[Deterministic] 物体 '{obj}' 不在场景物体列表中")

    # 检查4: 单手冲突（连续 PickupObject 无 PutObject/DropHandObject）
    # 简单检查：同一个机器人的 PickupObject 之间是否有 PutObject
    robot_blocks = re.split(r'(def\s+\w+\(robots\))', code)
    for block in robot_blocks:
        pickups = len(re.findall(r'PickupObject\(robots\[(\d)\]', block))
        puts = len(re.findall(r'PutObject\(robots\[\d\]', block))
        drops = len(re.findall(r'DropHandObject\(robots\[\d\]', block))
        if pickups > puts + drops + 1:  # +1 因为最后可能拿着
            issues.append(f"[Deterministic] 疑似单手冲突: PickupObject({pickups}次) > PutObject+Drop({puts+drops}次)")

    return issues


# ============================================================
# 7. 主流程：单个任务转换+验证
# ============================================================

def process_task(task_dir: Path, output_dir: Path, client,
                 translate_model: str, validate_model: str,
                 max_fix_rounds: int = 2) -> Dict:
    """处理单个任务：转换 → 验证 → 修复 → 保存"""
    task_name = task_dir.name
    print(f"\n{'='*60}")
    print(f"处理任务: {task_name}")
    print(f"{'='*60}")

    # 读取输入
    log_file = task_dir / "log.txt"
    pddl_file = task_dir / "code_planpddl.py"

    if not log_file.exists():
        return {"task": task_name, "status": "skip", "reason": "log.txt not found"}
    if not pddl_file.exists():
        return {"task": task_name, "status": "skip", "reason": "code_planpddl.py not found"}

    task_description = log_file.read_text(encoding='utf-8', errors='ignore').split('\n')[0].strip()
    combined_plan = pddl_file.read_text(encoding='utf-8', errors='ignore')
    objects_list = extract_objects_from_log(log_file)

    print(f"  任务描述: {task_description}")
    print(f"  场景物体: {objects_list[:80]}...")
    print(f"  PDDL 长度: {len(combined_plan)} chars")

    # 创建输出目录
    task_output = output_dir / task_name
    task_output.mkdir(parents=True, exist_ok=True)

    # 保存输入快照
    (task_output / "input_task.txt").write_text(task_description, encoding='utf-8')
    (task_output / "input_pddl.txt").write_text(combined_plan, encoding='utf-8')
    (task_output / "input_objects.txt").write_text(objects_list, encoding='utf-8')

    # ---- 阶段1: 转换 ----
    print(f"\n  [1/3] 转换中 (模型: {translate_model})...")
    t0 = time.time()
    translate_prompt = build_translate_prompt(task_description, combined_plan, objects_list)
    try:
        code = query_llm(client, translate_model, translate_prompt,
                        system=TRANSLATE_SYSTEM, max_tokens=2048, temperature=0.1)
        # 清理 markdown
        code = code.strip()
        if code.startswith('```python'):
            code = code[9:]
        if code.startswith('```'):
            code = code[3:]
        if code.endswith('```'):
            code = code[:-3]
        code = code.strip()
        translate_time = time.time() - t0
        print(f"  ✓ 转换完成 ({translate_time:.1f}s), 代码长度: {len(code)} chars")
    except Exception as e:
        print(f"  ✗ 转换失败: {e}")
        return {"task": task_name, "status": "translate_error", "error": str(e)}

    (task_output / "code_v0_raw.py").write_text(code, encoding='utf-8')

    # ---- 阶段2: 验证（多轮）----
    all_issues_history = []
    current_code = code

    for round_num in range(max_fix_rounds + 1):
        print(f"\n  [2/3] 验证轮次 {round_num + 1} (模型: {validate_model})...")

        # LLM 验证
        t0 = time.time()
        validate_prompt = build_validate_prompt(current_code, task_description, objects_list)
        try:
            val_response = query_llm(client, validate_model, validate_prompt,
                                    system=VALIDATE_SYSTEM, max_tokens=1024, temperature=0.0)
            validate_time = time.time() - t0
            is_valid, issue_count, issues, suggestions = parse_validation_response(val_response)
        except Exception as e:
            print(f"  ✗ 验证失败: {e}")
            is_valid, issue_count, issues, suggestions = False, 0, [f"LLM error: {e}"], []
            validate_time = time.time() - t0

        # 确定性检查
        det_issues = deterministic_check(current_code, objects_list)
        all_issues = issues + det_issues
        all_issue_count = len(all_issues)

        print(f"  LLM验证: VALID={is_valid}, 问题数={issue_count} ({validate_time:.1f}s)")
        print(f"  确定性检查: 问题数={len(det_issues)}")
        for iss in all_issues:
            print(f"    - {iss}")

        # 保存验证报告
        report = f"""验证轮次: {round_num + 1}
验证模型: {validate_model}
LLM VALID: {is_valid}
LLM 问题数: {issue_count}
确定性检查问题数: {len(det_issues)}
总问题数: {all_issue_count}

=== LLM 发现的问题 ===
{chr(10).join('- ' + i for i in issues) if issues else '(none)'}

=== 确定性检查发现的问题 ===
{chr(10).join('- ' + i for i in det_issues) if det_issues else '(none)'}

=== 修复建议 ===
{chr(10).join('- ' + s for s in suggestions) if suggestions else '(none)'}

=== LLM 原始响应 ===
{val_response if 'val_response' in dir() else '(N/A)'}
"""
        (task_output / f"validation_round{round_num + 1}.txt").write_text(report, encoding='utf-8')
        all_issues_history.append({
            "round": round_num + 1,
            "llm_valid": is_valid,
            "llm_issues": issues,
            "deterministic_issues": det_issues,
            "suggestions": suggestions
        })

        # 如果没有问题，验证通过
        if all_issue_count == 0:
            print(f"\n  ✓ 验证通过！")
            break

        # 如果还有问题且还有修复轮次，修复
        if round_num < max_fix_rounds:
            print(f"\n  [3/3] 修复中...")
            t0 = time.time()
            fix_prompt = build_fix_prompt(current_code, all_issues, suggestions,
                                          task_description, objects_list)
            try:
                fixed_code = query_llm(client, validate_model, fix_prompt,
                                      system=FIX_SYSTEM, max_tokens=2048, temperature=0.0)
                fixed_code = fixed_code.strip()
                if fixed_code.startswith('```python'):
                    fixed_code = fixed_code[9:]
                if fixed_code.startswith('```'):
                    fixed_code = fixed_code[3:]
                if fixed_code.endswith('```'):
                    fixed_code = fixed_code[:-3]
                fixed_code = fixed_code.strip()
                fix_time = time.time() - t0
                print(f"  ✓ 修复完成 ({fix_time:.1f}s)")
                (task_output / f"code_v{round_num + 1}_fixed.py").write_text(fixed_code, encoding='utf-8')
                current_code = fixed_code
            except Exception as e:
                print(f"  ✗ 修复失败: {e}")
                break
        else:
            print(f"\n  ⚠ 达到最大修复轮次，仍有 {all_issue_count} 个问题")

    # ---- 保存最终结果 ----
    (task_output / "code_plan_final.py").write_text(current_code, encoding='utf-8')

    summary = {
        "task": task_name,
        "task_description": task_description,
        "translate_model": translate_model,
        "validate_model": validate_model,
        "translate_time": translate_time,
        "final_valid": all_issue_count == 0,
        "final_issue_count": all_issue_count,
        "validation_rounds": round_num + 1,
        "issues_history": all_issues_history,
        "output_dir": str(task_output)
    }
    (task_output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"\n  最终结果: VALID={all_issue_count == 0}, 问题数={all_issue_count}, 轮次={round_num + 1}")
    print(f"  输出目录: {task_output}")
    return summary


# ============================================================
# 8. 批量处理
# ============================================================

def get_floor15_tasks(logs_dir: Path) -> List[Path]:
    """获取 floor 15 的10个任务目录"""
    tasks = []
    for d in sorted(logs_dir.iterdir()):
        if d.is_dir() and d.name.endswith("_09-09-2026-18-53-56"):
            tasks.append(d)
    return tasks


def main():
    parser = argparse.ArgumentParser(description="PDDL→Python 转换 + LLM 验证（独立版本）")
    parser.add_argument("--translate-model", default="deepseek-ai/DeepSeek-V3",
                       help="转换模型")
    parser.add_argument("--validate-model", default="moonshotai/Kimi-K2.7-Code",
                       help="验证模型")
    parser.add_argument("--task-dir", help="单个任务目录")
    parser.add_argument("--batch", action="store_true", help="批量处理 floor15 所有任务")
    parser.add_argument("--floor", type=int, default=15, help="floor plan 编号")
    parser.add_argument("--logs-dir", default="logs", help="logs 目录")
    parser.add_argument("--output-dir", default="plan_to_code_validated", help="输出目录")
    parser.add_argument("--max-fix-rounds", type=int, default=2, help="最大修复轮次")
    parser.add_argument("--api-key-file", default="api_key.txt", help="API key 文件")
    args = parser.parse_args()

    client = init_client(args.api_key_file)
    output_dir = PROJECT_ROOT / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    logs_dir = PROJECT_ROOT / args.logs_dir

    if args.batch:
        tasks = get_floor15_tasks(logs_dir)
        print(f"批量模式: 找到 {len(tasks)} 个任务")
    elif args.task_dir:
        tasks = [Path(args.task_dir)]
    else:
        print("请指定 --task-dir 或 --batch")
        sys.exit(1)

    results = []
    for task_dir in tasks:
        result = process_task(task_dir, output_dir, client,
                             args.translate_model, args.validate_model,
                             args.max_fix_rounds)
        results.append(result)

    # 汇总
    print(f"\n{'='*60}")
    print("汇总")
    print(f"{'='*60}")
    valid_count = sum(1 for r in results if r.get("final_valid"))
    print(f"总任务数: {len(results)}")
    print(f"验证通过: {valid_count}")
    print(f"验证失败: {len(results) - valid_count}")

    # 保存汇总
    summary_file = output_dir / "batch_summary.json"
    summary_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"\n汇总已保存: {summary_file}")

    # 打印表格
    print(f"\n{'任务':<50} {'通过':<6} {'问题数':<8} {'轮次':<6}")
    print("-" * 75)
    for r in results:
        name = r.get("task", "?")[:48]
        valid = "✓" if r.get("final_valid") else "✗"
        issues = r.get("final_issue_count", "?")
        rounds = r.get("validation_rounds", "?")
        print(f"{name:<50} {valid:<6} {str(issues):<8} {str(rounds):<6}")


if __name__ == "__main__":
    main()
