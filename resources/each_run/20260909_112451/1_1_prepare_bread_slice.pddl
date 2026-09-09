(define (problem prepare_bread_slice)
  (:domain robot3)
  (:objects
    robot3 - robot
    Knife - object
    Bread - object
    CounterTop - object
  )
  (:init
    (not (inaction robot3))
    (at robot3 CounterTop)
    (at-location Knife CounterTop)
    (at-location Bread CounterTop)
  )
  (:goal
    (and
      (sliced Bread)
    )
  )
)