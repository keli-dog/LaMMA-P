```lisp
(define (problem throwspatula_problem_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    spatula - object
    garbageCan - object
    storageArea - object
  )

  (:init
    (at robot2 storageArea)
    (at-location spatula garbageCan)
    (inaction robot2)
    (not (holding robot2 spatula))
  )

  (:goal
    (and
      (not (holding robot2 spatula))
      (at-location spatula garbageCan)
    )
  )

)
```