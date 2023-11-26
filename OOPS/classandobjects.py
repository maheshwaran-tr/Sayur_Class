'''
class Laptop -> brand , model , processer , colour ,  ram ,keyboard  backlight , windows version  

laptop 1 - > Asus , m515 , AMD Ryzen 7 , silver , 16gb , false , windows 11

laptop 2 - > hp , 15s , intel i5 , black , black , 8gb ,  true , windows 10 pro

'''

class Laptop:
    brand = ''
    model = ''
    processor = ''
    ram = ''
    colour = ''
    keyboard_BackLight = True
    windows_version = ''

def print_details(laptop):
    print("Brand : " +laptop.brand)
    print("Model : "+ laptop.model)
    print("Processor : " + laptop.processor)
    print("Colour : " + laptop.colour)
    print("RAM  : " + laptop.ram)
    print("with" if laptop.keyboard_BackLight else "with no" , "keyboard backlight")
    print("windows version : "+ laptop.windows_version)


asus = Laptop()
asus.brand = "Asus"
asus.model = "M515"
asus.processor = "Ryzen 7"
asus.colour = "Silver"
asus.ram = "16gb"
asus.keyboard_BackLight = False
asus.windows_version = "Windows 11"

hp = Laptop()
hp.brand = "HP"
hp.model = "15S"
hp.processor = "Intel i5"
hp.colour = "Black"
hp.ram = "8gb"
hp.keyboard_BackLight = True
hp.windows_version = "Windows 10 pro"

print_details(asus)
print("-" * 20)
print_details(hp)