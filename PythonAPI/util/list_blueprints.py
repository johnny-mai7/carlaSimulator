import carla

def list_blueprints():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    
    # List all blueprints to find a suitable ground plane
    for blueprint in blueprint_library.filter('static.prop.*'):
        print(blueprint.id)
    
if __name__ == '__main__':
    list_blueprints()
