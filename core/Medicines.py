#First stage is the creation of the Medicine Database. This file acts as the foundation of the entire system

from dataclasses import dataclass, field 
from typing import List, Dict, Optional

#creating medicine class and assigning attributes
@dataclass
class Medicine:
    name: str
    strength: str
    formulation: str 
    tablets_per_pack: int 
    manufacturer: str 
    code: str 
    barcode: str =""
    notes: str = "" 
    is_controlled:bool = False

    #Cleaning the data provided from user 
    def __post_init__(self):
        self.name = self.name.strip()
        self.strength = self.strength.strip()
        self.formulation = self.formulation.strip()
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
            f"Manufacturer: {self.manufacturer or 'N/A'}\n"
            f"Notes: {self.notes or 'N/A'}\n"
        )
        

