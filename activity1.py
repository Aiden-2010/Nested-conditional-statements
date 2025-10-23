medical_cause = input("Do you have a medical cause? Y/N ")
attendance = int(input("Enter the attendance of the students: "))
if medical_cause == "Y":
    print("You are allowed")
else:
    if attendance >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")