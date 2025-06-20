

class TestOpenAmazonHomePage:

    def test_open_amazon_homepage(self,app):
        app.open_amazon.open_amazon_homepage()
        app.open_amazon.continue_shopping()
        app.open_amazon.verify_homepage()
        app.open_amazon.verify_language()

    def test_search_for(self,app):
        app.open_amazon.open_amazon_homepage()
        app.open_amazon.continue_shopping()
        app.search_product.search_for()
        app.search_product.hover_to_product()
        app.search_product.check_image()

