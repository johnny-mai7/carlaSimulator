import carla

def main():
    # Connect to the CARLA server
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    
    # Read the XODR file
    xodr_file_path = 'C:\\CARLA\\PythonAPI\\util\\diverteddiamond.xodr'
    with open(xodr_file_path, 'r') as f:
        xodr_data = f.read()
    
    # Define parameters for map generation
    vertex_distance = 2.0  # in meters
    max_road_length = 500.0  # in meters
    wall_height = 0.0  # in meters
    extra_width = 0.6  # in meters
    
    # Generate the map
    generation_parameters = carla.OpendriveGenerationParameters(
        vertex_distance=vertex_distance,
        max_road_length=max_road_length,
        wall_height=wall_height,
        additional_width=extra_width,
        smooth_junctions=True,
        enable_mesh_visibility=True
    )
    world = client.generate_opendrive_world(xodr_data, generation_parameters)

    # Optionally set the spectator view
    spectator = world.get_spectator()
    spectator.set_transform(carla.Transform(
        carla.Location(x=0, y=0, z=50),
        carla.Rotation(pitch=-90)))
    
    # Spawn a ground plane using a suitable large static prop
    blueprint_library = world.get_blueprint_library()
    ground_bp = blueprint_library.find('static.prop.streetbarrier')  # Replace with your chosen blueprint

    # Calculate how many props are needed to cover the area
    num_props = 20  # Adjust based on the size of your map
    prop_size = 50  # Adjust based on the size of the prop
    
    for x in range(-num_props, num_props + 1):
        for y in range(-num_props, num_props + 1):
            ground_transform = carla.Transform(carla.Location(x=x * prop_size, y=y * prop_size, z=-1))
            world.try_spawn_actor(ground_bp, ground_transform)

    # Spawn a vehicle
    vehicle_bp = blueprint_library.find('vehicle.tesla.model3')
    spawn_points = world.get_map().get_spawn_points()
    if spawn_points:
        vehicle = world.spawn_actor(vehicle_bp, spawn_points[0])
        vehicle.set_autopilot(True)  # Optional: enable autopilot for the vehicle
    
    # Ensure the spectator view is set to follow the vehicle
    if vehicle:
        spectator.set_transform(vehicle.get_transform())
    
if __name__ == '__main__':
    main()
