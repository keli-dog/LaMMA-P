(define (problem newspaper_disposal_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Newspaper - object
    GarbageCan - object
    Desk - object
    Floor - object
  )
  (:init
    (not (inaction robot2))
    (at robot2 Floor)
    (at-location Newspaper Desk)
    (at-location GarbageCan Floor)
  )
  (:goal
    (and
      (at-location Newspaper GarbageCan)
    )
  )
)