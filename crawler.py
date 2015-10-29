__author__ = 'N05F3R4TU'

class Crawl(object):
    """
    Crawl the given URL
    """
    import queue
    __crawler_queue = queue.Queue()

    def __init__(self, url=None):
        """
        Cralwer Constructor
        """
        self.name = "Crawler Object"
        self.url = url

    def __str__(self):
        """
        Object as dictionary
        :return:
        """
        pass

    def __del__(self):
        """
        Clean your shit up
        :return:
        """
        print(self.__class__.__name__, "Destructed")
        return self.__class__.__name__

    def run(self):
        """
        For MultiThreading
        :return:
        """
        pass

    def update(self):
        """
        Update Shared dict
        :return:
        """
        pass

    def crawl(self):
        """
        The Crawl method starts crawling
        :return:
        """
        import requests
        from bs4 import BeautifulSoup
        session = requests.Session()
        links = set([href.get('href') for href in BeautifulSoup(session.get(url=self.url).text).find_all('a')])
        print(links)

    def user_agent(self):
        """
        Random return User-Agent
        :return:
        """
        import random
        agents = ['Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36']
        return {'User-Agent': random.choice(agents)}


    def proxy(self):
        """
        Proxy Method returns an proxy if enabled
        :return:
        """

    def url_parsing(self):
        """
        Parse Full-Url
        :return:
        """
        pass

if __name__ == '__main__':
    target = "http://www.nu.nl"
    spider = Crawl(url=target)
    spider.crawl()