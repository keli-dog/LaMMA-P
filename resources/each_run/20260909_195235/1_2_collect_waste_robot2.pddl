(define (problem collect_waste_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    GarbageBag - object
    GarbageCan - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot2 initialLocation)
    (at-location GarbageBag counterTop)
    (inaction robot2)
    (not (holding robot2 GarbageBag))
  )
  (:goal
    (and
      (at-location GarbageBag GarbageCan)
      (not (holding robot2 GarbageBag))
    )
  )
)