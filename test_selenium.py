from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration for headless mode

# Set up the WebDriver (in this case, using Chrome in headless mode)
driver = webdriver.Chrome(executable_path='/var/lib/jenkins/chromedriver', options=chrome_options)

try:
    # Open the webpage
    driver.get("http://35.180.87.169/index.html")

    # Get the title of the webpage
    title = driver.title

    expected_title = "Haithem Ansible Pipeline"
    assert title == expected_title, f"Expected title: {expected_title}, Actual title: {title}"

finally:
    # Close the browser window
    driver.quit()

