(define (problem prepare_fruits_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    apple - object
    knife - object
    bowl - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location knife counterTop)
    (at-location apple counterTop)
    (at-location bowl counterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (sliced apple)
      (at-location apple bowl)
    )
  )
)