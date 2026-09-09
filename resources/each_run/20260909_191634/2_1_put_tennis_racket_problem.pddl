(define (problem put_tennis_racket_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    TennisRacket - object
    Bed - object
    Desk - object
  )
  (:init
    (at robot2 Desk)
    (at-location TennisRacket Desk)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location TennisRacket Bed)
    )
  )
)