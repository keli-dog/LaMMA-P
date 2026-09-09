(define (problem put_keychain_in_drawer)
  (:domain robot2)
  (:objects
    robot2 - robot
    KeyChain - object
    Drawer - object
    KeyChainLocation - object
  )
  (:init
    (not (inaction robot2))
    (at robot2 KeyChainLocation)
    (at-location KeyChain KeyChainLocation)
    (object-close robot2 Drawer)
  )
  (:goal
    (and
      (at-location KeyChain Drawer)
      (object-close robot2 Drawer)
    )
  )
)