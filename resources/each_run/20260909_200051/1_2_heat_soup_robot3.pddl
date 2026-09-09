(define (problem heat_soup_robot3)
  (:domain robot3)
  (:objects
    robot3 - robot
    pot - object
    stove - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot3 initialLocation)
    (at-location pot counterTop)
    (inaction robot3)
    (not (holding robot3 pot))
  )
  (:goal
    (and
      (at-location pot stove)
      (switch-on robot3 stove)
    )
  )
)