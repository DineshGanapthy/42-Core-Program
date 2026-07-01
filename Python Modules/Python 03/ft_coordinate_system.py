import sys
import math

def get_player_pos() -> None:
    coordinate_list = []
    coordinate_tuple = ()
    first_coordinate = input("Enter new coordinate as floats in format 'x,y,z': ").split()
    coordinate_list.extend(first_coordinate)
    print(f"coordinate_list = {coordinate_list}")
    for i in coordinate_list:
        try:
            float(i)
            if len(coordinate_list) != 3:
                raise ValueError ("Only three Coordinates please")
        except ValueError:
            print(f"Invalid syntax")
            return 
    coordinate_tuple = tuple(coordinate_list)
    print(f"Got a first tuple: {coordinate_tuple}")
    x1 = float(coordinate_tuple[0])
    y1 = float(coordinate_tuple[1])
    z1 = float(coordinate_tuple[2])
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_to_center = math.sqrt((x1 - 0)**2 +(y1 - 0)**2 + (z1 - 0)**2)
    print(f"Distance to the center: {distance_to_center:.4f}\n")

#def get_coordinates_two() -> None:
    coordinate_list2 = []
    coordinate_tuple2 = ()
    second_coordinate = input("Enter new coordinate as floats in format 'x,y,z': ").split()
    coordinate_list2.extend(second_coordinate)
    for i in coordinate_list2:
        try:
            float(i)
            if len(coordinate_list2) != 3:
                raise ValueError ("Only three Coordinates please")
        except ValueError:
            print(f"Invalid syntax '{i}'")
            return
    coordinate_tuple2 = tuple(coordinate_list2)
    print(f"Got a first tuple: {coordinate_tuple2}")
    x2 = float(coordinate_tuple2[0])
    y2 = float(coordinate_tuple2[1])
    z2 = float(coordinate_tuple2[2])
    distance_between_points = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {distance_between_points:.4f}\n")
    
        # except ValueError:
        #     print(f"Invalid syntax '{i}'")
    # #for (argument) in coordinate_list:
    #     try:
    #         int(coordinate)
    #         coordinate_turple.append(coordinate_list)
    #         print(f"Got a  first turple: {coordinate_turple:.1f}")
    #         x1={coordinate_turple[0]}
    #         y1={coordinate_turple[1]}
    #         z1={coordinate_turple[2]}
    #         print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    #         #print(f"It includes: X={coordinate_turple[0]}, Y={coordinate_turple[1]}, Z={coordinate_turple[2]}")
    #         distance_to_center = math.sqrt((x1-0)**2 +(y1-0)**2 + (z1-0)**2)
    #         print(f"Distance to the center: {distance_to_center:.4f}")
    #     except ValueError:
    #         print(f"Invalid parameter '{argument}'")
    # coordinate_turple = ()
    # try:
    #     int(coordinate_list)
    #     coordinate_turple.append(coordinate_list)
    #     print(f"Got a  first turple: {coordinate_turple:.1f}")
    #     x1={coordinate_turple[0]}
    #     y1={coordinate_turple[1]}
    #     z1={coordinate_turple[2]}
    #     print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    #     #print(f"It includes: X={coordinate_turple[0]}, Y={coordinate_turple[1]}, Z={coordinate_turple[2]}")
    #     distance_to_center = math.sqrt((x1-0)**2 +(y1-0)**2 + (z1-0)**2)
    #     print(f"Distance to the center: {distance_to_center:.4f}")
    # except ValueError:
    #     print(f"Invalid syntax '{argument}'")




def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    get_player_pos()
    print("Get a second set of coordinates")
    #get_coordinates_two()

if __name__ == "__main__":
    ft_coordinate_system()