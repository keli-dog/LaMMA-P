(define (problem organize_garden_tools)
  (:domain robot1)
  (:objects
    robot1 - robot
    Shovel - object
    WateringCan - object
    Rake - object
    GardenShed - object
    GardenArea - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 GardenArea)
    (at-location Shovel GardenArea)
    (at-location WateringCan GardenArea)
    (at-location Rake GardenArea)
  )
  (:goal
    (and
      (at-location Shovel GardenShed)
      (at-location WateringCan GardenShed)
      (at-location Rake GardenShed)
      (cleaned robot1 Shovel)
      (cleaned robot1 WateringCan)
      (cleaned robot1 Rake)
    )
  )
)