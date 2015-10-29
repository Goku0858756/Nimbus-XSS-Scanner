__author__ = 'N05F3R4TU'
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # downloads_copy_link
    print(BeautifulSoup(requests.get(url="https://www.mongodb.org/downloads").text).find_all("a", {"href": "btn-primary btn-border-curved btn-large text-sm"}))
