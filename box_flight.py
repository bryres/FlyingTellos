from djitellopy import Tello
import time

def main():
    # Init Tello object that interacts with the Tello drone
    tello = Tello()

    if not tello.connect():
        print("Tello not connected")
        return

    tello.set_speed(20)

    try:

        tello.takeoff()
#        for i in range (4):
#        tello.move_right(60)
#        tello.move_up(30)
#        tello.rotate_counter_clockwise(90)
        print("Altitude: %s; Barometer: %s" %(tello.get_distance_tof(), tello.get_barometer()))

        height = tello.get_distance_tof()
        print("height: ", height)
        distance = height - 20
        print("distance: ", distance)
        tello.move_down(distance)

        print("Altitude: %s; Barometer: %s" %(tello.get_distance_tof(), tello.get_barometer()))
        tello.move_forward(100)

        tello.land()

    except Exception as e:
        print ("Caught exception.  Attempting to land.")
        print(e)
        # This will loop until the drone lands.
        emergency_land(tello)


def emergency_land(tello):
    while True:
        try:
            if tello.land():
                return
        except Exception as e:
            print("Exception caught; trying to land again.")
            print(e)
        time.sleep(2)

if __name__ == '__main__':
    main()
