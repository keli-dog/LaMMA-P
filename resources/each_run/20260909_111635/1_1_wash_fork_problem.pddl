(define (problem wash_fork_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Fork - object
    Sink - object
    Bowl - object
    CounterTop - object
  )
  (:init
    (at robot2 CounterTop)
    (at-location Fork CounterTop)
    (at-location Bowl CounterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (cleaned robot2 Fork)
      (at-location Fork Bowl)
    )
  )
)