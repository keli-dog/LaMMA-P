(define (problem place_laptop_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    laptop - object
    bed - object
    desk - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 desk)
    (at-location laptop desk)
    (at-location bed floor)
  )
  (:goal
    (and
      (at-location laptop bed)
    )
  )
)