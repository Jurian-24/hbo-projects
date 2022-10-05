"""
Usually companies use a predefined templates in their emails.
A company named XYZ would like to have a Python program that collects basic information and generates the content of the email.
You are assigned to implement the program with the following criteria:

- There are only two templates: Job Offer and Rejection.
- For the Job Offer email, the program asks: first name, last name, job title, annual salary, starting date.
- For the Rejection email, the program asks: first name, last name, job title, with or without feedback, one feedback statement in case it is with feedback.
- The program must check valid input formats.
- First and last names: each minimum two characters and maximum ten characters; cotaining only alphabets, both starting with capital letters.
- Job title: minimum 10 characters without numbers.
- Salary: valid floating point number between (and including) 20.000,00 and 80.000,00.
- Date: only in YYYY-MM-DD format, no negative numbers, days between 1 - 31, month between 1 - 12, year only 2021 and 2022.
- Feedback: if the email contains a feedback there is an extra line in the text otherwise that line must be removed (check the example below).
- The program will generate emails until the user answers No to the More Letters? question.
- In case of invalid input from the user, the program must proper message and then repeats the question again.
- A sample execution is presented below. Use this sample execution for the templates of the emails. Your program must have only two templates:


maak van elke functie een while loop ondanks dat dat pure tyfus is...
"""
startApp = True

def emailTypeChecker(emailType):
    if(emailType.lower() not in emailTypes):
        print('Invalid input')
        emailType = input('Please enter Job offer or Rejection  \n >>> ')
        emailTypeChecker(emailType)

    return emailType

def nameChecker(name, typeOfName):
    if(len(name) < 2 or len(name) > 10):
        print(f'Your {typeOfName} name has to be a minimum of 2 characters and a maximum of 10.')
        name = input(f'Enter your {typeOfName} name \n >>> ')
        nameChecker(name, typeOfName)
    return name

def jobChecker(job):
    if(len(job) < 10):
        print('Input error')
        job = input('Enter your job \n >>> ')
        jobChecker(job)
    if(any(char.isdigit() for char in job)):
        print('Input error')
        job = input('Enter your job  \n >>> ')
        jobChecker(job)

    return job

def salaryCheck(salary):
    #Check if it is the good format. Input: 30.500,50

    # Remove the comma and the period from the string to make it into cents
    salaryAsInt = salary.replace('.', '')
    salaryAsInt = salaryAsInt.replace(',', '')

    if(len(salary) < 9):
        print('Input error')
        salary = input('Enter your salary in this format: 20.000,00: ')
        salaryCheck(salary)
    elif(salary[3] == '.' and salary[7] == ','):
        print('Input error')
        salary = input('Enter your salary in this format: 20.000,00: ')
        salaryCheck(salary)
    elif(int(salaryAsInt) < 2000000 or int(salaryAsInt) > 8000000):
        print('Input error')
        salary = input('Enter your salary in this format: 20.000,00: ')
        salaryCheck(salary)

    return '€' + salary

def createJobOfferMail(firstName, lastName, job):
    salary = input('Enter your salary in this format: 20.000,00: ')
    salary = salaryCheck(salary)

    startingDate = input('Starting date: ')
    startingDate = dateChecker(startingDate)

    finalJobOfferEmail = f"""
        Here is the final letter to send:
        Dear {firstName.capitalize()} {lastName.capitalize()},
        After careful evaluation of your application for the position of {job},
        we are glad to offer you the job. Your salary will be {salary} euro annually.
        Your start date will be on {startingDate}. Please do not hesitate to contact us with any questions.
        Sincerely,
        HR Department of XYZ
    """

    print(finalJobOfferEmail)

def createRejectionMail(firstName, lastName, job):
    feedbackOption = input('With or without feedback? Yes/No: \n >>>')

    if(feedbackOption.lower() == 'yes'):
        feedback = input('Your feedback:')
    else:
        feedback = ''

    rejectionMail = f"""
        Dear {firstName} {lastName},
        After careful evaluation of your application for the position of {job},
        {feedback}
        We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.
        Sincerely,
        HR Department of Raccy IT
    """

    print(rejectionMail)

def dateChecker(date):

    if(date.count('-') > 2 or date.count('-') < 0):
        print('Input error')
        date = input('Starting date (format: YYYY-MM-DD): ')
        dateChecker(date)

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    availableYears = ['2021', '2022']

    fullMonths = [1, 3, 5, 7, 8, 10, 12]
    maxDays = 31

    #assign a new value to maxDays
    if(month == '02'):
        maxDays = 28
    elif(int(month) not in fullMonths):
        maxDays = 30
    print(year)
    if(int(day) > maxDays):
        print('Input error')
        date = input('Starting date (format: YYYY-MM-DD): ')
        dateChecker(date)
    elif(year not in availableYears):
        print('Input error')
        date = input('Starting date (format: YYYY-MM-DD): ')
        dateChecker(date)
    elif(0 >= int(month) > 12):
        print('Input error')
        date = input('Starting date (format: YYYY-MM-DD): ')
        dateChecker(date)

    return date

# def createCurrency(amount):
#     currency = "€{:,.2f}".format(amount)

#     main_currency = currency.split('.')[0]
#     fractional_currency = currency.split('.')[1]

#     new_main_currency = main_currency.replace(',', '.')
#     currency = new_main_currency + ',' + fractional_currency

#     return currency

while startApp == True:
    global emailTypes

    writeAnEmail = input('Do you want to create an email? Yes/no: ')

    if(writeAnEmail.lower() != 'yes'):
        exit()


    emailTypes = ['job offer', 'rejection']
    emailType = input('Job offer or Rejection?')
    #Check if the given input is valid
    emailType = emailTypeChecker(emailType)
    # Validation check for the first name
    firstName = input('Enter your first name \n >>> ')
    firstName = nameChecker(firstName, 'first')

    #Validation check for the last name
    lastName = input('Enter your last name \n >>> ')
    lastName = nameChecker(lastName, 'last')

    #Job validation
    job = input('Enter your job  \n >>> ')
    job = jobChecker(job)

    if(emailType.lower() == 'job offer'):
        createJobOfferMail(firstName, lastName, job)
    elif(emailType.lower() == 'rejection'):
        createRejectionMail(firstName, lastName, job)

    newMail = input('New E-mail? Yes/No \n >>> ')

    if(newMail.lower() == 'yes'):
        continue
    else:
        exit()
