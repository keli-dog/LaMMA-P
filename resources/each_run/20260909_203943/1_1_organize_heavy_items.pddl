(define (problem organize_heavy_items)
  (:domain robot1)
  (:objects
    robot1 - robot
    laptop - object
    book - object
    vase - object
    dresser - object
    floor - object
    initiallocation - object
  )
  (:init
    (at robot1 initiallocation)
    (at-location laptop floor)
    (at-location book floor)
    (at-location vase floor)
    (inaction robot1)
    (not (holding robot1 laptop))
    (not (holding robot1 book))
    (not (holding robot1 vase))
  )
  (:goal
    (and
      (at-location laptop dresser)
      (at-location book dresser)
      (at-location vase dresser)
    )
  )
)