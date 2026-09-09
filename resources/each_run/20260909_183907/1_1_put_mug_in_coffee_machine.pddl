(define (problem put_mug_in_coffee_machine)
  (:domain robot2)
  (:objects
    robot2 - robot
    Mug - object
    CoffeeMachine - object
    CounterTop - object
  )
  (:init
    (at robot2 CounterTop)
    (at-location Mug CounterTop)
    (at-location CoffeeMachine CounterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location Mug CoffeeMachine)
    )
  )
)