from logging import exception

from bs4 import BeautifulSoup
import requests
import sys
import abc


class URL(object):
    def go(self):
        global soup
        try:
            chars = set('fishpond')
            r = requests.get(input("Please enter a Fishpond URL: "))
            if ((c in chars) for c in r) and r.status_code == 200:
                soup = BeautifulSoup(r.content, "lxml")
        except NameError:
            print('Please enter a valid Fishpond URL')
            sys.exit(0)

r = requests.get("http://www.fishpond.co.nz/Books/Fiction_Literature")
soup = BeautifulSoup(r.content, "lxml")

class TemplateOne(object):
    def __init__(self, type_name):
        self.type = type_name
        self.span = None
        self.classes = None
        self.specific = None
        self.appends = None

    def temp(self):
        result = []
        for x in soup.find_all(self.span, {self.classes: self.specific}):
            try:
                result.append(x[self.appends])
            except IndexError:
                print("No products found found")
        return result

class TemplateTwo(object):
    def __init__(self, type_name):
        self.type = type_name
        self.span = None
        self.classes = None
        self.specific = None

    def temp2(self):
        result = []
        for x in soup.find_all(self.span, {self.classes: self.specific}):
            try:
                result.append(x.text)
            except IndexError:
                print("No products found found")
        return result


class TemplateOneBuilder(object):
    """
    An abstract builder class, for concrete builders to be derived from.
    """
    __metadata__ = abc.ABCMeta

    @abc.abstractmethod
    def set_span(self):
        pass

    @abc.abstractmethod
    def set_classes(self):
        pass

    @abc.abstractmethod
    def set_specific(self):
        pass

    @abc.abstractmethod
    def set_appends(self):
        pass


class TemplateTwoBuilder(object):
    """
    An abstract builder class, for concrete builders to be derived from.
    """
    __metadata__ = abc.ABCMeta

    @abc.abstractmethod
    def set_span(self):
        pass

    @abc.abstractmethod
    def set_classes(self):
        pass

    @abc.abstractmethod
    def set_specific(self):
        pass

class product_name(TemplateTwoBuilder):
    def __init__(self):
        self.type = TemplateTwo("Product")

    def set_span(self):
        self.type.span = "a"

    def set_classes(self):
        self.type.classes = "class"

    def set_specific(self):
        self.type.specific = "blue_link fn url"

class publishing_date(TemplateTwoBuilder):
    def __init__(self):
        self.type = TemplateTwo("Publishing Date")

    def set_span(self):
            self.type.span = "div"

    def set_classes(self):
            self.type.classes = "class"

    def set_specific(self):
            self.type.specific = "productSearch-metainfo"


class RRP(TemplateTwoBuilder):
    def __init__(self):
        self.type = TemplateTwo("RRP")

    def set_span(self):
        self.type.span = "s"

    def set_classes(self):
        self.type.classes = ""

    def set_specific(self):
        self.type.specific = ""

class sale_prices(TemplateTwoBuilder):
    def __init__(self):
        self.type = TemplateTwo("Sales Price")

    def set_span(self):
        self.type.span = "span"

    def set_classes(self):
        self.type.classes = "class"

    def set_specific(self):
        self.type.specific = "productSpecialPrice"

class saving_total(TemplateTwoBuilder):
    def __init__(self):
        self.type = TemplateTwo("Savings Total")

    def set_span(self):
        self.type.span = "span"

    def set_classes(self):
        self.type.classes = "class"

    def set_specific(self):
        self.type.specific = "you_save"


class photo_link(TemplateOneBuilder):
    def __init__(self):
        self.type = TemplateOne("Photo Link")

    def set_span(self):
        self.type.span = "img"

    def set_classes(self):
        self.type.classes = "class"

    def set_specific(self):
        self.type.specific = "photo"

    def set_appends(self):
        self.type.appends = "src"


class isbn(TemplateOneBuilder):
    def __init__(self):
        self.type = TemplateOne("ISBN")

    def set_span(self):
        self.type.span = "input"

    def set_classes(self):
        self.type.classes = "name"

    def set_specific(self):
        self.type.specific = "barcode"

    def set_appends(self):
        self.type.appends = "value"


class Director(object):
    """
    The director class, this will keep a concrete builder.
    """

    def __init__(self):
        self.builder = None

    def create(self):
        """
        Creates and returns a Vehicle using self.builder
        Precondition: not self.builder is None
        """
        assert not self.builder is None, "No defined builder"
        self.builder.set_span()
        self.builder.set_classes()
        self.builder.set_specific()
        self.builder.set_appends()
        return self.builder.type

    def create2(self):
        """
        Creates and returns a Vehicle using self.builder
        Precondition: not self.builder is None
        """
        assert not self.builder is None, "No defined builder"
        self.builder.set_span()
        self.builder.set_classes()
        self.builder.set_specific()
        return self.builder.type
