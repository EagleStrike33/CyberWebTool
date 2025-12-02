#!/usr/bin/env python3

# This is the main tool that will exploit five different web vulnerabilities on the 
# OWASP Juice Shop website. The vulnerabilities exploited are the following: SQLi, XSS,
# Broken Access Control, Broken Authentication, and Improper Input Validation.

# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
#Import Exploits
from Exploits import SQLi
from Exploits import XSS
from Exploits import IIV
from Exploits import BAC
from Exploits import BA

# Run the vulnerabilites
def run_full_scan(base_url="http://localhost:3000"):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    driver.get(base_url)

    # Close the welcome banner
    try:
        dismiss = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']")
        dismiss.click()
        cookies = driver.find_element(By.CSS_SELECTOR, "a[aria-label='dismiss cookie message']")
        cookies.click()
    except:
        pass

    sleep = 5 # Controls the sleep at key periods of execution. Add time to see the exploits...

    results = {
        "Injection - Login Admin": SQLi.test_sqli(driver, base_url, sleep),
        "XSS - DOM XSS": XSS.test_xss(driver, base_url, sleep),
        "Broken Access Control - View Basket": BAC.test_bac(driver, base_url, sleep),
        "Broken Authentication - Password Strength": BA.test_ba(driver, base_url, sleep),
        "Improper Input Validation - Zero Stars": IIV.test_iiv(driver, base_url, sleep)
    }

    for vuln, vulnerable in results.items():
        if vulnerable:
            status = "EXPLOITED"
        else:
            status = "FAILED"
        print(f"{vuln}: {status}")

    user_input = input("Please enter 'q' to quit completely.\n")
    if user_input == 'q':
        driver.quit()
    return results

if __name__ == "__main__":
    run_full_scan()