# Generated from Weather.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("!\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\r\n\2\r")
        buf.write("\2\16\2\16\3\2\3\2\3\3\3\3\3\3\5\3\26\n\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5 \n\5\2\2\6\3\3\5\4\7\5\t\6\3")
        buf.write("\2\5\5\2\13\f\17\17\"\"\4\2--\60\60\4\2EETT\2$\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\f\3\2\2\2\5")
        buf.write("\25\3\2\2\2\7\27\3\2\2\2\t\37\3\2\2\2\13\r\t\2\2\2\f\13")
        buf.write("\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\20")
        buf.write("\3\2\2\2\20\21\b\2\2\2\21\4\3\2\2\2\22\23\7/\2\2\23\26")
        buf.write("\7@\2\2\24\26\t\3\2\2\25\22\3\2\2\2\25\24\3\2\2\2\26\6")
        buf.write("\3\2\2\2\27\30\7q\2\2\30\31\7t\2\2\31\b\3\2\2\2\32\33")
        buf.write("\7U\2\2\33 \7W\2\2\34 \t\4\2\2\35\36\7U\2\2\36 \7P\2\2")
        buf.write("\37\32\3\2\2\2\37\34\3\2\2\2\37\35\3\2\2\2 \n\3\2\2\2")
        buf.write("\6\2\16\25\37\3\b\2\2")
        return buf.getvalue()


class WeatherLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    CHANGE = 2
    OR = 3
    UNIT = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'or'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "CHANGE", "OR", "UNIT" ]

    ruleNames = [ "WS", "CHANGE", "OR", "UNIT" ]

    grammarFileName = "Weather.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


