(define (problem put_bat_on_bed)
  (:domain robot1)
  (:objects
    robot1 - robot
    BaseballBat - object
    Bed - object
    Desk - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 Desk)
    (at-location BaseballBat Desk)
    (at-location Bed Bed)
  )
  (:goal
    (and
      (at-location BaseballBat Bed)
    )
  )
)