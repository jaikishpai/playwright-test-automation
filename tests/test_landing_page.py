from utility.logger import get_logger
import pytest

from playwright.sync_api import Page, expect

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
logger = get_logger(__name__)

@pytest.mark.regression
def test_landing_page(page:Page):
    logger.info("Starting Landing Page Test")
    lp = LandingPage(page)
    lp.navigate_to_landing_page()
    logger.info("Verifying Title and Logo")
    expect(page).to_have_title("Internet Speed Test | Fast.com")
    expect(lp.logo).to_be_visible()
    speed_value, speed_units = lp.get_speed()
    time_stamp = return_timestamp()
    logger.info(f'\n{time_stamp} :: Internet Speed :: {speed_value} {speed_units}')


def test_show_more_info(page:Page):
    logger.info("Starting Show More Info Test")
    lp = LandingPage(page)
    lp.navigate_to_landing_page()
    lp.wait_for_speedtest_completion()
    lp.click_show_more_info_link()
    logger.info("Verifying Latency Field and Upload Speed")
    expect(lp.latency_container).to_be_visible()
    expect(lp.upload_field).to_be_visible()
    upload_value, upload_units = lp.get_upload_speed()
    time_stamp = return_timestamp()
    logger.info(f'\n{time_stamp} :: Upload Speed :: {upload_value} {upload_units}')



