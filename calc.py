while True:
    print("\n---Mechanical Engineering Calculator---\n")
    print("\n1. Material Safety (Stress & FOS)")
    print("\n2. Fluid Continuity (Area & Velocity)")
    print("\n3.Exit\n")

    choice=input("Select an option (1-3): ")

    if choice == '1':
        print("\n---Material Safety (Stress & FOS)---\n")
        try:
            force = float(input("Enter the applied force (in Newtons): "))
            area = float(input("Enter the cross-sectional area (in square meters): "))
            allowable_stress = float(input("Enter the allowable stress (in Pascals): "))

            # Calculate stress
            stress = force / area
            # Calculate Factor of Safety (FOS)
            fos = allowable_stress / stress

            print(f"\nCalculated Stress: {stress:.2f} Pa")
            print(f"Factor of Safety (FOS): {fos:.2f}")

            if fos < 1:
                print("Warning: The design is unsafe (FOS < 1).")   
            else:
                print("The design is safe (FOS >= 1).")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Area cannot be zero. Please enter a valid area.")
        except ValueError:
         print("Invalid input. Please enter numeric values.")

        input("\nPress Enter to return to the main menu...")
    elif choice == '2':
        print("\n---Fluid Continuity (Area & Velocity)---\n")   
        try:
            a1=float(input("Enter the cross-sectional area at point 1 (in square meters): "))
            v1=float(input("Enter the fluid velocity at point 1 (in meters per second): "))
            a2=float(input("Enter the cross-sectional area at point 2 (in square meters): "))
            v2 = (a1 * v1) / a2
            print(f"\nCalculated Fluid Velocity at Point 2: {v2:.2f} m/s")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Area cannot be zero. Please enter a valid area.")
        input("\nPress Enter to return to the main menu...")
    elif choice == '3':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-3).")