(define (problem slice_lettuce_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Knife - object
    Lettuce - object
    CounterTop - object
  )
  (:init
    (at robot1 CounterTop)
    (at-location Knife CounterTop)
    (at-location Lettuce CounterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (sliced Lettuce)
    )
  )
)