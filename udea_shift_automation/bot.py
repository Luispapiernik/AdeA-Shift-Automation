import datetime
import re

from selenium.webdriver.common.keys import Keys

from udea_shift_automation.selenium_client import SeleniumClient


class Bot:
    def __init__(self):
        self.client = SeleniumClient()

    def is_logged_in(self) -> False:
        return False

    def log_in(self, *, username: str, password: str) -> bool:
        self.client.driver.get("https://biblioteca.udea.edu.co/turnosudea/#/")
        self.client.wait_and_fill(keys=[username], identifier="usuario")
        self.client.wait_and_fill(keys=[password, Keys.RETURN], identifier="clave")

        return self.is_logged_in()

    def schedule_meeting_room(self, url: str):
        self.client.driver.get(url)

        # select day
        today = datetime.datetime.today()
        shift_day = datetime.date(year=today.year, month=today.month, day=1)
        shift_day = (shift_day.weekday() + 1) % 7

        day_preceding_number = re.match(
            r"id=datepicker-(?P<number>\d+-\d+)-", "id=datepicker-38-584-"
        ).group("number")
        day_identifier = (
            f"datepicker-{day_preceding_number}-{today.day + shift_day - 1}"
        )
        print(day_identifier)

        self.client.wait_and_click(identifier=day_identifier)

        # select hour

    def schedule_meeting_room_1(self):
        self.schedule_meeting_room(
            url="https://biblioteca.udea.edu.co/turnosudea/#/sala/34/equipo/Sala%201"
        )

    def schedule_meeting_room_2(self):
        self.schedule_meeting_room(
            url="https://biblioteca.udea.edu.co/turnosudea/#/sala/34/equipo/Sala%202"
        )

    def schedule_meeting_room_3(self):
        self.schedule_meeting_room(
            url="https://biblioteca.udea.edu.co/turnosudea/#/sala/34/equipo/Sala%203"
        )
