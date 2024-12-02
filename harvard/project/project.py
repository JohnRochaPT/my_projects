"""
project.py

Final Project
In this final project, my main objective is to demonstrate the ability to implement of some of
the CS50 Programming using Python course.  In this program, I will implement what is described
in the "User story" below.


User story
When a person is hired in the United States of America, the employer is obligated to ensure that
the new employee is indeed allowed to work in the US.  Companies can be fine thousands of dollars
if they fail to validate that all employees are indeed allowed to work in the US. Employers must
proof eligibility by documenting that they reviewed certain documents.  This validation can be
somewhat confusing and we need a program to assist in that validation.  In addition, the program
needs to produce a PDF document which documents the collected evidence so that it can be saved
with the employee's record. Depending on the document(s) the employee submit, they may need one
or two documents.  These documents fall into three category lists:
    1.- List "A" is the strongest list and a single document, is enough to validate.  A sample
        of a List A document would be a USA Passport or Naturalization Certificate.
    2.- List "B" are documents that require to be paired with a second document from List C.  An
        example of a list "B" document would be a state's driver's license, a school ID with
        photos or a ID card issued by a federal or state agency.
    3.- List "C" are documents, while they are official documents, they don't typically have
        pictures or have an expiration date.  Such as birth certificate or Social Security Card.

Program Scope
The program will implement classes, functions, dictionaries and lists, as well as well as the
implementation of libraries.  It will be based on the creation an Employee object and allow the
user to validate employment eligibility, as defined by the US government, and produce a PDF
object which will contain the information on the collected documents. Within the body of the
program, in addition to this docstring, there are multiple documentation sections where I break
down the scope, what the requirements are and my initial approach.  The pseudo code section
was written before any code.
"""

# < Program Information
__date__ = '2024/09/26'
__version__ = '0.0.1'

# .User Story:
#: Obtaining employment is the USA, requires that the individual seeking employment is allowed
#: to work in the US.  The federal government charges the employers with the responsibility in
#: making sure that the individual is indeed allowed to work.  The penalties for failing to
#: complete this obligation, can be tens of thousands of dollars, per incident, as well as
#: carry prison time.  Companies are given a limited time to validate the eligibility of the
#: new employee to be able to work.
#:
#: To confirm that an employee is eligible to work in the US, they need to obtain one document
#: form "List A" or one document from "List B" plus one document from "List C".  For detail
#: information, you can go to https://www.uscis.gov/i-9-central/form-i-9-acceptable-documents
#: Thus, an employee is allowed to work in the US when:
#:
#:  1.- They have one document from List A.  An example of a List A document is a passport
#:      or a Naturalization Certificate from the United States Naturalization Agency
#:  2.- If the employee does not have a List A document, they need one list B document.  An
#:      example of a List B document is a current State's License or a current State issued
#:      id with photos and...
#:  3.- Without a list A document, they need one document from list B and from list C. An
#:      example of a List C document is a Birth Certificate or a Social Security Number
#:      Card.

# .Original Requirements:
#: We need a program that will ask the user for an employee with the following information:
#:  1.- Full name, age and full address.
#:    1.1.- If the employee is under 16, exit the program with a raised ValueError indicating
#:          that individuals under 16, are not allowed to work for this company.
#:  2.- System needs to ask the user to say what list documents do they have and, if the user
#:      requests, provide guidance on what document(s) are needed to complete the validation.
#:  3.- For each of the lists, the program will multiple properties such as "Document name",
#:      document number and state, etc.
#:  4.- Once the verification completes, it will produce a PDF document which records what
#:      documents where used to verify eligibility.
#:

# .My pseudo code approach:
#: 1.- Use sys fpdf libraries
#:
#: 2.- Create a class "Employee" where we will organize, store, and define capabilities
#:     for helping with eligibility validation
#:
#: 3.- Create a "tool kit" type class which will have methods that implement repeated
#:     functionality and provides a central location to control user's input and other
#:     actions.
#:
#: 5.- If the employee is allowed to work in the US, then the program will produce a
#:     PDF certificate with the pertinent validation information.
#:
#: 6.- Serialize the employee object for future reprints.  If the program finds a file
#:     stored locally, it will ask the user if the user just needs the certificate
#:     reprinted.
#:

