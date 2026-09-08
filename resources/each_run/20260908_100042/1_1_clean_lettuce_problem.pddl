(define (problem clean_lettuce_problem)
  (:domain robot1)
  (:objects 
    robot1 - robot
    Lettuce - object
    SinkBasin - object
    CounterTop - object
  )
  (:init 
    (at robot1 CounterTop) ; Robot is initially at the countertop.
    (at-location Lettuce CounterTop) ; The lettuce is on the countertop.
    (inaction robot1)
  )
  (:goal 
    (and 
      (cleaned Lettuce) ; Goal: Clean the lettuce
      (at-location Lettuce CounterTop) ; Place cleaned lettuce back at the countertop
    )
  )
)