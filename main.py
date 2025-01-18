import xml.etree.ElementTree as xm

tree = xm.parse("document.xml")#Парсе для считывания xml файла
rt = tree.getroot() #Извлекаем корневой элемент XML (person)

# Считывание данных из XML
first_name = rt.find("firstName").text
last_name = rt.find("lastName").text
street_address = rt.find("address/streetAddress").text
city = rt.find("address/city").text
postal_code = rt.find("address/postalCode").text
phone_numbers = []
for phone in rt.findall("phoneNumbers/phoneNumber"): #Возвращает список всех элементов <phoneNumber>, которые находятся внутри <phoneNumbers>
    phone_numbers.append(phone.text)
# Вывод информации
print(f"Имя: {first_name}")
print(f"Фамилия: {last_name}")
print(f"Адрес: {street_address}")
print(f"Город: {city}")
print(f"Почтовый индекс: {postal_code}")
print("Телефоны:")
for phone in phone_numbers:
    print(" ", phone)
