(define (problem pickup_newspaper_problem)
  (:domain robot3)
  (:objects
    robot3 - robot
    newspaper - object
    desk - object
    initialLocation - object
  )
  (:init
    (at robot3 initialLocation)
    (at-location newspaper desk)
    (inaction robot3)
    (not (holding robot3 newspaper))
  )
  (:goal
    (and
      (holding robot3 newspaper)
      (at robot3 desk)
    )
  )
)