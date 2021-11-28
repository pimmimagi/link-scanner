from selenium import webdriver
import requests, sys


def get_links(url: str):
    """Find all links on the given url.

           Returns:
              a list of all unique hyperlinks on the page,
              without page fragments or query parameters.
    """
    driver = webdriver.Chrome(
        "/Users/sarochasit/Desktop/ISP/link-scanner/chromedriver")
    driver.get(url)
    list_url = []
    all_elems = driver.find_element_by_xpath("//a[@href]")
    for elem in all_elems:
        if "#" or "?" in elem.get_attribute("href"):
            continue
        else:
            if elem.get_attribute("href") not in list_url:
                list_url.append(elem.get_attribute("href"))
    return list_url


def is_valid_url(url: str):
    """
    Return True if url is valid if it's not return False.
    """
    try:
        response = requests.head(url)
        response.raise_for_status()
    except requests.HTTPError:
        return False
    return True


def invalid_urls(url: list):
    """ Returns a new list containing only the invalid or unreachable URLs. 
    If no invalid URLs, return an empty list.
    """
    invalid_url = []
    for i in url:
        if not is_valid_url(i):
            invalid_url.append(i)
    return invalid_url


def main():
    if len(sys.argv) < 2:
        print("Usage:  python3 link_scan.py url")
        print("Test all hyperlinks on the given url.")
    else:
        list_url = get_links(sys.argv[1])
        invalid_url_list = invalid_urls(list_url)
        for i in list_url:
            print(i)
        print("Bad Links:")
        for j in invalid_url_list:
            print(j)


if __name__ == '__main__':
    main()
