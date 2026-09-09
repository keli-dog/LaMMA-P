I'll modify the plan to correct the variable names as requested, ensuring that all 'variablelocation' references are replaced with the variable itself (since the variable includes location information). Here's the corrected PDDL plan:

```pddl
(define (plan sandwich_preparation)
  (:parallel

    ;; SubTask 1: Prepare Bread (Robot1)
    (:sequence
      (gotoobject robot1 bread)
      (pickupobject robot1 bread)
      (gotoobject robot1 knife)
      (pickupobject robot1 knife)
      (sliceobject robot1 bread)
      (gotoobject robot1 plate)
      (putobject robot1 bread plate)
      (gotoobject robot1 fridge)
      (openobject robot1 fridge)
      (putobject robot1 plate fridge)
      (closeobject robot1 fridge)
    )

    ;; SubTask 2: Prepare Lettuce (Robot2)
    (:sequence
      (gotoobject robot2 lettuce)
      (pickupobject robot2 lettuce)
      (gotoobject robot2 sink)
      (cleanobject robot2 lettuce)
      (gotoobject robot2 knife)
      (pickupobject robot2 knife)
      (sliceobject robot2 lettuce)
      (gotoobject robot2 bowl)
      (putobject robot2 lettuce bowl)
      (gotoobject robot2 fridge)
      (openobject robot2 fridge)
      (putobject robot2 bowl fridge)
      (closeobject robot2 fridge)
    )

    ;; SubTask 3: Prepare Tomato (Robot3)
    (:sequence
      (gotoobject robot3 tomato)
      (pickupobject robot3 tomato)
      (gotoobject robot3 knife)
      (pickupobject robot3 knife)
      (sliceobject robot3 tomato)
      (gotoobject robot3 bowl)
      (putobject robot3 tomato bowl)
      (gotoobject robot3 fridge)
      (openobject robot3 fridge)
      (putobject robot3 bowl fridge)
      (closeobject robot3 fridge)
    )

    ;; SubTask 4: Prepare Condiments (Robot4)
    (:sequence
      (gotoobject robot4 butterknife)
      (pickupobject robot4 butterknife)
      (gotoobject robot4 fridge)
      (openobject robot4 fridge)
      (putobject robot4 butterknife fridge)
      (closeobject robot4 fridge)
    )
  )
)
```

Key changes made:
1. Replaced 'container' with 'bowl' (from the object list)
2. Replaced 'butter' with 'butterknife' (from the object list)
3. Maintained all other object names exactly as they appear in the provided object list
4. Kept the same structure of parallel and sequential blocks
5. Ensured all actions use the correct object names without any location suffixes

The plan now uses only the object names from the provided list, with no additional location information appended to them.