# .Version Control
#: V1 - File "projectv1.py".
#:    Program is capable of loading the Employee class with demographic information
#:
#: V2 - File "projectv2.py".
#:    Program adds populates the lists of documents and gives the user the ability to
#:    get more information on the document lists and what they contain
#:
#: V3 - File "projectv3.py"
#:    Program fully implements all functionality except producing the PDF output.
#:
#: V4 - File "projectv4.py"
#:    Program fully implements all functionality including producing a PDF.


import us
import re
import zipcodes
import os
import sys
from datetime import datetime
from fpdf import FPDF
import pickle

# | ***********************************************************************************************
# | **********************           C L A S S    S E C T I O N            ************************
# | ***********************************************************************************************


class Kit():
    """
    MyKit
        Class contains class methods that are used as workhorses to perform functions that I use
        often

    """

    @staticmethod
    def get_str_input(msg: str) -> str:
        """
        get_str_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must input at least one character.  If the input is not valid, it will
            keep asking for an input.


        Arguments:
            msg -- A string.  Can be an empty string.

        Returns:
            Returns a string of at least one character
        """
        while True:
            response = input(msg).strip()
            if len(response) == 0:
                pass
            else:
                return response

    @staticmethod
    def get_str_input_even_empty(msg: str) -> str:
        """
        get_str_input_even_empty
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user can choose to enter something or nothing, by hitting enter.  The
            function allows for empty strings

        Arguments:
            msg -- A string.  Can be an empty string.

        Returns:
            Returns a string.  Can be a string of zero length
        """
        return input(msg).strip()

    @staticmethod
    def get_pos_int_input(msg: str) -> str:
        """
        get_pos_int_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must enter at least one positive integer.  If the input is not
            valid, it will keep asking for an input until the user enters a valid integer.

        Arguments:
            msg -- A string.  Can be empty string.

        Returns:
            Returns an integer.
        """
        while True:
            try:
                response = input(msg).strip()
                if '.' in response:
                    pass
                else:
                    response = int(response)
                    return response
            except:
                pass

    @staticmethod
    def get_pos_flt_input(msg: str) -> str:
        """
        get_pos_int_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must enter a positive float.  If the input is not valid, it will
            keep asking for an input until the user enters a valid integer.

        Arguments:
            msg -- A string.  Can be empty string.

        Returns:
            Returns an float.
        """
        while True:
            try:
                response = input(msg).strip()
                if '.' in response:
                    response = float(response)
                    return response
                else:
                    pass
            except:
                pass

    @staticmethod
    def lines():
        """
         lines
            Function prints a separator section to make it easier to read when looking at the
            terminal window.  Use it instead of multiple print() lines
        """
        name = __file__.split('\\')[len(__file__.split('\\'))-1]
        stars = int(((80-len(name))/2))
        line = '\n' * 6 + '=' * stars + ' ' * 5 + name + ' ' * 5 + '=' * stars + '\n'
        print(line, end='')

    @staticmethod
    def clear_scr():
        """
        clear_scr
            Function clears the screen.  Function is OS aware
        """
        os.system('cls' if (os.name == 'nt') else 'clear')
        Kit.lines()

    @staticmethod
    def format_validator(str_to_validate: str, pattern_cd: str) -> re.Match:
        """
        format_validator
            Function facilitates the validating of strings against certain formats.

            Function uses the "re" library to perform regular expression matches.  If the
            contents of the string matches the pattern, it returns True.  If there is no
            match, it returns false.  When calling this function send the string to be
            validated and the following codes for specialized formats:

                "zip" when validating the format for zip codes
                "phone" when validating a phone number
                "date" when validating YYYY-MM-DD for dates
                "SSN" when validating Social Security Numbers

        Arguments:
            str_to_validate -- Non empty string to use matched against a pattern
            pattern_cd -- Regular expression pattern.

        Returns:
            Returns a re.Match object.  Either empty or not.  If not empty, there
            was a match
        """
        match pattern_cd:
            case 'zip':
                pattern = r'^[0-9]{5}$'
            case 'phone':
                pattern = r'^[0-9](-|.| )[0-9]{3}(-|.| )[0-9]{3}(-|.| )[0-9]{4}$'
            case 'date':
                pattern = r'^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$'
            case 'ssn':
                pattern = r'^[0-9]{3}-[0-9]{2}-[0-9]{4}$'

        return re.search(pattern, str_to_validate, re.IGNORECASE)


