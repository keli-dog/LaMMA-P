(define (problem put_plate_in_microwave)
  (:domain robot1)
  (:objects
    robot1 - robot
    Plate - object
    Microwave - object
    CounterTop - object
  )
  (:init
    (at robot1 CounterTop)
    (at-location Plate CounterTop)
    (at-location Microwave CounterTop)
    (not (inaction robot1))
    (object-close robot1 Microwave)
    (switch-off robot1 Microwave)
    (not (holding robot1 Plate))
  )
  (:goal
    (and
      (at-location Plate Microwave)
      (object-close robot1 Microwave)
      (switch-on robot1 Microwave)
    )
  )
)