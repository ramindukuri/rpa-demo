from RPA.Browser.Selenium import Selenium

browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)

def main():
    try:
        open_the_website("https://robocorp.com/docs/")
    
    finally:
        browser_lib.close_all_browsers()

if __name__ == "__main__":
    main()