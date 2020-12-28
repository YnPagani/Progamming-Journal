import db

db.create_table()

menu = """
Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

print("Welcome to the Programming Journal!")


def prompt_new_entry():
    # Asking user for data
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    # Adding data to db
    db.add_entry(entry_content, entry_date)


def view_entries(entries: list):
    # Indexes
    CONTENT = 0
    DATE = 1

    # When iterating over a cursor, the cursor will fetch the row that it's
    # pointing to, and then will move to point to the next row.
    # By default when fetching from the cursor, it will return a tuple for each
    # row.
    for entry in entries:
        print(f"{entry[DATE]}\n{entry[CONTENT]}\n\n")


while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        view_entries(db.get_entries())

    else:
        print("Invalid input, try again")
