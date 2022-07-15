import json
import csv
from collections import OrderedDict


def func_tools(csv_listk, step):
    for i in range(0, len(csv_listk), step):
        yield csv_listk[i:i + step]


def unpacking(lst):
    for i in lst:
        return i


with open("books.csv", "r") as csv_b:
    book_list = []
    reader = csv.DictReader(csv_b)
    for zero in reader:
        res = {key: zero[key] for key in zero.keys()}
        book_list.append(res)

with open("users.json", "r") as users:
    updated_users = []
    users_table = {"name", "gender", "address", "age", "books"}
    json_string = json.load(users)
    peso = func_tools(book_list, 8)
    for item in json_string:
        unpacked = unpacking(peso)
        item.setdefault("books", unpacked)
        generated_json = OrderedDict((key, item[key]) for key in users_table if key in item)
        updated_users.append(generated_json)
        with open("result.json", "w") as ref:
            json.dump(updated_users, ref, indent=4)
