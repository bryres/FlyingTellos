from djitellopy import Tello

def flybox(tello):
    tello.takeoff()
    for i in range (4):
        tello.move_forward(60)
        tello.rotate_clockwise(90)
    tello.land()

def stacked_box(tello):
    tello.takeoff()
    tello.
    for j in range (3):
        for i in range (4):
            tello.move_forward(60)
            tello.rotate_clockwise(90)
        tello.move_up(20)
    tello.land()

def adjusted_height(tello):
    tello.takeoff()
    print("Altitude: %s; Barometer: %s" % (tello.get_distance_tof(), tello.get_barometer()))

    height = tello.get_distance_tof()
    print("height: ", height)
    distance = height - 20
    print("distance: ", distance)
    tello.move_down(distance)

    print("Altitude: %s; Barometer: %s" % (tello.get_distance_tof(), tello.get_barometer()))
    tello.move_forward(100)
    tello.rotate_clockwise(180)
    tello.move_forward(100)
    tello.land()


def main():
    # Init Tello object that interacts with the Tello drone
    tello = Tello()
    tello.set_speed(20)

    try:
        flybox(tello)

    except Exception as e:
        print(e)
        tello.emergency_land()

if __name__ == '__main__':
    main()
