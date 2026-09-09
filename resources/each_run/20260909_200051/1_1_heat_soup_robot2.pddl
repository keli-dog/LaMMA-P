(define (problem heat_soup_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    pot - object
    stove - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot2 initialLocation)
    (at-location pot counterTop)
    (inaction robot2)
    (not (holding robot2 pot))
  )
  (:goal
    (and
      (at-location pot stove)
      (switch-on robot2 stove)
    )
  )
)