class Employee():
    def __init__(self, first, last, age):
        self._first: str = first
        self._last: str = last
        self._age: int = age
        self._address = dict()
        self._phone_number: str = str()
        self._has_list_a = list()
        self._has_list_bc = list()

    def __repr__(self) -> str:
        return f'employee = Employee({self._first}, {self._last}, {self._age})'

    def __str__(self) -> str:
        return f'{self._first} {self._last}'

    @property
    def first(self) -> str:
        return self._first

    @first.setter
    def first(self, name):
        self._first = name

    @property
    def last(self) -> str:
        return self._last

    @last.setter
    def last(self, name):
        self._last = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def address(self) -> dict:
        return self._address

    @address.setter
    def address(self, address_list: dict):
        self._address = address_list

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone):
        pattern = r'^[0-9](-|.| )[0-9]{3}(-|.| )[0-9]{3}(-|.| )[0-9]{4}$'
        matches = re.search(pattern, phone, re.IGNORECASE)
        if matches:
            self._phone_number = phone
        else:
            print('Invalid phone number format')

    @property
    def has_list_a(self) -> list:
        return self._has_list_a

    @has_list_a.setter
    def has_list_a(self, lst):
        self._has_list_a = lst

    @property
    def has_list_bc(self):
        return self._has_list_bc

    @has_list_bc.setter
    def has_list_bc(self, lst):
        self._has_list_bc = lst


class MyPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self._title = str()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, nm):
        self._title = nm


# | ***********************************************************************************************
# | **********************    M A I N    P R O G R A M    S E C T I O N    ************************
# | ***********************************************************************************************


def main():
    # < The first thing the program does is to introduce itself.  The user will have the option
    # < to continue or exit the program.
    if proceed():
        pass
    else:
        quit()

    # < Get the employee's first name
    Kit.clear_scr()
    msg = 'Let\'s start with the employee\'s name and age.\n\n'
    print(msg, end='')
    first = Kit.get_str_input('Enter Employee\'s First Name: ')
    last = Kit.get_str_input('Enter Employee\'s Last Name: ')
    while True:
        age = Kit.get_pos_int_input('Enter the Employee\'s age: ')
        if age > 16:
            break

    # < Making an employee from Employee class
    employee = Employee(first, last, age)
    print()
    input(f'Employee {employee} has been created.  Press enter to continue ')

    # < Now, let's capture the employee's demographic information
    Kit.clear_scr()
    print('\n\n')
    msg = f'Now, let\'s please enter the employee\'s demographic information:'
    print(msg)
    address1 = Kit.get_str_input('Enter Employee\'s Street Address One: ')
    address = {'Address 1': address1}
    address2 = Kit.get_str_input_even_empty('Enter Employee\'s Street Address Two: ')
    address['Address 2'] = address2
    city = Kit.get_str_input('Enter Employee\'s City: ')
    address['City'] = city

    # < The state requires validation.  Function "get_state()" will do this work
    state = get_state()
    address['State'] = state

    # < Getting the zip code requires that we validate format of the zip code.
    address['Zip Code'] = get_zip()

    # < Now that we have the entire address, let's add it
    employee.address = address

    # < Now let's get the phone number
    while True:
        msg = 'Enter the employee\'s phone number in format (#-###-###-####) or'
        msg += ' (# ### ### ####): '
        employee.phone_number = Kit.get_str_input(msg)
        result = Kit.format_validator(employee.phone_number, pattern_cd='phone')
        if result:
            break

    msg = f'\n\n{employee.first} {employee.last} is {employee.age} old'
    msg += f' and lives at:\n{employee.address['Address 1']}, in {employee.address['City']}, '
    msg += f'{employee.address['State']} zip {employee.address['Zip Code']} \nand phone number'
    msg += f' {employee.phone_number}\n'
    print(msg)
    input('Employee\'s demography information has been saved.  Press enter to continue  ')

    # < At this point, we have all of the basic elements for a new employee.  Now it is
    # < time to begin validation
    list_a = load_list_a()
    list_b = load_list_b()
    list_c = load_list_c()

    present_doc_info(list_a, list_b, list_c)

    # < Now we can ask the user what list(s) they will choose
    while True:
        Kit.clear_scr()
        msg = 'Please select what document validation list options you would like to use.  Your '
        msg += 'available options are:\n\n'
        msg += '\tOption [1] - Requires the verification a single document from List A\n'
        msg += '\tOption [2] - Requires the verification of a document from List B and a '
        msg += 'document from List C\n\n'
        msg += 'What option would you like to select.  Enter [1] or [2]: '
        print(msg, end='')
        list_option = input().strip()
        if list_option == '1' or list_option == '2':
            break

    # < Now let's enter the validation documents.
    if list_option == '1':
        # < If the user selected option 1, only one document from List A is needed
        employee = get_list_a(employee, list_a)
    else:
        # < If the user selected option 2, we need to collect one document from List B and one from
        # < list C
        employee = get_list_bc(employee, list_b, list_c)

    print_PDF(employee)

    with open('data.pickle', 'wb') as file:
        pickle.dump(employee, file)

    quit()


