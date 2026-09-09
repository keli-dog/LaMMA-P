(define (problem put_apple_in_fridge)
  (:domain robot1)
  (:objects
    robot1 - robot
    Apple - object
    Fridge - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location Apple counterTop)
    (not (inaction robot1))
    (object-close robot1 Fridge)
  )
  (:goal
    (and
      (at-location Apple Fridge)
      (object-close robot1 Fridge)
    )
  )
)