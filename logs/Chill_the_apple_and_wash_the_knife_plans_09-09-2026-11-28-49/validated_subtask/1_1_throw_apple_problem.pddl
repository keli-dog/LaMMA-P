(define (problem throw_apple_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    Apple - object
    GarbageCan - object
    counterTop - object
  )
  (:init
    (holding robot2 Apple)
    (sliced Apple)
    (at-location GarbageCan counterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location Apple GarbageCan)
    )
  )
)