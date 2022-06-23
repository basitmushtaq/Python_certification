class Cinema:
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        self.seats=[['S' for i in range(self.columns)] for j in range(self.rows)]



    def show_seats(self):
        for i,row in enumerate(self.seats):
            if i==0:
                print(' ',end=' ')
                for j in range(len(self.seats[i])):
                    print(j+1,end=' ')
                print('')
            
            print(i+1, end=' ')
            for element in (row):
                print(element,end=' ')
            print('')
    def set_seat(self,row,column):
        self.seats[row][column]='B'
    

    def get_seat(self,row,column):
        return self.seats[row][column]
