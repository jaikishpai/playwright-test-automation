import datetime

"""
Utility Module

Provides generic, reusable helper functions for common tasks such as date and 
time operations, string manipulations, and random data generation. 

"""

def return_timestamp(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    return datetime.datetime.now().strftime(format)
