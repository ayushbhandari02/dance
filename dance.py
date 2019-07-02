import enrolling_details
import workshop_details

print("Welcome \r to DANCE RTEE")
while (1):
    print("Do you want to enroll as a student Or want to attend a workshop")

    try:
        select = int(
            input("Press 1 to enroll as a student and press 2 to attend the upcoming workshop and press 3 to exit "))
        if (select == 0 or select > 3):
            print("Please select a number from the options above\n\n")
    except ValueError:
        print("only integer input to be given")
        exit()

    if select == 1:  # when the dancer wants to enroll as a student in the academy
        try:
            enrolling_details.name = input("enter the name ")
            if (enrolling_details.name.isdigit() == True):
                print("1 2 ka 4 to gana hai naam kisi ka thodi aise ho skta hai kaise ho sakta hai")
                exit()
            if (len(enrolling_details.name) > 25):
                print("apna hi naam likho bas\n")
                exit()
        except ValueError:
            print("only alphabets allowed")
            exit()
        try:
            enrolling_details.age = int(input("enter the age "))
            if (enrolling_details.age <= 0):
                print("bhai paida nhi hua aur dance karega kya")
                exit()
            if (enrolling_details.age > 150):
                print("guiness world record mein try kia kya")
                exit()
        except ValueError:
            print("only integer value to be given")
            exit()
        try:
            enrolling_details.dance_style = input("enter the dance style ")
            if (enrolling_details.dance_style.isdigit() == True):
                print("dance style ka naam likho dance style ka number nahi")
                exit()
        except ValueError:
            print("only alphabets allowed")
            exit()
        try:
            enrolling_details.basic_or_advance_batch = input("enter the batch type ")
            if (enrolling_details.basic_or_advance_batch.isdigit() == True):
                print("basic ya advance likho bas")
                exit()
        except ValueError:
            print("only albhabets allowed")
            exit()
        dancer = enrolling_details.EnrollingDetails(enrolling_details.name, enrolling_details.age,
                                                    enrolling_details.dance_style,
                                                    enrolling_details.basic_or_advance_batch)
        print(dancer.name, dancer.age, dancer.dance_style, dancer.basic_or_advance_batch)

    if select == 2:  # when a dancer wants to attend a workshop
        try:
            workshop_details.name = input("enter the name")
            if (workshop_details.name.isdigit() == True):
                print("integers not allowed")
                exit()
            if(len(workshop_details.name) > 25):
                print("apna hi naam likho bas\n")
                exit()

        except ValueError:
            print("only alphabets allowed")
        try:
            workshop_details.age = int(input("enter the age"))
            if (workshop_details.age > 150):
                print("guiness world record mein try kia kya")
                exit()
        except:
            print('only integer value allowed')
            exit()
        try:
            workshop_details.contact_number = int(input("enter the contact number"))
            if(len(workshop_details.contact_number != 10)):
                print("kripya apne 10 anko ka kramank daalen")
                exit()
        except ValueError:
            print("only integer value allowed")
        try:
            workshop_details.email_id = input("enter the email id")
        except ValueError:
            print("email id hai email id samajh ke dalo")
        dancer_ = workshop_details.WorkshopDetails(workshop_details.name, workshop_details.age,
                                                   workshop_details.contact_number, workshop_details.email_id)
        print(dancer_.name, dancer_.age, dancer_.contact_number, dancer_.email_id)

    if (select == 3):  # if you want to exit
        exit()
