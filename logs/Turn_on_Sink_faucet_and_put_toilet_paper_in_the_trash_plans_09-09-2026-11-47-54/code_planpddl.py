Here's the corrected PDDL plan with proper variable handling (variablelocation → variable itself):

```pddl
(define (plan household_tasks)
  (:parallel
    ;; Robot2 executing SubTask 1: Turn on Sink faucet
    (:sequence
      (gotoobject robot2 faucet)
      (switchon robot2 faucet)
    )
    
    ;; Robot3 executing SubTask 2: Put toilet paper in the trash
    (:sequence
      (gotoobject robot3 toiletpaper)
      (pickupobject robot3 toiletpaper)
      (gotoobject robot3 garbagecan)
      (putobject robot3 toiletpaper garbagecan)
    )
  )
)
```

The plan remains unchanged from your provided version as it already correctly:
1. Uses variables directly without redundant location parameters
2. Maintains proper PDDL syntax with only necessary parentheses
3. Preserves the parallel execution structure
4. Uses lowercase action names consistently
5. Keeps the original robot assignments and task sequencing

No further modifications were needed as the plan already met all the specified requirements.