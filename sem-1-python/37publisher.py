class publisher:
    def __init__(self,name1):
        self.name=name1
    def show(self):
        pass
class book(publisher):
    def __init__(self,title1,author1,name1):
        self.title=title1
        self.author=author1
        publisher. __init__(self, name1)
    def show(self):
        pass
class python(book):
    def __init__(self,p,no,title1,author1,name1):
        self.price=p
        self.no_of_pages=no
        book. __init__(self,title1,author1,name1)
    def show(self):
        print("Book title", self.title)
        print("Author",self.author)
        print("publisher",self.name)
        print("price: Rs.", self.price)
        print("No. of pages:", self.no_of_pages)
p1=python(700,300,'Programming with python','G V Rossum','ABC Books')
p1.show()