#!/usr/bin/env python

import glob
import os
import sys
import carla
import random
import pygame
import numpy as np
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_s, K_a, K_d

# Initialize Pygame
pygame.init()

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

# Mapping of user-friendly vehicle names to their blueprint IDs
vehicle_name_to_bp = {
    'dodge charger': 'vehicle.dodge.charger_2020',
    'police charger': 'vehicle.dodge.police_charger_2020',
    'ford crown taxi': 'vehicle.ford.crown_taxi',
    'lincoln mkz': 'vehicle.lincoln.mkz_2020',
    'mercedes coupe': 'vehicle.mercedes.coupe_2020',
    'mini cooper': 'vehicle.mini.cooper_s_2021',
    'nissan patrol': 'vehicle.nissan.patrol_2021',
    'european hgv': 'vehicle.carla.european_hgv',
    'firetruck': 'vehicle.carla.firetruck',
    'cybertruck': 'vehicle.tesla.cybertruck',
    'ambulance': 'vehicle.ford.ambulance',
    'sprinter': 'vehicle.mercedes.sprinter',
    't2 van': 'vehicle.volkswagen.t2_2021',
    'mitsubishi bus': 'vehicle.mitsubishi.fusorosa',
    'audi a2': 'vehicle.audi.a2',
    'audi e-tron': 'vehicle.audi.e_tron',
    'audi tt': 'vehicle.audi.tt',
    'bmw gran tourer': 'vehicle.bmw.gran_tourer',
    'chevrolet impala': 'vehicle.chevrolet.impala',
    'citroen c3': 'vehicle.citroen.c3',
    'jeep wrangler': 'vehicle.jeep.wrangler_rubicon',
    'micro microlino': 'vehicle.micro.microlino',
    'nissan micra': 'vehicle.nissan.micra',
    'seat leon': 'vehicle.seat.leon',
    'tesla model 3': 'vehicle.tesla.model3',
    'toyota prius': 'vehicle.toyota.prius',
    'carlacola van': 'vehicle.carla.carlacola',
    'vw t2 van': 'vehicle.volkswagen.t2',
    'harley davidson low rider': 'vehicle.harley_davidson.low_rider',
    'kawasaki ninja': 'vehicle.kawasaki.ninja',
    'vespa zx 125': 'vehicle.vespa.zx_125',
    'yamaha yzf': 'vehicle.yamaha.yzf',
    'bh crossbike': 'vehicle.bh.crossbike',
    'diamondback century': 'vehicle.diamondback.century',
    'gazelle omafiets': 'vehicle.gazelle.omafiets'
}

# Available maps in CARLA
available_maps = [
    'Town01',
    'Town02',
    'Town03',
    'Town04',
    'Town05',
    'Town06',
    'Town07',
    'Town08',
    'Town09',
    'Town10HD'
]

# Function to get a random or specified blueprint
def get_blueprint(world, filter):
    blueprint_library = world.get_blueprint_library()
    blueprint = random.choice(blueprint_library.filter(filter))
    return blueprint

# Function to spawn a vehicle
def spawn_vehicle(world, vehicle_type=None, transform=None):
    if vehicle_type is None:
        vehicle_bp = get_blueprint(world, 'vehicle.*')
    else:
        vehicle_bp = world.get_blueprint_library().find(vehicle_name_to_bp[vehicle_type.lower()])
    if transform is None:
        transform = random.choice(world.get_map().get_spawn_points())
    vehicle = world.spawn_actor(vehicle_bp, transform)
    vehicle.set_autopilot(True)
    print(f"Spawned vehicle: {vehicle.type_id} at {transform.location}")
    return vehicle

# Function to spawn a pedestrian
def spawn_pedestrian(world, max_attempts=10):
    pedestrian_bp = get_blueprint(world, 'walker.pedestrian.*')
    for _ in range(max_attempts):
        transform = carla.Transform(world.get_random_location_from_navigation())
        if world.get_map().get_waypoint(transform.location) is not None:
            pedestrian = world.try_spawn_actor(pedestrian_bp, transform)
            if pedestrian is not None:
                # Set pedestrian's movement mode to walking
                pedestrian_control = carla.WalkerControl()
                pedestrian_control.speed = 1.0  # Set walking speed
                pedestrian_control.direction = carla.Vector3D(1.0, 0.0, 0.0)  # Set initial direction
                pedestrian_control.use_default_keys = False
                pedestrian.apply_control(pedestrian_control)
                print(f"Spawned pedestrian: {pedestrian.type_id} at {transform.location}")
                return pedestrian
    print("Failed to spawn pedestrian after multiple attempts.")
    return None



def change_weather(world, weather_type):
    weather_presets = {
        'clear': carla.WeatherParameters.ClearNoon,
        'cloudy': carla.WeatherParameters.CloudyNoon,
        'rain': carla.WeatherParameters.WetNoon,
        'storm': carla.WeatherParameters.WetCloudyNoon,
        'foggy': carla.WeatherParameters.MidRainyNoon
    }
    if weather_type in weather_presets:
        weather = weather_presets[weather_type]
        world.set_weather(weather)
        print(f"Weather changed to {weather_type}")
    else:
        print(f"Weather type {weather_type} not recognized")

def change_map(client, map_name):
    if map_name in available_maps:
        world = client.load_world(map_name)
        print(f"Map changed to {map_name}")
        return world
    else:
        print(f"Map name {map_name} not recognized")
        return client.get_world()

