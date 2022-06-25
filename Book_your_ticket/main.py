import statistics
from Cinema import *
from user import *
class BookTicket:
    ticket_dict={}
    def __init__(self,rows,columns):
        self.cinema_obj=Cinema(rows,columns)
        self.total_seats=rows*columns
        self.front_rows=rows//2
        if self.total_seats<=60:
            self.total_income=self.total_seats*10
        else:
            front_price=10
            back_price=8
            front_seats=self.front_rows*columns
            self.total_income=front_seats*front_price+(self.total_seats-front_seats)*back_price
    
    def book_ticket(self):
         while(True):
                print('****************Buy a Ticket*******************')
                row=int(input("Enter the row number: "))-1
                column=int(input("Enter the column number: "))-1
                if self.cinema_obj.get_seat(row,column)=='B':
                    print('Seat already booked, please try another')
                    continue
                if self.total_seats>60:
                    if row >self.front_rows:
                        price=8
                    else:
                        price=10
                else:
                    price=10

                ch=int(input(f"You have selected row {row} and column {column}, your price is {price}\n1 to confirm\n2 to cancel\nyour choice:  "))
                if ch==1:
                    ticket_id=str(row)+':'+str(column)
                    print('****************User details*****************')
                    name=input("Enter your name: ")
                    gender=input("Enter 'M' for male 'F' for female: ")
                    age=int(input("Enter Age: "))
                    mobile_no=int(input("Enter mobile No.: "))
                    new_user=User(name,gender,age,mobile_no,price)
                    self.ticket_dict[ticket_id]=new_user
                    self.cinema_obj.set_seat(row,column)
                    print("Booked Successfully")
                    break


    def statistics(self):
        print('*************************Statistics*************************')
        purchases=len(self.ticket_dict)
        percentage_booked=(purchases/self.total_seats)*100
        current_income=0
        for item in self.ticket_dict.values():
            current_income+=item.get_price()
        print(f"Number of purchased tickets: {purchases}\n",
            f"Percentage: {percentage_booked}%\n",
            f"Current income: ${current_income}\nTotal income: ${self.total_income}",sep='5'
            )
        
    def show_booked_ticket(self,row,column):
        print('**********************Booked Tickets*********************')
        if self.cinema_obj.get_seat(row,column)=='S':
            print("Seat not booked yet")
        else:
            ticked_id=str(row)+':'+str(column)
            user_det=self.ticket_dict[ticked_id]
            name=user_det.get_name()
            gender=user_det.get_gender()
            age=user_det.get_age()
            price=user_det.get_price()
            phone_no=user_det.get_ph()
            print(f'Name: {name}\nGender: {gender}\nAge: {age}\nTicket Price: {price}\nPhone No: {phone_no}')

    def execute(self,choice):
        if choice==1:
            print('*******************Cinema*********************')
            self.cinema_obj.show_seats()
            return False
        elif choice==2:
           self.book_ticket()
           return False
        elif choice==3:
            self.statistics()
            return False
        elif choice==4:
            row=int(input("Enter row Number: "))
            column=int(input("Enter Column Number: "))
            self.show_booked_ticket(row,column)
            return False
        elif choice==0:
            return True
        else:
            print('Invalid choice')


rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of seats in each row: "))
book_ticket=BookTicket(rows,columns)
while(True):
    choice=int(input("1.Show the seats\n2. Buy a Ticket\n3. Statistics\n4. Show booked Tickets User Info\n0. Exit:\n"))

    if book_ticket.execute(choice):
        break