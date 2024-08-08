national_mumber_data = [{"First name": "Hallo", "Family name": "2", "National number": "93.07.14-411.07"},
                         {"First name": "John", "Family name": "Doe", "National number": "03.02.15-001.43"}
                         ]

clean_data = []

for i in national_mumber_data:
    national_mumber = []
    # Check if the national number is a number and remove special caractere
    for x in i['National number']:
        if x.isnumeric():
            national_mumber.append(x)
    corrected_national_number =  ''.join(national_mumber)

    corrected_list = {"DateOfBirht": None,
                      "ControlNumber": None,
                      "NationalNumber": None}
    
     # Check if the national number is egal to 11
    if len(corrected_national_number) == 11:
            corrected_list['NationalNumber'] = corrected_national_number
    else:
        print(f"The National number is not valid for the user: {i['First name']}")


    # Apply the date of bith to the new dictionary 
    formmated_data = corrected_national_number[:6]
    new_date = formmated_data[:2] + '/' + formmated_data[2:4] + '/' + formmated_data[4:]
    corrected_list['DateOfBirht'] = new_date
    clean_data.append(corrected_list)

    # Check number of control
    order_number = corrected_national_number[:9]
    modulo_order_number = int(order_number) % 97
    control_number = 97 - modulo_order_number 

    if control_number < 10:
        control_number = "0" + str(control_number)
    
    print(control_number)
    # print(f"test {corrected_national_number[-2:]}")
    if corrected_national_number[-2:] == control_number:
         corrected_list['ControlNumber'] = control_number
         corrected_list['DateOfBirht'] = "19" + corrected_list['DateOfBirht']
    else:
         corrected_list['ControlNumber'] = control_number
         corrected_list['DateOfBirht'] = "20" + corrected_list['DateOfBirht']

print(clean_data)
    
