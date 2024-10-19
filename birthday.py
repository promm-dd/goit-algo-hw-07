# from datetime import datetime

# class Birthday:
#     def __init__(self, value):
#         try:
#            self.value = datetime.strptime(value, "%d.%m.%Y") #преобразуем value в обьект datetime
#         except ValueError:
#             raise ValueError("Invalid date format. Use DD.MM.YYYY")
#     def __str__(self):
#         return self.value.strftime("%d.%m.%Y")  #преобразуем обьект datetime в строку 
    
    
    
    
    
    
#         #     def get_days_from_today(date):
#         #         try: 
#         #             input_date= datetime.strptime(date.strip(), "%Y-%m-%d").date()
#         #         except ValueError:
#         #             return "invalid date. Use 'YYYY-MM-DD' "
#         #         current_date= datetime.today().date()
#         #         delta= current_date - input_date
#         #         return delta.days

#         #     date_string = "2023-12-05"
#         #     days_difference =get_days_from_today(date_string)
#         #     print(days_difference)

#         #     get_days_from_today("2021-10-09")

#         #     date_string_invalid = "2021.10.09"
#         #     days_invalid = get_days_from_today(date_string_invalid)
#         #     print(days_invalid)
            