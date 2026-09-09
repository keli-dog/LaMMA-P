(define (problem makecoffee_problem_robot3)
  (:domain robot3)
  (:objects
    robot3 - robot
    coffeeMachine - object
    mug - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot3 initialLocation)
    (at-location mug coffeeMachine)
    (inaction robot3)
    (holding robot3 mug)
    (switch-on robot3 coffeeMachine)
  )
  (:goal
    (and
      (switch-off robot3 coffeeMachine)
      (not (holding robot3 mug))
    )
  )
)