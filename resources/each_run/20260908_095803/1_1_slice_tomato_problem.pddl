(define (problem slice_tomato_problem)
  (:domain robot1)
  (:objects 
    robot1 - robot
    tomato - object
    knife - object
    countertop - object
  )
  (:init 
    (at robot1 countertop) ; Robot is at the counter where objects are located.
    (at-location tomato countertop) ; Tomato is on the counter.
    (at-location knife countertop) ; Knife is also on the counter.
    (inaction robot1)
  )
  (:goal
    (and 
      (sliced tomato) ; The goal is to slice the tomato.
    )
  )
)