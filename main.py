import random

class Passenger:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.luggage = random.randint(5, 30)  # рандомна вага багажу в кг
        self.disability = bool(random.getrandbits(1))  # рандомно чи є інвалідність ніг
        self.passport_id = random.randint(100000, 999999)  # рандомний id паспорту
        self.ticket_id = random.randint(1000, 9999)  # рандомний id квитка

class Airplane:
    def __init__(self, gate):
        self.gate = gate
        self.airplane_type = random.choice(["Boeing 737", "Airbus A320", "Boeing 777", "Airbus A380", "Boeing 787"])
        self.route = random.choice(["New York to Los Angeles", "Chicago to Miami", "San Francisco to Seattle", "Boston to Atlanta", "Las Vegas to Denver"])
        self.duration = random.randint(1, 6)  # рандомна тривалість в годинах
        self.flight_id = random.randint(10000, 99999)  # рандомний id рейсу

class Ticket:
    def __init__(self, passenger, airplane, ticket_class, departure_time, arrival_time, seat_number, baggage_info):
        self.passenger_name = passenger.name
        self.passenger_age = passenger.age
        self.ticket_class = ticket_class
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_location = airplane.route.split(" to ")[0]
        self.arrival_location = airplane.route.split(" to ")[1]
        self.ticket_id = random.randint(100000, 999999)  # рандомний id квитка
        self.flight_id = airplane.flight_id
        self.seat_number = seat_number
        self.baggage_info = baggage_info
        self.airplane_type = airplane.airplane_type

# Створення об'єктів і виведення інформації
passenger1 = Passenger("John Doe", "18+", ">=185cm")
airplane1 = Airplane("Gate A1")
ticket1 = Ticket(passenger1, airplane1, "Business", "12:00", "15:00", "15A", "No overweight baggage")

print("Passenger Info:")
print("Name:", passenger1.name)
print("Age:", passenger1.age)
print("Height:", passenger1.height)
print("Luggage:", passenger1.luggage, "kg")
print("Disability:", "Yes" if passenger1.disability else "No")
print("Passport ID:", passenger1.passport_id)
print("Ticket ID:", passenger1.ticket_id)

print("\nAirplane Info:")
print("Gate:", airplane1.gate)
print("Airplane Type:", airplane1.airplane_type)
print("Route:", airplane1.route)
print("Duration:", airplane1.duration, "hours")
print("Flight ID:", airplane1.flight_id)

print("\nTicket Info:")
print("Passenger Name:", ticket1.passenger_name)
print("Passenger Age:", ticket1.passenger_age)
print("Ticket Class:", ticket1.ticket_class)
print("Departure Time:", ticket1.departure_time)
print("Arrival Time:", ticket1.arrival_time)
print("Departure Location:", ticket1.departure_location)
print("Arrival Location:", ticket1.arrival_location)
print("Ticket ID:", ticket1.ticket_id)
print("Flight ID:", ticket1.flight_id)
print("Seat Number:", ticket1.seat_number)
print("Baggage Info:", ticket1.baggage_info)
print("Airplane Type:", ticket1.airplane_type)
