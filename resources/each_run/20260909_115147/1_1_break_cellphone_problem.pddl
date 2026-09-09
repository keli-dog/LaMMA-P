(define (problem break_cellphone_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    CellPhone - object
    Desk - object
  )
  (:init
    (at robot2 Desk)
    (at-location CellPhone Desk)
    (not (inaction robot2))
  )
  (:goal
    (break robot2 CellPhone)
  )
)