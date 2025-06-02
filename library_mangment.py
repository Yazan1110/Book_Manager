import json

def load():
   try:
     with open("Books.json", "r") as f:
        global Books
        Books=json.load(f) 
   except (FileNotFoundError, json.JSONDecodeError):
        Books = {} 
def dump():
       with open("Books.json", "w") as f:
           json.dump(Books,f,indent=4)
load() 
      
import os
def Clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear") 

wanted=[]

def Enter():
    input("press enter to reurn to the main menu")    
    
def safe_int(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Please enter a valid number.")
        return None

def safe_float(prompt):
    try:
        return float(input(prompt).strip())
    except ValueError:
        print("Please enter a valid price.")
        return None    
 

def search_book():
    search_book=input("Search . . . . \n")
    if search_book in Books:
        print("------------------------------------")
        print(f"📖Title:{search_book.title()} ")        
        for key,value in Books[search_book].items():
         print(f"{key}: {value}")
        print("------------------------------------")
    else:
        print("Sorry, we dont have this book") 
        wanted.append(search_book)   
        
def Add_book():
        global Books
        B_name=input("Enter the book name please \n").capitalize().strip()
        if B_name in wanted:
            wanted.remove(B_name)
        if B_name in Books:
            Add_num=safe_int("This book already exists.  \nHow many copies do you want to add?\n")
            if Add_num==None:
                return
            Books[B_name]["📦 Copies"]+=Add_num
            Books[B_name]["✅ Available"]+=Add_num
            dump()  
            return 
        B_writer=input("Enter the name of the writer please\n").strip()
        B_copies=safe_int("How many copies are you adding to the library ?\n")
        if B_copies==None:
            return
        B_summary=input("write a summary or type 'Enter' to skip(Uberspringen)\n").strip()
        loan_price=safe_float("Enter the book loan price per day\n")
        if loan_price==None:
            return
        B_borrowed=0
        if B_summary:
            Books[B_name]={
                        
            "✍️  Writer":B_writer,
            "📦 Copies": B_copies,
            "✅ Available":B_copies-B_borrowed ,
            "📄 Summary":B_summary, 
            "💰 Price/day":loan_price,
            "📅 Borrowed for:": 0,
            "📌 Condition":"Available",
         
            }
         
           
             
        else:
             Books[B_name]={
           
            "✍️  Writer":B_writer,
            "📦 Copies": B_copies,
            "✅ Available":B_copies-B_borrowed ,
            "📄 Summary":"No Summary", 
            "💰 Price/day":loan_price,
            "📅 Borrowed for:": 0,
            "📌 Condition":"Available",
          
            }                               
        dump()  
                       
def Take_book():
      global Books
      Take=input("Name the book you Want to borrow").capitalize().strip()
      if Take in Books:
          print (Books[Take]["📌 Condition"] , "There are",Books[Take]["✅ Available"], "available")
          if Books[Take]["✅ Available"]==0 :
              print("last copy of this book is borrowed You can come back in {Days} ")
          
          
          else:
              hmany=safe_int(f"How many {Take} copies do you want to borrow")
              if hmany==None:
                  return
              if (hmany)>Books[Take]["✅ Available"]:
                  print("NO enough copies available !\nWe have only ", Books[Take]["✅ Available"])
                  return
              else:
                  print("you will pay per day",Books[Take]["💰 Price/day"]*int(hmany))
                  Days=(safe_int("How many days do you want to borrow this book"))
                  if Days==None:
                      return      
                  Total_price=Books[Take]["💰 Price/day"]*(hmany)*(Days)
                  print(f"You will pay {Total_price}" )
                  confirm=input("Do  you want to Take it Yes \ No\n").lower().strip()
                  if  confirm.startswith("y") :
                      print("You have  just borrowed ", hmany , Take , "for",Days,"days and paid", Total_price )
                      Books[Take]["✅ Available"]-= int(hmany)
                      Books[Take]["📅 Borrowed for:"]+=int(Days)
                      if Books[Take]["✅ Available"]==0:
                          Books[Take]["📌 Condition"]="Unavailable"           
                  else:
                     print("thanks")   
      else:
          print("""Thank you for your interest.
We will do our best to make the item available as soon as possible
and inform you once it's in stock.
           """)    
          wanted.append(Take)
      dump() 
def return_book():
        global Books
        returned=input("Name the book you want return\n").capitalize().strip()
        h_many=safe_int("How many copies are you returning\n")
        if h_many==None:
            return
        if returned in Books and Books[returned]["✅ Available"]+h_many<=Books[returned]["📦 Copies"] :
            Books[returned]["✅ Available"]+=h_many
            print("Thank you for Returning ",h_many,"of",returned)                      
        else:
            print("It seems like these books was never in this library,\ntry to remember from where did you borrow this book,\nor try another spelling ")
            donate=safe_int("Enter1 if you to donate this book and add it to our library or anything else to Exit\n")
            if donate==None:
                return
            if donate==1 :
                Add_book()                      
            dump() 
                                                                                                                                                                                                                     
def show_list() :
    global Books     
    print("------------------------------------")
    for title , info in Books.items()    :
        print(f"📖Title:{title.title()} ")
        for key , value in info.items():
            print(f"{key}: {value}")
        print("------------------------------------")
   
                     


        
while True:
     
    print("1- Add a book")
    print("2-Borrow a book")
    print("3-Return a book")
    print("4-Take a look at our list")
    print("5-Search by name ")
    print("6-Remove a book")
    print("7-Exit and save\n")
      
    Choice=(input("Choose from 1 to 5 :  \n").strip())
   
    
    
    if Choice.isdigit():                  
        if int(Choice)==1:
            Clear()
            Add_book()                                                                 
        elif int(Choice)==2:
            Clear()
            Take_book()
        elif int(Choice)==3:
            Clear()
            return_book()  
        elif int(Choice)==4:
            Clear()
            show_list()
        
        elif int(Choice)==5:
            search_book()
        
        elif int(Choice)==6:         
            try:
                del Books[input("\nName the book you wants to remove\n ").strip()]
            except:
                print("Wrong input, We may dont have this book")
                
        elif int(Choice)==7:                        
            Clear()            
            dump() 
            break
           
        else:
            print("Invalid Input")    
    else:
        print("Invalid Input")                                                                                 
    Enter()                                                                             
    
    Clear()         

    dump()                                                                                                                                                                                                                   