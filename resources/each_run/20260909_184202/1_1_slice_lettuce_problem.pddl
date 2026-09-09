(define (problem slice_lettuce_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    knife - object
    lettuce - object
    counterTop - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 counterTop)
    (at-location knife counterTop)
    (at-location lettuce counterTop)
  )
  (:goal
    (and
      (sliced lettuce)
    )
  )
)