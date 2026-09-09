# Task Description: Stage the furniture for a home staging photoshoot

## GENERAL TASK DECOMPOSITION
We'll decompose this task into parallelizable subtasks based on different furniture items and their optimal placement for staging. The key is to identify independent actions that can be performed simultaneously by different robots.

### Independent Subtasks:
1. **Arrange Living Room Furniture** (Skills: GoToObject, PickupObject, PutObject)
2. **Stage Bedroom Furniture** (Skills: GoToObject, PickupObject, PutObject)
3. **Decorate with Accessories** (Skills: GoToObject, PickupObject, PutObject, OpenObject, CloseObject)
4. **Adjust Lighting** (Skills: GoToObject, SwitchOn, SwitchOff)

These subtasks can be parallelized as they involve different objects in different areas.

## Action Plan

### Subtask 1: Arrange Living Room Furniture
Initial conditions:
- Sofa, CoffeeTable, ArmChair, SideTable are in default positions
- Robot not holding any furniture items

1. **GoToObject**(robot1, Sofa)
   - Pre: not(inaction robot1)
   - Eff: at(robot1 Sofa), not(inaction robot1)

2. **PickupObject**(robot1, Sofa, SofaLocation)
   - Pre: at-location(Sofa SofaLocation), at(robot1 SofaLocation), not(inaction robot1)
   - Eff: holding(robot1 Sofa), not(inaction robot1)

3. **PutObject**(robot1, Sofa, LivingRoomWall)
   - Pre: holding(robot1 Sofa), at(robot1 LivingRoomWall), not(inaction robot1)
   - Eff: at-location(Sofa LivingRoomWall), not(holding(robot1 Sofa)), not(inaction robot1)

4. **GoToObject**(robot1, CoffeeTable)
   - Pre: not(inaction robot1)
   - Eff: at(robot1 CoffeeTable), not(inaction robot1)

5. **PickupObject**(robot1, CoffeeTable, CoffeeTableLocation)
   - Pre: at-location(CoffeeTable CoffeeTableLocation), at(robot1 CoffeeTableLocation), not(inaction robot1)
   - Eff: holding(robot1 CoffeeTable), not(inaction robot1)

6. **PutObject**(robot1, CoffeeTable, InFrontOfSofa)
   - Pre: holding(robot1 CoffeeTable), at(robot1 InFrontOfSofa), not(inaction robot1)
   - Eff: at-location(CoffeeTable InFrontOfSofa), not(holding(robot1 CoffeeTable)), not(inaction robot1)

### Subtask 2: Stage Bedroom Furniture (Parallel with robot2)
Initial conditions:
- Dresser, Bed, SideTable are in default positions
- Robot not holding any furniture items

1. **GoToObject**(robot2, Dresser)
   - Pre: not(inaction robot2)
   - Eff: at(robot2 Dresser), not(inaction robot2)

2. **PickupObject**(robot2, Dresser, DresserLocation)
   - Pre: at-location(Dresser DresserLocation), at(robot2 DresserLocation), not(inaction robot2)
   - Eff: holding(robot2 Dresser), not(inaction robot2)

3. **PutObject**(robot2, Dresser, BedroomWall)
   - Pre: holding(robot2 Dresser), at(robot2 BedroomWall), not(inaction robot2)
   - Eff: at-location(Dresser BedroomWall), not(holding(robot2 Dresser)), not(inaction robot2)

4. **GoToObject**(robot2, SideTable)
   - Pre: not(inaction robot2)
   - Eff: at(robot2 SideTable), not(inaction robot2)

5. **PickupObject**(robot2, SideTable, SideTableLocation)
   - Pre: at-location(SideTable SideTableLocation), at(robot2 SideTableLocation), not(inaction robot2)
   - Eff: holding(robot2 SideTable), not(inaction robot2)

6. **PutObject**(robot2, SideTable, BesideBed)
   - Pre: holding(robot2 SideTable), at(robot2 BesideBed), not(inaction robot2)
   - Eff: at-location(SideTable BesideBed), not(holding(robot2 SideTable)), not(inaction robot2)

### Subtask 3: Decorate with Accessories
Initial conditions:
- Vase, Painting, HousePlant, Book