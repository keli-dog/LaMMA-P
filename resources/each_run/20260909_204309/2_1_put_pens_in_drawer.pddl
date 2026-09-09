(define (problem put_pens_in_drawer)
  (:domain robot3)
  (:objects
    robot3 - robot
    Pen - object
    Drawer - object
    SideTable - object
  )
  (:init
    (at robot3 SideTable)
    (at-location Pen SideTable)
    (at-location Drawer SideTable)
    (not (inaction robot3))
    (object-close robot3 Drawer)
  )
  (:goal
    (and
      (at-location Pen Drawer)
      (object-close robot3 Drawer)
    )
  )
)