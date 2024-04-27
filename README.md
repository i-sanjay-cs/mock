
---

# Automated Product Search on Amazon

This project demonstrates how to automate the process of searching for products on the Amazon website using Behave (a BDD framework for Python), Selenium (a web automation tool), and OpenPyXL (a library for working with Excel files).

## Prerequisites

Before running the tests, ensure you have the following prerequisites installed:

- Python 3.x
- pip (Python package installer)
- Chrome browser (or any other browser supported by Selenium)

## Installation

1. Clone this repository to your local machine:

    ```
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```
    cd automated-product-search
    ```

3. Install the required Python libraries using pip:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Create an Excel file (`products.xlsx`) with a column named "Products" containing the list of products you want to search for on the Amazon website.

2. Update the `search_products.feature` file to define the scenarios for searching products on Amazon.

3. Implement the step definitions in the `steps` directory to perform the necessary actions, such as opening the Amazon homepage, searching for products, and verifying the search results.

4. Run the Behave tests by executing the following command in the terminal:

    ```
    behave
    ```

## Example Feature File

```gherkin
Feature: Search functionality
  As a user
  I want to be able to search for products
  So that I can find the products I need

  Scenario: Search for products on Amazon
    Given I am on the Home page of Amazon
    When I search for different products from the search bar
    Then I should see search results for each product
```

## Example Step Definitions

```python
# Given step definition
@given(u'I am on the Home page of Amazon')
def open_browser_and_search(context):
    ...

# When step definition
@when(u'I search for different products from the search bar')
def search_for_products(context):
    ...

# Then step definition
@then(u'I should see search results for each product')
def verify_search_results(context):
    ...
```
