(define (problem preparetea_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    kettle - object
    stoveBurner - object
    counterTop - object
    initiallocation - object
  )
  (:init
    (at robot2 initiallocation)
    (inaction robot2)
    (at-location kettle counterTop)
    (not (holding robot2 kettle))
  )
  (:goal
    (and
      (at-location kettle stoveBurner)
      (not (holding robot2 kettle))
    )
  )
)