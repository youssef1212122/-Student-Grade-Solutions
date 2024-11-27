n = int(input("Enter the number of records: "))
print("Enter records in the format: 'Book Title - Days Borrowed'")
records = [input() for _ in range(n)]

book_data = {}
for record in records:
    title, days = record.split(" - ")
    days = int(days)
    if title in book_data:
        book_data[title] += days
    else:
        book_data[title] = days

most_borrowed = max(book_data.items(), key=lambda x: x[1])
least_borrowed = min(book_data.items(), key=lambda x: x[1])

average_days = sum(book_data.values()) / len(book_data)

sorted_books = sorted(book_data.items(), key=lambda x: x[1], reverse=True)

print(f"Most borrowed book: {most_borrowed[0]} ({most_borrowed[1]} days)")
print(f"Least borrowed book: {least_borrowed[0]} ({least_borrowed[1]} days)")
print(f"Average borrowing time: {average_days:.2f} days")
print("Books sorted by borrowing duration:")
for title, days in sorted_books:
    print(f"{title} - {days} days")
