(define (problem boilwater_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    pot - object
    faucet - object
    stoveBurner - object
    stoveKnob - object
    initiallocation - object
    counterTop - object
  )
  (:init
    (at robot2 initiallocation)
    (at-location pot counterTop)
    (inaction robot2)
    (not (holding robot2 pot))
    (switch-off robot2 stoveBurner)
  )
  (:goal
    (and
      (switch-on robot2 stoveBurner)
      (at-location pot stoveBurner)
    )
  )
)