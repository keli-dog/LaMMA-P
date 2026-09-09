(define (problem clean_surfaces_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    CounterTop - object
    DiningTable - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 CounterTop)
    (at-location CounterTop CounterTop)
    (at-location DiningTable DiningTable)
  )
  (:goal
    (and
      (cleaned robot1 CounterTop)
      (cleaned robot1 DiningTable)
    )
  )
)