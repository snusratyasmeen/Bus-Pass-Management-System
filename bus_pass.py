print("🚌 Bus Pass Management System")

passes = []

while True:
    print("\n1. Add Passenger")
    print("2. View Passes")
    print("3. Search Passenger")
    print("4. Update Pass")
    print("5. Cancel Pass")
    print("6. Count Passengers")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Passenger
    if choice == "1":
        pass_id = input("Enter pass ID: ")
        name = input("Enter passenger name: ")
        age = input("Enter passenger age: ")
        route = input("Enter bus route: ")
        pass_type = input("Enter pass type (Monthly/Quarterly): ")

        passenger = {
            "id": pass_id,
            "name": name,
            "age": age,
            "route": route,
            "type": pass_type
        }

        passes.append(passenger)

        print("✅ Bus pass added successfully!")

    # View Passes
    elif choice == "2":
        if len(passes) == 0:
            print("❌ No bus passes found.")
        else:
            print("\n🚌 Bus Pass Details")
            print("--------------------------")

            for passenger in passes:
                print("Pass ID:", passenger["id"])
                print("Passenger Name:", passenger["name"])
                print("Age:", passenger["age"])
                print("Bus Route:", passenger["route"])
                print("Pass Type:", passenger["type"])
                print("--------------------------")

    # Search Passenger
    elif choice == "3":
        search_id = input("Enter pass ID to search: ")

        found = False

        for passenger in passes:
            if passenger["id"] == search_id:
                print("\n✅ Passenger Found")
                print("Pass ID:", passenger["id"])
                print("Passenger Name:", passenger["name"])
                print("Age:", passenger["age"])
                print("Bus Route:", passenger["route"])
                print("Pass Type:", passenger["type"])

                found = True
                break

        if not found:
            print("❌ Passenger not found.")

    # Update Pass
    elif choice == "4":
        update_id = input("Enter pass ID: ")

        found = False

        for passenger in passes:
            if passenger["id"] == update_id:

                new_route = input("Enter new bus route: ")
                new_type = input("Enter new pass type: ")

                passenger["route"] = new_route
                passenger["type"] = new_type

                print("✅ Bus pass updated successfully!")

                found = True
                break

        if not found:
            print("❌ Pass not found.")

    # Cancel Pass
    elif choice == "5":
        cancel_id = input("Enter pass ID to cancel: ")

        found = False

        for passenger in passes:
            if passenger["id"] == cancel_id:
                passes.remove(passenger)

                print("✅ Bus pass cancelled successfully!")

                found = True
                break

        if not found:
            print("❌ Pass not found.")

    # Count Passengers
    elif choice == "6":
        print("🚌 Total Passengers:", len(passes))

    # Exit
    elif choice == "7":
        print("Thank you for using Bus Pass Management System! 🚌")
        break

    else:
        print("❌ Invalid choice!")
