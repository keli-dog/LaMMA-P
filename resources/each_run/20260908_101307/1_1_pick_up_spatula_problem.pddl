(define (problem pick_up_spatula_problem)
  (:domain robot2)
  (:objects 
    robot2 - robot
    spatula - object
    countertop - object
  )
  (:init 
    (at robot2 countertop) ; Robot is at the location of the spatula.
    (at-location spatula countertop) ; Spatula is located on the countertop.
    (inaction robot2)
  )
  (:goal 
    (and 
      (holding robot2 spatula)
    )
  )
)