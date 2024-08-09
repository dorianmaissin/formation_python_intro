# --------------------------------------->>>>>>>> IMPORT
from datetime import datetime
import pprint as pp
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
# --------------------------------------->>>>>>>> DATA
# Data to be clean
national_mumber_data = [{"First name": "Hallo", "Family name": "2", "National number": "93.07.14-411.07"},
                         {"First name": "John", "Family name": "Doe", "National number": "03.02.15-001.43"},
                         {"First name": "Alice", "Family name": "Water", "National number": "93.07.14-411"}
                         ]

# Final Data
clean_data = []

# --------------------------------------->>>>>>>> FUNCTION

# Correvert to date formart and add the birthday to the dictionary
def generate_date_and_birthday(century):
    corrected_list['ControlNumber'] = control_number
    corrected_list['DateOfBirht'] = century + corrected_list['DateOfBirht']
    date_format = '%Y/%m/%d'
    date_of_birth = corrected_list['DateOfBirht']
    formatted_date = datetime.strptime(date_of_birth, date_format)
    date_of_birth = formatted_date
    today = datetime.today()
    age = today.year - date_of_birth.year
    corrected_list['Age'] = age
    formatted_date_two = formatted_date.strftime('%d/%B/%Y')
    corrected_list['DateOfBirht'] = formatted_date_two

def calculate_modulo_97():
    order_number = corrected_national_number[:9]
    modulo_order_number = int(order_number) % 97
    control_number = 97 - modulo_order_number
    return control_number

# add slash to the string witht the number of the birthday
def formated_date(date):
    formmated_data = date
    new_date = formmated_data[:2] + '/' + formmated_data[2:4] + '/' + formmated_data[4:]
    corrected_list['DateOfBirht'] = new_date
    clean_data.append(corrected_list)

def append_control_national_number(control_num, corrected_national_num):
    corrected_list['ControlNumber'] = control_num
    corrected_list['NationalNumber'] = corrected_national_num+ control_num

# --------------------------------------->>>>>>>> MAIN LOOP
for i in national_mumber_data:
    national_mumber = []
    # Check if the national number is a number and remove special caractere
    for x in i['National number']:
        if x.isnumeric():
            national_mumber.append(x)
    corrected_national_number =  ''.join(national_mumber)

    # Creation of the new dictionary
    corrected_list = {"DateOfBirht": None,
                      "ControlNumber": None,
                      "NationalNumber": None,
                      "Age": None}
    
     # Check if the national number is egal to 11
    if len(corrected_national_number) == 11:
            corrected_list['NationalNumber'] = corrected_national_number

    # Add the control number if the size if the national number is equal to 9 
    elif len(corrected_national_number) == 9:
        control_number = calculate_modulo_97()
        if control_number < 10:
            control_number = "0" + str(control_number)
            append_control_national_number(control_number, corrected_national_number)
        else:
            append_control_national_number(control_number, corrected_national_number)
    else:
        print(f"The National number is not valid for the user: {i['First name']}")

    # Apply the date of bith to the new dictionary 
    formated_date(corrected_national_number[:6])

    # Check number of control
    control_number = calculate_modulo_97()

    if control_number < 10:
        control_number = "0" + str(control_number)
    else:
        control_number = str(control_number)


    if corrected_list['NationalNumber'][-2:] == control_number:
        generate_date_and_birthday("19")
    else:
        generate_date_and_birthday("20")

pp.pprint(clean_data)
    
