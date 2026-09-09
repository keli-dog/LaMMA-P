(define (problem wash_lettuce_problem)
  (:domain robot3)
  (:objects
    robot3 - robot
    Lettuce - object
    Sink - object
    CounterTop - object
  )
  (:init
    (at robot3 CounterTop)
    (at-location Lettuce CounterTop)
    (not (inaction robot3))
  )
  (:goal
    (and
      (cleaned robot3 Lettuce)
      (at-location Lettuce CounterTop)
    )
  )
)