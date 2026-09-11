(define (problem sanitize_carbohydrate_items)
  (:domain robot1)
  (:objects
    robot1 - robot
    apple - object
    bread - object
    potato - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (cleaned robot1 apple)
      (cleaned robot1 bread)
      (cleaned robot1 potato)
    )
  )
)