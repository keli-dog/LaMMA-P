(define (problem put_toiletpaper_in_trash)
  (:domain robot3)
  (:objects
    robot3 - robot
    ToiletPaper - object
    GarbageCan - object
    CounterTop - object
  )
  (:init
    (at robot3 CounterTop)
    (at-location ToiletPaper CounterTop)
    (at-location GarbageCan Floor)
    (not (inaction robot3))
  )
  (:goal
    (and
      (at-location ToiletPaper GarbageCan)
    )
  )
)