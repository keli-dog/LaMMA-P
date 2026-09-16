(define (problem clear_coffee_table_problem)
  (:domain robot4)
  (:objects
    robot4 - robot
    CoffeeTable - object
    Book - object
    Mug - object
    Shelf - object
  )
  (:init
    (not (inaction robot4))
    (at robot4 Shelf)
    (at-location Book CoffeeTable)
    (at-location Mug CoffeeTable)
  )
  (:goal
    (and
      (at-location Book Shelf)
      (at-location Mug Shelf)
    )
  )
)