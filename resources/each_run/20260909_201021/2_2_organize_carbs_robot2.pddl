(define (problem organize_carbs_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
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
    (at robot2 initialLocation)
    (at-location bread counterTop)
    (at-location potato counterTop)
    (at-location apple counterTop)
    (at-location lettuce counterTop)
    (at-location tomato counterTop)
    (inaction robot2)
    (not (holding robot2 bread))
    (not (holding robot2 potato))
    (not (holding robot2 apple))
    (not (holding robot2 lettuce))
    (not (holding robot2 tomato))
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