(define (problem getwinebottle_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    WineBottle - object
    Fridge - object
    CounterTop - object
    initiallocation - object
  )
  (:init
    (at robot1 initiallocation)
    (at-location WineBottle CounterTop)
    (inaction robot1)
    (not (holding robot1 WineBottle))
  )
  (:goal
    (and
      (holding robot1 WineBottle)
      (at robot1 Fridge)
    )
  )
)