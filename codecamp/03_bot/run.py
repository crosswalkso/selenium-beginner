import time
from booking.booking import Booking

search = input()

with Booking(teardown=True) as bot:
    # time.sleep(1)
    bot.change_currency(search)
