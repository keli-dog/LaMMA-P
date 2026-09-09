(define (problem refrigerate_perishables)
  (:domain robot1)
  (:objects
    robot1 - robot
    Egg - object
    Fridge - object
    CounterTop - object
  )
  (:init
    (at robot1 CounterTop)
    (at-location Egg CounterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location Egg Fridge)
      (object-close robot1 Fridge)
    )
  )
)