?robot ?object))
             )
  :effect (and
            (at end (not(holding ?robot ?object)))
            (over all (not(inaction ?robot)))
          )
)
```

### Explanation:
1. **Durative Actions**: Each action is defined as a durative action with specified durations for simplicity.
2. **Conditions and Effects**:
   - `GoToObject`: Moves the robot to an object's location, assuming it takes 5 time units.
   - `PickupObject`: Picks up an object if the robot is at its location, taking 3 time units.
   - `ThrowObject`: Throws the held object into a garbage can, taking 2 time units.

### Notes:
- The plan assumes that all objects are initially located in a generic "location" for simplicity. In practice, you would need to specify actual locations based on your environment setup.
- Durations are assumed for demonstration purposes and should be adjusted according to the real-world scenario or simulation requirements.
- Ensure that the robot's actions do not conflict with each other by properly sequencing them or allowing parallel execution where appropriate.

This PDDL plan can now be used in a planning domain to achieve the goal of throwing the spatula into the garbage can.