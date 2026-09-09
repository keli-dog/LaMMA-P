(define (problem put_fork_in_bowl_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    fork - object
    bowl - object
    counterTop - object
  )
  (:init
    (holding robot2 fork)
    (at-location bowl counterTop)
    (not (inaction robot2))
    (at robot2 counterTop)
  )
  (:goal
    (and
      (at-location fork bowl)
    )
  )
)