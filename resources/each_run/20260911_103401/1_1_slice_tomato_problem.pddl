(define (problem slice_tomato_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    tomato - object
    counterTop - object
    diningTable - object
  )
  (:init
    (at robot2 counterTop)
    (at-location tomato diningTable)
  )
  (:goal
    (and
      (sliced tomato)
    )
  )
)