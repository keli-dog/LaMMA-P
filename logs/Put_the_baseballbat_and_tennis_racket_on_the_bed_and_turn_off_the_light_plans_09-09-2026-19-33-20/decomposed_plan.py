Here's the task decomposition for putting the baseball bat and tennis racket on the bed and turning off the light:

### GENERAL TASK DECOMPOSITION
We can identify three independent subtasks that can be parallelized:
1. SubTask 1: Put the baseball bat on the bed (Skills: GoToObject, PickupObject, PutObject)
2. SubTask 2: Put the tennis racket on the bed (Skills: GoToObject, PickupObject, PutObject)
3. SubTask 3: Turn off the light (Skills: GoToObject, SwitchOff)

SubTasks 1 and 2 can be performed in parallel by different robots since they involve different objects but the same destination (bed). SubTask 3 is completely independent and can be done simultaneously.

### Action Sequence for Each Subtask

#### SubTask 1: Put Baseball Bat on Bed
Initial conditions:
1. Robot not holding baseball bat
2. Robot not at baseball bat location
3. Robot not at bed location

Action sequence:
1. GoToObject(Robot, BaseballBat)
   - Parameters: ?robot - robot, ?BaseballBat - object
   - Preconditions: (not (inaction Robot))
   - Effects: (at Robot BaseballBat), (not (inaction Robot))

2. PickupObject(Robot, BaseballBat, BaseballBatLocation)
   - Parameters: ?robot - robot, ?BaseballBat - object, ?BaseballBatLocation - object
   - Preconditions: (at-location BaseballBat BaseballBatLocation), (at Robot BaseballBatLocation), (not (inaction Robot))
   - Effects: (holding Robot BaseballBat), (not (inaction Robot))

3. GoToObject(Robot, Bed)
   - Parameters: ?robot - robot, ?Bed - object
   - Preconditions: (not (inaction Robot))
   - Effects: (at Robot Bed), (not (inaction Robot))

4. PutObject(Robot, BaseballBat, Bed)
   - Parameters: ?robot - robot, ?BaseballBat - object, ?Bed - object
   - Preconditions: (holding Robot BaseballBat), (at Robot Bed), (not (inaction Robot))
   - Effects: (at-location BaseballBat Bed), (not (holding Robot BaseballBat)), (not (inaction Robot))

#### SubTask 2: Put Tennis Racket on Bed
Initial conditions:
1. Robot not holding tennis racket
2. Robot not at tennis racket location
3. Robot not at bed location

Action sequence:
1. GoToObject(Robot, TennisRacket)
   - Parameters: ?robot - robot, ?TennisRacket - object
   - Preconditions: (not (inaction Robot))
   - Effects: (at Robot TennisRacket), (not (inaction Robot))

2. PickupObject(Robot, TennisRacket, TennisRacketLocation)
   - Parameters: ?robot - robot, ?TennisRacket - object, ?TennisRacketLocation - object
   - Preconditions: (at-location TennisRacket TennisRacketLocation), (at Robot TennisRacketLocation), (not (inaction Robot))
   - Effects: (holding Robot TennisRacket), (not (inaction Robot))

3. GoToObject(Robot, Bed)
   - Parameters: ?robot - robot, ?Bed - object
   - Preconditions: (not (inaction Robot))
   - Effects: (at Robot Bed), (not (inaction Robot))

4. PutObject(Robot, TennisRacket, Bed)
   - Parameters: ?robot - robot, ?TennisRacket - object, ?Bed - object
   - Preconditions: (holding Robot TennisRacket), (at Robot Bed), (not (inaction Robot))
   - Effects: (at-location TennisRacket Bed), (not (holding Robot TennisRacket)), (not (inaction Robot))

#### SubTask 3: Turn Off the Light
Initial conditions:
1. Robot not at light switch location
2. Light is initially on (assuming)

Action sequence:
1. GoToObject(Robot, LightSwitch)
   - Parameters: ?robot - robot, ?LightSwitch - object
   - Preconditions: (not (inaction Robot))
   - Effects: (at Robot LightSwitch), (not (inaction Robot))

2. SwitchOff(Robot, LightSwitch)
   - Parameters: ?robot - robot, ?LightSwitch - object
   - Preconditions: (not (inaction Robot)), (at Robot LightSwitch)
   - Effects: (switch-off Robot LightSwitch), (not (inaction Robot))

### Parallel Execution Possibilities:
- Robot1 can handle SubTask 1 (BaseballBat)