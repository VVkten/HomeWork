def validate_month(month):
    try:
        month = int(month)
        if month >= 1 and month <= 12:
            return True
        else:
            return False
    except ValueError:
        return False

def validate_year(year):
    try:
        year = int(year)
        if year >= 1900 and year <= 2019:
            return True
        else:
            return False
    except ValueError:
        return False

def create_test_file(name, year, month):
    with open("testFile.txt", "w") as f:
        f.write(f"Прізвище: {name}\n")
        f.write(f"Рік народження: {year}\n")
        f.write(f"Місяць народження: {month}\n")


def get_user_input():

    name = input("Введіть ваше ім'я: ")

    while True:
        year = input("Введіть рік народження: ")
        month = input("Введіть місяць народження: ")

        if validate_month(month) == True and validate_year(year) == True:
            return name, month, year
            break
        else:
            print("Некоректний місяць чи рік!\n"
                  "Будь ласка, введіть реальні дані")


def main():
    name, year, month = get_user_input()
    create_test_file(name, year, month)
    print('Програма завершенна')


if __name__ == '__main__':
    main()