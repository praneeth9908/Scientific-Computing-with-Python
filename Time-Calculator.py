def add_time(start, duration, day=None):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    period = period.upper()
    
    # Convert start to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    if period == 'AM' and start_hour == 12:
        start_hour = 0

    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(':'))
    
    # Add times
    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    final_period = 'AM' if final_hour_24 < 12 else 'PM'
    final_hour = final_hour_24 % 12
    if final_hour == 0:
        final_hour = 12

    # Calculate new day
    if day:
        day_index = days.index(day.capitalize())
        new_day = days[(day_index + days_later) % 7]
        day_str = f", {new_day}"
    else:
        day_str = ''

    # Calculate suffix for days later
    if days_later == 0:
        later_str = ''
    elif days_later == 1:
        later_str = ' (next day)'
    else:
        later_str = f' ({days_later} days later)'

    return f"{final_hour}:{str(final_minute).zfill(2)} {final_period}{day_str}{later_str}"
