(define (problem break_cellphone_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Cellphone - object
    Desk - object
  )
  (:init
    (at robot2 Desk)
    (at-location Cellphone Desk)
    (not (inaction robot2))
  )
  (:goal
    (and
      (break robot2 Cellphone)
    )
  )
)