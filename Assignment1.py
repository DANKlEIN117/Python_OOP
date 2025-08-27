
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on.")

    def power_off(self):
        print(f"{self.brand} {self.model} is shutting down.")



class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model) 
        self.os = os
        self.storage = storage

    def take_photo(self):
        print(f"{self.brand} {self.model} took a photo!")

    def show_specs(self):
        print(f"""
        Brand: {self.brand}
        Model: {self.model}
        OS: {self.os}
        Storage: {self.storage}GB
        """)
        


phone1 = Smartphone("Samsung", "Galaxy S22", "Android", 256)
phone2 = Smartphone("Apple", "iPhone 14", "iOS", 128)

phone1.power_on()
phone1.show_specs()
phone1.take_photo()
phone1.power_off()
print("""

""")
phone2.power_on()
phone2.show_specs()
phone2.take_photo()
phone2.power_off()
