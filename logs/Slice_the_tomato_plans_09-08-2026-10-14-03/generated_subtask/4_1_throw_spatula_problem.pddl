(define (problem throw_spatula_problem)
  (:domain robot1)
  (:objects 
    robot1 - robot
    spatula - object
    garbageCan - object
    counterTop - object
  )
  (:init 
    (at robot1 counterTop) ; Robot is at the CounterTop.
    (at-location spatula counterTop) ; Spatula is located on the CounterTop.
    (at-location garbageCan counterTop) ; Garbage can is also located on the CounterTop.
    (inaction robot1)
  )
  (:goal 
    (and
      (not(holding robot1 spatula)) ; The goal is to have the spatula thrown into the garbage can, so it should not be held by the robot anymore.
    )
  )
)