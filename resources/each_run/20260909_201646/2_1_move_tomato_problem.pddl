(define (problem move_tomato_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Tomato - object
    DiningTable - object
    Fridge - object
  )
  (:init
    (at robot2 DiningTable)
    (at-location Tomato DiningTable)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location Tomato Fridge)
      (object-close Fridge)
    )
  )
)