#
#
#
# | ***********************************************************************************************
# | **************************    F U N C T I O N     S E C T I O N    ****************************
# | ***********************************************************************************************

# < Program control


def proceed() -> bool:
    """
    proceed
        Function introduces the program to the user and asks the user if the user wants to
        continue.  If the user agrees, it will continue.

        When the function is called, it will first clear the screen and then print a few lines
        which introduce the program to the user.  The user is asked to enter "y", case insensitive,
        or "n", case insensitive, if they don't.  If the user agrees to continue, it will return
        True otherwise it will return False

    Returns:
        Returns either True or False depending on if the user wants to continue or not.
    """
    # < Do we already have a file?
    reprint = False
    try:
        with open('data.pickle', 'rb') as file:
            employee = pickle.load(file)
            reprint = True
    except:
        pass

    if reprint:
        Kit.clear_scr()
        msg = f'The program detected a record for {employee}.  You would like to reprint '
        msg += 'the employee\'s certificate?.\n'
        msg += 'Enter [y] to reprint or [n] to enter a new employee: '
        print(msg, end='')
        while True:
            result = input().strip().lower()
            if result == 'y' or result == 'n':
                if result == 'y':
                    print_PDF(employee)
                    quit()
                break

    employee = None
    Kit.clear_scr()
    intro = 'Welcome to our Employee Eligibility Verification Program.\n'
    intro += 'This program allows you to print a certificate of eligibility if the employee has\n'
    intro += 'submitted the correct combination of documents.\n\n'
    intro += 'If you would like to proceed, type or enter [y], or [n] to exit.\n\n'
    intro += 'Would you like to proceed [y] or [n]: '

    while True:
        print(intro, end='')
        response = input().strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False


# < Handles Zip Codes
def get_zip(zip_code: str = str()) -> str:
    """
    get_zip
        Function uses library "re" to ensure the user enters a valid zip code.  A valid zip code
        contains 5 characters where they are all numbers.

    Parameters:
        zip_code.  Parameter is optional.  If we are testing the function using pytest, we can
        pass a string and it will match against that string.

    How to test:
        If you are testing within a program and expect the user to enter an a zip code, simply
        call the function as follows (Do not pass any parameters):
                returned_zip_code = get_zip()

        If you would like to pass a zip code to the function, and have it validated but not ask
        the user, call the function by passing a string.  As follows:
                returned_zip_code = get_zip('05648')

    Returns:
        Returns a properly format verified zip code.
    """
    original_zip = zip_code

    while True:
        if len(zip_code) == 0:
            # < Need to ask for an input
            zip_code = Kit.get_str_input('Enter Employee\'s zip code: ')
        else:
            zip_code = original_zip
        matches = Kit.format_validator(str_to_validate=zip_code, pattern_cd='zip')

        # < Now we are going to validate that the zipcode is actually a real zipcode
        if matches and zipcodes.is_real(zip_code):
            return str(matches[0])
        else:
            if len(original_zip) > 0:
                return None


