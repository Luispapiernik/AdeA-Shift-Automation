import time

from udea_shift_automation.bot import Bot
from udea_shift_automation.config import settings


def main():
    bot = Bot()

    bot.log_in(username=settings.username, password=settings.password)
    time.sleep(1)
    bot.schedule_meeting_room_1()
    time.sleep(1000)


if __name__ == "__main__":
    main()
