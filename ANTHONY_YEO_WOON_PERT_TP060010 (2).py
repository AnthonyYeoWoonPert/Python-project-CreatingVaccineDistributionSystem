# ANTHONY YEO WOON PERT
# TP060010

def get_new_id(eid):
    with open("patient_id.txt", "r") as rf:
        rec = rf.readline()
    if eid == "KL":
        ind = 0
    elif eid == "SLG":
        ind = 1
    mylist = rec.strip().split("|")
    nextid = mylist[ind]
    # read right side 3 character
    newid = str(int(nextid[3:]) + 1)
    if len(newid) == 1:
        # read left side 3 character
        nextid = nextid[:3] + "0000" + newid
    elif len(newid) == 2:
        nextid = nextid[:3] + "000" + newid
    elif len(newid) == 3:
        nextid = nextid[:3] + "00" + newid
    elif len(newid) == 4:
        nextid = nextid[:3] + "0" + newid
    elif len(newid) == 5:
        nextid = nextid[:3] + newid

    mylist[ind] = nextid
    rec = "|".join(mylist)
    with open("patient_id.txt", "w") as wf:
        wf.write(rec)
    return (nextid)


def flg1():
    # New patient registration
    print("\n\nWelcome to Nonami Vaccination register counter")

    # To ask the name of the patient
    incorrect = 1
    while incorrect == 1:
        print("Please enter your name")
        name = str(input("Eg.AnthonyYeoWoonPert"))

        if name.isalpha():
            print("Name Accepted")
            print("Welcome " + name)
            incorrect = 0
        else:
            print("Invalid Input")

    # To ask the contact number of the patient
    incorrect = 1
    while incorrect == 1:
        print("\nPlease enter contact number:")
        contact_number = str(input("Eg.0162953541"))
        if contact_number.isdigit():
            import re
            if 10 <= len(contact_number) <= 11:
                pattern = (r'(^(01)[+0-9])*([0-9]{7,8}$)')
                match = re.match(pattern, contact_number)
                if match:
                    print("Contact Number Accepted")
                    print(contact_number)
                    incorrect = 0
                else:
                    print("Contact Number Invalid")
                    print(contact_number)
                    incorrect = 1
            else:
                print("Contact Number Invalid")
                print(contact_number)
                incorrect = 1
        else:
            print("Contact Number Invalid")
            print(contact_number)
            incorrect = 1

    # To ask the age of the patient
    incorrect = 1
    while incorrect == 1:
        print("\nPlease enter your age:")
        age = str(input("Eg.20"))
        if age.isdigit():
            incorrect = 0
            age = int(age)
        else:
            print("Age Invalid")

    # To check the eligibility of the vaccine based on patient age
    if age >= 12:

        incorrect = 1
        while incorrect == 1:
            # To store the vaccination centre chosen by the patient
            print("\nPlease choose a vaccination centre")
            print("1 - Kuala Lumpur vaccination centre")
            print("2 - Selangor vaccination centre")
            vaccination_centre_code = str(input("eg.1/2"))
            if vaccination_centre_code.isdigit():
                vaccination_centre_code = int(vaccination_centre_code)

                # If the patient enter wrongly, this will loop till they correct
                if vaccination_centre_code != 1:
                    if vaccination_centre_code != 2:
                        incorrect = 1
                        # To reconfirm if the patient enter an invalid response
                        print("\nAnswer is invalid")
                        print("Please retry")
                    else:
                        incorrect = 0
                else:
                    incorrect = 0
            else:
                incorrect = 1
                # To reconfirm if the patient enter an invalid response
                print("\nAnswer is invalid")
                print("Please retry")

        incorrect = 1
        while incorrect == 1:
            # Ask patient when they want to take their vaccine
            print("\nAre you taking the vaccine today?")
            print("1 - Yes, I'm taking the vaccine today")
            print("2 - No, I'm taking the vaccine some other day")
            choose = str(input("Eg.1"))
            if choose == "1":
                incorrect = 0
            elif choose == "2":
                incorrect = 0
            else:
                incorrect = 1
                print("\nAnswer is invalid")
                print("Please retry")

        incorrect = 1
        while incorrect == 1:
            if choose == "1":
                import datetime
                # date1 = datetime.datetime.today()
                day = datetime.datetime.now().day
                month = datetime.datetime.now().month
                year = datetime.datetime.now().year
                date1 = datetime.date(year, month, day)
                incorrect = 0
            else:
                import datetime

                incorrect = 1
                while incorrect == 1:
                    year = str(input("Enter a month"))
                    month = str(input('Enter a month'))
                    day = str(input('Enter a day'))
                    if year.isdigit():
                        if month.isdigit():
                            if day.isdigit():
                                year = int(year)
                                month = int(month)
                                day = int(day)

                                if month > 12:
                                    incorrect = 1
                                    # To reconfirm if the patient enter an invalid response
                                    print("\nAnswer is invalid")
                                    print("Please retry")
                                else:
                                    if month == 1 / 3 / 5 / 7 / 8 / 10 / 12:
                                        if day > 31:
                                            incorrect = 1
                                            # To reconfirm if the patient enter an invalid response
                                            print("\nAnswer is invalid")
                                            print("Please retry")
                                        else:
                                            incorrect = 0
                                    elif month == 4 / 6 / 9 / 11:
                                        if day >= 31:
                                            incorrect = 1
                                            # To reconfirm if the patient enter an invalid response
                                            print("\nAnswer is invalid")
                                            print("Please retry")
                                        else:
                                            incorrect = 0
                                    else:
                                        if day > 29:
                                            incorrect = 1
                                            # To reconfirm if the patient enter an invalid response
                                            print("\nAnswer is invalid")
                                            print("Please retry")
                                        else:
                                            incorrect = 0
                            else:
                                print("Invalid Input")
                        else:
                            print("Invalid Input")
                    else:
                        print("Invalid Input")

                date1 = datetime.date(year, month, day)

        if age < 18:

            incorrect = 1
            while incorrect == 1:
                print("\nPlease choose a vaccine type")
                print("1 - AF [2 dosage is required, interval between doses are 2 weeks]")
                print("2 - CZ [2 dosage is required, interval between doses are 3 weeks]")
                print("3 - DM [2 dosage is required, interval between doses are 4 weeks]")
                option = str(input("Eg.1"))
                if option.isdigit():
                    option = int(option)
                    if 0 >= option or option >= 4:
                        incorrect = 1
                        print("Invalid Input")
                    else:
                        incorrect = 0
                else:
                    print("Invalid input")

            # Age range 1 = patient who age 13 - 17 years old
            age_range = 1



        # For patient at age group 18 - 45 yrs old
        elif 18 <= age <= 45:

            incorrect = 1
            while incorrect == 1:
                print("\nPlease choose a vaccine type")
                print("1 - AF [2 dosage is required, interval between doses are 2 weeks]")
                print("2 - BV [2 dosage is required, interval between doses are 3 weeks]")
                print("3 - CZ [2 dosage is required, interval between doses are 3 weeks]")
                print("4 - DM [2 dosage is required, interval between doses are 4 weeks]")
                print("5 - EC [1 dosage is required]")
                option = str(input("Eg.1"))
                if option.isdigit():
                    option = int(option)
                    if 0 >= option or option >= 6:
                        incorrect = 1
                        print("Invalid Input")
                    else:
                        incorrect = 0
                else:
                    print("Invalid input")

            # Age range 2 = patient who age 18 - 45 years old
            age_range = 2


        # For patient at age group 46 yrs old and older
        elif age > 45:

            incorrect = 1
            while incorrect == 1:
                print("\nPlease choose a vaccine type")
                print("1 - AF [2 dosage is required, interval between doses are 2 weeks]")
                print("2 - BV [2 dosage is required, interval between doses are 3 weeks]")
                print("3 - DM [2 dosage is required, interval between doses are 4 weeks]")
                print("4 - EC [1 dosage is required]")
                option = str(input("Eg.1"))
                if option.isdigit():
                    option = int(option)
                    if 0 >= option or option >= 5:
                        incorrect = 1
                        print("Invalid Input")
                    else:
                        incorrect = 0
                else:
                    print("Invalid input")

            # Age range 3 = patient who age more than 45 years old
            age_range = 3

        if age_range == 1:

            # Fill in the vaccine type according to the patient
            if option == 1:
                vaccine_type = "AF"
            elif option == 2:
                vaccine_type = "CZ"
            elif option == 3:
                vaccine_type = "DM"

        elif age_range == 2:

            # Fill in the vaccine type according to the patient
            if option == 1:
                vaccine_type = "AF"
            elif option == 2:
                vaccine_type = "BV"
            elif option == 3:
                vaccine_type = "CZ"
            elif option == 4:
                vaccine_type = "DM"

            elif option == 5:
                vaccine_type = "EC"

        elif age_range == 3:

            # Fill in the vaccine type according to the patient
            if option == 1:
                vaccine_type = "AF"
            elif option == 2:
                vaccine_type = "BV"
            elif option == 3:
                vaccine_type = "DM"
            elif option == 4:
                vaccine_type = "EC"

        import datetime
        # Add time for 2nd dose
        print(date1)
        if vaccine_type == "AF":
            add = datetime.timedelta(days=14)
        elif vaccine_type == "BV":
            add = datetime.timedelta(days=21)
        elif vaccine_type == "CZ":
            add = datetime.timedelta(days=21)
        elif vaccine_type == "DM":
            add = datetime.timedelta(days=28)
        elif vaccine_type == "EC":
            add = datetime.timedelta(days=0)
        date2 = date1 + add
        print(date2)

        if vaccination_centre_code == 1:
            patient_id = get_new_id("KL")
            vaccination_center = "Kuala Lumpur"
        elif vaccination_centre_code == 2:
            patient_id = get_new_id("SLG")
            vaccination_center = "Selangor"

        with open("patient.txt", "a") as af:
            patients = [patient_id, name, str(contact_number), str(age), str(vaccination_center), str(vaccine_type),
                        str(date1), str(date2)]
            af.write("|".join(patients) + "\n")
        patient.append(patients)
        print(patients)

        if vaccination_centre_code == 1:
            with open("KL_vaccination_center.txt", "a") as af:
                record = []
                dose1 = "D1-NOT_COMPLETE"
                if vaccine_type == "EC":
                    dose2 = "N/A"
                else:
                    dose2 = "D2-NOT_COMPLETE"
                record.append(patient_id)
                record.append(str(vaccination_center))
                record.append(str(date1))
                record.append(str(dose1))
                record.append(str(date2))
                record.append(str(dose2))
                af.write(":".join(record) + "\n")

        elif vaccination_centre_code == 2:
            with open("SLG_vaccination_center.txt", "a") as af:
                record = []
                dose1 = "D1-NOT_COMPLETE"
                if vaccine_type == "EC":
                    dose2 = "N/A"
                else:
                    dose2 = "D2-NOT_COMPLETE"
                record.append(patient_id)
                record.append(str(vaccination_center))
                record.append(str(date1))
                record.append(str(dose1))
                record.append(str(date2))
                record.append(str(dose2))
                af.write(":".join(record) + "\n")

    else:
        # Inform those who is under the age of 12 that they are not eligible for the vaccine
        print("Sorry, you are not eligible for the vaccines")