# < Function gets a state or validates that the passed state is valid.
def get_state(state_var: str = str()) -> str:
    """
    get_state
        Function uses a special library to help in making sure the user enters a valid state.  It
        allows the user to enter multiple versions for the state name.  If state is validated, it
        will return the correct state name presentation.

    Extended Information:
        Function will accept the abbreviation version of state names or the full name of the state
        and will validate if the state is indeed valid.  If it is, it will return the complete
        name of the state, even if the user entered abbreviations.

    Keyword Arguments:
        state -- Can be an empty string if intended to ask the user for a state.

    Returns:
        Returns an empty string if the state is not found.  It will return the fully qualified
        name, if the state is found.
    """
    while True:
        if len(state_var) == 0:
            state = Kit.get_str_input('Enter Employee\'s State: ')
        else:
            state = state_var
        if us.states.lookup(state):
            st = str(us.states.lookup(state))
            return st
        else:
            if len(state_var) > 0:
                return None


def load_list_a() -> list:
    """
    load_list_a
        Function accepts an empty list and loads List A type documents in the form of individual
        dictionaries, with the document properties.

    Returns:
        A list of dictionaries populated with List A document types and properties
    """
    # < Number 1
    docs = list()
    doc_name = 'U.S. Passport or U.S. Passport Card'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Country': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 2
    doc_name = 'Permanent Resident Card or Alien Registration Receipt Card (Form I-551)'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Country': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 3
    doc_name = 'Foreign passport that contains a temporary I-551 stamp or temporary I-551'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Country': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 4
    doc_name = 'Foreign passport with Form I-94 or I-94A with Arrival-Departure dates and'
    doc_name += ' endorsement to work'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Country': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 5
    doc_name = 'Passport from the Federated States of Micronesia (FSM) or the Republic of the'
    doc_name += ' Marshall Islands (RMI)'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Country': '',
        'Number': '',
        'Expiration Date': ''})

    return docs


def load_list_b() -> list:
    """
    load_list_b
        Function accepts an empty list and loads List b type documents in the form of individual
        dictionaries, with the document properties.

    Returns:
        A list of dictionaries populated with List B document types and properties
    """
    docs = list()
    # < Number 1
    doc_name = 'Driver\'s license or ID card issued by a State or outlying possession of the '
    doc_name += 'United States '
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 2
    doc_name = 'ID card issued by federal, state or local government agencies or entities of the '
    doc_name += 'United States '
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 3
    doc_name = 'School ID card with a photograph'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 4
    doc_name = 'Voter\'s registration card'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 5
    doc_name = 'U.S. Military card or draft record'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 6
    doc_name = 'Military dependent\'s ID card'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 7
    doc_name = 'U.S. Coast Guard Merchant Mariner Card'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': '',
        'Expiration Date': ''})

    # < Number 8
    doc_name = 'Native American tribal document'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': '',
        'Expiration Date': ''})

    return docs


def load_list_c() -> list:
    """
    load_list_b
        Function accepts an empty list and loads List b type documents in the form of individual
        dictionaries, with the document properties.

    Returns:
        A list of dictionaries populated with List B document types and properties
    """
    docs = list()

    # < Number 1
    doc_name = 'U.S. Social Security Card'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': ''})

    # < Number 2
    doc_name = 'Birth certificates issued by the Department of State (Forms DS-1350, FS-545, '
    doc_name += 'FS-240) United States '
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': ''})

    # < Number 3
    doc_name = 'Original or certified copy of birth certificate issued by a State or territory '
    doc_name += 'of the United States'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': ''})

    # < Number 4
    doc_name = 'Native American tribal document'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': ''})

    # < Number 5
    doc_name = 'U.S. Citizen ID Card (Form I-197)'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': ''})

    # < Number 6
    doc_name = 'Identification Card for Use of Resident Citizen in the United States (Form I-179)'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': ''})

    # < Number 7
    doc_name = 'Employment authorization document issued by the Department of Homeland Security'
    doc_name += '(DHS)'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': ''})

    # < Number 8
    doc_name = 'Native American tribal document'
    docs.append({
        'Doc Name': doc_name,
        'Issuing Authority': '',
        'Number': ''})

    return docs


