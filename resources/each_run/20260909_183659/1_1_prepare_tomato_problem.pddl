(define (problem prepare_tomato_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    tomato - object
    plate - object
    microwave - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location tomato counterTop)
    (at-location plate microwave)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location tomato plate)
    )
  )
)