(define (problem acquire_plate_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    plate - object
    countertop - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 countertop)
    (at-location plate countertop)
  )
  (:goal
    (holding robot1 plate)
  )
)