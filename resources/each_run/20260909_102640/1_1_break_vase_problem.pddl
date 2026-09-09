(define (problem break_vase_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    vase - object
    sideTable - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 sideTable)
    (at-location vase sideTable)
    (not (break robot1 vase))
  )
  (:goal
    (break robot1 vase)
  )
)