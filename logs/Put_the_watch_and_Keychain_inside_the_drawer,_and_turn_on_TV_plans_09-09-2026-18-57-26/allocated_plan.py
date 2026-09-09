### SOLUTION

#### Analysis:
1. **Robot Capabilities**: All three robots have identical skill sets including all required skills (GoToObject, PickupObject, OpenObject, PutObject, CloseObject, SwitchOn). Their mass capacities are sufficient for all objects (max object mass is 28.3 for ArmChair, while robots have mass capacity of 100).

2. **Task Parallelization**: 
   - Storing watch and keychain can be parallelized since they're independent operations
   - TV activation is completely independent and can run in parallel

3. **Optimized Allocation**:
   - Robot1: Handle watch storage
   - Robot2: Handle keychain storage
   - Robot3: Handle TV activation

#### Detailed Allocation:

**SubTask 1: Store Watch in Drawer (Robot1)**
1. GoToObject(Watch)
2. PickupObject(Watch)
3. GoToObject(Drawer)
4. OpenObject(Drawer)
5. PutObject(Watch, Drawer)

**SubTask 2: Store Keychain in Drawer (Robot2)**
1. GoToObject(Keychain)
2. PickupObject(Keychain)
3. GoToObject(Drawer)
4. Wait for drawer to be opened (if not already open)
5. PutObject(Keychain, Drawer)
6. CloseObject(Drawer) [after both items are stored]

**SubTask 3: Turn on TV (Robot3)**
1. GoToObject(TV)
2. SwitchOn(TV)

#### Execution Flow:
- All three robots can start simultaneously
- Robot1 and Robot2 will coordinate on drawer operations:
  - First robot to reach drawer opens it
  - Last robot to finish storing items closes it
- Robot3 operates completely independently

#### Benefits:
- Maximum parallelization (all three robots utilized)
- No skill gaps (all robots have required skills)
- No mass constraints violated
- Drawer operations properly sequenced through natural coordination

#### Alternative Consideration:
If we wanted to use only 2 robots:
- Robot1 could handle both watch and keychain sequentially
- Robot2 could handle TV
But this would be slower than using all three robots.

The proposed 3-robot solution is optimal given the available resources.