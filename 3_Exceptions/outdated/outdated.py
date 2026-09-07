def main():
    date = input("Enter date (month/date/year: )")
    result = date_converter(date)
    print(result)

def date_converter(date):
    acceptable_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    if "/" in date:
        month, day, year = date.split('/')

        day_no = int(day)
        month_no = int(month)
        for x in range(1, 10):
            if day_no == x:
                day_no = f"0{day_no}"
            if month_no == x:
                month_no = f"0{month_no}"

        return f"{year}-{month_no}-{day_no}"
    else:
        month, day, year = date.split(' ')
        proper_day = list(day)
        proper_day.remove(',')
        day_no = int("".join(proper_day))

        month_check = False

        for index, m in enumerate(acceptable_months):
            if month.lower() == m.lower():
                month_no = index + 1
                month_check = True
        if not month_check:
            raise ValueError

        for x in range(1, 10):
            if day_no == x:
                day_no = f"0{day_no}"
            if month_no == x:
                month_no = f"0{month_no}"
                
        return f"{year}-{month_no}-{day_no}"
        
        
main()