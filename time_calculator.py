def add_time(start, duration, starting_day=""):
    # Split the 'start' input into hours and minutes and store the AM/PM part
    pieces = start.split()
    time = pieces[0].split(":")
    end = pieces[1]

    # Calculate the 24-hour clock format if the time is PM
    if end == "PM":
        hour = int(time[0]) + 12
        time[0] = str(hour)
    
    # Split the 'duration' input into hours and minutes
    dur_time = duration.split(":")
    
    # Add hours and minutes to the initial time
    new_hour = int(time[0]) + int(dur_time[0])
    new_minutes = int(time[1]) + int(dur_time[1])

    # Handle the case where minutes exceed 60
    if new_minutes >= 60:
        hours_add = new_minutes // 60
        new_minutes -= hours_add * 60
        new_hour += hours_add

    # Handle the case where hours exceed 24
    days_add = 0
    if new_hour > 24:
        days_add = new_hour // 24
        new_hour -= days_add * 24
    
    # Determine whether the result should be AM or PM
    # Convert to 12-hour clock format
    if new_hour > 0 and new_hour < 12:
        end = "AM"
    elif new_hour == 12:
        end = "PM"
    elif new_hour > 12:
        end = "PM"
        new_hour -= 12
    else:  # new_hour == 0
        end = "AM"
        new_hour += 12

    # Determine if there are additional days added and format accordingly
    if days_add > 0:
        if days_add == 1:
            days_later = " (next day)"
        else:
            days_later = " (" + str(days_add) + " days later)"
    else:
        days_later = ""

    # Define the days of the week
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    # Handle the starting_day parameter to calculate the day of the week
    if starting_day:
        # Calculate how many weeks have passed and adjust days_add
        weeks = days_add // 7
        i = week_days.index(starting_day.lower().capitalize()) + (days_add - 7 * weeks)
        
        # Ensure the day index stays within the range (0-6)
        if i > 6:
            i -= 7
        day = ", " + week_days[i]
    else:
        day = ""
    
    # Format the new time with hours, minutes, AM/PM, day of the week, and days later
    new_time = str(new_hour) + ":" + \
        (str(new_minutes) if new_minutes > 9 else ("0" + str(new_minutes))) + \
        " " + end + day + days_later
    
    return new_time
