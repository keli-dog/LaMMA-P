(define (problem go_to_tomato_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    tomato - object
    knife - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location tomato counterTop)
    (at-location knife counterTop)
    (inaction robot1)
  )
  (:goal
    (and
      (at robot1 tomato)
    )
  )
)