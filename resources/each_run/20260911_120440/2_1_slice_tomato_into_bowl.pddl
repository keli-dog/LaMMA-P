(define (problem slice_tomato_into_bowl)
  (:domain robot2)
  (:objects
    robot2 - robot
    tomato - object
    bowl - object
    counterTop1 - object
    counterTop2 - object
  )
  (:init
    (not (inaction robot2))
    (at robot2 counterTop1)
    (at-location tomato counterTop1)
    (at-location bowl counterTop2)
  )
  (:goal
    (and
      (sliced tomato)
      (at-location tomato bowl)
    )
  )
)