(define (problem put_pen_on_bed)
  (:domain robot2)
  (:objects
    robot2 - robot
    pen - object
    bed - object
    desk - object
  )
  (:init
    (at robot2 desk)
    (at-location pen desk)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location pen bed)
    )
  )
)