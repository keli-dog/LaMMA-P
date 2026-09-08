(define (problem pick_up_spatula_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    spatula - object
    countertop - object
  )
  (:init
    (at robot2 countertop)
    (at-location spatula countertop)
    (inaction robot2)
  )
  (:goal
    (and
      (holding robot2 spatula)
    )
  )
)