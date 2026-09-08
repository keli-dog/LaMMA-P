(define (problem pickup_tomato_problem)
  (:domain robot1)
  (:objects 
    robot1 - robot
    tomato - object
    knife - object
    countertop - object
  )
  
  (:init 
    ; Robot is not inaction, implying it's ready to perform actions.
    (not (inaction robot1))
    
    ; Tomato and Knife are located on the CounterTop.
    (at-location tomato countertop)
    (at-location knife countertop)

    ; The robot starts at an unspecified location but needs to go to the Tomato first.
  )
  
  (:goal 
    ; Goal is for the Robot to be holding the Tomato.
    (holding robot1 tomato)
  )
)