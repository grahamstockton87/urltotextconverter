# Import necessary libraries
import requests
import validators
from bs4 import BeautifulSoup

defaultUrl = ('https://www.acouplecooks.com/how-to-cook-eggs/')

# Ask user to enter URL and validate it
def askUserAndCheck():
    url = input('Enter URL to copy text or type [d] for default: ')

    # If user enters "d", use default URL
    if url == 'd':
        url = defaultUrl

    # Check if URL is valid
    if validators.url(url):
        print("URL is valid")
        response = requests.get(url)
        grabTextFromValidURL(response, url)
    else:
        print("URL is not valid")
        askUserAndCheck()


# Scrape text from valid URL
def grabTextFromValidURL(response, url):
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()

        lines = text.splitlines()

        # Remove blank lines
        filtered_lines = [line for line in lines if line.strip()]
        text = "\n".join(filtered_lines)

        # Remove non-ASCII characters
        text = "".join(c for c in text if ord(c) < 128)

        # Write text to file
        writeToFile(text, url)


# Write text to file
def writeToFile(text, url):
    name = input('Name the file: ')
    path = 'C:/Users/graha/PycharmProjects/urltotextconverter/Outputs/' + name
    with open(path, "w") as file:
        file.write('The Url for this website is:' + '\n' + url + '\n')
        file.write('The name of this file is: ' + name + '\n')
        file.write(text)
    print("succesfully exported " + path)


# Ask user if they want to convert again
def askAgain():
    again = input('Would you like to convert again? [y/n]')
    if (again == 'y', 'Y'):
        askUserAndCheck()
    else:
        askAgain()

if __name__ == '__main__':
    # Call askUserAndCheck() function to start program
    askUserAndCheck()




