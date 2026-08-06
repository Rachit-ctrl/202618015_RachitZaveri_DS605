import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]

    start_urls = [
        "https://books.toscrape.com/catalogue/page-1.html"
    ]

    count = 0

    def parse(self, response):

        books = response.css("article.product_pod h3 a::attr(href)").getall()

        for book in books:

            if self.count >= 100:
                return

            yield response.follow(book, callback=self.parse_book)

        next_page = response.css("li.next a::attr(href)").get()

        if next_page and self.count < 100:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):

        if self.count >= 100:
            return

        self.count += 1

        yield {

            "title": response.css("h1::text").get(),

            "category": response.css("ul.breadcrumb li a::text").getall()[-1],

            "price": response.css("p.price_color::text").get(),

            "rating": response.css("p.star-rating::attr(class)").get().replace("star-rating ", ""),

            "availability": response.css("p.availability::text").getall()[-1].strip(),

            "product_description": response.xpath(
                '//div[@id="product_description"]/following-sibling::p/text()'
            ).get(),

            "UPC": response.xpath(
                '//th[text()="UPC"]/following-sibling::td/text()'
            ).get(),

            "number_of_reviews": response.xpath(
                '//th[text()="Number of reviews"]/following-sibling::td/text()'
            ).get(),

            "product_url": response.url

        }