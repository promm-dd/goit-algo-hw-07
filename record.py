# from .birthday import Birthday
# class Record:
#     def __init__(self, name):
#         self.name = Name(name) #здесь создаем обьект класса Name котор хранит имя контакта/ мы используем класс Name чтобы унаследов его свойства 
#         self.phones = []  #атрибут обьекта (список)
#         self.birthday = None
#     def add_birthday(self, date):
#         self.date.append(Phone( ))
        
#     def add_phone(self, phone): 
#         self.phones.append(Phone(phone))  #(Phone(phone)) это создание нового обьекта класса Phone, который содержит номер телефона
#     def remove_phone(self, phone): 
#         self.phones =[p for p in self.phones if p.value != phone]  #p.value атрибут обьекта Phone
#     def edit_phone(self, old_phone, new_phone):
#         if not self.find_phone(old_phone): #существует ли старый номер в списке телефонов 
#             raise ValueError(f"old phone {old_phone} not found")
#         self.remove_phone(old_phone)
#         self.add_phone(new_phone)
#     def find_phone(self, phone):
#         for p in self.phones : #Проходим по каждому объекту телефона в списке
#             if p.value == phone:     # Если номер телефона совпадает с переданным возвращаем объект

#                 return p
#         return None
#      # Возвращаем строковое представление контакта
#     def __str__(self) -> str:
#         return f" Contact name: {self.name.value}, phones: {'____________ '.join(p.value for p in self.phones)}  "