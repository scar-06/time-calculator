def add_time(start, duration, start_day=''):
    # txt = start

    # x = txt.split()

    # print(x)
    # first, we insert above tuple data into lists,
    time_list = list()
    time_list.append(start)
    time_list.append(duration)
    # print("Current time and duration to be added respectively: ", time_list)

    # next, we split the times into separate variables
    starting_time = time_list[0]
    duration_digits = time_list[1]
    original_time = starting_time.split()
    start_time_digits = original_time[0]
    time_period = original_time[1]
    print("Starting time:", start_time_digits + time_period, "and Duration time:", duration_digits)

    # next, we create algorithms for start time + duration time additions
    starting_minutes = start_time_digits.split(':')[1]
    duration_minutes = duration_digits.split(':')[1]
    starting_hours = start_time_digits.split(':')[0]
    duration_hours = duration_digits.split(':')[0]
    minutes = int(starting_minutes) + int(duration_minutes)
    hours = int(starting_hours) + int(duration_hours)

    # next, we set up the "minutes-into-hours" calculation algorithm
    if minutes > 59:
        minutes -= 60
        hours += 1
    if minutes < 10:
        if minutes == 0:
            minutes = '00'
        else:
            minutes = str(minutes)
            minutes = minutes.rjust(2, "0")
            # print("Type for 'minutes': ", type(minutes))

    # print(f"Total Result time: {hours}:{minutes}")

    # next, we set up the 12-hour clock format algorithm
    twelve_count = 0
    new_hours = int(hours)
    # print("New Hours: ", new_hours)
    while new_hours >= 12:
        if new_hours == 12:
            # new_hours = 12
            # print("New Hours At a Value of 12 Present")
            twelve_count = twelve_count + 1
            break
        elif new_hours > 12:
            new_hours = new_hours - 12
            # print("New Hours Above The Sum of 12: ", new_hours)
        twelve_count = twelve_count + 1

        if new_hours == 0:
            new_hours += 12
        else:
            continue
    # print('Total 12 counts: ', twelve_count)

    # next, we set up our AM/PM calculation algorithm
    new_time_period = time_period
    opposite_time_range = range(1, hours, 2)
    same_time_range = range(2, hours, 2)
    if new_time_period == "AM":
        if twelve_count == 0 or twelve_count in same_time_range:
            new_time_period = "AM"
        elif twelve_count in opposite_time_range:
            new_time_period = "PM"

    elif new_time_period == "PM":
        if twelve_count == 0 or twelve_count in same_time_range:
            new_time_period = "PM"
        elif twelve_count in opposite_time_range:
            new_time_period = "AM"

    # next, we set up the day tracker
    day_tracker = ""
    day_duration = 0
    pm_time_range = range(3, hours, 2)
    am_time_range = range(4, hours, 2)
    if time_period == "AM":
        if twelve_count == 2:
            day_duration = 1
            day_tracker = "next day"
        elif twelve_count in am_time_range:
            day_duration = int(twelve_count / 2)
            day_tracker = f"{day_duration} days later"

    elif time_period == "PM":
        if twelve_count == 1 or twelve_count == 2:
            day_duration = 1
            day_tracker = "next day"
        elif twelve_count in pm_time_range:
            day_duration = int((twelve_count + 1) / 2)
            day_tracker = f"{day_duration} days later"

    new_day = ""
    days_of_week = ["Sunday", 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if start_day.capitalize() in days_of_week:
        if start_day.capitalize() == 'Sunday':
            if day_duration == 0:
                new_day = days_of_week[0]
            elif day_duration in range(1, 7):
                new_day = days_of_week[day_duration]
            else:
                while day_duration > 6:
                    new_day = days_of_week[day_duration - 7]

        elif start_day.capitalize() == 'Monday':
            if day_duration == 0:
                new_day = days_of_week[1]
            elif day_duration in range(1, 6):
                new_day = days_of_week[day_duration + 1]
            elif day_duration == 6:
                new_day = days_of_week[1]
            else:
                while day_duration >= 7:
                    new_day = days_of_week[day_duration - 6]

        elif start_day.capitalize() == 'Tuesday':
            if day_duration == 0:
                new_day = days_of_week[2]
            elif day_duration in range(1, 5):
                new_day = days_of_week[day_duration + 2]
            elif day_duration in range(5, 7):
                new_day = days_of_week[day_duration - 5]

            else:
                # try:
                while day_duration >= 7:
                    # if day_duration == 7:
                    #     new_day = days_of_week[2]
                    if 7 <= day_duration < 12:
                        # while True:
                        #     new_day_duration = day_duration - 5
                        new_day = days_of_week[day_duration - 5]
                        break
                    elif day_duration >= 12 and day_duration < 19:
                        new_day = days_of_week[day_duration - 12]
                        break
                    elif day_duration >= 19:
                        new_day = days_of_week[day_duration - 19]
                        break
                # except:
                # while day_duration >= 7:
                #     if day_duration == 20:
                #         new_day = days_of_week[day_duration - 19]
                #         break


        elif start_day.capitalize() == 'Wednesday':
            if day_duration == 0:
                new_day = days_of_week[3]
            elif day_duration in range(1, 4):
                new_day = days_of_week[day_duration + 3]
            elif day_duration in range(4, 7):
                new_day = days_of_week[day_duration - 4]
            else:
                while day_duration >= 7:
                    new_day = days_of_week[day_duration - 4]

        elif start_day.capitalize() == 'Thursday':
            if day_duration == 0:
                new_day = days_of_week[4]
            elif day_duration in range(1, 3):
                new_day = days_of_week[day_duration + 4]
            elif day_duration in range(3, 7):
                new_day = days_of_week[day_duration - 3]
            else:
                while day_duration >= 7:
                    new_day = days_of_week[day_duration - 3]

        elif start_day.capitalize() == 'Friday':
            if day_duration == 0:
                new_day = days_of_week[5]
            elif day_duration in range(1, 2):
                new_day = days_of_week[day_duration + 5]
            elif day_duration in range(2, 7):
                new_day = days_of_week[day_duration - 2]
            else:
                while day_duration >= 7:
                    new_day = days_of_week[day_duration - 2]


        elif start_day.capitalize() == 'Saturday':
            if day_duration == 0:
                new_day = days_of_week[6]
            elif day_duration in range(1, 8):
                new_day = days_of_week[day_duration - 1]
            else:
                while day_duration >= 8:
                    new_day = days_of_week[day_duration - 8]


    if not day_tracker and not new_day:
        new_time = f"{new_hours}:{minutes} {new_time_period}"
    elif not new_day:
        new_time = f"{new_hours}:{minutes} {new_time_period} ({day_tracker})"
    elif not day_tracker:
        new_time = f"{new_hours}:{minutes} {new_time_period}, {new_day}"
    else:
        new_time = f"{new_hours}:{minutes} {new_time_period}, {new_day} ({day_tracker})"

    return new_time
