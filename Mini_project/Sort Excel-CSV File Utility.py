'''Sort Excel/CSV File Utility - Reads a file of records, sorts them, and
 then writes them back to the file.
 Allow the user to choose various sort style and sorting based on a particular field.'''

import csv
from os import path
from re import X
file_path = path.abspath(__file__) # full path of your script
dir_path = path.dirname(file_path) # full path of the directory of your script
csv_file_path = path.join(dir_path,'default.csv') # absolute zip file path


class Sorter:
    def __init__(self, file_path):
        self.filepath=file_path
        self.rows,self.fields=self.load_csv_dict(file_path)



    def load_csv_dict(self,file_path):
        rows=[]
        try:       
            with open(file_path,'r') as csvfile:
                new_file=csv.DictReader(csvfile)
                header=True
                
                for row in new_file:
                    if header:
                        fields = list(row)
                        header=False
                    rows.append(row)
                return rows,fields
        except:
            print('Cannot find file')
            return None,None
        

    def display(self):
       
        for column in self.fields:
            print("%15s"%column,end="\t")
        print('\n')
        for row in self.rows:
            # parsing each column of a row
            for col in row.values():
                print("%15s"%col,end="\t"),
            print('\n')
        print('\n\n')
    def sort_menu(self):
        print('Enter the field number you would like to sort by:\n')
        for i, field in enumerate(self.fields):
            print(f'{i}:{field}')
        print('Your Choice: ')

    def sorter(self,field,type_sort):
        if field>=len(self.fields):
            print("Invalid Field")
            return
        else:
            keyy=self.fields[field]
            if type_sort==1: 
                self.rows.sort(key=lambda x: x[keyy], reverse=False)
            elif type_sort==2:
                self.rows.sort(key=lambda x: x[keyy], reverse=True)
            else:
                print('Invalid choice')

                
        print('\n')
    
    def save_to_file(self):
        with open (self.filepath,'w') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(self.rows)







if __name__=='__main__':
    while(True):
        separator='*'*50
        print(separator,"Welcome".center(50),separator,sep='\n')
        try:
            choice=int(input('1. read default file\n2.custom csv file(saved in same path)\n3. to exit\nenter your choice: '))
        except ValueError:
            choice=4
        if choice==3:
            break
        if choice==1 or choice==2:
            if choice==1:
                csv_file_path = path.join(dir_path,'default.csv')
            elif choice==2:
                file_name=input('enter file name: ')
                csv_file_path = path.join(dir_path,file_name)
            new_sorter=Sorter(csv_file_path)    
            if not new_sorter.rows:
                print("File not Found")
                break
            new_sorter.display()
            new_sorter.sort_menu()
            try:
                field=int(input())
                type_sort=int(input('1 for Ascending order\n2 for Descending\nYour choice:\t'))
            except:
                print("invalid choice\n")
            else:
                new_sorter.sorter(field,type_sort)
                new_sorter.save_to_file()
                print("Sorted successfully")
                new_sorter.display()
        else:
            print('Invalid choice')
                



            

    