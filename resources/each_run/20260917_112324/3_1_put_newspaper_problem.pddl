(define (problem put_newspaper_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Newspaper - object
    GarbageCan - object
    Desk - object
    Floor - object
  )
  (:init
    (at robot2 Floor)
    (at-location Newspaper Desk)
    (at-location GarbageCan Floor)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location Newspaper GarbageCan)
    )
  )
)