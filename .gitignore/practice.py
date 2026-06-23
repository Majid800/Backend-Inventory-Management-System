#practice 
from medicines import Medicine 
from medicines_database import MedicineDatabase 

medicine1 = Medicine(name = "Atorvstatin", strength = "20mg", formulation = "tablets", tablets_per_pack= 28, is_controlled = False, manufacturer = "Teva", code = "ATO20TAB" )
medicine2 = Medicine(name = "Amlodipine", strength = "10mg", formulation = "tablets", tablets_per_pack= 28, is_controlled= False, manufacturer = "Teva", code = "AML10TAB")

#print(medicine1)
#print(medicine2)

#database = MedicineDatabase()

#MedicineDatabase.add_medicine(database,medicine1)
#MedicineDatabase.add_medicine(database,medicine2)

#MedicineDatabase.search_by_code(database,"ATO20TAB")

#print(database.medicines)

            
        