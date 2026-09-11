(define (problem slice_nutritional_supplies)
  (:domain robot1)
  (:objects
    robot1 - robot
    apple - object
    bread - object
    lettuce - object
    tomato - object
    knife - object
    countertop1 - object
    countertop2 - object
    diningtable - object
    fridge - object
  )
  (:init
    (at robot1 countertop1)
    (inaction robot1)
    (at-location knife countertop1)
    (at-location apple countertop1)
    (at-location bread diningtable)
    (at-location lettuce fridge)
    (at-location tomato countertop2)
  )
  (:goal
    (and
      (sliced apple)
      (sliced bread)
      (sliced lettuce)
      (sliced tomato)
    )
  )
)