(define (problem turn_on_faucet_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    faucet - object
    sink - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location faucet sink)
    (not (inaction robot2))
  )
  (:goal
    (and
      (switch-on robot2 faucet)
    )
  )
)