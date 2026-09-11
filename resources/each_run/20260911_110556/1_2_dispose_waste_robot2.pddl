(define (problem dispose_waste_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    garbageBag - object
    garbageCan - object
    counterTop - object
    floor - object
  )
  (:init
    (at robot2 floor)
    (at-location garbageBag counterTop)
    (at-location garbageCan floor)
    (inaction robot2)
    (not (holding robot2 garbageBag))
  )
  (:goal
    (and
      (at-location garbageBag garbageCan)
      (not (holding robot2 garbageBag))
    )
  )
)