(define (problem put_items_in_drawer_and_shelf)
  (:domain robot2)
  (:objects
    robot1 - robot
    pen creditcard keychain watch remotecontrol - object
    book newspaper - object
    drawer1 shelf garbagecan - object
    coffeetable sidetable floor - object
  )
  (:init
    (at robot1 floor)
    (at-location pen coffeetable)
    (at-location creditcard coffeetable)
    (at-location keychain sidetable)
    (at-location watch sidetable)
    (at-location remotecontrol coffeetable)
    (at-location book coffeetable)
    (at-location newspaper sidetable)
  )
  (:goal
    (and
      (at-location pen drawer1)
      (at-location creditcard drawer1)
      (at-location keychain drawer1)
      (at-location watch drawer1)
      (at-location remotecontrol drawer1)
      (at-location book shelf)
      (at-location newspaper garbagecan)
    )
  )
)