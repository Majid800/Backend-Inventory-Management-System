#Generating unqiue medicine code from the manual entry of medicine from user
#code layout for example: Atorvstatin 20mg Tablets -> ATO20TAB 
#The first three letters of medicine name, then the strength as integers, finally first three letters of the formulation of medicine. 



def generate_medicine_code(name, strength, formulation, manufacturer, pack_size):
    cleaned_name = ""

    for character in name:
        if character.isalpha():
            cleaned_name = cleaned_name + character 

    cleaned_name = cleaned_name.upper()

    name_part = cleaned_name[:3]

    strength_digits = ""

    for character in strength:
        if character.isdigit():
            strength_digits = strength_digits + character 
    
    strength_part = strength_digits[:3]

    
    cleaned_form = ""
    formulation = formulation.lower()

    for character in formulation:
        if character.isalpha():
            cleaned_form = cleaned_form + character 
    
    form_part = cleaned_form[:3].upper()

    cleaned_manufacturer = ""
    for character in manufacturer:
        if character.isalpha():
            cleaned_manufacturer = cleaned_manufacturer + character

    manufacturer_part = cleaned_manufacturer[:3].upper()
    
    pack_size_part = str(pack_size)

    
    code = name_part + strength_part + form_part + manufacturer_part + pack_size_part

    return code 
