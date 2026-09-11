(define (problem move_apple_to_fridge)
  (:domain robot1)
  (:objects
    robot1 - robot
    Apple - object
    Fridge - object
    CounterTop - object
    Floor - object
  )
  (:init
    (at robot1 Floor)
    (at-location Apple CounterTop)
    (inaction robot1)
  )
  (:goal
    (at-location Apple Fridge)
  )
)