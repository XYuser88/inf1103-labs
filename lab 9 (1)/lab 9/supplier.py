#Supplier class
class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def display_information(self) -> None:
        print("Supplier ID:", self.supplier_id)
        print("Supplier Name:", self.name)
        print("Contact Email:", self.contact_email)