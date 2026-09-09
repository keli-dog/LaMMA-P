(define (problem sanitize_carbs_robot1)
  (:domain robot1)
  (:objects
    robot1 - robot
    bread - object
    potato - object
    apple - object
    lettuce - object
    tomato - object
    sink - object
    cleanCounter - object
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
      (cleaned robot1 bread)
      (cleaned robot1 potato)
      (cleaned robot1 apple)
      (cleaned robot1 lettuce)
      (cleaned robot1 tomato)
      (at-location bread cleanCounter)
      (at-location potato cleanCounter)
      (at-location apple cleanCounter)
      (at-location lettuce cleanCounter)
      (at-location tomato cleanCounter)
    )
  )
)