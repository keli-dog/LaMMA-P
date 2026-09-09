(define (problem put_tomato_in_fridge)
  (:domain robot3)
  (:objects
    robot3 - robot
    tomato - object
    fridge - object
    counterTop - object
  )
  (:init
    (at robot3 counterTop)
    (at-location tomato counterTop)
    (not (inaction robot3))
  )
  (:goal
    (and
      (at-location tomato fridge)
      (object-close robot3 fridge)
    )
  )
)