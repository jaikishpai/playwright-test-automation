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
        self.show_more_link = page.get_by_role(role="link",name="Show more info")
        self.speed_value = page.locator("#speed-value")
        self.logo = page.get_by_label("FAST.com logo")

    def navigate_to_landing_page(self):
        self.page.goto(self.landing_page)

    def click_show_more_info_link(self):
        self.show_more_link.click()

    def get_speed_value(self):
        self.show_more_link.wait_for(state="visible")
        return self.speed_value.text_content()

