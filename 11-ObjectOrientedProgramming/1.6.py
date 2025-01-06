class Phone():
       def __init__(self, brand, model, storage):
         self.brand = brand
         self.model = model
         self.storage = storage
         self.is_on = False 
         self.is_app_opened = False
         self.app_opened = " "
         self.free_storage = 89
        
       def on(self):
            self.is_on = True

       def off(self):
            self.is_on = False

       def open_app(self, app):
            self.is_app_opened = True
            self.app_opened = app
            return app

       def close_app(self):
            self.is_app_opened = False
           
       def show_free_sorage(self):
         return f'The free storage is: {self.free_storage} GB'

       def download_new_app(self, app_size, app_name):
         self.free_storage -= app_size
         print(f'Just downloaded new app: {app_name}')

       def display_info(self):
         print(f'Brand model: {self.brand}')
         print(f'Phone model: {self.model}')
         print(f'Stock storage:{self.storage} GB')
         print(self.show_free_sorage())
         if self.is_on == True: 
            print('Phone is on and displaying:')
            if self.is_app_opened == True:
                 print("app:", self.app_opened)
            else: 
                 print('main screen')
         else: 
               print('Phone is off')


def main(): 
    my_phone = Phone("Apple", "iPhone12", 128)

    my_phone.on()
    my_phone.open_app("Discord")
    my_phone.download_new_app(10, "Instagram")
    my_phone.download_new_app(1, "Bring")
    my_phone.display_info()

                   

if __name__ =="__main__":
    main()
           


        