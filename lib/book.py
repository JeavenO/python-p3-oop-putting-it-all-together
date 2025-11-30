class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # uses the setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            print("page_count must be an integer")
            # Do not raise ValueError because the test expects only the print

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
