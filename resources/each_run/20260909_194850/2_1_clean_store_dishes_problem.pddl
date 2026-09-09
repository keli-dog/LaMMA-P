(define (problem clean_store_dishes_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    plate - object
    cup - object
    sink - object
    cabinet - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location plate counterTop)
    (at-location cup counterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (cleaned robot2 plate)
      (cleaned robot2 cup)
      (at-location plate cabinet)
      (at-location cup cabinet)
      (object-close robot2 cabinet)
    )
  )
)