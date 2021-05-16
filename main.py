from datetime import datetime

from not_a_date_exception import NotADateException


def convert_string_to_date(date):
    return datetime.strptime(date, "%d-%m-%Y")


def format_YMD_to_DMY(date):
    if not isinstance(date, datetime):
        raise NotADateException

    return date.strftime("%d-%m-%Y")


def main():
    print(convert_string_to_date("16-5-2021"))
    print(format_YMD_to_DMY(datetime(2021, 5, 16)))
    print(format_YMD_to_DMY("18349"))


if __name__ == '__main__':
    main()
