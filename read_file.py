with open("data.txt") as file:
    for line in file:
        car_brand = line.strip()
        print(car_brand)
        cars_record = file.readline().strip()
        print(cars_record)
        for i in enumerate(cars_record):
            print(file.readline().strip())
        file.readline()
        print()