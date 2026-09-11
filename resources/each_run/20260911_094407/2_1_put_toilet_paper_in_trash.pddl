(define (problem put_toilet_paper_in_trash)
  (:domain robot3)
  (:objects
    robot3 - robot
    ToiletPaper - object
    GarbageCan - object
    counterTop - object
    floor - object
  )
  (:init
    (at robot3 floor)
    (at-location ToiletPaper counterTop)
    (not (inaction robot3))
  )
  (:goal
    (and
      (at-location ToiletPaper GarbageCan)
    )
  )
)