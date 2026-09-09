(define (problem break_alarmclock_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    AlarmClock - object
    Desk - object
  )
  (:init
    (at robot1 Desk)
    (at-location AlarmClock Desk)
    (not (inaction robot1))
  )
  (:goal
    (and
      (break robot1 AlarmClock)
    )
  )
)