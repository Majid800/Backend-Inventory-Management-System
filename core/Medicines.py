#First stage is the creation of the Medicine Database. This file acts as the foundation of the entire system

from dataclasses import dataclass, field 
from typing import list, Dict, Optional

#creating medicine class and assigning attributes
@dataclass
class Medicine:
    name: str
    strength: str
    formuation: str 
    tablets_per_pack: int 
    manufacturer: str 
    is_controlled:bool = False
    code: str 
    barcode: str =""
    notes: str = "" 

    #Cleaning the data provided from user 
    def __post_init__(self):
        self.name = self.name.strip()
        self.strength = self.strength.strip()
        self.formulation = self.formulation.strip()
        self.tablets_per_pack = self.tablets_per_pack.strip()
        self.code = self.code.strip().upper()
        self.barcode = self.barcode.strip()
        self.manufacturer.strip()

        #Raising Input Errors
        if self.tablets_per_pack <0:
            raise ValueError("tablets per pack cannot be negative")
        if not isinstance(self.is_controlled, bool):
            raise TypeError("Is the drug a controlled drug?")
    
    #String representation of instance created within medicine class
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Strength: {self.strength}\n"
            f"Formulation: {self.formulation}\n"
            f"Tablets per pack: {self.tablets_per_pack}\n"
            f"Code: {self.code}\n"
            f"Barcode: {self.barcode or 'N/A'}\n"
            f"Manufacturer: {self.manufacturer or 'N\A'}\n"
            f"Notes: {self.notes or 'N/A'}\n"
        )
        
#storing medicine records within database and provide add/search/delete/list functionality. Uses medicine code as the unique key 
class MedicineDatabase:
    def __init__(self):
        self.medicines: Dict[str, Medicine] = {}

    #Add medicine function. Preventing duplication of medication within database
    def add_medicine(self, medicine:Medicine):
        if medicine.code in self.medicines:
            raise ValueError (f"Medicine code '{medicine.code} already exists.")
        self.medicines[medicine.code] = medicine

    #Searching for medicine
    def search_by_code(self, code):
        code = code.strip().upper()
        return self.medicines.get(code)
    
    #Deleting medicine
    def delete_medidicine(self,code)
        code = code.strip().upper()
        if code in self.medicines:
            del self.medicines[code]
            return True
        return False 
    
    def list_all_medicines(self):
        return list(self.medicines.values())
    
    def is_empty(self):
        return len(self.medicines) ==0