(define (problem open_book_problem)
  (:domain robot3)
  (:objects
    robot3 - robot
    Book - object
    Shelf - object
  )
  (:init
    (at robot3 Shelf)
    (at-location Book Shelf)
    (not (inaction robot3))
  )
  (:goal
    (and
      (object-open robot3 Book)
    )
  )
)