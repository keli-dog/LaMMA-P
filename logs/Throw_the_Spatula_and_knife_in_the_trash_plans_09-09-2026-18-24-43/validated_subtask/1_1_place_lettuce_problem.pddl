(define (problem place_lettuce_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Lettuce - object
    Plate - object
    CounterTop - object
  )
  (:init
    (at robot1 CounterTop)
    (at-location Lettuce CounterTop)
    (at-location Plate CounterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location Lettuce Plate)
    )
  )
)