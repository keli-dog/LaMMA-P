(define (problem arrange_accessories_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    RemoteControl - object
    CoffeeTable - object
    SideTable - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 SideTable)
    (at-location RemoteControl SideTable)
  )
  (:goal
    (and
      (at-location RemoteControl CoffeeTable)
    )
  )
)