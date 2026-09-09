(define (problem break_desklamp_problem)
  (:domain robot5)
  (:objects
    robot5 - robot
    DeskLamp - object
    Desk - object
  )
  (:init
    (at robot5 Desk)
    (at-location DeskLamp Desk)
    (not (inaction robot5))
  )
  (:goal
    (and
      (break robot5 DeskLamp)
    )
  )
)