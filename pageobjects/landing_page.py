from utility.logger import logger

from playwright.sync_api import Page

import config.projectconstant as pc
"""
This project uses the Page Object Model (POM).

This class represents a page and includes all the elements and their actions 
to provide an abstraction layer.

It ensures a clean, reusable, and maintainable structure for automation.
"""

class LandingPage:

    def __init__(self, page: Page):
        self.page = page
        self.landing_page = pc.LANDING_PAGE
        self.logo = page.get_by_label("FAST.com logo")
        self.show_more_link = page.get_by_role(role="link",name="Show more info")
        self.speed_value = page.locator("#speed-value")
        self.speed_units = page.locator("#speed-units")
        self.latency_container = page.locator("#latency-container")
        self.upload_complete_class = page.locator("span#upload-value.extra-measurement-value-container.succeeded")
        self.upload_field = page.locator("#upload-label")
        self.upload_speed_value = page.locator("#upload-value")
        self.upload_speed_units = page.locator("#upload-units")
        self.settings_button = page.locator("#settings-link")



    def navigate_to_landing_page(self):
        logger.info("Navigating to landing page")
        self.page.goto(self.landing_page)

    def click_show_more_info_link(self):
        logger.info("Clicking show more info link")
        self.show_more_link.click()

    def wait_for_speedtest_completion(self):
        logger.info("Waiting for speed test completion")
        self.show_more_link.wait_for(state="visible", timeout=60000)

    def get_speed(self):
        logger.info("Getting speed value")
        self.wait_for_speedtest_completion()
        return self.speed_value.text_content(), self.speed_units.text_content()

    def get_upload_speed(self):
        logger.info("Getting upload speed value")
        self.upload_complete_class.wait_for(state="visible", timeout=60000)
        return self.upload_speed_value.text_content(), self.upload_speed_units.text_content()

    def click_settings_button(self):
        logger.info("Clicking settings button")
        self.settings_button.click()



