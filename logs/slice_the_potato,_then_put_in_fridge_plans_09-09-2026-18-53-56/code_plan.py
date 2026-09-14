def slice_potato_and_store(robot):
    GoToObject(robot, 'Knife')
    PickupObject(robot, 'Knife')
    GoToObject(robot, 'Potato')
    SliceObject(robot, 'Potato')
    GoToObject(robot, 'CounterTop')
    PutObject(robot, 'Knife', 'CounterTop')
    GoToObject(robot, 'Potato')
    PickupObject(robot, 'Potato')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Potato', 'Fridge')
    CloseObject(robot, 'Fridge')

def execute_task():
    slice_potato_and_store(robots[0])