def flg2():
    patient = []
    with open("patient.txt", "r") as rf:
        for line in rf:
            mylist = line.strip().split("|")
            patient.append(mylist)
    print("this is flag 2")
    no_of_rec = len(patient)
    search = input("Please enter the patient ID to search :")
    for i in range(no_of_rec):
        if search in patient[i][0]:
            print("1 - ", patient[i][1])
            print("2 - ", patient[i][2])
            print("3 - ", patient[i][3])
            idx = str(input("Enter the no of field to modify :"))
            if idx.isdigit():
                idx = int(idx)
                if 4 <= idx or idx <= 0:
                    print("Invalid input")
                    print("Please try again")
                    break
                else:
                    patient[i][idx] = input("Enter a new Value :")
                    break
            else:
                print("Invalid input")
                print("Please try again")
                break
    with open("patient.txt", "w") as wf:
        for line in patient:
            wf.write("|".join(line) + "\n")


def flg3():
    print("this is flag 3")
    record = []
    print("\nPlease specify your vaccination center")
    print("1 - Kuala Lumpur Vaccination Center")
    print("2 - Selangor Vaccination Center")
    choice = str(input("Eg. 1"))
    if choice == "1":
        with open("KL_vaccination_center.txt", "r") as rf:
            for lines in rf:
                my_list = lines.strip().split(":")
                record.append(my_list)
        no_of_rec = len(record)

        search = input("Please enter the patient ID to search :")
        for i in range(no_of_rec):
            if search in record[i][0]:
                print("1 - dose 1 : ", record[i][3])
                print("2 - dose 2 : ", record[i][5])
                index = int(input("Enter the no of field to modify :"))
                if index == 1:
                    pos = 3
                    update = "D1-COMPLETE"
                elif index == 2:
                    if record[i][3] != "D1-COMPLETE":
                        print("Invalid Input")
                        print("Dose 1 Not Complete")
                        pos = 5
                        update = "D2-NOT_COMPLETE"
                    else:
                        pos = 5
                        update = "D2-COMPLETE"
                else:
                    print("Invalid Input")
                    print("Please retry")
                    break

                record[i][pos] = update
                break

        with open("KL_vaccination_center.txt", "w") as wf:
            for lines in record:
                wf.write(":".join(lines) + "\n")

    elif choice == "2":
        with open("SLG_vaccination_center.txt", "r") as rf:
            for lines in rf:
                my_list = lines.strip().split(":")
                record.append(my_list)
        no_of_rec = len(record)

        search = input("Please enter the patient ID to search :")
        for i in range(no_of_rec):
            if search in record[i][0]:
                print("1 - dose 1 : ", record[i][3])
                print("2 - dose 2 : ", record[i][5])
                index = int(input("Enter the no of field to modify :"))
                if index == 1:
                    pos = 3
                    update = "D1-COMPLETE"
                elif index == 2:
                    if record[i][3] != "D1-COMPLETE":
                        print("Invalid Input")
                        print("Dose 1 Not Complete")
                        pos = 5
                        update = "D2-NOT_COMPLETE"
                    else:
                        pos = 5
                        update = "D2-COMPLETE"
                else:
                    print("Invalid Input")
                    print("Please retry")

                record[i][pos] = update
                break

        with open("SLG_vaccination_center.txt", "w") as wf:
            for lines in record:
                wf.write(":".join(lines) + "\n")

    else:
        print("invalid input")
        print("Please try again")


