def put_vase_on_sofa(robots):
    GoToObject(robots[0], 'Vase')
    PickupObject(robots[0], 'Vase')
    GoToObject(robots[0], 'Sofa')
    PutObject(robots[0], 'Vase', 'Sofa')

def execute_task():
    put_vase_on_sofa([robot0])