(define (problem slice_tomato_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    knife - object
    tomato - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location knife counterTop)
    (at-location tomato counterTop)
  )
  (:goal
    (and
      (sliced tomato)
    )
  )
)