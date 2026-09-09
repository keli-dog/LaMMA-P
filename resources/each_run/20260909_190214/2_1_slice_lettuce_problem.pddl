(define (problem slice_lettuce_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    lettuce - object
    knife - object
    counterTop - object
    diningTable - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 counterTop)
    (at-location lettuce counterTop)
    (at-location knife diningTable)
  )
  (:goal
    (and
      (sliced lettuce)
    )
  )
)