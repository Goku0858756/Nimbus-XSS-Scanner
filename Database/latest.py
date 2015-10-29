__author__ = 'N05F3R4TU'
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # downloads_copy_link
    # aa = BeautifulSoup(requests.get(url="https://www.mongodb.org/downloads#production").text).find_all("a", {"href": "btn-primary btn-border-curved btn-large text-sm"})
    aa = BeautifulSoup(requests.get(url="https://www.mongodb.org/downloads#production").text)

    print(aa.prettify())
