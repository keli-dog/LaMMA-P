(define (problem slice_potato_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Potato - object
    Knife - object
    CounterTop - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 CounterTop)
    (at-location Potato CounterTop)
    (at-location Knife CounterTop)
  )
  (:goal
    (and
      (sliced Potato)
    )
  )
)