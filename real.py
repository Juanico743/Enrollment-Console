# Set all value going to use
# Set the COST PER UNIT
costPerUnits = 1811.37

# Set FEES as Dictionary
# 1. LABORATORY FEE with the value of ₱ 6504.00
# 2. REGISTRAR CARD with the value of ₱ 1463.35
# 3. PUBLICATION??? with the value of ₱ 216.80
# 4. STUDENT COUNCIL with the value of ₱ 500.00
# 5. STUDENT ID with the value of ₱ 108.40
# 6. MISCELLANEOUS with the value of ₱ 7571.80
fees = {"LABORATORY FEE": 6504.00,
        "REGISTRAR CARD": 1463.35,
        "PUBLICATION???": 216.80,
        "STUDENT COUNCIL": 500.00,
        "STUDENT ID": 108.40,
        "MISCELLANEOUS": 7571.80
        }

# Set SCHOLARSHIP as Dictionary
# 1. NON-SCHOLAR with the value of 0%
# 2. FULL-SCHOLAR with the value of 100%
# 3. PARTIAL-SCHOLAR with the value of 50%
scholarshipGrant = {"NON-SCHOLAR": 0,
                    "FULL-SCHOLAR": 100,
                    "PARTIAL-SCHOLAR": 50
                    }

# Set YEAR LEVEL as List
# 1. 1st Year
# 2. 2nd Year
# 3. 3rd Year
# 4. 4th Year
# 5. 5th Year
allYearLevel = ["1st Yr", "2nd Yr", "3rd Yr", "4th Yr", "5th Yr"]

# Create a container for a selected FEES and SCHOLARSHIP
selectedFees = []
selectedScholarshipGrant = 0

# Get the STUDENT NAME
studentName = input("STUDENT NAME: ")

# Get the student UNITS ENROLLED
while True:
    try:
        unitsEnrolled = int(input("UNITS ENROLLED: "))
        if unitsEnrolled > 0:
            break
        else:
            print("Try Again")
    except (ValueError, NameError):
        print("Try Again")

# Compute for the TOTAL UNIT in this formula:
# TOTAL UNITS = ( UNITS ENROLLED *  COST PER UNIT)
totalUnits = unitsEnrolled * costPerUnits

# Get the student YEAR LEVEL as COMBO BOX with:
print("=" * 25)
for i in range(5):
    print("|" + f"{f'{i + 1} - {allYearLevel[i]}':^23}" + "|")
print("=" * 25)
yearLevel = input("YEAR LEVEL: ")
print("")

# Get the FEES as a CHECKBOX
# Display all the choices for the User
# Ask the user to choose from 1 to 6 only and type "DONE" to stop the Checkbox loop
# Set the all chosen FEES and add their value as TOTAL FEES

print("=" * 35 + "\n" +
      "|" + f"{' NOTE:':<33}" + "|\n" +
      "|" + f"{' Select from 1-6':<33}" + "|\n" +
      "|" + f"{' Type DONE if your already good.':<33}" + "|\n" +
      "=" * 35)

while True:
    index = 1
    box = "⬜"
    totalFees = 0
    print("=" * 35 + "\n" +
          "FEES:")
    for key in fees:
        temp = box
        if index in selectedFees:
            box = "🟦"
            totalFees += fees[key]
        print(f"{f'    {index}{box}   {key}':<35}")
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
            if chosenFees not in selectedFees:
                selectedFees.append(chosenFees)
            else:
                print("Already Selected!!!")
                while True:
                    try:
                        removeFees = input("Do you want to remove it from selected. Type (YES or NO): ")
                        if removeFees in ["YES", "Yes", "yes", "Y", "y"]:
                            selectedFees.remove(chosenFees)
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

