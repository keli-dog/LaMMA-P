(define (problem collect_waste_robot3)
  (:domain robot3)
  (:objects
    robot3 - robot
    GarbageBag - object
    GarbageCan - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot3 initialLocation)
    (at-location GarbageBag counterTop)
    (inaction robot3)
    (not (holding robot3 GarbageBag))
  )
  (:goal
    (and
      (at-location GarbageBag GarbageCan)
      (not (holding robot3 GarbageBag))
    )
  )
)