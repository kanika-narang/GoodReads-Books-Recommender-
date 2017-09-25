import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "mytest"

#     def start_requests(self):
#         urls = [
#             'https://www.goodreads.com/book/show/2767052',
#             'https://www.goodreads.com/book/show/41865',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'mytest-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)


import scrapy
import csv


class QuotesSpider(scrapy.Spider):
    name = "mytest"
    start_urls = ['https://www.goodreads.com/book/show/2767052']
    idd=None

    def parse(self,response):
        base_url='https://www.goodreads.com/book/show/'
        global idd
        with open('/home/kanika/Documents/3rdsem/Machine Learning/project/goodbooks-10k/books.csv' ) as csvfile:
            line=csv.reader(csvfile,delimiter=',')
            for row in line:
                print(row[2])
                idd = row[2]
                full_url=base_url + row[2]
                request= scrapy.Request(url=full_url,callback=self.parse_details)
                request.meta['bookid']=row[2]
                yield request
                    

    def parse_details(self, response,):
            yield {
                'id' : response.meta['bookid'],
                'title': response.css('div.infoBoxRowItem::text').extract_first(),
                'author': response.css('div.stacked > span > a > span::text')[0].extract(),
                'description' :response.css('div.readable > span::text')[1].extract(),
                # 'bookformat' : response.css('div.row > span::text')[0].extract(),
                # 'bookEdition' : response.css('div.row > span::text')[1].extract(),
                # 'numberofpages' : response.css('div.row > span::text')[2].extract(),
                'Language' : response.css('div.clearFloats > div.infoBoxRowItem::text')[3].extract(),
                'GoodReadAverageRating': response.css('span.average::text')[0].extract(),
                'NumberofRatings' : response.css('a.gr-hyperlink > span.votes::attr(title)').extract(),

            }


