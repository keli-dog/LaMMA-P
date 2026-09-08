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
    (inaction robot1)

    ; Initial locations of objects.
    (at-location tomato countertop)
    (at-location knife countertop)
  )

  (:goal 
    ; The goal is to slice the tomato.
    (sliced tomato)
  )
)