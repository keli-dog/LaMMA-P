```lisp
(define (problem dispose_waste_robot1)
  (:domain robot1)
  (:objects
    robot1 - robot
    garbageBag - object
    garbageCan - object
    counterTop - object
    floor - object
  )
  (:init
    (at robot1 floor)
    (at-location garbageBag counterTop)
    (at-location garbageCan floor)
  )
  (:goal
    (and
      (at-location garbageBag garbageCan)
      (not (holding robot1 garbageBag))
    )
  )
)
```