entries = []


def add_entry(entry_content: str, entry_date: str):
    entries.append({"content": entry_content,
                    "date": entry_date})


def get_entries() -> list:
    return entries

