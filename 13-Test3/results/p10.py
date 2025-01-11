def f(dates):
    import re
    dates_list = []
    pattern = "^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$" 
    dates_splited = dates.split(",")
    for i in dates_splited:
        if re.match(pattern, i):
            dates_list.append(i)
    return dates_list


    









if __name__ == "__main__":
    dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
    print(f(dates))