(define (problem go_to_trash_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    trash - object
    countertop - object
  )
  (:init
    (at robot2 countertop)
  )
  (:goal
    (and
      (at robot2 trash)
    )
  )
)