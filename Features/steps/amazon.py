import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import openpyxl

# Function to read data from Excel file
def read_products_from_excel(excel_file):
    try:
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active
        products_column = sheet['Products']
        products = [cell.value for cell in products_column if cell.value]
        return products
    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")
        return []


# Load product data from Excel
products = read_products_from_excel('C:/Users/sanja/OneDrive/Documents/Worldline Assessment/WDGET2024048/products.xlsx')

# Define step definitions
@given(u'I am on the Home page of Amazon')
def open_browser_and_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.amazon.in/")
    context.driver.maximize_window()

@when(u'I search for different products from the search bar')
def search_for_products(context):
    for product in products:
        search_product(context, product)

def search_product(context, product):
    # Click on the search bar
    search_bar = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#twotabsearchtextbox")))
    search_bar.click()

    # Input the product into the search bar
    search_bar.send_keys(product)

    # Press Enter key to submit the search
    search_bar.send_keys(Keys.ENTER)

    # Wait for search results to load
    time.sleep(5)

@then(u'I should see search results for each product')
def verify_search_results(context):
    # Verify search results for each product
    for product in products:
        assert product in context.driver.page_source, f"Search result for {product} not found"
