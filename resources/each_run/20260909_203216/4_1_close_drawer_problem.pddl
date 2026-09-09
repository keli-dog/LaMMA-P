(define (problem close_drawer_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Drawer2 - object
    Dresser - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 Dresser)
    (at-location Drawer2 Dresser)
  )
  (:goal
    (and
      (object-close robot1 Drawer2)
    )
  )
)