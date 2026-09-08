(define (problem slice_tomato_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    tomato - object
    knife - object
    countertop - object
  )
  (:init
    (at robot1 countertop)
    (at-location tomato countertop)
    (at-location knife countertop)
    (inaction robot1)
  )
  (:goal
    (and
      (sliced tomato)
    )
  )
)