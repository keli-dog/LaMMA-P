(define (problem put_remote_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    RemoteControl - object
    CoffeeTable - object
    SideTable - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 CoffeeTable)
    (at-location RemoteControl CoffeeTable)
  )
  (:goal
    (and
      (at-location RemoteControl SideTable)
    )
  )
)