def flg4():
    print("this is flag 4")

    ec1 = 0
    allrec = []
    with open("SLG_vaccination_center.txt", "r") as fh:
        for line in fh:
            mylist = line.strip().split(":")
            if int(mylist.count("N/A")) == 1:
                if int(mylist.count("D1-NOT_COMPLETE")) == 1:
                    ec1 = ec1 + 1
            allrec.append(mylist)
    no_of_rec = len(allrec)
    print("\n\n")
    print("-" * 105)
    print("|" + "SELANGOR VACCINATION CENTER".center(103) + "|")
    print("-" * 105)
    print("PATIENT ID".center(20) + "|" + "D1 DATE".center(20) + "|" + "D1 STATUS".center(20) + "|" + "D2 DATE".center(
        20) + "|" + "D2 STATUS".center(20) + "|")
    print("-" * 105)
    for i in range(no_of_rec):
        print(allrec[i][0].center(20) + "|" + allrec[i][2].center(20) + "|" + allrec[i][3].center(20) + "|" + allrec[i][
            4].center(20) + "|" + allrec[i][5].center(20) + "|")
        print("-" * 105)

    slg_patient = []
    with open("SLG_vaccination_center.txt", "r") as rf:
        slg_patient = rf.read()
    SLG_table = []
    SLG_dose1_not_complete = int(slg_patient.count("D1-NOT_COMPLETE"))
    SLG_dose1_complete = int(slg_patient.count("D1-COMPLETE"))
    SLG_dose2_complete = int(slg_patient.count("D2-COMPLETE")) + int(slg_patient.count("N/A") - ec1)
    SLG_dose2_not_complete = int(SLG_dose1_complete - SLG_dose2_complete)
    SLG_total = int(SLG_dose1_complete + SLG_dose1_not_complete)
    SLG_percentage = int((SLG_dose2_complete / SLG_total) * 100)
    SLG_table.append(str(SLG_dose1_not_complete))
    SLG_table.append(str(SLG_dose1_complete))
    SLG_table.append(str(SLG_dose2_complete))
    SLG_table.append(str(SLG_dose2_not_complete))
    SLG_table.append(str(SLG_percentage))
    print("\n\n")
    print("-" * 105)
    print("|" + "SELANGOR VACCINATION CENTER".center(100) + "|")
    print("-" * 105)
    print("D1 NOT_COMPLETE".center(20) + "|" + "D1 COMPLETE".center(20) + "|" + "D2 NOT_COMPLETE".center(
        20) + "|" + "FULLY_VACCINATED".center(20) + "|" + "PERCENTAGE VACCINATED".center(20) + "|")
    print("-" * 105)
    print(SLG_table[0].center(20) + "|" + SLG_table[1].center(20) + "|" + SLG_table[3].center(20) + "|" + SLG_table[
        2].center(20) + "|" + (SLG_table[4] + "%").center(20) + "|")
    print("-" * 105)

    allrec = []
    ec1 = 0
    with open("KL_vaccination_center.txt", "r") as fh:
        for line in fh:
            mylist = line.strip().split(":")
            if int(mylist.count("N/A")) == 1:
                if int(mylist.count("D1-NOT_COMPLETE")) == 1:
                    ec1 = ec1 + 1
            allrec.append(mylist)
    no_of_rec = len(allrec)
    print("\n\n")
    print("-" * 105)
    print("|" + "KUALA LUMPUR VACCINATION CENTER".center(103) + "|")
    print("-" * 105)
    print("PATIENT ID".center(20) + "|" + "D1 DATE".center(20) + "|" + "D1 STATUS".center(20) + "|" + "D2 DATE".center(
        20) + "|" + "D2 STATUS".center(20) + "|")
    print("-" * 105)
    for i in range(no_of_rec):
        print(allrec[i][0].center(20) + "|" + allrec[i][2].center(20) + "|" + allrec[i][3].center(20) + "|" + allrec[i][
            4].center(20) + "|" + allrec[i][5].center(20) + "|")
        print("-" * 105)

    kl_patient = []
    with open("KL_vaccination_center.txt", "r") as rf:
        kl_patient = rf.read()
    KL_table = []
    KL_dose1_not_complete = int(kl_patient.count("D1-NOT_COMPLETE"))
    KL_dose1_complete = int(kl_patient.count("D1-COMPLETE"))
    KL_dose2_complete = int(kl_patient.count("D2-COMPLETE")) + int(kl_patient.count("N/A") - ec1)
    KL_dose2_not_complete = int(KL_dose1_complete - KL_dose2_complete)
    KL_total = int(KL_dose1_complete + KL_dose1_not_complete)
    KL_percentage = int((KL_dose2_complete / KL_total) * 100)
    KL_table.append(str(KL_dose1_not_complete))
    KL_table.append(str(KL_dose1_complete))
    KL_table.append(str(KL_dose2_complete))
    KL_table.append(str(KL_dose2_not_complete))
    KL_table.append(str(KL_percentage))
    print("\n\n")
    print("-" * 105)
    print("|" + "KUALA LUMPUR VACCINATION CENTER".center(100) + "|")
    print("-" * 105)
    print("D1 NOT_COMPLETE".center(20) + "|" + "D1 COMPLETE".center(20) + "|" + "D2 NOT_COMPLETE".center(
        20) + "|" + "FULLY_VACCINATED".center(20) + "|" + "PERCENTAGE VACCINATED".center(20) + "|")
    print("-" * 105)
    print(
        KL_table[0].center(20) + "|" + KL_table[1].center(20) + "|" + KL_table[3].center(20) + "|" + KL_table[2].center(
            20) + "|" + (KL_table[4] + "%").center(20) + "|")
    print("-" * 105)


