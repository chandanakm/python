class A:
    def __init__(self, category, item, quantity):
        self.catname=category
        self.itemname=item
        self.qua=quantity
        print(self.catname, self.itemname, self.qua)
obj=A('south','dose','2')
