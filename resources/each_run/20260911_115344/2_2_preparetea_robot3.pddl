(define (problem preparetea_robot3)
  (:domain robot3)
  (:objects
    robot3 - robot
    stoveBurner - object
    initiallocation - object
  )
  (:init
    (at robot3 initiallocation)
    (inaction robot3)
    (not (at robot3 stoveBurner))
  )
  (:goal
    (switch-on robot3 stoveBurner)
  )
)