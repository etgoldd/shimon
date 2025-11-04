from vehicle import Vehicle, Truck, Car

PLATE_ERROR = "Not a valid plate number!"
SPEED_ERROR = "Not a valid max speed!"

class Garage:
    
    def __init__(self):
        garage_db: dict[str, list[Vehicle]]
        truck_contents: dict[str, int]
        db_modified: bool
        
    def _add_vehicle(self, vehicle: Vehicle) -> None:
        pass

    def add_vehicle(self) -> None:
        print("Fill Vehicle Details: ")
        response = input("is it a (T)ruck or regular (C)ar? (enter T/C) ").lower()
        while not response[0]in ("t", "c"):
            response = input("is it a (T)ruck or regular (C)ar? (enter T/C) ").lower()
        is_truck = response[0] == "t"
        plate_number = -1
        speed = -1
        while True:
            response = input("Enter plate number: ")
            try: 
                _ = int(response)
                plate_number = response
            except Exception:
                print(PLATE_ERROR)
                continue
            if 6 < len(response) < 10:
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
        
        if not is_truck:
            vehicle = Car(plate_number, speed)
        else: 
            vehicle = Truck(plate_number, speed, input("Enter Truck payload: "))
        self._add_vehicle(vehicle)
    

    def _get_fastest_vehicle(self) -> Vehicle:
        pass

    def get_fastest_vehicle(self) -> None:
        print(self._get_fastest_vehicle())

    def _get_pretty_plates(self) -> list[str]:
        pass

    def get_pretty_plates(self) -> None:
        print(self._get_pretty_plates())

    def _sync_trucks_contents(self) -> None:
        pass
    
    def _get_trucks_contents(self) -> list[str]:
        pass

    def get_trucks_contents(self) -> None:
        print(self._get_trucks_contents())

    def empty_db(self) -> None:
        pass