from antlr4 import *
from WeatherLexer import WeatherLexer
from WeatherListener import WeatherListener
from WeatherParser import WeatherParser
import sys

class WeatherPrintListener(WeatherListener):
    def enterUnit(self, ctx):
        print("Unit: %s" % ctx.UNIT())

def main(argv):
    lexer = WeatherLexer(FileStream(argv[1]))
    stream = CommonTokenStream(lexer)
    parser = WeatherParser(stream)
    tree = parser.start()
    printer = WeatherPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
