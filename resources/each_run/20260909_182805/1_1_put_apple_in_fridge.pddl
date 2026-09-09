(define (problem put_apple_in_fridge)
  (:domain robot1)
  (:objects
    robot1 - robot
    Apple - object
    Fridge - object
    CounterTop - object
  )
  (:init
    (at robot1 CounterTop)
    (at-location Apple CounterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location Apple Fridge)
    )
  )
)