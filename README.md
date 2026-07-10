# Python CI/CD Login Test Project

This project demonstrates a simple CI/CD pipeline using GitHub Actions.

## Project Content

- A simple Python email validation function
- Exactly one unit test using pytest
- Exactly one Selenium UI test using a headless browser
- A GitHub Actions workflow that runs automatically on every push

## Tests

The unit test checks the email validation function.

The Selenium UI test opens a demo login page, fills in the username and password fields, submits the login form, and verifies that the secure area page loads correctly.

## CI/CD Pipeline

The workflow file is located at:

.github/workflows/ci-cd.yml

The pipeline runs on Ubuntu and performs the following steps:

1. Sets up Python
2. Installs dependencies
3. Runs the unit test
4. Runs the Selenium UI test
5. Prints the deployment confirmation message after both tests complete