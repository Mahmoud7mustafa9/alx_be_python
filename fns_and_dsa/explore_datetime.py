from datetime import datetime
from datetime import timedelta 
from datetime import date



def display_current_datetime():

    current_date = datetime.now()
    time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {time}")

display_current_datetime()

number = int(input('Enter the number of days to add to the current date: '))

def calculate_future_date():
    current_date = date.today()
    future_date = current_date + timedelta(days=number)
    dates = future_date.strftime("%Y-%m-%d")
    print(f'Future date: {dates}')

calculate_future_date()