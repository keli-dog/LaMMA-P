(define (problem place_soap_in_sink)
  (:domain robot1)
  (:objects
    robot1 - robot
    SoapBar - object
    Sink - object
    CounterTop - object
    Floor - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 CounterTop)
    (at-location SoapBar CounterTop)
    (at-location Sink Floor)
  )
  (:goal
    (and
      (at-location SoapBar Sink)
    )
  )
)