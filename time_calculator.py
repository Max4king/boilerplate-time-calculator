def add_time(start, duration,day_of_week=None):
    num_days = ""
    init_time = convert_12_to_60(start)
    added_time = convert_12_to_60(duration)
    total_time = init_time + added_time
    if added_time >= 1440:
        if day_of_week:
            num_days = calculate_day(total_time,day_of_week)
            return convert_60_to_12(total_time) + num_days
        else:
            num_days = calculate_day(total_time)
    elif day_of_week:
        day_of_week = day_of_week[0].upper() + day_of_week[1:].lower()    
    num_days = calculate_day(total_time)
    return convert_60_to_12(total_time) + num_days

def calculate_day(total_time,days=None):
    days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    day_amt = 0
    day_str = ""
    while total_time >= 1440:
        day_amt += 1
        total_time -= 1440
    if days:
        days = days[0].upper() + days[1:]
        index_of_days = days_of_week.index(days)
        for i in range(day_amt):
            index_of_days = index_of_days%7 + 1
        day_str += f", {days_of_week[index_of_days]}"
    elif day_amt == 1:
        day_str += " (next day)" 
    elif day_amt > 1:
        day_str += f" ({day_amt} days later)"
    return day_str

def convert_60_to_12(time):
    return convert_24_to_12(convert_60_to_24(time))

def convert_12_to_60(time):
    return convert_24_to_60(convert_12_to_24(time))

def convert_12_to_24(time):
    new_time = time.split(":")
    hour = int(new_time[0])
    minor_time = new_time[1].split()
    minutes = int(minor_time[0])
    if len(minor_time) > 1:
        day_format = minor_time[1]
        if day_format == "PM":
            day_format_in_hour = 12
            hour = hour + day_format_in_hour
        elif day_format == "AM" and hour == 12:
            hour = 0
    #print(hour,"Hr", minutes,"mins", day_format, "12-hour-format")
    hour_24_format = [hour,minutes]
    return hour_24_format

def convert_24_to_60(time):
    hour, minutes = time
    minutes += hour*60
    return minutes

def convert_60_to_24(minutes):
    hour = 0
    while minutes > 60:
        minutes -= 60
        hour += 1
    return hour, minutes

def convert_24_to_12(time):
    hour, minutes = time
    AM_PM = "AM"
    if hour == 0:
        hour = 12
    else:
        while hour-12 >= 0:
            hour -= 12
            AM_PM = "PM"
    if minutes < 9:
        minutes = "0" + str(minutes)
    convertted_time = str(hour)+":"+minutes+" "+AM_PM 
    return convertted_time


print(add_time("11:06 PM", "2:02"))