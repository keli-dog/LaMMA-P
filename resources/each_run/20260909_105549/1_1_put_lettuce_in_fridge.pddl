(define (problem put_lettuce_in_fridge)
  (:domain robot1)
  (:objects
    robot1 - robot
    lettuce - object
    fridge - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location lettuce counterTop)
    (not (inaction robot1))
    (object-close robot1 fridge)
  )
  (:goal
    (and
      (at-location lettuce fridge)
    )
  )
)