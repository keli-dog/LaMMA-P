(define (problem place_sponge_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    DishSponge - object
    Sink - object
    CounterTop - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 CounterTop)
    (at-location DishSponge CounterTop)
    (at-location Sink Floor)
  )
  (:goal
    (and
      (at-location DishSponge Sink)
    )
  )
)