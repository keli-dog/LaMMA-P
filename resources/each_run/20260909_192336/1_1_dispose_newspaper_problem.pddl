(define (problem dispose_newspaper_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    newspaper - object
    garbageCan - object
    desk - object
  )
  (:init
    (holding robot2 newspaper)
    (at robot2 desk)
    (inaction robot2)
  )
  (:goal
    (and
      (at-location newspaper garbageCan)
      (not (holding robot2 newspaper))
    )
  )
)