(define (problem place_sponge_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    DishSponge - object
    Sink - object
    counterTop - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 counterTop)
    (at-location DishSponge counterTop)
    (at-location Sink counterTop)
  )
  (:goal
    (and
      (at-location DishSponge Sink)
    )
  )
)