(define (problem close_blinds_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Blinds - object
    Window - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 Window)
    (object-open robot1 Blinds)
  )
  (:goal
    (and
      (object-close robot1 Blinds)
    )
  )
)