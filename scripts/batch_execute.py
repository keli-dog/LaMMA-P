#!/usr/bin/env python3
import os, re, subprocess, argparse, csv, sys, time, signal
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

def execute_task(task_dir, floor_no, log_path, timeout=300):
    """用 Popen 实时读取输出，边跑边写日志，超时 kill"""
    task_name = os.path.basename(task_dir)
    if not os.path.exists(os.path.join(task_dir, 'code_plan.py')):
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write('[ERROR] code_plan.py not found\n')
        return 'no_code_plan', {}

    set_floor_no(floor_no)
    cmd = [sys.executable, 'scripts/execute_plan.py', '--command', task_name]

    with open(log_path, 'w', encoding='utf-8') as logf:
        logf.write(f"=== START {time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        logf.write(f"CMD: {' '.join(cmd)}\n")
        logf.write(f"floor_no: {floor_no}\n")
        logf.write("=" * 60 + "\n\n")
        logf.flush()

        try:
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1, env={**os.environ, 'PYTHONUNBUFFERED': '1'})
        except Exception as e:
            logf.write(f"[POPEN ERROR] {e}\n")
            return 'launch_error', {}

        output_lines = []
        start = time.time()
        try:
            for line in proc.stdout:
                logf.write(line)
                logf.flush()
                output_lines.append(line)
                # 同时打印到控制台（tmux 里能看到）
                print(f"    {line.rstrip()}")
            proc.wait(timeout=max(1, timeout - (time.time() - start)))
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            msg = f"\n[TIMEOUT] 超过 {timeout}秒，强制终止（可能导航死锁/转圈）\n"
            logf.write(msg)
            print(msg)
            output_lines.append(msg)
        except Exception as e:
            proc.kill()
            msg = f"\n[EXCEPTION] {type(e).__name__}: {e}\n"
            logf.write(msg)
            print(msg)
            output_lines.append(msg)

        output = ''.join(output_lines)
        logf.write(f"\n=== END {time.strftime('%Y-%m-%d %H:%M:%S')} (exit={proc.returncode}) ===\n")

    metrics = {}
    for key in ['SR', 'TC', 'GCR', 'Exec', 'RU']:
        m = re.search(rf'{key}:([\d.]+)', output)
        metrics[key] = m.group(1) if m else ''
    status = 'success' if metrics.get('SR') else ('timeout' if 'TIMEOUT' in output else 'failed')
    return status, metrics

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
        log_path = os.path.join(args.output_dir, f'{dn}.log')
        status, metrics = execute_task(task_dir, args.floor, log_path, args.timeout)
        if status == 'success': ok += 1
        print(f"  >> {status} | SR={metrics.get('SR','')} GCR={metrics.get('GCR','')} Exec={metrics.get('Exec','')}")
        with open(summary, 'a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([dn, status, metrics.get('SR',''), metrics.get('TC',''),
                metrics.get('GCR',''), metrics.get('Exec',''), metrics.get('RU','')])
    print(f"\n=== Done: {ok}/{len(tasks)} success | {summary} ===")

if __name__ == '__main__':
    main()