# Get the SCHOLARSHIP GRANT as RADIO BUTTON
# Display all the choices for the User
# Ask the user to choose from 1 to 3 only
# Set the chosen SCHOLARSHIP GRANT value as SCHOLARSHIP
print("=" * 35 + "\n" +
      "|" + f"{' NOTE:':<33}" + "|\n" +
      "|" + f"{' Select from 1-3':<33}" + "|\n" +
      "|" + f"{' Type DONE if your already good.':<33}" + "|\n" +
      "=" * 35)

while True:
    index = 1
    radio = "⚪"
    totalDiscount = 0
    print("=" * 35 + "\n" +
          "SCHOLARSHIP GRANT:")
    for key in scholarshipGrant:
        temp = radio
        if index == selectedScholarshipGrant:
            totalDiscount += scholarshipGrant[key]
            radio = "🔵"
        print(f"    {index}{radio}   {key}")
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
            if chosenScholarship != selectedScholarshipGrant:
                selectedScholarshipGrant = chosenScholarship
            else:
                print("Already Selected!!!")
        else:
            print("Try Again")
    except (ValueError, NameError):
        print("Try Again")
print("")

# Computer for TOTAL AMOUNT with this computation:
# TOTAL AMOUNT = ( TOTAL UNITS + TOTAL FEES ) - (( TOTAL UNITS + TOTAL FEES ) / SCHOLARSHIP )
# Round it of to two Decimal Format it with comma seperator
totalAmount = format(round((totalUnits + totalFees) - ((totalUnits + totalFees) / totalDiscount), 2), ',.2f')

# Print TOTAL AMOUNT
# Stop the program
print("=" * 35 + "\n" +
      "|" + " " * 33 + "|\n" +
      "| TOTAL AMOUNT: " + f"{f'₱ {totalAmount}':^18}" + "|\n" +
      "|" + " " * 33 + "|\n" +
      "=" * 35 + "\n")


# -----------------------------------


# Set all value going to use
# Set the COST PER UNIT

# Set FEES as Dictionary
# 1. LABORATORY FEE with the value of ₱ 6504.00
# 2. REGISTRAR CARD with the value of ₱ 1463.35
# 3. PUBLICATION??? with the value of ₱ 216.80
# 4. STUDENT COUNCIL with the value of ₱ 500.00
# 5. STUDENT ID with the value of ₱ 108.40
# 6. MISCELLANEOUS with the value of ₱ 7571.80

# Set SCHOLARSHIP as Dictionary
# 1. NON-SCHOLAR with the value of 0%
# 2. FULL-SCHOLAR with the value of 100%
# 3. PARTIAL-SCHOLAR with the value of 50%

# Set YEAR LEVEL as List
# 1. 1st Year
# 2. 2nd Year
# 3. 3rd Year
# 4. 4th Year
# 5. 5th Year

# Create a container for a selected FEES and SCHOLARSHIP

# Get the STUDENT NAME

# Get the student UNITS ENROLLED

# Compute for the TOTAL UNIT in this formula:
# TOTAL UNITS = ( UNITS ENROLLED *  COST PER UNIT)

# Get the student YEAR LEVEL as COMBO BOX with
# Display all the choices for the User
# Ask the user to choose from 1 to 5 only

# Get the FEES as a CHECKBOX
# Display all the choices for the User
# Ask the user to choose from 1 to 6 only and type "DONE" to stop the Checkbox loop
# Set the all chosen FEES and add their value as TOTAL FEES

# Get the SCHOLARSHIP GRANT as RADIO BUTTON
# Display all the choices for the User
# Ask the user to choose from 1 to 3 only and type "DONE" to stop the Checkbox loop
# Set the chosen SCHOLARSHIP GRANT value as SCHOLARSHIP

# Computer for TOTAL AMOUNT with this computation:
# TOTAL AMOUNT = ( TOTAL UNITS + TOTAL FEES ) - (( TOTAL UNITS + TOTAL FEES ) / SCHOLARSHIP )

# Print TOTAL AMOUNT
# Stop the program
