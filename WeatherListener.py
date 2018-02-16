# Generated from Weather.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WeatherParser import WeatherParser
else:
    from WeatherParser import WeatherParser

# This class defines a complete listener for a parse tree produced by WeatherParser.
class WeatherListener(ParseTreeListener):

    # Enter a parse tree produced by WeatherParser#start.
    def enterStart(self, ctx:WeatherParser.StartContext):
        pass

    # Exit a parse tree produced by WeatherParser#start.
    def exitStart(self, ctx:WeatherParser.StartContext):
        pass


    # Enter a parse tree produced by WeatherParser#expression.
    def enterExpression(self, ctx:WeatherParser.ExpressionContext):
        pass

    # Exit a parse tree produced by WeatherParser#expression.
    def exitExpression(self, ctx:WeatherParser.ExpressionContext):
        pass


    # Enter a parse tree produced by WeatherParser#weather.
    def enterWeather(self, ctx:WeatherParser.WeatherContext):
        pass

    # Exit a parse tree produced by WeatherParser#weather.
    def exitWeather(self, ctx:WeatherParser.WeatherContext):
        pass


    # Enter a parse tree produced by WeatherParser#unit.
    def enterUnit(self, ctx:WeatherParser.UnitContext):
        pass

    # Exit a parse tree produced by WeatherParser#unit.
    def exitUnit(self, ctx:WeatherParser.UnitContext):
        pass


