(define (problem slice_lettuce_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    knife - object
    lettuce - object
    counterTop - object
    cabinet - object
  )
  (:init
    (at robot1 counterTop)
    (at-location knife counterTop)
    (at-location lettuce counterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (sliced lettuce)
      (at-location lettuce cabinet)
    )
  )
)