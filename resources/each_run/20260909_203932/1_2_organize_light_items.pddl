(define (problem organize_light_items)
  (:domain robot2)
  (:objects
    robot2 - robot
    watch - object
    keychain - object
    creditcard - object
    pen - object
    drawer - object
    floor - object
    initiallocation - object
  )
  (:init
    (at robot2 initiallocation)
    (at-location watch floor)
    (at-location keychain floor)
    (at-location creditcard floor)
    (at-location pen floor)
    (inaction robot2)
    (not (holding robot2 watch))
    (not (holding robot2 keychain))
    (not (holding robot2 creditcard))
    (not (holding robot2 pen))
  )
  (:goal
    (and
      (at-location watch drawer)
      (at-location keychain drawer)
      (at-location creditcard drawer)
      (at-location pen drawer)
    )
  )
)