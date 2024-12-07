import pytest
from playwright.sync_api import Page, expect

import utility
from pageobjects.landing_page import LandingPage
from utility import timestamp
from utility.timestamp import return_timestamp

"""
This module contains tests for the Landing Page.

The tests validate the functionality and UI elements of the Landing Page 
using the Page Object Model (POM) design pattern.

These tests ensure the page behaves as expected, providing reliable and 
maintainable automation coverage.
"""

@pytest.mark.regression
def test_landing_page(page:Page):
    lp = LandingPage(page)
    lp.navigate_to_landing_page()
    expect(page).to_have_title("Internet Speed Test | Fast.com")
    expect(lp.logo).to_be_visible()
    speed_value = lp.get_speed_value()
    time_stamp = return_timestamp()
    print(f'\n{time_stamp} :: Speed Value :: {speed_value}')



