(define (problem organize_inventory_robot2)
  (:domain robot2)
  (:objects
    robot2 - robot
    creditcard - object
    pen - object
    keychain - object
    watch - object
    drawer2 - object
    initialLocation - object
    floor - object
  )
  (:init
    (at robot2 initialLocation)
    (at-location creditcard floor)
    (at-location pen floor)
    (at-location keychain floor)
    (at-location watch floor)
    (not (inaction robot2))
    (not (holding robot2 creditcard))
    (not (holding robot2 pen))
    (not (holding robot2 keychain))
    (not (holding robot2 watch))
    (not (object-open robot2 drawer2))
  )
  (:goal
    (and
      (at-location creditcard drawer2)
      (at-location pen drawer2)
      (at-location keychain drawer2)
      (at-location watch drawer2)
      (object-close robot2 drawer2)
    )
  )
)