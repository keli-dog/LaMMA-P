(define (problem slice_potato_problem)
  (:domain robot1)
  
  (:objects 
    robot1 - robot
    potato - object
    knife - object
    countertop - object
  )
  
  (:init 
    ; Robot's initial state and location.
    (at robot1 countertop) 
    (inaction robot1)

    ; Initial locations of objects.
    (at-location potato countertop)
    (at-location knife countertop)
  )

  (:goal 
    ; Goal is to have the potato sliced.
    (sliced potato)
  )
)