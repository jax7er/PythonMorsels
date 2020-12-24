import re


def entries_by_date(diary_file):
    text = diary_file.read()

    text = text.replace("&nbsp;", " ")
    text = text.replace("&quot;", "\"")
    text = text.replace("&amp;", "&")

    elements = re.split(r"(\d{4}-\d{2}-\d{2})\s*?\n{2}", text)
    
    return [
        (date, entry.strip()) 
        for date, entry in zip(elements[1::2], elements[2::2])
    ]


def main(diary_file_name):
    with open(diary_file_name) as diary_file:
        for date, entry in entries_by_date(diary_file):
            with open(date + ".txt", "w") as entry_file:
                entry_file.write(entry)

            print(date, "written")


if __name__ == "__main__":
    from sys import argv

    main(argv[1])
