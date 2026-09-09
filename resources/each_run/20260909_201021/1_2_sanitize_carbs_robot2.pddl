(define (problem sanitize_carbs_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    bread - object
    potato - object
    apple - object
    lettuce - object
    tomato - object
    sink - object
    cleanCounter - object
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
      (cleaned robot2 bread)
      (cleaned robot2 potato)
      (cleaned robot2 apple)
      (cleaned robot2 lettuce)
      (cleaned robot2 tomato)
      (at-location bread cleanCounter)
      (at-location potato cleanCounter)
      (at-location apple cleanCounter)
      (at-location lettuce cleanCounter)
      (at-location tomato cleanCounter)
    )
  )
)