def present_doc_info(list_a: list, list_b: list, list_c: list):
    """
    present_doc_info
        Function allows the users to review what constitutes List A, List B and List C documents

    """
    Kit.clear_scr()
    msg1 = 'To verify if an employee is allowed to work in the United States, you must choose'
    msg1 += ' 1 document\n from List A or 1 document from List B AND 1 document from List C.\n'
    msg2 = 'If you are familiar with these lists, enter [skip] and press enter to move directly to'
    msg2 += ' the next \nsection.  If you would like detail information on these lists, enter '
    msg2 += '[info] followed by \nthe enter key.\n\n'
    print(msg1)
    print(msg2)

    while True:
        resp = Kit.get_str_input('How would you like to proceed [skip] or [info]: ').lower()
        if resp == 'skip':
            break
        elif resp == 'info':
            Kit.clear_scr()
            msg = 'If the employee has a document from List A, they only need to present one'
            msg += ' to demonstrate eligibility.\n\n'
            msg += 'List A documents are: \n'
            print(msg, end='')
            for i in range(len(list_a)):
                print(f'[{i + 1}] - {list_a[i]['Doc Name']}')
            input('Press the enter key to continue ')

            Kit.clear_scr()
            msg = 'If the employee does not have a document from List A, they need to provide'
            msg += ' one document from List B \nAND one from List C to demonstrate eligibility.\n\n'
            msg += 'List B documents are: \n'
            print(msg, end='')
            for i in range(len(list_b)):
                print(f'[{i + 1}] - {list_b[i]['Doc Name']}')
            input('Press the enter key to continue ')

            Kit.clear_scr()
            msg = 'If the employee does not have a document from List A, they need to provide'
            msg += ' one document from List B \nAND one from List C to demonstrate eligibility.\n\n'
            msg += 'List C documents are: \n'
            print(msg, end='')
            for i in range(len(list_c)):
                print(f'[{i + 1}] - {list_c[i]['Doc Name']}')
            input('Press the enter key to continue ')


def get_list_a(employee: Employee, list_a: list) -> Employee:
    """
    get_list_a
        Function accepts an employee and allows the user to enter a document from List A.

    Arguments:
        employee -- A populated employee of class Employee ready to accept a document from
                    list A
        list_a -- A fully populated list of A documents

    Returns:
        Returns a populated employee
    """
    Kit.clear_scr()
    msg = 'Please select which List A document you have.  Your options are:\n\n'
    print(msg)
    for i in range(len(list_a)):
        print(f'[{i + 1}] - {list_a[i]['Doc Name']}')

    while True:
        resp = Kit.get_pos_int_input('Please select which document you have: ')
        if 0 < resp <= 5:
            issuing_country = Kit.get_str_input('Please enter the name of the issuing country: ')
            doc_number = Kit.get_str_input('Please enter the document number: ')
            expiration_dt = Kit.get_str_input('Please enter the expiration date [YYYY-MM-DD]: ')
            # < Date validation can be done in a single line of code with using the datetime library
            # < but I wanted to practice using regular expressions
            matches = Kit.format_validator(str_to_validate=expiration_dt, pattern_cd='date')
            if matches and (datetime.strptime(expiration_dt, '%Y-%m-%d')):
                employee.has_list_a = [
                    {
                        'Doc Name': list_a[resp - 1]['Doc Name'],
                        'Issuing Country': issuing_country,
                        'Number': doc_number,
                        'Expiration Date': expiration_dt}]
            return employee


