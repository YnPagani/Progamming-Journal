import sqlite3

connection = sqlite3.connect("data.db")


def create_table():
    with connection:
        # Behind the scene SQLite is creating a cursor when we use execute()
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);")


def add_entry(entry_content: str, entry_date: str):
    with connection:
        # This way SQLite will do the string interpolation, so avoiding SQL
        # injection attacks.
        connection.execute("INSERT INTO entries VALUES (?,?);",
                           (entry_content, entry_date))


def get_entries() -> sqlite3.Cursor:
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
