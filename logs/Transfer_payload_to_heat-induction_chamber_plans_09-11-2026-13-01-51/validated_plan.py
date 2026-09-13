```lisp
(define (problem slice_potato_apple)
  (:domain robot4)
  (:objects
    robot4 - robot
    potato - object
    apple - object
    knife - object
    pot - object
    counterTop - object
  )
  (:init
    (at robot4 counterTop)
    (at-location potato counterTop)
    (at-location apple counterTop)
    (at-location knife counterTop)
    (at-location pot counterTop)
  )
  (:goal
    (and
      (sliced potato)
      (sliced apple)
    )
  )
)
```