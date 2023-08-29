def car_parameters(*, time: int, speed: int, weight: int) -> str:

    values = {
        'time': time,
        'speed': speed,
        'weight': weight
    }

    for key, value in values.items():
        if value < 0:
            raise ValueError(f"Please enter positive value ({key}: {value})")
    distance = time * speed
    return f"Car weight of {weight}kg" \
           f" was moving {time} seconds " \
           f"with speed {speed}m/s" \
           f" and traveled {distance} meters"


if __name__ == '__main__':
    print(car_parameters(time=7, speed=10, weight=1254))
