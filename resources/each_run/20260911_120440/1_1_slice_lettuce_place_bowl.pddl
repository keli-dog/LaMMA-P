(define (problem slice_lettuce_place_bowl)
  (:domain robot1)
  (:objects
    robot1 - robot
    lettuce - object
    bowl - object
    counterTop1 - object
    counterTop2 - object
    floor - object
  )
  (:init
    (at robot1 floor)
    (at-location lettuce counterTop1)
    (at-location bowl counterTop2)
    (inaction robot1)
  )
  (:goal
    (and
      (sliced lettuce)
      (at-location lettuce bowl)
    )
  )
)