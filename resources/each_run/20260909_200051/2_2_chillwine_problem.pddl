(define (problem chillwine_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    WineBottle - object
    Fridge - object
    initiallocation - object
  )
  (:init
    (at robot2 initiallocation)
    (holding robot2 WineBottle)
    (at robot2 Fridge)
    (inaction robot2)
  )
  (:goal
    (and
      (at-location WineBottle Fridge)
      (object-close robot2 Fridge)
    )
  )
)