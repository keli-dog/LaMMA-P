(define (problem turn_on_tv_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Television - object
    CoffeeTable - object
  )
  (:init
    (at robot2 CoffeeTable)
    (at-location Television CoffeeTable)
    (not (inaction robot2))
  )
  (:goal
    (and
      (switch-on robot2 Television)
    )
  )
)