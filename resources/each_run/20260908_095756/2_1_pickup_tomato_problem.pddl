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
  )
  (:goal 
    (and 
      (holding robot1 tomato)
    )
  )
)