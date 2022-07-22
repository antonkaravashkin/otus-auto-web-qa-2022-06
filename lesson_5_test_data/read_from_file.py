import json
import csv


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
            for i in range(wanted_parts)]


def merging_users_books():
    result_json = []
    refactored_books = []
    with open("books.csv", "r") as csv_b, open("users.json", "r") as users:
        books_list = list(csv.DictReader(csv_b))
        for i in range(len(books_list)):
            books = {"title": books_list[i]["Title"],
                     "author": books_list[i]["Author"],
                     "pages": int(books_list[i]["Pages"]),
                     "genre": books_list[i]["Genre"]
                     }
            refactored_books.append(books)
        users_json = json.load(users)
        splitted_books = split_list(alist=refactored_books, wanted_parts=len(users_json))
    for item, value in zip(users_json, splitted_books):
        item["books"] = value
        generated_user = {key: item[key] for key in ("name", "gender", "address", "age", "books")}
        result_json.append(generated_user)
    with open("result.json", "w") as result:
        json.dump(result_json, result, indent=4)
