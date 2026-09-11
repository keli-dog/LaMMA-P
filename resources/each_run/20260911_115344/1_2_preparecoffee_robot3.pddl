(define (problem preparecoffee_robot3)
  (:domain robot3)
  (:objects
    robot3 - robot
    coffeeMachine - object
    startingLocation - object
  )
  (:init
    (at robot3 startingLocation)
    (inaction robot3)
  )
  (:goal
    (switch-off robot3 coffeeMachine)
  )
)