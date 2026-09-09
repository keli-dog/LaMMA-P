(define (problem operatetoaster_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Toaster - object
    initialLocation - object
  )
  (:init
    (at robot1 initialLocation)
    (inaction robot1)
    (switch-off robot1 Toaster)
    (at-location Toaster initialLocation)
  )
  (:goal
    (and
      (switch-on robot1 Toaster)
      (switch-off robot1 Toaster)
    )
  )
)