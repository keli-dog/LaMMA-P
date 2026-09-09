(define (problem place_laptop_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    laptop - object
    bed - object
    desk - object
  )
  (:init
    (holding robot1 laptop)
    (at-location laptop desk)
    (at robot1 desk)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location laptop bed)
    )
  )
)