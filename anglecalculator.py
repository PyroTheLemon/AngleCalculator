import time

def internal_angle():
    return (angle_number-2)*180
def single_angle():
    return internal_angle() / angle_number
def external_angle():
    return 180-single_angle()
#CODED BY Pyro.I
while True:
    print("Angle Calculation")
    print("Select An Operation")
    print("1. Internal Calculation")
    print("2. Single Angle Calculation")
    print("3. External Angle Calculation")
    print("4. All")
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
            angle_number = float(input("Give the number of corner's: "))

            if choice == '1':
                print(angle_number, "- 2.0) 180 = ", internal_angle())
            elif choice == '2':
                print(internal_angle(), "/", angle_number, "=", single_angle())
            elif choice == '3':
                print("180 -", single_angle(), "=", external_angle())
            elif choice == '4':
                print("(", angle_number, "- 2 ) * 180=", internal_angle(), "| <-- Internal Angle")
                print(internal_angle(), "/", angle_number, "=", single_angle(), "| <-- Single Angle")
                print("180 -", single_angle(), "=", external_angle(), "| <-- External Angle")
            another_calculation = input("Wanna make another calculation?(Y/n): ")
            if another_calculation == "n":
                print("Bye.")
                time.sleep(1.5)
                exit()
    else:
            print("Please give vaild input! --->(Y/n)") 
