(define (problem dispose_waste_robot3)
  (:domain robot3)
  (:objects
    robot3 - robot
    garbageBag - object
    garbageCan - object
    counterTop - object
    floor - object
  )
  (:init
    (at robot3 floor)
    (at-location garbageBag counterTop)
    (at-location garbageCan floor)
    (inaction robot3)
    (not (holding robot3 garbageBag))
  )
  (:goal
    (and
      (at-location garbageBag garbageCan)
      (not (holding robot3 garbageBag))
    )
  )
)