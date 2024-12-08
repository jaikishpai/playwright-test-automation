# Playwright Test Automation

This repository is a test automation framework built using [Playwright](https://playwright.dev/python/). It demonstrates robust, scalable, and maintainable testing practices.

## Features

- **Page Object Model (POM):** Implements POM for abstraction and reusability of web elements and actions.
- **Pytest Integration:** Leverages Pytest for test execution, reporting, and scalability.
- **HTML Reports:** Automatically generates detailed HTML reports for each test run.
- **Configurable Logging:** Includes project-level logging for enhanced debugging and traceability.
- **Cross-Browser Support:** Tests can be executed on multiple browsers supported by Playwright.

## Project Structure

```
playwright-test-automation/
├── .github/workflows/          # CI/CD workflows for GitHub Actions
├── pageobjects/                # Page Object classes encapsulating web elements and actions
├── tests/                      # Test cases for the application
├── utility/                    # Utility functions like logging, timestamp generation, etc.
├── Pipfile                     # Dependency management using Pipenv
├── pytest.ini                  # Pytest configuration
└── README.md                   # Project documentation
```

## Prerequisites

- Python 3.10 or later
- [Pipenv](https://pipenv.pypa.io/en/latest/) for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jaikishpai/playwright-test-automation.git
   cd playwright-test-automation
   ```

2. Install dependencies:
   ```bash
   pip install pipenv
   pipenv install --dev
   ```

3. Install Playwright browsers:
   ```bash
   pipenv run playwright install
   ```

## Running Tests

To execute the tests:

1. Activate the Pipenv environment:
   ```bash
   pipenv shell
   ```

2. Run all tests:
   ```bash
   pytest
   ```

3. Generate an HTML report:
   ```bash
   pytest --html=report.html --self-contained-html
   ```

## CI/CD Integration

This project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) to automate testing. The workflow:
- Installs dependencies.
- Runs tests on each push or pull request.
- Uploads the HTML test report as an artifact.

To view the artifact, navigate to the **Actions** tab on GitHub after a workflow run.

## Logging

The framework includes a custom logger for consistent and detailed logging. Logs are written to both the console and optionally to a file for persistent storage.
