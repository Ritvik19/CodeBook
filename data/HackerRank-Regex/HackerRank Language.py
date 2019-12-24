import re

string = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'
string = string.replace(':', '|')
regex = r'^[1-9]\d{4}\s' + '(' + string + ')$'
pattern = re.compile(regex)
n = int(input())
for i in range(n):
    if pattern.match(input()):
        print('VALID')
    else:
        print('INVALID')
