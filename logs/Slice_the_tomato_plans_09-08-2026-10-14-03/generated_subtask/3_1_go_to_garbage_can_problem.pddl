(define (problem go_to_garbage_can_problem)
  (:domain robot1)
  (:objects 
    robot1 - robot
    GarbageCan - object
    Floor - object
  )
  (:init 
    (at robot1 Floor) ; Assume the robot starts on the floor.
    (inaction robot1) ; The robot is not in action initially.
    (at-location GarbageCan Floor) ; The garbage can is located on the floor.
  )
  (:goal 
    (and
      (at robot1 GarbageCan)
    )
  )
)