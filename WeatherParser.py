# Generated from Weather.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write(" \4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\5\2\f\n\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\5\3\25\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\34\n\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2\36\2\13\3")
        buf.write("\2\2\2\4\24\3\2\2\2\6\33\3\2\2\2\b\35\3\2\2\2\n\f\5\4")
        buf.write("\3\2\13\n\3\2\2\2\13\f\3\2\2\2\f\r\3\2\2\2\r\16\7\2\2")
        buf.write("\3\16\3\3\2\2\2\17\20\5\6\4\2\20\21\7\4\2\2\21\22\5\6")
        buf.write("\4\2\22\25\3\2\2\2\23\25\5\6\4\2\24\17\3\2\2\2\24\23\3")
        buf.write("\2\2\2\25\5\3\2\2\2\26\27\5\b\5\2\27\30\7\5\2\2\30\31")
        buf.write("\5\b\5\2\31\34\3\2\2\2\32\34\5\b\5\2\33\26\3\2\2\2\33")
        buf.write("\32\3\2\2\2\34\7\3\2\2\2\35\36\7\6\2\2\36\t\3\2\2\2\5")
        buf.write("\13\24\33")
        return buf.getvalue()


class WeatherParser ( Parser ):

    grammarFileName = "Weather.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'or'" ]

    symbolicNames = [ "<INVALID>", "WS", "CHANGE", "OR", "UNIT" ]

    RULE_start = 0
    RULE_expression = 1
    RULE_weather = 2
    RULE_unit = 3

    ruleNames =  [ "start", "expression", "weather", "unit" ]

    EOF = Token.EOF
    WS=1
    CHANGE=2
    OR=3
    UNIT=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WeatherParser.EOF, 0)

        def expression(self):
            return self.getTypedRuleContext(WeatherParser.ExpressionContext,0)


        def getRuleIndex(self):
            return WeatherParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = WeatherParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WeatherParser.UNIT:
                self.state = 8
                self.expression()


            self.state = 11
            self.match(WeatherParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def weather(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WeatherParser.WeatherContext)
            else:
                return self.getTypedRuleContext(WeatherParser.WeatherContext,i)


        def CHANGE(self):
            return self.getToken(WeatherParser.CHANGE, 0)

        def getRuleIndex(self):
            return WeatherParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = WeatherParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.weather()
                self.state = 14
                self.match(WeatherParser.CHANGE)
                self.state = 15
                self.weather()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.weather()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WeatherContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WeatherParser.UnitContext)
            else:
                return self.getTypedRuleContext(WeatherParser.UnitContext,i)


        def OR(self):
            return self.getToken(WeatherParser.OR, 0)

        def getRuleIndex(self):
            return WeatherParser.RULE_weather

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeather" ):
                listener.enterWeather(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeather" ):
                listener.exitWeather(self)




    def weather(self):

        localctx = WeatherParser.WeatherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_weather)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.unit()
                self.state = 21
                self.match(WeatherParser.OR)
                self.state = 22
                self.unit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.unit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIT(self):
            return self.getToken(WeatherParser.UNIT, 0)

        def getRuleIndex(self):
            return WeatherParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)




    def unit(self):

        localctx = WeatherParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(WeatherParser.UNIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





