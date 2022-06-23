class User:
    def __init__(self,name, gender, age, mobile_no,price):
        self.name=name
        self.gender=gender
        self.age=age
        self.mobile_no=mobile_no
        self.price=price
    
    def get_name(self):
        return self.name
    

    def get_gender(self):
        return self.gender
    

    def get_age(self):
        return self.age
    

    def get_ph(self):
        return self.mobile_no
    

    def get_price(self):
        return self.price
    