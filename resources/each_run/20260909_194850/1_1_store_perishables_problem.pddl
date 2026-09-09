(define (problem store_perishables_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Egg - object
    Fridge - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location Egg counterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location Egg Fridge)
    )
  )
)