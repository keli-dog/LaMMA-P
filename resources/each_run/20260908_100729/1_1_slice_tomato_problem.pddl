(define (problem slice_tomato_problem)
  (:domain robot1)
  (:objects 
    robot1 - robot
    tomato - object
    knife - object
    countertop - object
  )
  
  (:init 
    ; Robot's initial state and location.
    (at robot1 countertop) 

    ; Initial locations of objects.
    (at-location tomato countertop)
    (at-location knife countertop)

    ; The robot is not inaction initially.
    (not (inaction robot1))
  )
  
  (:goal 
    ; Goal: Slice the tomato
    (sliced tomato)
  )
)