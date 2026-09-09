(define (problem pick_up_fork_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Fork - object
    CounterTop - object
  )
  (:init
    (at robot2 CounterTop)
    (at-location Fork CounterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (holding robot2 Fork)
    )
  )
)