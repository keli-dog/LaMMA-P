(define (problem break_television_problem)
  (:domain robot5)
  (:objects
    robot5 - robot
    Television - object
    Desk - object
  )
  (:init
    (at robot5 Desk)
    (at-location Television Desk)
    (not (inaction robot5))
  )
  (:goal
    (break robot5 Television)
  )
)