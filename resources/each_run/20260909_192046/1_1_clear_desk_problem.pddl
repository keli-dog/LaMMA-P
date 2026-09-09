(define (problem clear_desk_problem)
  (:domain robot3)
  (:objects
    robot3 - robot
    desk - object
    shelf - object
    book - object
    mug - object
    pen - object
    floor - object
  )
  (:init
    (not (inaction robot3))
    (at robot3 floor)
    (at-location book desk)
    (at-location mug desk)
    (at-location pen desk)
  )
  (:goal
    (and
      (at-location book shelf)
      (at-location mug shelf)
      (at-location pen shelf)
    )
  )
)