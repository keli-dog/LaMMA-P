(define (problem put_book_on_bed)
  (:domain robot4)
  (:objects
    robot4 - robot
    Book - object
    Bed - object
    Desk - object
  )
  (:init
    (at robot4 Desk)
    (at-location Book Desk)
    (not (inaction robot4))
  )
  (:goal
    (and
      (at-location Book Bed)
    )
  )
)