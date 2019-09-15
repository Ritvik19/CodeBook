# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class Pythonist2Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print('->', attr, '>', value)

parser = Pythonist2Parser()
for _ in range(int(input())):
    parser.feed(input())
parser.close()
