(define (problem prepare_bread_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Bread - object
    Knife - object
    Plate - object
    Fridge - object
    CounterTop - object
    DiningTable - object
  )
  (:init
    (at robot2 CounterTop)
    (at-location Bread CounterTop)
    (at-location Knife CounterTop)
    (at-location Plate DiningTable)
    (not (inaction robot2))
  )
  (:goal
    (and
      (sliced Bread)
      (object-close robot2 Fridge)
    )
  )
)