(define (problem get_clean_plate_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Plate - object
    counterTop - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 counterTop)
    (at-location Plate counterTop)
  )
  (:goal
    (and
      (holding robot1 Plate)
    )
  )
)