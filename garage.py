from typing import Any, Optional
from collections import defaultdict
from vehicle import Vehicle, Truck, Car


PLATE_ERROR = "Not a valid plate number!"
SPEED_ERROR = "Not a valid max speed!"
NO_VEHICLES_ERROR = "No relevant vehicles!"


class Garage:

    def __init__(self) -> None:
        self.garage_db: dict[str, list[Vehicle]] = {"cars": [], "trucks": []}
        self.truck_contents: defaultdict[str, int] = defaultdict(int)
        self.db_modified: bool = False
        self.fastest_vehicle_cache: Optional[Vehicle] = None
        self.most_common_truck_content_cache: Optional[str] = None

    def _add_vehicle(self, vehicle: Vehicle) -> None:
        if isinstance(vehicle, Truck):
            self.garage_db["trucks"].append(vehicle)
            self.truck_contents[vehicle.contents] += 1
        else:
            self.garage_db["cars"].append(vehicle)
        if (self.fastest_vehicle_cache is None) or (vehicle.speed > self.fastest_vehicle_cache.speed):
            self.fastest_vehicle_cache = vehicle

    def add_vehicle(self) -> None:
        print("Fill Vehicle Details: ")
        response = input("is it a (T)ruck or regular (C)ar? (enter T/C) ").lower()
        while not response[0] in ("t", "c"):
            response = input("is it a (T)ruck or regular (C)ar? (enter T/C) ").lower()
        is_truck = response[0] == "t"
        plate_number = "000000"
        speed = -1
        while True:
            response = input("Enter plate number: ")
            try:
                _ = int(response)
                plate_number = response
            except Exception:
                print(PLATE_ERROR)
                continue
            if 1 < len(response) < 10:
                break
            print(PLATE_ERROR)
        while True:
            response = input("Enter max speed: ")
            try:
                speed = int(response)
            except Exception:
                print(SPEED_ERROR)
            if 0 < speed < 500:
                break
            print(SPEED_ERROR)

        vehicle: Vehicle
        if not is_truck:
            vehicle = Car(plate_number, speed)
        else:
            vehicle = Truck(plate_number, speed, input("Enter Truck payload: "))
        self._add_vehicle(vehicle)

    def _remove_vehicle(self, plate_number: str) -> bool:
        for vehicle_type in ("cars", "trucks"):
            for i, vehicle in enumerate(self.garage_db[vehicle_type]):
                if vehicle.plate_number == plate_number:
                    del self.garage_db[vehicle_type][i]
                    self.db_modified = True
                    return True
        return False

    def remove_vehicle(self) -> None:
        plate_number = input("Enter plate number of vehicle to remove: ")
        if not self._remove_vehicle(plate_number):
            print(NO_VEHICLES_ERROR)

    def _get_fastest_vehicle(self) -> Vehicle:
        return self.fastest_vehicle_cache if self.fastest_vehicle_cache is not None else Car("000000", 0)

    def get_fastest_vehicle(self) -> None:
        fastest_vehicle = self._get_fastest_vehicle()
        if fastest_vehicle.plate_number == "000000":
            print(NO_VEHICLES_ERROR)
        else:
            print(f"Fastest Vehicle: Plate Number: {fastest_vehicle.plate_number}, Max Speed: {fastest_vehicle.speed}")

    def _get_pretty_plates(self) -> list[str]:
        plate_numbers = [vehicle.plate_number for vehicle in self.garage_db["cars"] + self.garage_db["trucks"]]
        pretty_plates = [plate for plate in plate_numbers if "42" in plate]
        return pretty_plates

    def get_pretty_plates(self) -> None:
        print(self._get_pretty_plates())

    def _sync_trucks_contents(self) -> None:
        if not self.db_modified:
            return
        self.truck_contents = defaultdict(int)
        for truck in self.garage_db["trucks"]:
            assert isinstance(truck, Truck)
            self.truck_contents[truck.contents] += 1
        self.db_modified = False

    def _get_common_truck_content(self) -> Optional[str]:
        self._sync_trucks_contents()
        if not self.truck_contents:
            return None
        common_content = max(self.truck_contents, key=lambda content: self.truck_contents[content])
        return common_content

    def get_common_truck_content(self) -> None:
        common_content = self._get_common_truck_content()
        if common_content is None:
            print(NO_VEHICLES_ERROR)
        else:
            print(f"Most common truck content: {common_content}")

    def _get_trucks_contents(self) -> list[str]:
        self._sync_trucks_contents()
        return list(self.truck_contents.keys())

    def get_trucks_contents(self) -> None:
        for content in self._get_trucks_contents():
            print(content)

    def empty_db(self) -> None:
        self.garage_db = {"cars": [], "trucks": []}
        self.truck_contents = defaultdict(int)
        self.db_modified = False
        self.fastest_vehicle_cache = None
