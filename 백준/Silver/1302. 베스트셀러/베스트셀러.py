n = int(input())
books={}
for i in range(n):
    book = input().rstrip()
    if books.get(book):
        books[book]+=1
    else:
        books[book]=1
target = max(books.values())
arr=[]
for book,number  in books.items():
    if number==target:
        arr.append(book)
print(sorted(arr)[0])


