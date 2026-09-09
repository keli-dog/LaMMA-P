(define (problem put_pen_on_bed)
  (:domain robot1)
  (:objects
    robot1 - robot
    pen - object
    bed - object
    desk - object
    floor - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 desk)
    (at-location pen desk)
    (at-location bed floor)
  )
  (:goal
    (and
      (at-location pen bed)
    )
  )
)