def flg5():
    print("this is flag 5")

    table = []
    with open("patient.txt", "r") as rf:
        for line in rf:
            all_list = line.strip().split("|")
            table.append(all_list)
        no_of_rec = len(table)
        search = input("Please enter patient ID to search :")
        for i in range(no_of_rec):
            if search in table[i][0]:
                print("-" * 42)
                print("|" + "PATIENT INFORMATION".center(40) + "|")
                print("-" * 42)
                print("ID".center(20) + ":" + table[i][0].center(20) + "|")
                print("NAME".center(20) + ":" + table[i][1].center(20) + "|")
                print("CONTACT NO".center(20) + ":" + table[i][2].center(20) + "|")
                print("AGE".center(20) + ":" + table[i][3].center(20) + "|")
                print("VACCINATION CENTER".center(20) + ":" + table[i][4].center(20) + "|")
                print("VACCINE CODE".center(20) + ":" + table[i][5].center(20) + "|")
                print("-" * 42)
                break

    table1 = []
    with open("KL_vaccination_center.txt", "r") as rf:
        for line in rf:
            all_list = line.strip().split(":")
            table1.append(all_list)
        no_of_rec1 = len(table1)
        for i in range(no_of_rec1):
            if search in table1[i][0]:
                print("-" * 85)
                print("D1 DATE".center(20) + "|" + "D1 STATUS".center(20) + "|" + "D2 DATE".center(
                    20) + "|" + "D2 STATUS".center(20) + "|")
                print("-" * 85)
                print(table1[i][2].center(20) + "|" + table1[i][3].center(20) + "|" + table1[i][4].center(20) + "|" +
                      table1[i][5].center(20) + "|")
                print("-" * 85)
    table2 = []
    with open("SLG_vaccination_center.txt", "r") as rf:
        for line in rf:
            all_list = line.strip().split(":")
            table2.append(all_list)
        no_of_rec2 = len(table2)
        for i in range(no_of_rec2):
            if search in table2[i][0]:
                print("-" * 105)
                print("D1 DATE".center(20) + "|" + "D1 STATUS".center(20) + "|" + "D2 DATE".center(
                    20) + "|" + "D2 STATUS".center(20) + "|")
                print("-" * 105)
                print(table1[i][2].center(20) + "|" + table1[i][3].center(20) + "|" + table1[i][4].center(20) + "|" +
                      table1[i][5].center(20) + "|")
                print("-" * 105)

