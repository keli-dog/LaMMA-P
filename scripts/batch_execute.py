#!/usr/bin/env python3
import os, re, subprocess, argparse, csv, sys
from pathlib import Path
from difflib import get_close_matches

def extract_tasks_from_log(log_file):
    tasks = []
    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            m = re.search(r'Processing Task: (.+?): \d+/\d+', line)
            if m: tasks.append(m.group(1).strip())
    return tasks

def find_task_dir(task_name, logs_dir):
    dir_pattern = re.sub(r'[^\w\s]', '', task_name).replace(' ', '_')
    all_dirs = [d.name for d in Path(logs_dir).iterdir()
                if d.is_dir() and '_plans_' in d.name]
    matches = get_close_matches(dir_pattern, all_dirs, n=1, cutoff=0.3)
    return os.path.join(logs_dir, matches[0]) if matches else None

def set_floor_no(floor_no):
    path = 'scripts/execute_plan.py'
    with open(path, 'r') as f: content = f.read()
    with open(path, 'w') as f:
        f.write(re.sub(r'floor_no = \d+', f'floor_no = {floor_no}', content))

def execute_task(task_dir, floor_no, timeout=300):
    task_name = os.path.basename(task_dir)
    if not os.path.exists(os.path.join(task_dir, 'code_plan.py')):
        return 'no_code_plan', {}, 'code_plan.py not found'
    set_floor_no(floor_no)
    try:
        result = subprocess.run(
            [sys.executable, 'scripts/execute_plan.py', '--command', task_name],
            capture_output=True, text=True, timeout=timeout)
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired as e:
        output = (e.stdout or '') + (e.stderr or '')
        output += f'\n[TIMEOUT] 超过 {timeout}秒，强制终止（可能导航死锁/转圈）'
        return 'timeout', {}, output
    metrics = {}
    for key in ['SR', 'TC', 'GCR', 'Exec', 'RU']:
        m = re.search(rf'{key}:([\d.]+)', output)
        metrics[key] = m.group(1) if m else ''
    status = 'success' if metrics.get('SR') else 'failed'
    return status, metrics, output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--floor', type=int, required=True)
    parser.add_argument('--logs-dir', default='./logs')
    parser.add_argument('--output-dir', default='./execution_results')
    parser.add_argument('--timeout', type=int, default=300, help='单任务超时秒数')
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    log_file = f'logs/floorplan_{args.floor}pddl_deepseek.log'
    if not os.path.exists(log_file):
        print(f"[ERROR] {log_file} not found"); return
    tasks = extract_tasks_from_log(log_file)
    print(f"=== Floor {args.floor}: {len(tasks)} tasks, timeout={args.timeout}s ===")
    summary = os.path.join(args.output_dir, f'summary_floor{args.floor}.csv')
    with open(summary, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(['task_name', 'status', 'SR', 'TC', 'GCR', 'Exec', 'RU'])
    ok = 0
    for i, task_name in enumerate(tasks, 1):
        print(f"\n[{i}/{len(tasks)}] {task_name}")
        task_dir = find_task_dir(task_name, args.logs_dir)
        if not task_dir:
            print("  [SKIP] dir not found")
            with open(summary, 'a', newline='', encoding='utf-8') as f:
                csv.writer(f).writerow([task_name, 'dir_not_found', '', '', '', '', ''])
            continue
        dn = os.path.basename(task_dir)
        print(f"  Dir: {dn}")
        status, metrics, output = execute_task(task_dir, args.floor, args.timeout)
        with open(os.path.join(args.output_dir, f'{dn}.log'), 'w', encoding='utf-8') as f:
            f.write(output)
        if status == 'success': ok += 1
        print(f"  {status} | SR={metrics.get('SR','')} GCR={metrics.get('GCR','')} Exec={metrics.get('Exec','')}")
        with open(summary, 'a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([dn, status, metrics.get('SR',''), metrics.get('TC',''),
                metrics.get('GCR',''), metrics.get('Exec',''), metrics.get('RU','')])
    print(f"\n=== Done: {ok}/{len(tasks)} success | {summary} ===")

if __name__ == '__main__':
    main()
