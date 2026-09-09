(define (problem store_dry_goods_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Bread - object
    Cabinet - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location Bread counterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location Bread Cabinet)
      (object-close robot1 Cabinet)
    )
  )
)