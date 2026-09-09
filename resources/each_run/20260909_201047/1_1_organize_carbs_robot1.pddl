(define (problem organize_carbs_robot1)
  (:domain robot1)
  (:objects
    robot1 - robot
    bread - object
    potato - object
    apple - object
    lettuce - object
    tomato - object
    cabinet - object
    fridge - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot1 initialLocation)
    (at-location bread counterTop)
    (at-location potato counterTop)
    (at-location apple counterTop)
    (at-location lettuce counterTop)
    (at-location tomato counterTop)
    (inaction robot1)
    (not (holding robot1 bread))
    (not (holding robot1 potato))
    (not (holding robot1 apple))
    (not (holding robot1 lettuce))
    (not (holding robot1 tomato))
  )
  (:goal
    (and
      (at-location bread cabinet)
      (at-location potato cabinet)
      (at-location apple fridge)
      (at-location lettuce fridge)
      (at-location tomato fridge)
    )
  )
)