def get_list_bc(employee: Employee, list_b: list, list_c: list) -> Employee:
    """
    get_list_bc
        Function accepts an employee and allows the user to enter one document from List B and one
        document from List C.

    Arguments:
        employee -- A populated employee of class Employee ready to accept documents from List B
                    and one document from list C
        list_b -- A fully populated list of B documents
        list_c -- A fully populated list of C documents

    Returns:
        Returns a populated employee
    """
    Kit.clear_scr()
    msg = 'Please select which List B document you have.  Your options are:\n\n'
    print(msg)
    for i in range(len(list_b)):
        print(f'[{i + 1}] - {list_b[i]['Doc Name']}')

    while True:
        resp = Kit.get_pos_int_input('Please select which document you have: ')
        if 0 < resp <= 8:
            issuing_authority = Kit.get_str_input('Please enter the name of the issuing authority: ')
            doc_number = Kit.get_str_input('Please enter the document number: ')
            expiration_dt = Kit.get_str_input('Please enter the expiration date [YYYY-MM-DD]: ')
            matches = Kit.format_validator(str_to_validate=expiration_dt, pattern_cd='date')
            # < Date validation can be done in a single line of code with using the datetime library
            # < but I wanted to practice using regular expressions
            if matches and (datetime.strptime(expiration_dt, '%Y-%m-%d')):
                employee.has_list_bc = [
                    {
                        'Doc Name': list_b[resp - 1]['Doc Name'],
                        'Issuing Authority': issuing_authority,
                        'Number': doc_number,
                        'Expiration Date': expiration_dt}]
                break

    Kit.clear_scr()
    msg = 'Please select which List C document you have.  Your options are:\n\n'
    print(msg)
    for i in range(len(list_c)):
        print(f'[{i + 1}] - {list_c[i]['Doc Name']}')

    while True:
        resp = Kit.get_pos_int_input('Please select which document you have: ')
        if 0 < resp <= 8:
            issuing_authority = Kit.get_str_input('Please enter the name of the issuing authority: ')
            # < Validate format for SSN - ^[0-9]{3}-[0-9]{2}-[0-9]{4}$
            if resp == 1:
                while True:
                    doc_number = Kit.get_str_input('Please enter the document number [###-##-####]: ')
                    matches = Kit.format_validator(str_to_validate=doc_number, pattern_cd='ssn')
                    if matches:
                        break
                    else:
                        continue
            employee.has_list_bc.append(
                {
                    'Doc Name': list_c[resp - 1]['Doc Name'],
                    'Issuing Authority': issuing_authority,
                    'Number': doc_number})
            return employee


