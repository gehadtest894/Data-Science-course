class Book:
    def __init__(self,book_id,title,auther,category):
        self.book_id= book_id
        self.title= title
        self.auther= auther
        self.category= category
        
    
#book1=Book(1,"python","Osama El Zero","programming")   
#book2=Book(2,"Machine learning","Mohamed El Desoky","Ai")  
#print(book1.auther) 
#print(book2.category)
class Bookltem(Book):
    def __init__(self, book_id, title, auther, category,barcode,location,item_id):
        super().__init__(book_id, title, auther, category)
        self.barcode= barcode
        self.location= location
        self.item_id= item_id
        self.is_available= True
        



class Member:
    def __init__(self,member_id,name,barcode):
        self.member_id= member_id
        self.name= name
        self.barcode= barcode
        self.borrowed_books= []
        self.fines= 0
    def borrow_book(self,book_item):
        if len(self.borrowed_books)<5 and book_item.is_available:
         self.borrowed_books.append(book_item)
         book_item.is_available= False
         print(f"{self.name} borrowed\"{book_item.title}\".")  
        else :
         print("connot borrow books or book is unavailable")        
    
    
        
    
class librarian:
    def __init__(self,name):
        self.name= name 
    def add_book(self,book_list,book):
     book_list.append(book)
     print(f"Book'{book.title}'added successfully")
     def remove_book(self,book_list,book_id):
         for book in book_list:
             if book.book_id== book_id:
                 book_list.remove(book)
                 print(f"Book'{book.title}' remove successful")
                 return
             print("Book not found")
             
             
                              
    
     
                               
from datetime import datetime, timedelta
class BookLending:
    def __init__(self,book_item,member):
        self.book_item= book_item
        self.memder= member
        self.issue_date= datetime.now()
        self.due_date= self.issue_date + timedelta(days=10)
        def return_book(self):
         self.book_item .is_available= True
         return_date= datetime.now()
         if return_date> self.due_date:
             self.member.fines +=10
             print(f"late return ! fine added:10$")
             print(f"'{self.book_item.title}' returned successful")
             
             
             
              
            
        