(define (problem go_to_spatula_problem)
  (:domain robot2)
  (:objects 
    robot2 - robot
    spatula - object
    countertop - object ; Assuming spatula is on countertop for this example.
  )
  
  (:init 
    (at robot2 countertop) ; Robot starts at the countertop where the spatula might be located.
    (inaction robot2)
    (at-location spatula countertop) ; Spatula's location
  )

  (:goal 
    (and 
      (at robot2 spatula)
    )
  )
)