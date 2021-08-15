from collections import Counter

n = int(input())
books = []
for _ in range(n):
    books.append(input())

books.sort()
cnt = Counter(books)

print(cnt.most_common(n=1)[0][0])
