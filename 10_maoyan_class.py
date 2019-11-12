from urllib import request
from fake_useragent import UserAgent
import re
import random,time


class MaoyanMovie():

    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    def get_data(self,url):
        headers = {'User-Agent':UserAgent().random}
        res = request.Request(url=url,headers=headers)
        resp = request.urlopen(res)
        time.sleep(random.randint(1, 2))
        html = resp.read().decode()

        return html

    def save_data(self,data):
        r_list = re.compile('<div class="movie-item-info">.*?title="(.*?)" data-act="boarditem-click" data-val=.*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>',re.S)
        r = r_list.findall(data)

        with open('a.txt', 'w') as f:
            for i in r:
                a = '电影名：' + i[0].strip() + '\n'
                b = i[1].strip() + '\n'
                c = i[2].strip() + '\n'
                f.write(a)
                f.write(b)
                f.write(c)
        print('===========')


    def run(self):
        start_page = int(input('起始页码:'))
        end_page = int(input('终止页码:'))
        with open('a.html', 'w+') as f:
            for i in range(start_page,end_page):
                page = (i-1)*10
                url = self.url.format(page)
                f.write(self.get_data(url))
            data = f.read()
            self.save_data(data)







if __name__ == '__main__':
    s = MaoyanMovie()
    s.run()
