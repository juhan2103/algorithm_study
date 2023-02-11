n = int(input())
books = {}
for i in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
max_freq = max(books.values())
best_celler = []
for book, number in books.items():
    if number == max_freq:
        best_celler.append(book)
print(sorted(best_celler)[0])
