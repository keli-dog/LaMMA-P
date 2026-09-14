def put_box_on_sofa_and_bowl_in_box(robots):
    GoToObject(robots[0], 'Box')
    PickupObject(robots[0], 'Box')
    GoToObject(robots[0], 'Sofa')
    PutObject(robots[0], 'Box', 'Sofa')
    GoToObject(robots[0], 'Bowl')
    PickupObject(robots[0], 'Bowl')
    GoToObject(robots[0], 'Box')
    PutObject(robots[0], 'Bowl', 'Box')

def execute_task():
    put_box_on_sofa_and_bowl_in_box([robot0])