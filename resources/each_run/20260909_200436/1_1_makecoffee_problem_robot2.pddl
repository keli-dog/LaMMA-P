(define (problem makecoffee_problem_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    coffeeMachine - object
    mug - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot2 initialLocation)
    (at-location coffeeMachine counterTop)
    (at-location mug counterTop)
    (inaction robot2)
    (not (holding robot2 mug))
    (switch-off robot2 coffeeMachine)
  )
  (:goal
    (and
      (switch-on robot2 coffeeMachine)
      (holding robot2 mug)
    )
  )
)