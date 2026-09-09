(define (problem put_watering_can_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    WateringCan - object
    CoffeeTable - object
    Shelf - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 Shelf)
    (at-location WateringCan Shelf)
    (at-location CoffeeTable Floor)
  )
  (:goal
    (and
      (at-location WateringCan CoffeeTable)
    )
  )
)