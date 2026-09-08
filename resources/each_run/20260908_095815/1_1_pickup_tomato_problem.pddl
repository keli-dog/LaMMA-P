(define (problem pickup_tomato_problem)
  (:domain robot1)
  (:objects 
    robot1 - robot
    tomato - object
    counterTop - object
  )
  (:init 
    (at-location tomato counterTop)  
    (inaction robot1)
    ; Adding the initial position of the robot to match with action preconditions.
    (at robot1 counterTop)
  )
  (:goal 
    (and 
      (holding robot1 tomato)
    )
  )
)