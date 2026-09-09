(define (problem slice_apple_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Apple - object
    Knife - object
    CounterTop - object
    FruitBowl - object
    CuttingBoard - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 CounterTop)
    (at-location Knife CounterTop)
    (at-location Apple FruitBowl)
    (at-location Apple CuttingBoard)
  )
  (:goal
    (and
      (sliced Apple)
    )
  )
)