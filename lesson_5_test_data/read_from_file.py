import json
import csv


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
            for i in range(wanted_parts)]


with open("books.csv", "r") as csv_b:
    book_list = []
    reader = csv.DictReader(csv_b)
    for books in reader:
        new_books_dict = {key: books[key] for key in books.keys()}
        book_list.append(new_books_dict)

with open("users.json", "r") as users:
    updated_users = []
    users_table = ("name", "gender", "address", "age", "books")
    json_string = json.load(users)
    splited_books = split_list(alist=book_list, wanted_parts=28)
    for item, value in zip(json_string, splited_books):
        item["books"] = value
        generated_json = ({key: item[key] for key in users_table})
        updated_users.append(generated_json)
        with open("result.json", "w") as ref:
            json.dump(updated_users, ref, indent=4)
