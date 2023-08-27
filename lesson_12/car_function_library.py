def car_parameters(**kwargs):
    for key in kwargs:
        if kwargs[key] < 0:
            raise ValueError('Please enter positive value')
    distance = kwargs['time'] * kwargs['speed']
    return f"Car weight of {kwargs['weight']}kg" \
           f" was moving {kwargs['time']} seconds " \
           f"with speed {kwargs['speed']}m/s" \
           f" and traveled {distance} meters"


if __name__ == '__main__':
    print(car_parameters(time=5, speed=2, weight=1200))
