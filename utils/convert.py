def currency(amount: float) -> str:
    """takes a value, and makes a string makes the value more readable
       e.g. 6000000 -> 6,000,000

    Args:
        amount (float): the value that needs to be converted into a string

    Returns:
        str: readable format of the value.
    """

    return "£{:,}".format(float("{:.2f}".format(float(amount))))

def stats(stat: int) -> str:
    """converts a value from 0 - 100 into a loading bar.
       e.g. 70 -> ■■■■■■■□□□

    Args:
        stat (int): a value between 0 - 100 exclusive.

    Returns:
        str: stringified stat value using filled in and unfilled boxes.
    """

    stat = stat // 10
    return ((stat * '■') + ((10 - stat) * '□'))

def roman(num: int) -> str:
    """converts an integer value into roman numerals.

    Args:
        num (int): a integer value

    Returns:
        str: stringified roman numeral value of the integer given.
    """

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV","I"]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def deltatime(time: int) -> str:
    """conversts the number of seconds into days, hours, minutes, and seconds.

    Args:
        time (int): the amount of time to be converted.

    Returns:
        str: the string version
    """
    time_days = time // 86400
    string = ""
    if time_days > 0:
        if time_days > 1:
            string += str(time_days) + " days, "
        else:
            string += str(time_days) + " day, "

    time_hours = (time // 3600) - (time_days * 24)
    if time_hours > 0:
        if time_hours > 1:
            string += str(time_hours) + " hours, "
        else:
            string += str(time_hours) + " hour, "

    time_minutes = (time // 60) - (time_hours * 60) - (time_days * 1440)
    if time_minutes > 0:
        if time_minutes > 1:
            string += str(time_minutes) + " minutes remaining."
        else:
            string += str(time_minutes) + " minute remaining."
    else:
        string = string[:-2] + " remaining."
    return string

def tuple_to_list(data):
    """
    Function converts a 2D tuple into a 2D list.

    Args:
        data ((Tuple)): 2D tuple.

    Returns:
        list: contains the 2D tuple in list form.
    """
    return [list(record) for record in data]
