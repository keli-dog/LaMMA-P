(define (problem open_laptop_problem)
  (:domain robot3)
  (:objects
    robot3 - robot
    Laptop - object
    DiningTable - object
  )
  (:init
    (at robot3 DiningTable)
    (at-location Laptop DiningTable)
    (not (inaction robot3))
  )
  (:goal
    (and
      (object-open robot3 Laptop)
    )
  )
)