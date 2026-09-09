(define (problem handleegg_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    egg - object
    pot - object
    counterTop - object
    initiallocation - object
  )
  (:init
    (at robot1 initiallocation)
    (at-location egg counterTop)
    (at-location pot counterTop)
    (inaction robot1)
    (not (holding robot1 egg))
  )
  (:goal
    (and
      (at-location egg pot)
      (not (holding robot1 egg))
    )
  )
)