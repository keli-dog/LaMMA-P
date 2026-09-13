```lisp
(define (problem close_all_open)
  (:domain robot3)
  (:objects
    robot3 - robot
    drawer1 drawer2 drawer3 drawer4 dresser shelf floor - object
  )
  (:init
    (at robot3 floor)
    (inaction robot3)
    (object-open robot3 drawer1)
    (object-open robot3 drawer2)
    (object-open robot3 drawer3)
    (object-open robot3 drawer4)
    (object-open robot3 dresser)
    (object-open robot3 shelf)
  )
  (:goal
    (and
      (object-close robot3 drawer1)
      (object-close robot3 drawer2)
      (object-close robot3 drawer3)
      (object-close robot3 drawer4)
      (object-close robot3 dresser)
      (object-close robot3 shelf)
    )
  )
)
```