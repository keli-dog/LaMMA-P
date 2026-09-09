(define (problem prepare_egg_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    egg - object
    plate - object
    microwave - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location egg counterTop)
    (at-location plate microwave)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location egg plate)
    )
  )
)