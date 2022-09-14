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
