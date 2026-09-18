
for i in range(25):
    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})
    time.sleep(0.1)

task_over = True
time.sleep(5)


exec = float(success_exec) / float(total_exec) if total_exec > 0 else 0.0

print (ground_truth)
objs = list([obj for obj in c.last_event.metadata["objects"]])

def find_obj_in_container(container_obj, target_name, objs, depth=0):
    """递归查找容器内是否包含目标物体（支持内胆嵌套，如 GarbageCan->GarbageBag->Newspaper）"""
    if depth > 2:  # 最多递归2层，避免无限递归
        return False
    if container_obj.get('receptacleObjectIds') is None:
        return False
    # 检查当前层
    for r in container_obj['receptacleObjectIds']:
        if target_name in r:
            return True
    # 递归检查内胆
    for r in container_obj['receptacleObjectIds']:
        for obj in objs:
            if obj['objectId'] == r:
                if find_obj_in_container(obj, target_name, objs, depth + 1):
                    return True
    return False


gcr_tasks = 0.0
gcr_complete = 0.0
for obj_gt in ground_truth:
    obj_name = obj_gt['name']
    state = obj_gt['state']
    contains = obj_gt['contains']
    gcr_tasks += 1
    gt_done = False

    # --- 优先检查 state 类型 ---
    if state is not None and state != '':
        for obj in objs:
            if obj_name in obj["name"]:
                if state == 'SLICED' and obj.get("isSliced", False):
                    gt_done = True
                elif state == 'OFF' and not obj.get("isToggled", True):
                    gt_done = True
                elif state == 'ON' and obj.get("isToggled", False):
                    gt_done = True
                elif state == 'HOT' and obj.get("temperature", "") == 'Hot':
                    gt_done = True
                elif state == 'COOKED' and obj.get("isCooked", False):
                    gt_done = True
                elif state == 'OPENED' and obj.get("isOpen", False):
                    gt_done = True
                elif state == 'CLOSED' and not obj.get("isOpen", True):
                    gt_done = True
                elif state == 'PICKED' and obj.get("isPickedUp", False):
                    gt_done = True
                elif state == 'BROKEN' and obj.get("isBroken", False):
                    gt_done = True

    # --- 再检查 contains 类型（与 state 互斥，避免重复计数）---
    elif len(contains) != 0:
        for obj in objs:
            if obj_name in obj["name"]:
                for rec in contains:
                    if find_obj_in_container(obj, rec, objs):
                        gt_done = True

    if gt_done:
        gcr_complete += 1
    print(f"  [GT] {obj_name} state={state} contains={contains} -> {'OK' if gt_done else 'MISS'}")


sr = 0
tc = 0
if gcr_tasks == 0:
    gcr = 1
else:
    gcr = gcr_complete / gcr_tasks

if gcr == 1.0:
    tc = 1

max_trans += 1
no_trans_gt += 1
print (no_trans_gt, max_trans, no_trans)
if max_trans == no_trans_gt and no_trans_gt == no_trans:
    ru = 1
elif max_trans == no_trans_gt:
    ru = 0
else:
    ru =  (max_trans - no_trans) / (max_trans - no_trans_gt)

if tc == 1 and ru == 1:
    sr = 1

print (f"SR:{sr}, TC:{tc}, GCR:{gcr}, Exec:{exec}, RU:{ru}")

generate_video()
