from datetime import datetime, timedelta

start_date_parts = list(map(int, input().split(".")))
end_date_parts = list(map(int, input().split(".")))

start_date = datetime(start_date_parts[2], start_date_parts[1], start_date_parts[0])
end_date = datetime(end_date_parts[2], end_date_parts[1], end_date_parts[0])

holidays_count = 0
current_date = start_date

while current_date <= end_date:
    if current_date.weekday() >= 5:  # Saturday=5, Sunday=6
        holidays_count += 1
    current_date += timedelta(days=1)

print(holidays_count)
