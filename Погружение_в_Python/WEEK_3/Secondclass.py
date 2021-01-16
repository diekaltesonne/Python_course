import os
import csv
import re

class CarBase:

    def __init__(self,car_type,brand, photo_file_name, carrying):

        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)

class Car(CarBase):

    def __init__(self,car_type, brand, photo_file_name, carrying, passenger_seats_count):

        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(re.sub(r'[^0-9\.]', '', passenger_seats_count))


class Truck(CarBase):

    def __init__(self,car_type,brand, photo_file_name, carrying, body_whl):


        body = body_whl.strip().split('x')
        try:
            super().__init__(car_type, brand, photo_file_name, carrying)
            self.body_length = float(re.sub(r'[^0-9\.]', '', body[2]))
            self.body_width =  float(re.sub(r'[^0-9\.]', '', body[1]))
            self.body_height = float(re.sub(r'[^0-9\.]', '', body[0]))
        except IndexError:
            self.body_height = 0.0
            self.body_width = 0.0
            self.body_length = 0.0
            class SpecMachine(CarBase):

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


    def __init__(self,car_type,brand, photo_file_name, carrying, extra):

        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):

    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) is 7:
                if row[0] == "car":car_list.append(Car(row[0],row[1],row[3],row[5],row[2]))
                if row[0] == "truck":car_list.append(Truck(row[0],row[1],row[3],row[5], row[4]))
                if row[0] == "spec_machine":car_list.append(SpecMachine(row[0],row[1],row[3],row[5],row[4]))
    return car_list
