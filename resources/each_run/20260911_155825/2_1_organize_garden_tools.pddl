(define (problem organize_garden_tools)
  (:domain robot1)
  (:objects
    robot1 - robot
    watering_can - object
    side_table - object
    shelf - object
    floor - object
  )
  (:init
    (at robot1 floor)
    (at-location watering_can side_table)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location watering_can shelf)
    )
  )
)