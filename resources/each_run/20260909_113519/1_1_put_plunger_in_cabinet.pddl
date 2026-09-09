(define (problem put_plunger_in_cabinet)
  (:domain robot3)
  (:objects
    robot3 - robot
    plunger - object
    cabinet - object
    counterTop - object
  )
  (:init
    (at robot3 counterTop)
    (at-location plunger counterTop)
    (object-close robot3 cabinet)
    (not (inaction robot3))
  )
  (:goal
    (and
      (at-location plunger cabinet)
      (object-close robot3 cabinet)
    )
  )
)