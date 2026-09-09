### SOLUTION

#### Analysis of Robots and Tasks:
1. **Robot Capabilities**: All three robots have identical skill sets and mass capacities (100kg), making them fully interchangeable for all tasks.
2. **Task Parallelization**: The five subtasks can be executed in parallel where possible, with some dependencies:
   - SubTask 5 (lights) should be last
   - SubTasks 1-4 can run in parallel

#### Optimal Allocation:
We'll use all three robots to maximize parallelization:

**Robot1 Assignment:**
- **SubTask 1**: Store perishables in fridge
  - Sequence: Pickup Egg → Put in Fridge → Pickup Milk → Put in Fridge
  - Skills needed: GoToObject, PickupObject, PutObject, OpenObject, CloseObject
  - Mass considerations: All objects < 1kg (well below capacity)

**Robot2 Assignment:**
- **SubTask 2**: Clean and store dishes
  - Sequence: Clean Plate → Store in Cabinet → Clean Cup → Store in Cabinet
  - Skills needed: GoToObject, PickupObject, PutObject, OpenObject, CloseObject
  - Mass considerations: All dishes < 1kg

**Robot3 Assignment:**
- **SubTask 3**: Turn off appliances
  - Sequence: SwitchOff CoffeeMachine → SwitchOff Microwave → SwitchOff Toaster
  - Skills needed: GoToObject, SwitchOff
- **SubTask 4**: Close cabinets/drawers
  - Sequence: Close all open cabinets and drawers
  - Skills needed: GoToObject, CloseObject

**Final Task (SubTask 5):**
- Any available robot can handle turning off lights after completing their primary tasks
- Robot3 is best positioned as it finishes appliance shutdown first

#### Execution Plan:
1. **Phase 1 (Parallel Execution):**
   - Robot1: Starts storing perishables
   - Robot2: Begins dish cleaning/storage
   - Robot3: Turns off appliances then closes cabinets

2. **Phase 2 (Sequential):**
   - First available robot (likely Robot3) turns off lights after confirming:
     - All food is stored (Robot1 done)
     - All dishes put away (Robot2 done)
     - All appliances off (Robot3 done)
     - All cabinets closed (Robot3 done)

#### Verification:
- Each robot confirms completion of its assigned subtasks
- Final light switch-off serves as system-wide completion signal

#### Benefits:
- Maximizes parallel execution with three robots
- All mass constraints satisfied (objects << robot capacity)
- All skill requirements met by every robot
- Logical task ordering maintained
- Efficient use of available robotic resources

This allocation completes the "Secure the Kitchen" task in minimal time while satisfying all constraints. The identical robot capabilities allow for flexible reassignment if any robot encounters issues during execution.