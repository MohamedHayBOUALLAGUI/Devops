from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (in this case, using Firefox)
driver = webdriver.Firefox()

try:
    # Open the webpage
    driver.get("file:///path/to/your/local/project/index.html")

    # Get the title of the page
    title = driver.title

    # Check if the title matches the expected value
    expected_title = "Haithem Ansible Pipeline"
    assert title == expected_title, f"Expected title: {expected_title}, Actual title: {title}"

finally:
    # Close the browser window
    driver.quit()

