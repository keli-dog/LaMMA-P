(define (problem put_book_in_box)
  (:domain robot1)
  (:objects
    robot1 - robot
    Book - object
    Box - object
    Desk - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 Desk)
    (at-location Book Desk)
    (at-location Box Desk)
  )
  (:goal
    (and
      (at-location Book Box)
    )
  )
)