import sys
import math

def get_player_pos() -> None:
    coordinate_list = [input("Enter new coordinate as floats in format 'x,y,z': ")]
    coordinate_turple = ()
    try:
        int(coordinate_list)
        coordinate_turple.append(coordinate_list)
        print(f"Got a  first turple: {coordinate_turple:.1f}")
        x1={coordinate_turple[0]}
        y1={coordinate_turple[1]}
        z1={coordinate_turple[2]}
        print(f"It includes: X={x1}, Y={y1}, Z={z1}")
        #print(f"It includes: X={coordinate_turple[0]}, Y={coordinate_turple[1]}, Z={coordinate_turple[2]}")
        distance_to_center = math.sqrt((x1-0)**2 +(y1-0)**2 + (z1-0)**2)
        print(f"Distance to the center: {distance_to_center:.4f}")
    except ValueError:
        print(f"Invalid syntax '{argument}'")




def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    get_player_pos()

if __name__ == "__main__":
    ft_coordinate_system()