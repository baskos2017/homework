from lxml import etree

tree = etree.parse('data/books.xml')
root = tree.getroot()

cheap_books = tree.xpath("//book[number(price) < 25.00]")

print("Список книг з ціною менше 25.00:")
for book in cheap_books:
    title = book.find("title").text
    author = book.find("author").text
    price = book.find("price").text
    print(f"Назва: {title}, Автор: {author}, Ціна: ${price}")
