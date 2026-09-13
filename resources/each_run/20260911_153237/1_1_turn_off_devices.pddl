(define (problem turn_off_devices)
  (:domain robot1)
  (:objects
    robot1 - robot
    FloorLamp - object
    LightSwitch - object
    Television - object
    Laptop - object
    Floor - object
  )
  (:init
    (at robot1 Floor)
    (switch-on robot1 FloorLamp)
    (switch-on robot1 LightSwitch)
    (switch-on robot1 Television)
    (switch-on robot1 Laptop)
  )
  (:goal
    (and
      (switch-off robot1 FloorLamp)
      (switch-off robot1 LightSwitch)
      (switch-off robot1 Television)
      (switch-off robot1 Laptop)
    )
  )
)