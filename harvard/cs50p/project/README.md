
# Employee Eligibility Verification Tool
In this final CS50 assignment, my main objective is to demonstrate the **ability to implement** of most concepts and techniques taught in the CS50 Programming using Python course. In this assignment, I will implement a solution that addresses the below user story.  
> **Note:** This readme file has essentially **two sections**.  The first section is more of a summary section designed to allow the reader to gain a high level understanding of the solution the program tries to resolve and the approach.   It then proceeds to a more detail section where the task is broken down further. 

#### Video Demo:  <[CS50 Final Project](https://youtu.be/7osw9SbpJlA) >

## Files

 - **project.py** ⇒ File is the main python project file
 - **test_project.py** ⇒ File completes performs the required unit testing
 - **seal.png** ⇒ File is an asset file used as part of the PDF file that the program produces
 - **certificate.pdf** ⇒ File is the PDF output produced by the program
 - **data.pickle** ⇒ File contains a serialized copy of the Employee class defined in the program.
 - **image.png** ⇒ File contains sample of the PDF this program produces.
 - **requirements.txt** ⇒ File a list of the libraries that need to be installed.
 - **ITCEDSCR.TTF** ⇒ File is a special font used in the program.

## Brief User Story:
When a person is hired in the United States of America, the employer is obligated to ensure that the new employee is indeed **allowed to work in the United States**.  Companies can be fined thousands of dollars if they fail to validate that all employees are indeed allowed to work in the US. Employers must proof eligibility by attesting they reviewed certain documents.

This validation can be somewhat confusing. Therefore we need a program to assist in that validation. In addition, to assist in validation, we would like the program to produce a PDF document which we can store with the employee's profile. Depending on the document(s) the employee submits, they may need to present more than one document. Valid documents fall under three categories:

 1. **List A Documents** - Is the strongest list and a single document is enough to validate eligibility. A example of a List "A" document would be a USA Passport or Naturalization Certificate.
 2. **List B Documents** - Are documents that require to be paired with a second document from List "C". An example of a list "B" document would be a State's Driver's License, a school ID with photos or a ID card issued by a federal or state agency.
 3. **List C Documents**  - Are documents, which while they are official documents, they don't typically have pictures or have an expiration date. Such as birth certificate or Social Security Card.

# Detailed Section
This section will breakdown the above user story and my approach to solving the identified problem.


## Program Scope
My objective in this program is to demonstrate my ability to successfully implement the various concepts taught in the CS50 course. I did not want to write something that just met the minimum requirements but something that was worth of submitting to the Harvard's CS50 team. In this program I will be showcasing:

 - **Utility Class** - Developed an utility class that contains a significant number of static methods with code that I use often within the program itself
 - **Main Class** -  Complex class which becomes the main subject in the program. This class has:
	 - Getters and Setters
	 - Method behaving as attributes
	 - Lists variables which themselves contain dictionaries
	 - Dictionary variables
 - Comprehensive **Docstring(s)** which include how to test information
 - Comprehensive validation routines, **using regular expressions as well as other techniques**, including (if appropriate, the user will be asked to re-enter their input):
	 - Single **- context aware -** validator function that can implement multiple regular expression patterns depending on the way it is called
	 - Logical variables, such as those storing US States, indeed **validate** that they do contain real States before loading them.
	 - Zip codes variables, contain real zip codes and not just that they look like zip codes
	 - Phone numbers allow for multiple formats
	 - Dates are formatted properly as well as they are valid dates
 - Implements **Serialization** techniques
	 - Program saves the main subject "object" in a populated state
	 - Saves in a binary file
	 - Users can load a new employee or print an existing employee
 - **Complex functions** which **return complex objects**, such as lists and dictionaries or even my own objects

## Expanded User Story
Obtaining employment is the USA, requires that the individual seeking employment is allowed to work in the US. The federal government charges the employers with the responsibility in making sure that the individual is indeed allowed to work. The penalties for failing to complete this obligation, can be tens of thousands of dollars, per incident, as well as carry prison time. Companies are given a limited time to validate the eligibility of the new employee to be able to work.

To confirm that an employee is eligible to work in the US, they need to obtain one document form "List A" or one document from "List B" PLUS one document from "List C". For detail information, you can go to https://www.uscis.gov/i-9-central/form-i-9-acceptable-documents Thus, an employee is allowed to work in the US when:

 1. **One List A Document:** Employees can show eligibility with one document from List A. An example of a List A document is a **US Passport** or a **Naturalization Certificate** from the United States Naturalization Agency
 2. If the employee does not have a List A document, they need one document from List B and one document from List C. An example of a List B document is a current **State's License** or a current **State Issued ID** with photos
 3. List C documents typically don't have a photo or an expiration date.  An example of a List C document is a **Birth Certificate** or a **Social Security Number** Card.

## Expanded User Requirements:
We need a program that will ask the user for an employee with the following information:

 - Full name, age and full address
	 - If the employee is under 16, exit the program with a raised ValueError indicating that individuals under 16, are not allowed to work for this company
 - System needs to ask the user to say what list documents do they have and, if the user requests, provide guidance on what document(s) are needed to complete the validation.
 - For each of the lists, the program will have multiple properties such as "Document name", document number and state, etc.
 - Once the verification completes, it will produce a PDF document which records what documents where used to verify eligibility.

## My pseudo code approach:

 - Use **sys**, **fpdf**, **datetime**, **os**, **zipcode**, **pickle** and **re** libraries
 - Create a class **Employee** where we will organize, store, and define capabilities for helping with eligibility validation
 - Create a **tool kit** type class which will have methods that implement repeated functionality and provides a central location to control user's input and other actions.
 - If the employee is allowed to work in the US, then the program will **produce a PDF certificate** with the pertinent validation information.
 - Once the program prints a certificate, it saves the "employee" object serialized. When the program loads, if it finds a serialized employee object, it allows the user to simply reprint the certificate or load a new employee.  

 

# Sample Certificate
![alt text](image.png)

 
