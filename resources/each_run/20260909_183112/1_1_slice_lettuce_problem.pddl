(define (problem slice_lettuce_problem)
  (:domain robot3)
  (:objects
    robot3 - robot
    knife - object
    lettuce - object
    counterTop - object
  )
  (:init
    (at robot3 counterTop)
    (at-location knife counterTop)
    (at-location lettuce counterTop)
    (not (inaction robot3))
  )
  (:goal
    (and
      (sliced lettuce)
    )
  )
)