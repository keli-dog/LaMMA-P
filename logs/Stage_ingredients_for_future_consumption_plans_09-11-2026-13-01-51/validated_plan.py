```lisp
(define (problem prep_pot)
  (:domain robot2)
  (:objects
    robot2 - robot
    pot - object
    counterTop - object
    floor - object
    cabinet - object
  )
  (:init
    (at robot2 floor)
    (at-location pot cabinet)
  )
  (:goal
    (at-location pot counterTop)
  )
)
```