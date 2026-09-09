(define (problem clear_coffee_table_problem)
  (:domain robot4)
  (:objects
    robot4 - robot
    Book - object
    Mug - object
    CoffeeTable - object
    Shelf - object
  )
  (:init
    (at robot4 CoffeeTable)
    (at-location Book CoffeeTable)
    (at-location Mug CoffeeTable)
    (not (inaction robot4))
  )
  (:goal
    (and
      (not (at-location Book CoffeeTable))
      (not (at-location Mug CoffeeTable))
      (at-location Book Shelf)
      (at-location Mug Shelf)
    )
  )
)