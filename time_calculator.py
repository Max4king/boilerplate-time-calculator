def add_time(start, duration,day_of_week=None):
    num_days = ""
    start = convert_12_to_60(start)
    duration = convert_12_to_60(duration)
    total_time = start + duration

    if duration >= 1440:
        if day_of_week:
            days = calculate_day(total_time,day_of_week)
            return convert_60_to_12(total_time) + num_days + days
        else:
            num_days = calculate_day(total_time)
            

    return convert_60_to_12(total_time) + num_days

def calculate_day(total_time,days_of_week=None):
    days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return

def convert_60_to_12(time):
    return convert_24_to_12(convert_60_to_24(time))

def convert_12_to_60(time):
    return convert_24_to_60(convert_12_to_24(time))

def convert_12_to_24(time):
    new_time = time.split(":")
    hour = int(new_time[0])
    minor_time = new_time[1].split()
    minutes = int(minor_time[0])
    day_format = minor_time[1]
    if day_format == "PM":
        day_format_in_hour = 12
        hour = hour + day_format_in_hour
    elif day_format == "AM" and hour == 12:
        hour = 0
    print(hour,"Hr", minutes,"mins", day_format, "12-hour-format")
    hour_24_format = [hour,minutes]
    return hour_24_format

def convert_24_to_60(time):
    hour, minutes = time
    minutes += hour*60
    return minutes

def convert_60_to_24(time):
    return

def convert_24_to_12(time):
    return


print(add_time("11:06 PM", "2:02"))