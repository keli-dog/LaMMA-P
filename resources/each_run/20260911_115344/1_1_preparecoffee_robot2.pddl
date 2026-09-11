(define (problem preparecoffee_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    mug - object
    coffeeMachine - object
    counterTop - object
    storageArea - object
    startingLocation - object
  )
  (:init
    (at robot2 startingLocation)
    (at-location mug storageArea)
    (at-location coffeeMachine counterTop)
    (inaction robot2)
    (not (holding robot2 mug))
  )
  (:goal
    (at-location mug counterTop)
  )
)