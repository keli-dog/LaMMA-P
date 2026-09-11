(define (problem turn_off_appliances_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    coffee_machine - object
    microwave - object
    toaster - object
    stove_knob1 - object
    stove_knob2 - object
    stove_knob3 - object
    stove_knob4 - object
    light_switch - object
    counter_top - object
    floor - object
  )
  (:init
    (at robot1 floor)
    (not (inaction robot1))
    (at-location coffee_machine counter_top)
    (at-location microwave counter_top)
    (at-location toaster counter_top)
    (at-location stove_knob1 counter_top)
    (at-location stove_knob2 counter_top)
    (at-location stove_knob3 counter_top)
    (at-location stove_knob4 counter_top)
    (at-location light_switch counter_top)
  )
  (:goal
    (and
      (switch-off robot1 coffee_machine)
      (switch-off robot1 microwave)
      (switch-off robot1 toaster)
      (switch-off robot1 stove_knob1)
      (switch-off robot1 stove_knob2)
      (switch-off robot1 stove_knob3)
      (switch-off robot1 stove_knob4)
      (switch-off robot1 light_switch)
    )
  )
)