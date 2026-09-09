(define (problem put_bowl_in_box_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    bowl - object
    box - object
    sofa - object
    counterTop - object
  )
  (:init
    (not (inaction robot2))
    (at robot2 counterTop)
    (at-location bowl counterTop)
    (at-location box sofa)
  )
  (:goal
    (and
      (at-location bowl box)
    )
  )
)