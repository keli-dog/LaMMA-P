(define (problem put_book_in_box)
  (:domain robot1)
  (:objects
    robot1 - robot
    Book - object
    Box - object
    Desk - object
  )
  (:init
    (at robot1 Desk)
    (at-location Book Desk)
    (at-location Box Desk)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location Book Box)
    )
  )
)