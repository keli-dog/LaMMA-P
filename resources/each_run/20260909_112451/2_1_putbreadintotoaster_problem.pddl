(define (problem putbreadintotoaster_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    BreadSlice - object
    Toaster - object
    counterTop - object
    initialLocation - object
  )
  (:init
    (at robot2 initialLocation)
    (at-location BreadSlice counterTop)
    (holding robot2 BreadSlice)
    (inaction robot2)
    (switch-off robot2 Toaster)
  )
  (:goal
    (and
      (at-location BreadSlice Toaster)
      (not (holding robot2 BreadSlice))
    )
  )
)