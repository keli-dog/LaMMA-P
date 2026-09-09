(define (problem collect_waste_robot1)
  (:domain robot1)
  (:objects
    robot1 - robot
    GarbageBag - object
    GarbageCan - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot1 initialLocation)
    (at-location GarbageBag counterTop)
    (inaction robot1)
    (not (holding robot1 GarbageBag))
  )
  (:goal
    (and
      (at-location GarbageBag GarbageCan)
      (not (holding robot1 GarbageBag))
    )
  )
)