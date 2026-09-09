(define (problem transfer_payload_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    plate - object
    potato - object
    microwave - object
    counterTop - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 counterTop)
    (at-location plate counterTop)
    (at-location potato plate)
    (object-open robot1 microwave)
  )
  (:goal
    (and
      (at-location plate microwave)
      (object-close robot1 microwave)
    )
  )
)