#storing medicine records within database and provide add/search/delete/list functionality. Uses medicine code as the unique key 
from typing import Dict, List, Optional 
from medicines import Medicine 
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
    def delete_medidicine(self,code):
        code = code.strip().upper()
        if code in self.medicines:
            del self.medicines[code]
            return True
        return False 
    
    def list_all_medicines(self):
        return list(self.medicines.values())
    
    def is_empty(self):
        return len(self.medicines) ==0