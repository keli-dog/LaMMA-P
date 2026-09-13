(define (problem transport_payload_to_chamber)
  (:domain robot2)
  (:objects
    robot2 - robot
    apple - object
    microwave - object
    countertop - object
  )
  (:init
    (at robot2 countertop)
    (at-location apple countertop)
    (inaction robot2)
  )
  (:goal
    (and
      (at-location apple microwave)
    )
  )
)