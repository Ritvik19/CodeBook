# Enter your code here. Read input from STDIN. Print output to STDOUT
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for a in attrs:
            print "->", a[0], ">", a[1]
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for a in attrs:
            print "->", a[0], ">", a[1]

# instantiate the parser and fed it some HTML
html = ""
for i in range(int(input())):
    html += raw_input()
parser = MyHTMLParser()
parser.feed(html)
parser.close()
