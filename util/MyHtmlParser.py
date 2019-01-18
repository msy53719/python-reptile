from html.parser import HTMLParser
from util import environment_check


class my_html_parser(HTMLParser):
    def handle_charref(self, name):
        pass

    def handle_startendtag(self, tag, attrs):
        if(tag=='body'):
            for attr in attrs:
                print(attr[1][1])

    def handle_endtag(self, tag):
         pass

    def handle_comment(self, data):
        pass

    def handle_pi(self, data):
        pass


parser = my_html_parser()
parser.feed(environment_check.gethtml('http://www.jmrenti.org'))
