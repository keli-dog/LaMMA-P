(define (problem close_drawer_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    Drawer1 - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 Drawer1)
  )
  (:goal
    (object-close robot1 Drawer1)
  )
)