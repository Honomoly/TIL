def show_items(item):
    item.show_item()

prd = Product('노트북', 1000000)
book = Book('파이썬', 20000)

show_items(prd)
show_items(book)