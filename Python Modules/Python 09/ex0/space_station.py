from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional

class SpaceStaton(BaseModel):
    station_id: str = Field(min_lenght=3, max_lenght=10)
    name: str = Field(min_lenght=1, max_lenght=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintence: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_lenght=200)

def main() -> None:
    print("Space Station Data Validation")
    try:
        print("=====================================")
        station = SpaceStaton(
            station_id="ISS001",
            name = "International Space Station",
            crew_size = 6,
            power_level = 85.5,
            oxygen_level = 92.3,
            last_maintence = datetime.now(),
            is_operational = True 
        )

        if station.is_operational:
            status = "Operational"
        else:
            status = "Not Operational"

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        if station.crew_size == 1:
            print(f"Crew: {station.crew_size} person")
        else:
            print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {status}")


    except ValidationError as e:
        print("\n=====================================")
        print("Validation Error:")
        for error in e.errors():
            print(error["msg"])

    try:
        bad_station = SpaceStaton(
            station_id="ISS001",
            name = "International Space Station",
            crew_size = 25,
            power_level = 85.5,
            oxygen_level = 92.3,
            last_maintence = datetime.now(),
            is_operational = True 
        )

        # if station.is_operational:
        #     status = "Operational"
        # else:
        #     status = "Not Operational"

        # print("Valid station created:")
        # print(f"ID: {station.station_id}")
        # print(f"Name: {station.name}")
        # if station.crew_size == 1:
        #     print(f"Crew: {station.crew_size} person")
        # else:
        #     print(f"Crew: {station.crew_size} people")
        # print(f"Power: {station.power_level}%")
        # print(f"Oxygen: {station.oxygen_level}%")
        # print(f"Status: {station.station_id}")


    except ValidationError as e:
        print("\n=====================================")
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])



if __name__ == "__main__":
    main()
