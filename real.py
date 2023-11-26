# Set all value going to use
# Set FEES as Dictionary
fees = {"LABORATORY FEE": 2500,
        "REGISTRAR (WTF)": 50,
        "PUBLICATION???": 200,
        "STUDENT COUNCIL": 300,
        "STUDENT ID": 200,
        "MISCELLANEOUS": 1000
        }
# Set SCHOLARSHIP as Dictionary
scholarship = {"NO SCHOLAR": 0,
               "FULL-SCHOLAR": 50,
               "PARTIAL-SCHOLAR": 20
               }
checkBox = []
radioButton = 0
# Get the STUDENT NAME
studentName = input("STUDENT NAME: ")

# Get the student UNITS ENROLLED
unitsEnrolled = int(input("UNITS ENROLLED: "))
# Get the student YEAR LEVEL as DROPDOWN with:
# 1. 1stYR
# 2. 2ndYR
# 3. 3rdYR
# 4. 4thYR
# 5. 5thYR
yearLevel = input("YEAR LEVEL: ")
print("")

# Get the FEES as a CHECKBOX with:
# 1. LABORATORY FEE with te value of ???
# 2. REGISTRAR (WTF) with te value of ???
# 3. PUBLICATION??? with te value of ???
# 4. STUDENT COUNCIL with te value of ???
# 5. STUDENT ID with te value of ???
# 6. MISCELLANEOUS with te value of ???
# Ask the user to choose from 1 to 6 only and type "STOP" to stop the Checkbox loop
# Set the all chosen FEES and add their value as TOTAL FEES

print("=" * 35 + "\n" +
      "|"+f"{' NOTE:':<33}" + "|\n" +
      "|"+f"{' Select from 1-6':<33}" + "|\n" +
      "|"+f"{' Type DONE if your already good.':<33}" + "|\n" +
      "=" * 35)

while True:
    index = 1
    box = "⬜️"
    totalFees = 0
    print("=" * 35 + "\n" +
          "FEES:")
    for key in fees:
        temp = box
        if index in checkBox:
            box = "🟦"
            totalFees += fees[key]
        print(f"{f'    {index}{box}  {key}':<35}")
        box = temp
        index += 1
    print("=" * 35)

    try:
        chosenFees = input("SELECT: ")
        if chosenFees in ["DONE", "Done", "done"]:
            break
        else:
            chosenFees = int(chosenFees)
        if 1 <= chosenFees <= 6:
            if chosenFees not in checkBox:
                checkBox.append(chosenFees)
            else:
                print("Already Selected!!!")
                while True:
                    try:
                        removeFees = input("Do you want to remove it from selected. Type (YES or NO): ")
                        if removeFees in ["YES", "Yes", "yes", "Y", "y"]:
                            checkBox.remove(chosenFees)
                            break
                        elif removeFees in ["NO", "No", "no", "N", "n"]:
                            break
                        else:
                            print("Try Again")
                    except (ValueError, NameError):
                        print("Try Again")
        else:
            print("Try Again")
    except (ValueError, NameError):
        print("Try Again")

# Get the SCHOLARSHIP WTF as RADIO BUTTON with:
# 1. NO SCHOLAR
# 2. FULL-SCHOLAR
# 3. PARTIAL-SCHOLAR
# Ask the user to choose from 1 to 3 only
# Set the chosen SCHOLARSHIP WTF value as SCHOLARSHIP

print("=" * 35 + "\n" +
      "|"+f"{' NOTE:':<33}" + "|\n" +
      "|"+f"{' Select from 1-3':<33}" + "|\n" +
      "|"+f"{' Type DONE if your already good.':<33}" + "|\n" +
      "=" * 35)

while True:
    index = 1
    radio = "⚪️"
    totalDiscount = 0
    print("=" * 35 + "\n" +
          "SCHOLARSHIP WTF:")
    for key in scholarship:
        temp = radio
        if index == radioButton:
            totalDiscount += scholarship[key]
            radio = "🔵"
        print(f"    {index}{radio}  {key}")
        radio = temp
        index += 1
    print("=" * 35)

    try:
        chosenScholarship = input("SELECT: ")
        if chosenScholarship in ["DONE", "Done", "done"]:
            break
        else:
            chosenScholarship = int(chosenScholarship)
        if 1 <= chosenScholarship <= 3:
            if chosenScholarship != radioButton:
                radioButton = chosenScholarship
            else:
                print("Already Selected!!!")
        else:
            print("Try Again")
    except (ValueError, NameError):
        print("Try Again")
print("")

# Computer for TOTAL AMOUNT with this computation:
# TOTAL AMOUNT = TOTAL FEES / SCHOLARSHIP

totalAmount = round(totalFees / (1+(totalDiscount * 0.01)), 2)

# Print TOTAL AMOUNT
# Stop the program
print("=" * 35 + "\n" +
      "|" + " " * 33 + "|\n" +
      "| TOTAL AMOUNT: " + f"{f' ₱{totalAmount}':^18}" + "|\n" +
      "|" + " " * 33 + "|\n" +
      "=" * 35 + "\n")

# -----------------------------------


# Get the STUDENT NAME
# Get the student UNITS ENROLLED
# Get the student YEAR LEVEL as DROPDOWN with:
# 1. 1stYR
# 2. 2ndYR
# 3. 3rdYR
# 4. 4thYR
# 5. 5thYR)

# Get the FEES as a CHECKBOX with:
# 1. LABORATORY FEE with te value of ???
# 2. REGISTRAR (WTF) with te value of ???
# 3. PUBLICATION??? with te value of ???
# 4. STUDENT COUNCIL with te value of ???
# 5. STUDENT ID with te value of ???
# 6. MISCELLANEOUS with te value of ???
# Ask the user to choose from 1 to 6 only and type "STOP" to stop the Checkbox loop
# Set the all chosen FEES and add their value as TOTAL FEES

# Get the SCHOLARSHIP WTF as RADIO BUTTON with:
# 1. NO SCHOLAR
# 2. FULL-SCHOLAR
# 3. PARTIAL-SCHOLAR
# Ask the user to choose from 1 to 3 only
# Set the chosen SCHOLARSHIP WTF value as SCHOLARSHIP

# Computer for TOTAL AMOUNT with this computation:
# TOTAL AMOUNT = TOTAL FEES / SCHOLARSHIP

# Print TOTAL AMOUNT
# Stop the program
