(define (problem pickup_laptop_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    laptop - object
    desk - object
  )
  (:init
    (at robot1 desk)
    (at-location laptop desk)
    (not (inaction robot1))
  )
  (:goal
    (and
      (holding robot1 laptop)
    )
  )
)