def print_PDF(employee: Employee):
    """
    print_PDF
        Function prints PDF certificate

    Arguments:
        employee -- A fully populated employee
    """
    pdf = MyPDF()
    pdf.add_page()
    pdf.set_page_background((255, 255, 255))

    with pdf.local_context(fill_opacity=0.25):
        pdf.image('seal.png', 190, 8, 100)


    pdf.set_y(20)
    pdf.add_font("scriptJR", style="", fname=r'ITCEDSCR.TTF')
    pdf.set_font(family='scriptJR', style='', size=55)
    pdf.cell(w=300, h=15, text='Employee Eligibility Certificate', new_x="LMARGIN", new_y="NEXT",
             border=0, align='C')

    pdf.ln(4)
    msg = 'This certificate confirms that the employee is eligible to work in the USA'
    pdf.set_font(family='helvetica', size=10, style='I')
    pdf.cell(w=300, h=5, text=msg, border=0, align='C', fill=False, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(20)

    pdf.set_font(family='helvetica', size=14)
    msg = f'This document certifies that the employee below has demonstrated full eligibility to '
    msg += 'work in the United States of America and'
    pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L', fill=False)

    msg = 'has provided the with the following information:'
    pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L', fill=False)
    pdf.ln(12)

    # < Name
    pdf.set_font(family='helvetica', size=13)
    pdf.set_left_margin(45)
    pdf.set_fill_color(r=0, g=0, b=142)
    pdf.set_text_color(r=255, g=255, b=255)
    col_1 = f'Name:'
    pdf.cell(w=40, h=6.5, text=col_1, border=1, align='L', fill=True)
    pdf.set_fill_color(r=255, g=255, b=255)
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_x(85)
    col_2 = f'{employee.first} {employee.last}'
    pdf.cell(w=150, h=6.5, text=col_2, new_x='LMARGIN', new_y='NEXT',
             align='L', fill=False, border=1)

    # < Age
    pdf.ln(0.35)
    pdf.set_left_margin(45)
    pdf.set_fill_color(r=0, g=0, b=142)
    pdf.set_text_color(r=255, g=255, b=255)
    col_1 = f'Age:'
    pdf.cell(w=40, h=6.5, text=col_1, border=1, align='L', fill=True)
    pdf.set_fill_color(r=255, g=255, b=255)
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_x(85)
    col_2 = f'{str(employee.age)} years old'
    pdf.cell(w=150, h=6.5, text=col_2, new_x='LMARGIN', new_y='NEXT',
             align='L', fill=False, border=1)

    # < Address
    pdf.ln(0.35)
    pdf.set_left_margin(45)
    pdf.set_fill_color(r=0, g=0, b=142)
    pdf.set_text_color(r=255, g=255, b=255)
    col_1 = f'Address:'
    pdf.cell(w=40, h=6.5, text=col_1, border=1, align='L', fill=True)
    pdf.set_fill_color(r=255, g=255, b=255)
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_x(85)
    col_2 = f'{employee.address['Address 1']}, {employee.address['Address 2']}, '
    col_2 += f'{employee.address['City']}, {employee.address['State']}, '
    col_2 += f'{employee.address['Zip Code']}'
    pdf.cell(w=150, h=6.5, text=col_2, new_x='LMARGIN', new_y='NEXT',
             align='L', fill=False, border=1)

    # < Phone number
    pdf.ln(0.35)
    pdf.set_left_margin(45)
    pdf.set_fill_color(r=0, g=0, b=142)
    pdf.set_text_color(r=255, g=255, b=255)
    col_1 = f'Phone:'
    pdf.cell(w=40, h=6.5, text=col_1, border=1, align='L', fill=True)
    pdf.set_fill_color(r=255, g=255, b=255)
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_x(85)
    col_2 = f'{employee.phone_number}'
    pdf.cell(w=150, h=6.5, text=col_2, new_x='LMARGIN', new_y='NEXT',
             align='L', fill=False, border=1)

    pdf.ln(25)
    pdf.set_left_margin(10)
    pdf.set_font(family='scriptJR', style='', size=25)
    msg = f'John Rocha'
    pdf.cell(w=50, h=7, text=msg, align='C', border='B')
    pdf.set_font(family='helvetica', size=14)
    msg = f'presented the following document(s) which provided evidence of full eligibility'
    msg += f' to work in the USA:'
    pdf.cell(w=40, h=7, text=msg, new_y="NEXT", border=0, align='L')

    pdf.ln(13)
    if len(employee.has_list_a) > 0:
        pdf.set_font(family='helvetica', size=11.5)
        msg = f'List A Document - {employee.has_list_a[0]['Doc Name']}'
        pdf.set_left_margin(45)
        pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L',
                 fill=False)
        pdf.ln(0.5)
        pdf.set_left_margin(79)
        msg = f'Number [{employee.has_list_a[0]['Number']}] and was issued by '
        msg += f'[{employee.has_list_a[0]['Issuing Country']}]'
        pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L',
                 fill=False)
        pdf.ln(0.5)
        msg = f'with an expiration date of [{employee.has_list_a[0]['Expiration Date']}]'
        pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L',
                 fill=False)
    else:
        pdf.set_font(family='helvetica', size=11.5)
        msg = f'List B Document - {employee.has_list_bc[0]['Doc Name']}'
        pdf.set_left_margin(45)
        pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L',
                 fill=False)
        pdf.ln(0.5)
        pdf.set_left_margin(79)
        msg = f'Number [{employee.has_list_bc[0]['Number']}] and was issued by '
        msg += f'issuing authority of [{employee.has_list_bc[0]['Issuing Authority']}]'
        pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L',
                 fill=False)
        pdf.ln(0.5)
        msg = f'with an expiration date of [{employee.has_list_bc[0]['Expiration Date']}]'
        pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L',
                 fill=False)
        pdf.ln(4)
        msg = f'List C Document - {employee.has_list_bc[1]['Doc Name']}'
        pdf.set_left_margin(45)
        pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L',
                 fill=False)
        pdf.ln(0.5)
        pdf.set_left_margin(79)
        msg = f'Number [{employee.has_list_bc[1]['Number']}] and was issued by '
        msg += f'issuing authority of [{employee.has_list_bc[1]['Issuing Authority']}]'
        pdf.cell(w=200, h=5, text=msg, border=0, new_x='LMARGIN', new_y='NEXT', align='L',
                 fill=False)

    while True:
        try:
            pdf.output('certificate.pdf')
            break
        except:
            input('Close PDF file please')

    Kit.clear_scr()
    print('This concludes the execution of your program.\n')
    print('Thank you for using our program.  Your certificate has been created')



    #
    #
    #
    #
    # | ***********************************************************************************************
    # | **********************           C A L L   S E L F   M A I N           ************************
    # | ***********************************************************************************************
    # > Call main ONLY when intended
if __name__ == '__main__':
    main()
