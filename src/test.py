mydictionary = {
    "one": {"First":"Kenny", "Last":"Twigg"},
    "Two": {"Age":28, "Postcode":"M12"}
}

for value in mydictionary:
    # print(mydictionary[value])
    for val in mydictionary[value]:
        print(val, ":", mydictionary[value][val])