def login():
    incorrect = 1
    while incorrect == 1:
        print("Welcome to Nonami Vaccination center")
        print("1 - sign up")
        print("2 - log in")
        choice = str(input("eg.1"))
        if choice == "1":
            while incorrect == 1:
                allrec = []
                while incorrect == 1:
                    with open("password.txt", "r") as fh:
                        for line in fh:
                            mylist = line.strip().split(":")
                            allrec.append(mylist)
                        no_of_rec = len(allrec)

                    username = input("Please enter username")
                    for i in range(no_of_rec):
                        if username in allrec[i][0]:
                            print("Username taken")
                            incorrect = 1
                            break
                        else:
                            incorrect = 0

                password = input("Enter passwword")
                with open("password.txt", "a") as af:
                    login = []
                    login.append(str(username))
                    login.append(str(password))
                    af.write(":".join(login) + "\n")
                    print("Sign up complete")
                    break


        elif choice == "2":
            incorrect = 1
            while incorrect == 1:
                login = []
                with open("password.txt", "r") as rf:
                    for lines in rf:
                        my_list = lines.strip().split(":")
                        login.append(my_list)
                no_of_rec = len(login)

                search = input("Please enter username:")
                for i in range(no_of_rec):
                    if search in login[i][0]:
                        password = input("Enter password:")
                        if password == login[i][1]:
                            print("Login successful")
                            incorrect = 0
                            break
                        else:
                            print("Incorrect password entered")
                            incorrect = 1
        else:
            print("Invalid Input")
            print("Please retry")
            incorrect = 1


# start
login()
patient = []
with open("patient.txt", "r") as rf:
    for line in rf:
        mylist = line.strip().split("|")
        patient.append(mylist)

while True:
    # To display a menu option to allow users to choose the function
    print("\n\nWelcome to Nonami Vaccination Center")
    print("Please choose an option")
    print("1 - New registration")
    print("2 - Alter existing patient information")
    print("3 - Vaccination Administration")
    print("4 - Vaccination Center List")
    print("5 - Patient Vaccination Status")
    print("6 - Exit")
    flg = str(input("Eg. 1"))
    if flg.isdigit():
        flg = int(flg)

        if 1 <= flg <= 6:
            if flg == 1:
                flg1()

            elif flg == 2:
                flg2()

            elif flg == 3:
                flg3()

            elif flg == 4:
                flg4()

            elif flg == 5:
                flg5()

            elif flg == 6:
                print("this is flag 6")
                break

        else:
            print("Invalid input")
            print("Please retry")
    else:
        print("Invalid input")
        print("Please retry")
