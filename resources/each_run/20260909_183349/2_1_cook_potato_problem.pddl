(define (problem cook_potato_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    pan - object
    stoveBurner - object
    stoveKnob - object
    counterTop - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 counterTop)
    (at-location pan counterTop)
    (at-location stoveBurner counterTop)
    (at-location stoveKnob counterTop)
  )
  (:goal
    (and
      (at-location pan stoveBurner)
      (switch-on robot1 stoveKnob)
    )
  )
)