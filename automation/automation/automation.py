import  re
import shutil
from faker import Faker
"""
working in a  document called a  potential-contacts by reading file and extract data using of faker and regex library, 
find and collect all email addresses and phone numbers.
the phone numbers should be stored in xxx-yyy-zzzz format.
when the  emails and phone numbers are found they should be stored in two separate documents.
"""
fake = Faker('en_US')

with open('potential-contacts.txt', 'r') as f:
    
    data_file = f.read().replace('\n', '')


regexForEmail = re.compile(r'''([a-zA-Z0-9._%+-]+ @[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)

regexForPhone = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE)


arr_email = []

arr_phone = []



for phone_obj in regexForPhone.findall(data_file):

    number_phone = '-'.join([phone_obj[1], phone_obj[3], phone_obj[5]])
    
    number_phone = re.sub(r'[(|)]','', number_phone)
    
    if number_phone not in arr_phone:
    
        arr_phone.append(number_phone)

for email_obj in regexForEmail.findall(data_file):
    
    if email_obj[0] not in arr_email:
    
        arr_email.append(email_obj[0])

arr_phone.sort()

arr_email.sort()

with open("./assets/phone_numbers.txt","w+") as f:
    
    for obj in arr_phone:
    
     f.write(obj + "\n")

with open("./assets/emails.txt","w+") as f:
    
    for obj in arr_email:
    
     f.write(obj + "\n")