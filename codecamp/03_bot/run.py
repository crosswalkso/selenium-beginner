import time
from booking.booking import Booking
from booking.back_ex import back_ex

# search = input()

try:
    with Booking(teardown=True) as bot:
        # time.sleep(1)
        bot.change_currency("JPY")
        bot.select_place_to_go("제주도")
        bot.select_dates("2023-03-08", "2023-03-15")
        bot.select_adults(5)
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()  # A workaround to let our bot to grab the data properly

        queries = bot.report_results()
        back_ex(queries)

except Exception as e:
    if "in PATH" in str(e):
        print(
            "You are trying to run the bot from command line \n"
            "Please add to PATH your Selenium Drivers \n"
            "Windows: \n"
            "    set PATH=%PATH%;C:path-to-your-folder \n \n"
            "Linux: \n"
            "    PATH=$PATH:/path/toyour/folder/ \n"
        )
    else:
        raise
