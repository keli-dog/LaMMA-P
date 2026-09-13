(define (problem organize_inventory_robot1)
  (:domain robot1)
  (:objects
    robot1 - robot
    book - object
    laptop - object
    remotecontrol - object
    newspaper - object
    box - object
    drawer1 - object
    initialLocation - object
    floor - object
  )
  (:init
    (at robot1 initialLocation)
    (at-location book floor)
    (at-location laptop floor)
    (at-location remotecontrol floor)
    (at-location newspaper floor)
    (at-location box floor)
    (inaction robot1)
    (not (holding robot1 book))
    (not (holding robot1 laptop))
    (not (holding robot1 remotecontrol))
    (not (holding robot1 newspaper))
    (not (holding robot1 box))
    (not (object-open robot1 drawer1))
  )
  (:goal
    (and
      (at-location book drawer1)
      (at-location laptop drawer1)
      (at-location remotecontrol drawer1)
      (at-location newspaper drawer1)
      (at-location box drawer1)
      (object-close robot1 drawer1)
    )
  )
)