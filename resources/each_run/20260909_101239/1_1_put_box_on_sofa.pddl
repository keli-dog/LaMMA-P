(define (problem put_box_on_sofa)
  (:domain robot2)
  (:objects
    robot2 - robot
    Box - object
    Sofa - object
    CoffeeTable - object
  )
  (:init
    (at robot2 CoffeeTable)
    (at-location Box CoffeeTable)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location Box Sofa)
    )
  )
)