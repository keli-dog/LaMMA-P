(define (problem slice_tomato_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    knife - object
    tomato - object
    counterTop - object
  )
  (:init
    (not (inaction robot2))
    (at robot2 counterTop)
    (at-location knife counterTop)
    (at-location tomato counterTop)
  )
  (:goal
    (and
      (sliced tomato)
    )
  )
)