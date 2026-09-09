(define (problem put_lettuce_in_fridge_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    lettuce - object
    fridge - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location lettuce counterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location lettuce fridge)
      (object-close robot2 fridge)
    )
  )
)