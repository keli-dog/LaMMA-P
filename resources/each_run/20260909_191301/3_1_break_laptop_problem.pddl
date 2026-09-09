(define (problem break_laptop_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Laptop - object
    Desk - object
  )
  (:init
    (at robot1 Desk)
    (at-location Laptop Desk)
    (not (inaction robot1))
  )
  (:goal
    (and
      (break robot1 Laptop)
    )
  )
)