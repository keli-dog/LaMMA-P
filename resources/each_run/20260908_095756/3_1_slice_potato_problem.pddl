(define (problem slice_potato_problem)
  (:domain robot1)
  
  (:objects 
    robot1 - robot
    potato - object
    knife - object
    counterTop - object
  )
  
  (:init 
    ; Robot's initial state and location.
    (at robot1 counterTop) 
    
    ; Initial locations of objects.
    (at-location potato counterTop)
    (at-location knife counterTop)

    ; The robot is not inaction initially.
    (not (inaction robot1))
  )
  
  (:goal 
    ; Goal: Slice the potato
    (sliced potato)
  )
)