def process_image(image, display_surface):
    array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
    array = np.reshape(array, (image.height, image.width, 4))
    array = array[:, :, :3]  # Convert BGRA to BGR
    array = array[:, :, ::-1]  # Convert BGR to RGB
    surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
    display_surface.blit(surface, (0, 0))
    pygame.display.flip()

# Inside the toggle_auto_driving function
def toggle_manual_driving(vehicle, enable_manual, camera, display_surface):
    if enable_manual:
        # Keep autopilot enabled when manual driving is toggled on
        vehicle.set_autopilot(True)
        if display_surface is None:  # Check if display surface is not created
            pygame.init()
            window_size = (800, 600)
            display_surface = pygame.display.set_mode(window_size)
            pygame.display.set_caption('CARLA Auto Control')
        camera.listen(lambda image: process_image(image, display_surface))
    else:
        # Disable manual controls and stop listening for camera images
        vehicle.set_autopilot(True)  # Make sure autopilot is enabled
        camera.stop()
        pygame.quit()



def spawn_camera(world, vehicle):
    camera_bp = get_blueprint(world, 'sensor.camera.rgb')
    camera_transform = carla.Transform(carla.Location(x=-5.5, z=2.5))
    camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)
    return camera

def handle_control_events(vehicle):
    control = carla.VehicleControl()
    keys = pygame.key.get_pressed()
    
    if keys[K_UP] or keys[K_w]:
        control.throttle = 1.0
        control.reverse = False
    elif keys[K_DOWN] or keys[K_s]:
        control.throttle = 1.0
        control.reverse = True
    else:
        control.throttle = 0.0

    if keys[K_LEFT] or keys[K_a]:
        control.steer = -1.0
    elif keys[K_RIGHT] or keys[K_d]:
        control.steer = 1.0
    else:
        control.steer = 0.0

    vehicle.apply_control(control)
    
def toggle_vehicle_pov(vehicles, cameras):
    print("Select a vehicle to view POV:")
    for i, vehicle in enumerate(vehicles):
        print(f"{i}. {vehicle.type_id}")
    vehicle_idx = input("Enter the index of the vehicle: ")
    if vehicle_idx.isdigit():
        idx = int(vehicle_idx)
        if 0 <= idx < len(vehicles):
            camera = cameras[idx]
            return camera
        else:
            print("Invalid vehicle index.")
    else:
        print("Invalid input.")
        
def process_image(image, display_surface):
    if isinstance(image, carla.SensorData):
        array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
        array = np.reshape(array, (image.height, image.width, 4))
        array = array[:, :, :3]  # Convert BGRA to BGR
        array = array[:, :, ::-1]  # Convert BGR to RGB
        surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
        display_surface.blit(surface, (0, 0))
        pygame.display.flip()
    else:
        print("Received unknown sensor data.")


def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

    vehicles = []  # Track spawned vehicles
    pedestrians = []
    cameras = []
    manual_driving_flags = []

    display_surface = None

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            print("\nCARLA Simulator Control Menu:")
            print("1. Add vehicle")
            print("2. Add pedestrian")
            print("3. Change weather")
            print("4. Change map")
            print("5. View vehicle POV")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print("Choose vehicle:")
                print("1. Random")
                print("Available vehicles:")
                for index, vehicle_name in enumerate(vehicle_name_to_bp.keys()):
                    print(f"{index + 2}. {vehicle_name}")
                vehicle_choice = input("Enter vehicle number or 'random': ")
                if vehicle_choice.isdigit():
                    vehicle_index = int(vehicle_choice) - 2  # Adjust index for user-selected vehicles
                    if 0 <= vehicle_index < len(vehicle_name_to_bp):
                        selected_vehicle = list(vehicle_name_to_bp.keys())[vehicle_index]
                        vehicle = spawn_vehicle(world, selected_vehicle)
                        vehicles.append(vehicle)
                        manual_driving_flags.append(False)
                        cameras.append(spawn_camera(world, vehicle))
                    else:
                        print("Invalid vehicle number.")
                elif vehicle_choice.lower() == 'random':
                    selected_vehicle = random.choice(list(vehicle_name_to_bp.keys()))
                    vehicle = spawn_vehicle(world, selected_vehicle)
                    vehicles.append(vehicle)
                    manual_driving_flags.append(False)
                    cameras.append(spawn_camera(world, vehicle))
                else:
                    print("Invalid input.")
            elif choice == '2':
                pedestrians.append(spawn_pedestrian(world))
            elif choice == '3':
                print("Available weather types: clear, cloudy, rain, storm, foggy")
                weather_type = input("Enter weather type: ")
                change_weather(world, weather_type)
            elif choice == '4':
                print(f"Available maps: {', '.join(available_maps)}")
                map_name = input("Enter map name: ")
                world = change_map(client, map_name)
            elif choice == '5':
                if not cameras:
                    print("No vehicles spawned yet.")
                else:
                    camera = toggle_vehicle_pov(vehicles, cameras)
                    display_surface = pygame.display.get_surface() if pygame.get_init() else None
                    process_image(camera.read(), display_surface)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    finally:
        print("Cleaning up spawned actors...")
        for vehicle in vehicles:
            vehicle.destroy()
        for pedestrian in pedestrians:
            pedestrian.destroy()
        for camera in cameras:
            camera.destroy()
        print("All actors destroyed. Exiting...")
        if pygame.get_init():
            pygame.quit()

if __name__ == '__main__':
    main()
