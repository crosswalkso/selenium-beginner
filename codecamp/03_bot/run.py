import time
from booking.booking import Booking

# search = input()

with Booking(teardown=True) as bot:
    # time.sleep(1)
    bot.change_currency("EUR")
    bot.select_place_to_go("제주도")
    bot.select_dates("2023-03-08", "2023-03-15")
    bot.select_adults(5)
    bot.click_search()
