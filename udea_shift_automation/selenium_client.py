from typing import Any, List, TypeVar

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EventType = TypeVar("EventType", bound=Any)
WebElement = TypeVar("WebElement", bound=Any)


class SeleniumClient:
    def __init__(self, *, timeout: int = 10) -> None:
        options = webdriver.ChromeOptions()

        capabilities = webdriver.DesiredCapabilities.CHROME

        self.driver = webdriver.Chrome(
            "storage/chromedriver",
            desired_capabilities=capabilities,
            options=options,
        )
        self.wait_driver = WebDriverWait(self.driver, timeout)
        self.driver.maximize_window()

    def wait(
        self, *, identifier: str, identifier_type: str, event: EventType
    ) -> WebElement:
        """
        This method wait for an HTML element to be loaded into the website and
        returns it

        Parameters
        ----------
        identifier: str
            Html element identifier, e.g: id, class, xpath, css selector, ...
        identifier_type
            Type of the HTML element identifier been used, e.g: By.ID,
            By.XPATH, ...
        event
            event that launches the HTML element when ready

        Returns
        -------
        out
            Expected HTML element
        """
        return self.wait_driver.until(event((identifier_type, identifier)))

    def wait_and_click(
        self, *, identifier: str, identifier_type: str = By.ID
    ) -> WebElement:
        """
        This method is basically a wrapper of the wait method, which in
        addition of waiting for the element to be clickable, clicks on it

        See also
        --------
        wait
        """
        element_web: WebElement = self.wait(
            identifier=identifier,
            identifier_type=identifier_type,
            event=EC.element_to_be_clickable,
        )
        element_web.click()
        return element_web

    def wait_and_fill(
        self, *, keys: List[str], identifier: str, identifier_type: str = By.ID
    ) -> WebElement:
        """
        This method is basically a wrapper of the wait method, which in
        addition of waiting for the element to be present in the HTML page,
        writes text on it

        See also
        --------
        wait
        """
        element_web: WebElement = self.wait(
            identifier=identifier,
            identifier_type=identifier_type,
            event=EC.presence_of_element_located,
        )
        element_web.clear()

        for key in keys:
            element_web.send_keys(key)

        return element_web
