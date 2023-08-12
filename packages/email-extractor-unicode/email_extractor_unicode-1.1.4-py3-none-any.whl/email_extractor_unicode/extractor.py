import undetected_chromedriver as uc
import re
import requests
from bs4 import BeautifulSoup
import subprocess
import os

counter = 0

def extract_emails(text):
    # Regular expression pattern to find emails
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def extract_emails_from_phone_file(phone_file_path, emails_file_path):
    global counter
    # Create a single driver instance
    driver = None

    try:
        driver = uc.Chrome()

        # Open the phone.txt file to read phone numbers line by line
        with open(phone_file_path, 'r') as file:
            phone_numbers = [phone.strip() for phone in file.readlines()]

        # Initialize a set to store all emails without duplicates
        all_emails = set()

        # Loop through each phone number, visit the corresponding URL, and extract emails
        for phone in phone_numbers:
            if "+1" in phone:
                phone = phone.replace("+1" , "")
            try:
                url = f'https://www.smartbackgroundchecks.com/phone/{phone}'
                driver.get(url)

                # Get the page source
                page_source = driver.page_source

                # Define the pattern to extract URLs from anchor tags
                pattern = r'<a\s+href="(.*?)".*?>'

                # Use re.findall to find all occurrences of the pattern in the source code
                links = re.findall(pattern, page_source)

                # Filter and extract only the links you need
                target_links = [link for link in links if link.startswith('https://www.smartbackgroundchecks.com/people/')]

                # Remove duplicates by converting the list to a set and then back to a list
                unique_links = list(set(target_links))

                # Visiting each link, collecting emails, and writing them to the file
                for link in unique_links:
                    try:
                        driver.get(link)
                        emails_on_page = extract_emails(driver.page_source)
                        if emails_on_page:
                            for email in emails_on_page:
                                if email not in all_emails:
                                    all_emails.add(email)
                                    with open(emails_file_path, 'a') as file:
                                        file.write(f"{email}\n")
                                    counter+=1
                                    print(f"{counter}: {phone} >> {email}")
                    except Exception as e:
                        print(f"Error while processing link {link}: {e}")
            except Exception as e:
                print(f"Error while processing phone number {phone}: {e}")
                continue
        
        input(" All phone numbers have been processed - Press enter to exit ")

    finally:
        # Close the driver when you're done visiting all URLs
        if driver is not None:
            driver.quit()

def get_package_version(package_name):
    try:
        output = subprocess.check_output(['pip', 'show', package_name], universal_newlines=True)
        lines = output.strip().split('\n')
        version_line = next((line for line in lines if line.startswith('Version:')), None)
        if version_line:
            _, version = version_line.split(':')
            return version.strip()
        else:
            return None
    except subprocess.CalledProcessError:
        return None

def checker():

    url = "https://pypi.org/project/email-extractor-unicode/"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        exit()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the <h1> element with the specified class
    h1_element = soup.find("h1", class_="package-header__name")

    # Extract the text inside the <h1> element
    if h1_element:
        package_name_version = h1_element.get_text().strip()

        # Use regular expression to extract the version number
        version_number = re.search(r'\d+\.\d+\.\d+', package_name_version)
        if version_number:
            installed_version_number = version_number.group(0)
            package_name = 'email-extractor-unicode'
            version_number = get_package_version(package_name)
            if str(installed_version_number) == str(version_number):
                phone_file_path = input("Please type phone file name or path to file: ")
                emails_file_path = input("How do you want to save emails? eg, emails.txt: ")
                extract_emails_from_phone_file(phone_file_path, emails_file_path)
            else:
                subprocess.check_call(["pip", "install", "email-extractor-unicode", "--upgrade"])
                os.system("cls")
                phone_file_path = input("Please type phone file name or path to file: ")
                emails_file_path = input("How do you want to save emails? eg, emails.txt: ")
                extract_emails_from_phone_file(phone_file_path, emails_file_path)
        else:
            os.system("cls")
            phone_file_path = input("Please type phone file name or path to file: ")
            emails_file_path = input("How do you want to save emails? eg, emails.txt: ")
            extract_emails_from_phone_file(phone_file_path, emails_file_path)        
    else:
        phone_file_path = input("Please type phone file name or path to file: ")
        emails_file_path = input("How do you want to save emails? eg, emails.txt: ")
        extract_emails_from_phone_file(phone_file_path, emails_file_path)
