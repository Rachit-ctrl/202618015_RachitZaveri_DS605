import scrapy


class BooksSpider(scrapy.Spider):

    name = "books"

    allowed_domains = ["books.toscrape.com"]

    start_urls = [
        "https://books.toscrape.com/"
    ]

    # We only need 5 catalog pages for the assignment
    max_pages = 5

    def parse(self, response):

        # Determine current catalog page number
        if "page-" in response.url:
            page_number = int(
                response.url.split("page-")[1].split(".html")[0]
            )
        else:
            page_number = 1

        self.logger.info(
            f"Scraping catalog page {page_number}"
        )

        # ---------------------------------------
        # Extract book links
        # ---------------------------------------

        book_links = response.css(
            "article.product_pod h3 a::attr(href)"
        ).getall()

        self.logger.info(
            f"Found {len(book_links)} books on page {page_number}"
        )

        # ---------------------------------------
        # Visit individual book pages
        # ---------------------------------------

        for book_link in book_links:

            book_url = response.urljoin(book_link)

            yield scrapy.Request(
                url=book_url,
                callback=self.parse_book
            )

        # ---------------------------------------
        # Pagination
        # ---------------------------------------

        if page_number < self.max_pages:

            next_page = response.css(
                "li.next a::attr(href)"
            ).get()

            if next_page:

                yield response.follow(
                    next_page,
                    callback=self.parse
                )

    def parse_book(self, response):

        # Title
        title = response.css(
            "div.product_main h1::text"
        ).get()

        # Price
        price = response.css(
            "p.price_color::text"
        ).get()

        # Rating
        rating = response.css(
            "p.star-rating::attr(class)"
        ).get()

        # Availability
        availability = "".join(
            response.css(
                "p.instock.availability::text"
            ).getall()
        ).strip()

        # Category
        category = response.css(
            "ul.breadcrumb li:nth-child(3) a::text"
        ).get()

        # Description
        description = response.css(
            "#product_description + p::text"
        ).get()

        # UPC
        upc = response.css(
            "table tr:nth-child(1) td::text"
        ).get()

        # Number of reviews
        number_of_reviews = response.css(
            "table tr:nth-child(7) td::text"
        ).get()

        # Store record
        yield {
            "title": title,
            "category": category,
            "price": price,
            "rating": rating,
            "availability": availability,
            "description": description,
            "UPC": upc,
            "number_of_reviews": number_of_reviews,
            "product_url": response.url
        }