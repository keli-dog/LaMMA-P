(define (problem trash_newspaper_problem)
  (:domain robot4)
  (:objects
    robot4 - robot
    newspaper - object
    garbageCan - object
    coffeeTable - object
    floor - object
  )
  (:init
    (at robot4 coffeeTable)
    (at-location newspaper coffeeTable)
    (at-location garbageCan floor)
    (not (inaction robot4))
  )
  (:goal
    (and
      (at-location newspaper garbageCan)
    )
  )
)