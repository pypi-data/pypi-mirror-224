# Generated from FoostacheParser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,311,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,1,5,1,65,8,1,10,1,12,
        1,68,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,3,4,3,81,8,
        3,11,3,12,3,82,1,4,1,4,1,4,1,4,1,5,5,5,90,8,5,10,5,12,5,93,9,5,1,
        6,1,6,1,6,5,6,98,8,6,10,6,12,6,101,9,6,1,6,1,6,1,7,1,7,1,7,1,7,5,
        7,109,8,7,10,7,12,7,112,9,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,3,9,121,
        8,9,1,9,3,9,124,8,9,1,9,1,9,3,9,128,8,9,1,9,1,9,1,10,1,10,1,10,5,
        10,135,8,10,10,10,12,10,138,9,10,1,10,3,10,141,8,10,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,180,8,15,1,15,1,
        15,1,15,1,15,1,15,1,15,5,15,188,8,15,10,15,12,15,191,9,15,1,16,1,
        16,5,16,195,8,16,10,16,12,16,198,9,16,1,16,1,16,1,16,1,16,1,16,3,
        16,205,8,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,213,8,16,10,16,12,
        16,216,9,16,3,16,218,8,16,3,16,220,8,16,1,17,1,17,1,17,5,17,225,
        8,17,10,17,12,17,228,9,17,1,17,3,17,231,8,17,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,5,20,251,8,20,10,20,12,20,254,9,20,1,20,1,20,1,20,1,20,1,21,
        3,21,261,8,21,1,21,3,21,264,8,21,1,22,1,22,3,22,268,8,22,1,22,3,
        22,271,8,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,280,8,24,1,25,
        1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,0,1,30,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,1,2,0,42,42,44,44,
        319,0,60,1,0,0,0,2,66,1,0,0,0,4,77,1,0,0,0,6,80,1,0,0,0,8,84,1,0,
        0,0,10,91,1,0,0,0,12,94,1,0,0,0,14,104,1,0,0,0,16,115,1,0,0,0,18,
        118,1,0,0,0,20,131,1,0,0,0,22,146,1,0,0,0,24,151,1,0,0,0,26,154,
        1,0,0,0,28,159,1,0,0,0,30,179,1,0,0,0,32,219,1,0,0,0,34,230,1,0,
        0,0,36,232,1,0,0,0,38,234,1,0,0,0,40,243,1,0,0,0,42,260,1,0,0,0,
        44,265,1,0,0,0,46,272,1,0,0,0,48,279,1,0,0,0,50,281,1,0,0,0,52,286,
        1,0,0,0,54,291,1,0,0,0,56,296,1,0,0,0,58,301,1,0,0,0,60,61,3,2,1,
        0,61,62,5,0,0,1,62,1,1,0,0,0,63,65,3,4,2,0,64,63,1,0,0,0,65,68,1,
        0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,3,1,0,0,0,68,66,1,0,0,0,69,
        78,3,6,3,0,70,78,3,8,4,0,71,78,3,12,6,0,72,78,3,14,7,0,73,78,3,20,
        10,0,74,78,3,38,19,0,75,78,3,40,20,0,76,78,3,58,29,0,77,69,1,0,0,
        0,77,70,1,0,0,0,77,71,1,0,0,0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,
        1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,5,1,0,0,0,79,81,5,4,0,0,80,
        79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,7,1,0,0,
        0,84,85,5,2,0,0,85,86,3,10,5,0,86,87,5,5,0,0,87,9,1,0,0,0,88,90,
        5,6,0,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,
        92,11,1,0,0,0,93,91,1,0,0,0,94,95,5,3,0,0,95,99,3,32,16,0,96,98,
        3,16,8,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,
        0,100,102,1,0,0,0,101,99,1,0,0,0,102,103,5,7,0,0,103,13,1,0,0,0,
        104,105,5,3,0,0,105,106,3,32,16,0,106,110,3,18,9,0,107,109,3,16,
        8,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,
        0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,114,5,7,0,0,114,15,1,0,0,
        0,115,116,5,34,0,0,116,117,5,37,0,0,117,17,1,0,0,0,118,120,5,35,
        0,0,119,121,5,38,0,0,120,119,1,0,0,0,120,121,1,0,0,0,121,123,1,0,
        0,0,122,124,5,40,0,0,123,122,1,0,0,0,123,124,1,0,0,0,124,127,1,0,
        0,0,125,126,5,39,0,0,126,128,5,40,0,0,127,125,1,0,0,0,127,128,1,
        0,0,0,128,129,1,0,0,0,129,130,5,41,0,0,130,19,1,0,0,0,131,132,3,
        22,11,0,132,136,3,2,1,0,133,135,3,24,12,0,134,133,1,0,0,0,135,138,
        1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,139,141,3,28,14,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,
        1,0,0,0,142,143,5,3,0,0,143,144,5,15,0,0,144,145,5,7,0,0,145,21,
        1,0,0,0,146,147,5,3,0,0,147,148,5,18,0,0,148,149,3,30,15,0,149,150,
        5,7,0,0,150,23,1,0,0,0,151,152,3,26,13,0,152,153,3,2,1,0,153,25,
        1,0,0,0,154,155,5,3,0,0,155,156,5,14,0,0,156,157,3,30,15,0,157,158,
        5,7,0,0,158,27,1,0,0,0,159,160,5,3,0,0,160,161,5,13,0,0,161,162,
        5,7,0,0,162,163,3,2,1,0,163,29,1,0,0,0,164,165,6,15,-1,0,165,180,
        3,32,16,0,166,167,3,32,16,0,167,168,5,23,0,0,168,180,1,0,0,0,169,
        170,3,32,16,0,170,171,5,24,0,0,171,172,5,21,0,0,172,180,1,0,0,0,
        173,174,5,25,0,0,174,180,3,30,15,4,175,176,5,27,0,0,176,177,3,30,
        15,0,177,178,5,28,0,0,178,180,1,0,0,0,179,164,1,0,0,0,179,166,1,
        0,0,0,179,169,1,0,0,0,179,173,1,0,0,0,179,175,1,0,0,0,180,189,1,
        0,0,0,181,182,10,3,0,0,182,183,5,22,0,0,183,188,3,30,15,4,184,185,
        10,2,0,0,185,186,5,26,0,0,186,188,3,30,15,3,187,181,1,0,0,0,187,
        184,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,
        31,1,0,0,0,191,189,1,0,0,0,192,220,5,29,0,0,193,195,5,32,0,0,194,
        193,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,
        217,1,0,0,0,198,196,1,0,0,0,199,205,3,34,17,0,200,201,5,30,0,0,201,
        202,3,36,18,0,202,203,5,31,0,0,203,205,1,0,0,0,204,199,1,0,0,0,204,
        200,1,0,0,0,205,214,1,0,0,0,206,207,5,29,0,0,207,213,3,34,17,0,208,
        209,5,30,0,0,209,210,3,36,18,0,210,211,5,31,0,0,211,213,1,0,0,0,
        212,206,1,0,0,0,212,208,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,
        214,215,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,217,204,1,0,0,0,
        217,218,1,0,0,0,218,220,1,0,0,0,219,192,1,0,0,0,219,196,1,0,0,0,
        220,33,1,0,0,0,221,231,5,37,0,0,222,226,5,9,0,0,223,225,7,0,0,0,
        224,223,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,
        227,229,1,0,0,0,228,226,1,0,0,0,229,231,5,43,0,0,230,221,1,0,0,0,
        230,222,1,0,0,0,231,35,1,0,0,0,232,233,5,36,0,0,233,37,1,0,0,0,234,
        235,5,3,0,0,235,236,5,20,0,0,236,237,3,32,16,0,237,238,5,7,0,0,238,
        239,3,2,1,0,239,240,5,3,0,0,240,241,5,15,0,0,241,242,5,7,0,0,242,
        39,1,0,0,0,243,244,5,3,0,0,244,245,5,19,0,0,245,246,3,32,16,0,246,
        247,3,42,21,0,247,248,5,7,0,0,248,252,3,2,1,0,249,251,3,48,24,0,
        250,249,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,
        253,255,1,0,0,0,254,252,1,0,0,0,255,256,5,3,0,0,256,257,5,15,0,0,
        257,258,5,7,0,0,258,41,1,0,0,0,259,261,5,36,0,0,260,259,1,0,0,0,
        260,261,1,0,0,0,261,263,1,0,0,0,262,264,3,44,22,0,263,262,1,0,0,
        0,263,264,1,0,0,0,264,43,1,0,0,0,265,267,5,33,0,0,266,268,5,36,0,
        0,267,266,1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,271,3,46,23,
        0,270,269,1,0,0,0,270,271,1,0,0,0,271,45,1,0,0,0,272,273,5,33,0,
        0,273,274,5,36,0,0,274,47,1,0,0,0,275,280,3,50,25,0,276,280,3,52,
        26,0,277,280,3,54,27,0,278,280,3,56,28,0,279,275,1,0,0,0,279,276,
        1,0,0,0,279,277,1,0,0,0,279,278,1,0,0,0,280,49,1,0,0,0,281,282,5,
        3,0,0,282,283,5,11,0,0,283,284,5,7,0,0,284,285,3,2,1,0,285,51,1,
        0,0,0,286,287,5,3,0,0,287,288,5,10,0,0,288,289,5,7,0,0,289,290,3,
        2,1,0,290,53,1,0,0,0,291,292,5,3,0,0,292,293,5,12,0,0,293,294,5,
        7,0,0,294,295,3,2,1,0,295,55,1,0,0,0,296,297,5,3,0,0,297,298,5,13,
        0,0,298,299,5,7,0,0,299,300,3,2,1,0,300,57,1,0,0,0,301,302,5,3,0,
        0,302,303,5,17,0,0,303,304,5,37,0,0,304,305,5,7,0,0,305,306,3,2,
        1,0,306,307,5,3,0,0,307,308,5,15,0,0,308,309,5,7,0,0,309,59,1,0,
        0,0,28,66,77,82,91,99,110,120,123,127,136,140,179,187,189,196,204,
        212,214,217,219,226,230,252,260,263,267,270,279
    ]

class FoostacheParser ( Parser ):

    grammarFileName = "FoostacheParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'{{\"'", "'{{'", "<INVALID>", 
                     "'\"}}'", "<INVALID>", "'}}'", "<INVALID>", "<INVALID>", 
                     "':after'", "':before'", "':between'", "':else'", "':elseif'", 
                     "':end'", "':escape'", "':filter'", "':if'", "':iterate'", 
                     "':with'", "<INVALID>", "'and'", "'exists'", "'is'", 
                     "'not'", "'or'", "'('", "')'", "<INVALID>", "'['", 
                     "']'", "'^'", "':'", "'|'", "'%'", "<INVALID>", "<INVALID>", 
                     "'0'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "OPENL", "OPEN", "TEXT", "CLOSEL", 
                      "TEXTL", "CLOSE", "WS", "OPENQS", "AFTER", "BEFORE", 
                      "BETWEEN", "ELSE", "ELSEIF", "END", "ESCAPE", "FILTER", 
                      "IF", "ITERATE", "WITH", "TYPE", "AND", "EXISTS", 
                      "IS", "NOT", "OR", "LPAREN", "RPAREN", "DOT", "LBRACKET", 
                      "RBRACKET", "CARET", "COLON", "PIPE", "PERCENT", "INTEGER", 
                      "ID", "ZERO", "DOTN", "PINTEGERN", "NUMBER_SPECIFIER", 
                      "ESCCHARQS", "CLOSEQS", "CHARQS" ]

    RULE_template = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_rawText = 3
    RULE_literal = 4
    RULE_literalText = 5
    RULE_stringField = 6
    RULE_numberField = 7
    RULE_inlineFilter = 8
    RULE_numberFormat = 9
    RULE_ifBlock = 10
    RULE_ifTag = 11
    RULE_elseifBlock = 12
    RULE_elseifTag = 13
    RULE_elseBlock = 14
    RULE_expression = 15
    RULE_path = 16
    RULE_objectKey = 17
    RULE_arrayIndex = 18
    RULE_withBlock = 19
    RULE_iterateBlock = 20
    RULE_indexRange = 21
    RULE_indexRangeB = 22
    RULE_indexRangeC = 23
    RULE_iterateClause = 24
    RULE_iterateBeforeClause = 25
    RULE_iterateAfterClause = 26
    RULE_iterateBetweenClause = 27
    RULE_iterateElseClause = 28
    RULE_filterBlock = 29

    ruleNames =  [ "template", "statements", "statement", "rawText", "literal", 
                   "literalText", "stringField", "numberField", "inlineFilter", 
                   "numberFormat", "ifBlock", "ifTag", "elseifBlock", "elseifTag", 
                   "elseBlock", "expression", "path", "objectKey", "arrayIndex", 
                   "withBlock", "iterateBlock", "indexRange", "indexRangeB", 
                   "indexRangeC", "iterateClause", "iterateBeforeClause", 
                   "iterateAfterClause", "iterateBetweenClause", "iterateElseClause", 
                   "filterBlock" ]

    EOF = Token.EOF
    COMMENT=1
    OPENL=2
    OPEN=3
    TEXT=4
    CLOSEL=5
    TEXTL=6
    CLOSE=7
    WS=8
    OPENQS=9
    AFTER=10
    BEFORE=11
    BETWEEN=12
    ELSE=13
    ELSEIF=14
    END=15
    ESCAPE=16
    FILTER=17
    IF=18
    ITERATE=19
    WITH=20
    TYPE=21
    AND=22
    EXISTS=23
    IS=24
    NOT=25
    OR=26
    LPAREN=27
    RPAREN=28
    DOT=29
    LBRACKET=30
    RBRACKET=31
    CARET=32
    COLON=33
    PIPE=34
    PERCENT=35
    INTEGER=36
    ID=37
    ZERO=38
    DOTN=39
    PINTEGERN=40
    NUMBER_SPECIFIER=41
    ESCCHARQS=42
    CLOSEQS=43
    CHARQS=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TemplateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(FoostacheParser.EOF, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate" ):
                listener.enterTemplate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate" ):
                listener.exitTemplate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplate" ):
                return visitor.visitTemplate(self)
            else:
                return visitor.visitChildren(self)




    def template(self):

        localctx = FoostacheParser.TemplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_template)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.statements()
            self.state = 61
            self.match(FoostacheParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.StatementContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.StatementContext,i)


        def getRuleIndex(self):
            return FoostacheParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = FoostacheParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 63
                    self.statement() 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rawText(self):
            return self.getTypedRuleContext(FoostacheParser.RawTextContext,0)


        def literal(self):
            return self.getTypedRuleContext(FoostacheParser.LiteralContext,0)


        def stringField(self):
            return self.getTypedRuleContext(FoostacheParser.StringFieldContext,0)


        def numberField(self):
            return self.getTypedRuleContext(FoostacheParser.NumberFieldContext,0)


        def ifBlock(self):
            return self.getTypedRuleContext(FoostacheParser.IfBlockContext,0)


        def withBlock(self):
            return self.getTypedRuleContext(FoostacheParser.WithBlockContext,0)


        def iterateBlock(self):
            return self.getTypedRuleContext(FoostacheParser.IterateBlockContext,0)


        def filterBlock(self):
            return self.getTypedRuleContext(FoostacheParser.FilterBlockContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = FoostacheParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.rawText()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.stringField()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.numberField()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.ifBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.withBlock()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.iterateBlock()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 76
                self.filterBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RawTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.TEXT)
            else:
                return self.getToken(FoostacheParser.TEXT, i)

        def getRuleIndex(self):
            return FoostacheParser.RULE_rawText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRawText" ):
                listener.enterRawText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRawText" ):
                listener.exitRawText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRawText" ):
                return visitor.visitRawText(self)
            else:
                return visitor.visitChildren(self)




    def rawText(self):

        localctx = FoostacheParser.RawTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rawText)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 79
                    self.match(FoostacheParser.TEXT)

                else:
                    raise NoViableAltException(self)
                self.state = 82 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENL(self):
            return self.getToken(FoostacheParser.OPENL, 0)

        def literalText(self):
            return self.getTypedRuleContext(FoostacheParser.LiteralTextContext,0)


        def CLOSEL(self):
            return self.getToken(FoostacheParser.CLOSEL, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = FoostacheParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(FoostacheParser.OPENL)
            self.state = 85
            self.literalText()
            self.state = 86
            self.match(FoostacheParser.CLOSEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXTL(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.TEXTL)
            else:
                return self.getToken(FoostacheParser.TEXTL, i)

        def getRuleIndex(self):
            return FoostacheParser.RULE_literalText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralText" ):
                listener.enterLiteralText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralText" ):
                listener.exitLiteralText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralText" ):
                return visitor.visitLiteralText(self)
            else:
                return visitor.visitChildren(self)




    def literalText(self):

        localctx = FoostacheParser.LiteralTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literalText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 88
                self.match(FoostacheParser.TEXTL)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def path(self):
            return self.getTypedRuleContext(FoostacheParser.PathContext,0)


        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def inlineFilter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.InlineFilterContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.InlineFilterContext,i)


        def getRuleIndex(self):
            return FoostacheParser.RULE_stringField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringField" ):
                listener.enterStringField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringField" ):
                listener.exitStringField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringField" ):
                return visitor.visitStringField(self)
            else:
                return visitor.visitChildren(self)




    def stringField(self):

        localctx = FoostacheParser.StringFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stringField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(FoostacheParser.OPEN)
            self.state = 95
            self.path()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 96
                self.inlineFilter()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(FoostacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def path(self):
            return self.getTypedRuleContext(FoostacheParser.PathContext,0)


        def numberFormat(self):
            return self.getTypedRuleContext(FoostacheParser.NumberFormatContext,0)


        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def inlineFilter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.InlineFilterContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.InlineFilterContext,i)


        def getRuleIndex(self):
            return FoostacheParser.RULE_numberField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberField" ):
                listener.enterNumberField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberField" ):
                listener.exitNumberField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberField" ):
                return visitor.visitNumberField(self)
            else:
                return visitor.visitChildren(self)




    def numberField(self):

        localctx = FoostacheParser.NumberFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_numberField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(FoostacheParser.OPEN)
            self.state = 105
            self.path()
            self.state = 106
            self.numberFormat()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 107
                self.inlineFilter()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(FoostacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InlineFilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIPE(self):
            return self.getToken(FoostacheParser.PIPE, 0)

        def ID(self):
            return self.getToken(FoostacheParser.ID, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_inlineFilter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineFilter" ):
                listener.enterInlineFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineFilter" ):
                listener.exitInlineFilter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineFilter" ):
                return visitor.visitInlineFilter(self)
            else:
                return visitor.visitChildren(self)




    def inlineFilter(self):

        localctx = FoostacheParser.InlineFilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_inlineFilter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(FoostacheParser.PIPE)
            self.state = 116
            self.match(FoostacheParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberFormatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.flags = None # Token
            self.width = None # Token
            self.precision = None # Token
            self.specifier = None # Token

        def PERCENT(self):
            return self.getToken(FoostacheParser.PERCENT, 0)

        def NUMBER_SPECIFIER(self):
            return self.getToken(FoostacheParser.NUMBER_SPECIFIER, 0)

        def DOTN(self):
            return self.getToken(FoostacheParser.DOTN, 0)

        def ZERO(self):
            return self.getToken(FoostacheParser.ZERO, 0)

        def PINTEGERN(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.PINTEGERN)
            else:
                return self.getToken(FoostacheParser.PINTEGERN, i)

        def getRuleIndex(self):
            return FoostacheParser.RULE_numberFormat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberFormat" ):
                listener.enterNumberFormat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberFormat" ):
                listener.exitNumberFormat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberFormat" ):
                return visitor.visitNumberFormat(self)
            else:
                return visitor.visitChildren(self)




    def numberFormat(self):

        localctx = FoostacheParser.NumberFormatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numberFormat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(FoostacheParser.PERCENT)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 119
                localctx.flags = self.match(FoostacheParser.ZERO)


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 122
                localctx.width = self.match(FoostacheParser.PINTEGERN)


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 125
                self.match(FoostacheParser.DOTN)
                self.state = 126
                localctx.precision = self.match(FoostacheParser.PINTEGERN)


            self.state = 129
            localctx.specifier = self.match(FoostacheParser.NUMBER_SPECIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifTag(self):
            return self.getTypedRuleContext(FoostacheParser.IfTagContext,0)


        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def END(self):
            return self.getToken(FoostacheParser.END, 0)

        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def elseifBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.ElseifBlockContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.ElseifBlockContext,i)


        def elseBlock(self):
            return self.getTypedRuleContext(FoostacheParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = FoostacheParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.ifTag()
            self.state = 132
            self.statements()
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 133
                    self.elseifBlock() 
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 139
                self.elseBlock()


            self.state = 142
            self.match(FoostacheParser.OPEN)
            self.state = 143
            self.match(FoostacheParser.END)
            self.state = 144
            self.match(FoostacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfTagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def IF(self):
            return self.getToken(FoostacheParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(FoostacheParser.ExpressionContext,0)


        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_ifTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfTag" ):
                listener.enterIfTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfTag" ):
                listener.exitIfTag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfTag" ):
                return visitor.visitIfTag(self)
            else:
                return visitor.visitChildren(self)




    def ifTag(self):

        localctx = FoostacheParser.IfTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(FoostacheParser.OPEN)
            self.state = 147
            self.match(FoostacheParser.IF)
            self.state = 148
            self.expression(0)
            self.state = 149
            self.match(FoostacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseifTag(self):
            return self.getTypedRuleContext(FoostacheParser.ElseifTagContext,0)


        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_elseifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseifBlock" ):
                listener.enterElseifBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseifBlock" ):
                listener.exitElseifBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifBlock" ):
                return visitor.visitElseifBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseifBlock(self):

        localctx = FoostacheParser.ElseifBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elseifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.elseifTag()
            self.state = 152
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifTagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def ELSEIF(self):
            return self.getToken(FoostacheParser.ELSEIF, 0)

        def expression(self):
            return self.getTypedRuleContext(FoostacheParser.ExpressionContext,0)


        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_elseifTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseifTag" ):
                listener.enterElseifTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseifTag" ):
                listener.exitElseifTag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifTag" ):
                return visitor.visitElseifTag(self)
            else:
                return visitor.visitChildren(self)




    def elseifTag(self):

        localctx = FoostacheParser.ElseifTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elseifTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(FoostacheParser.OPEN)
            self.state = 155
            self.match(FoostacheParser.ELSEIF)
            self.state = 156
            self.expression(0)
            self.state = 157
            self.match(FoostacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def ELSE(self):
            return self.getToken(FoostacheParser.ELSE, 0)

        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = FoostacheParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(FoostacheParser.OPEN)
            self.state = 160
            self.match(FoostacheParser.ELSE)
            self.state = 161
            self.match(FoostacheParser.CLOSE)
            self.state = 162
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FoostacheParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ExpressionContext
            super().__init__(parser)
            self.expr1 = None # ExpressionContext
            self.expr2 = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(FoostacheParser.OR, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpression" ):
                return visitor.visitOrExpression(self)
            else:
                return visitor.visitChildren(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ExpressionContext
            super().__init__(parser)
            self.expr1 = None # ExpressionContext
            self.expr2 = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(FoostacheParser.AND, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpression" ):
                return visitor.visitAndExpression(self)
            else:
                return visitor.visitChildren(self)


    class BoolExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def path(self):
            return self.getTypedRuleContext(FoostacheParser.PathContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpression" ):
                return visitor.visitBoolExpression(self)
            else:
                return visitor.visitChildren(self)


    class ExistsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def path(self):
            return self.getTypedRuleContext(FoostacheParser.PathContext,0)

        def EXISTS(self):
            return self.getToken(FoostacheParser.EXISTS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExistsExpression" ):
                listener.enterExistsExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExistsExpression" ):
                listener.exitExistsExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExistsExpression" ):
                return visitor.visitExistsExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(FoostacheParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(FoostacheParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(FoostacheParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(FoostacheParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(FoostacheParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpression" ):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)


    class TypeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def path(self):
            return self.getTypedRuleContext(FoostacheParser.PathContext,0)

        def IS(self):
            return self.getToken(FoostacheParser.IS, 0)
        def TYPE(self):
            return self.getToken(FoostacheParser.TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExpression" ):
                listener.enterTypeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExpression" ):
                listener.exitTypeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeExpression" ):
                return visitor.visitTypeExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FoostacheParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = FoostacheParser.BoolExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 165
                self.path()
                pass

            elif la_ == 2:
                localctx = FoostacheParser.ExistsExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 166
                self.path()
                self.state = 167
                self.match(FoostacheParser.EXISTS)
                pass

            elif la_ == 3:
                localctx = FoostacheParser.TypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 169
                self.path()
                self.state = 170
                self.match(FoostacheParser.IS)
                self.state = 171
                self.match(FoostacheParser.TYPE)
                pass

            elif la_ == 4:
                localctx = FoostacheParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.match(FoostacheParser.NOT)
                self.state = 174
                self.expression(4)
                pass

            elif la_ == 5:
                localctx = FoostacheParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(FoostacheParser.LPAREN)
                self.state = 176
                self.expression(0)
                self.state = 177
                self.match(FoostacheParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 187
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = FoostacheParser.AndExpressionContext(self, FoostacheParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 182
                        self.match(FoostacheParser.AND)
                        self.state = 183
                        localctx.expr2 = self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = FoostacheParser.OrExpressionContext(self, FoostacheParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 185
                        self.match(FoostacheParser.OR)
                        self.state = 186
                        localctx.expr2 = self.expression(3)
                        pass

             
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FoostacheParser.RULE_path

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CaretPathContext(PathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.PathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CARET(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.CARET)
            else:
                return self.getToken(FoostacheParser.CARET, i)
        def objectKey(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.ObjectKeyContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.ObjectKeyContext,i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.LBRACKET)
            else:
                return self.getToken(FoostacheParser.LBRACKET, i)
        def arrayIndex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.ArrayIndexContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.ArrayIndexContext,i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.RBRACKET)
            else:
                return self.getToken(FoostacheParser.RBRACKET, i)
        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.DOT)
            else:
                return self.getToken(FoostacheParser.DOT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaretPath" ):
                listener.enterCaretPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaretPath" ):
                listener.exitCaretPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaretPath" ):
                return visitor.visitCaretPath(self)
            else:
                return visitor.visitChildren(self)


    class DotPathContext(PathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.PathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(FoostacheParser.DOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotPath" ):
                listener.enterDotPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotPath" ):
                listener.exitDotPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDotPath" ):
                return visitor.visitDotPath(self)
            else:
                return visitor.visitChildren(self)



    def path(self):

        localctx = FoostacheParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_path)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = FoostacheParser.DotPathContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(FoostacheParser.DOT)
                pass

            elif la_ == 2:
                localctx = FoostacheParser.CaretPathContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 193
                        self.match(FoostacheParser.CARET) 
                    self.state = 198
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                self.state = 217
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 204
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [9, 37]:
                        self.state = 199
                        self.objectKey()
                        pass
                    elif token in [30]:
                        self.state = 200
                        self.match(FoostacheParser.LBRACKET)
                        self.state = 201
                        self.arrayIndex()
                        self.state = 202
                        self.match(FoostacheParser.RBRACKET)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 214
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 212
                            self._errHandler.sync(self)
                            token = self._input.LA(1)
                            if token in [29]:
                                self.state = 206
                                self.match(FoostacheParser.DOT)
                                self.state = 207
                                self.objectKey()
                                pass
                            elif token in [30]:
                                self.state = 208
                                self.match(FoostacheParser.LBRACKET)
                                self.state = 209
                                self.arrayIndex()
                                self.state = 210
                                self.match(FoostacheParser.RBRACKET)
                                pass
                            else:
                                raise NoViableAltException(self)
                     
                        self.state = 216
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,17,self._ctx)



                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FoostacheParser.RULE_objectKey

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdObjectKeyContext(ObjectKeyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ObjectKeyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FoostacheParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdObjectKey" ):
                listener.enterIdObjectKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdObjectKey" ):
                listener.exitIdObjectKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdObjectKey" ):
                return visitor.visitIdObjectKey(self)
            else:
                return visitor.visitChildren(self)


    class QsObjectKeyContext(ObjectKeyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FoostacheParser.ObjectKeyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPENQS(self):
            return self.getToken(FoostacheParser.OPENQS, 0)
        def CLOSEQS(self):
            return self.getToken(FoostacheParser.CLOSEQS, 0)
        def CHARQS(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.CHARQS)
            else:
                return self.getToken(FoostacheParser.CHARQS, i)
        def ESCCHARQS(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.ESCCHARQS)
            else:
                return self.getToken(FoostacheParser.ESCCHARQS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQsObjectKey" ):
                listener.enterQsObjectKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQsObjectKey" ):
                listener.exitQsObjectKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQsObjectKey" ):
                return visitor.visitQsObjectKey(self)
            else:
                return visitor.visitChildren(self)



    def objectKey(self):

        localctx = FoostacheParser.ObjectKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_objectKey)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                localctx = FoostacheParser.IdObjectKeyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(FoostacheParser.ID)
                pass
            elif token in [9]:
                localctx = FoostacheParser.QsObjectKeyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(FoostacheParser.OPENQS)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42 or _la==44:
                    self.state = 223
                    _la = self._input.LA(1)
                    if not(_la==42 or _la==44):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 229
                self.match(FoostacheParser.CLOSEQS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(FoostacheParser.INTEGER, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_arrayIndex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayIndex" ):
                listener.enterArrayIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayIndex" ):
                listener.exitArrayIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayIndex" ):
                return visitor.visitArrayIndex(self)
            else:
                return visitor.visitChildren(self)




    def arrayIndex(self):

        localctx = FoostacheParser.ArrayIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arrayIndex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(FoostacheParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.OPEN)
            else:
                return self.getToken(FoostacheParser.OPEN, i)

        def WITH(self):
            return self.getToken(FoostacheParser.WITH, 0)

        def path(self):
            return self.getTypedRuleContext(FoostacheParser.PathContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.CLOSE)
            else:
                return self.getToken(FoostacheParser.CLOSE, i)

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def END(self):
            return self.getToken(FoostacheParser.END, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_withBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithBlock" ):
                listener.enterWithBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithBlock" ):
                listener.exitWithBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithBlock" ):
                return visitor.visitWithBlock(self)
            else:
                return visitor.visitChildren(self)




    def withBlock(self):

        localctx = FoostacheParser.WithBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_withBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(FoostacheParser.OPEN)
            self.state = 235
            self.match(FoostacheParser.WITH)
            self.state = 236
            self.path()
            self.state = 237
            self.match(FoostacheParser.CLOSE)
            self.state = 238
            self.statements()
            self.state = 239
            self.match(FoostacheParser.OPEN)
            self.state = 240
            self.match(FoostacheParser.END)
            self.state = 241
            self.match(FoostacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterateBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.OPEN)
            else:
                return self.getToken(FoostacheParser.OPEN, i)

        def ITERATE(self):
            return self.getToken(FoostacheParser.ITERATE, 0)

        def path(self):
            return self.getTypedRuleContext(FoostacheParser.PathContext,0)


        def indexRange(self):
            return self.getTypedRuleContext(FoostacheParser.IndexRangeContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.CLOSE)
            else:
                return self.getToken(FoostacheParser.CLOSE, i)

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def END(self):
            return self.getToken(FoostacheParser.END, 0)

        def iterateClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FoostacheParser.IterateClauseContext)
            else:
                return self.getTypedRuleContext(FoostacheParser.IterateClauseContext,i)


        def getRuleIndex(self):
            return FoostacheParser.RULE_iterateBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterateBlock" ):
                listener.enterIterateBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterateBlock" ):
                listener.exitIterateBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterateBlock" ):
                return visitor.visitIterateBlock(self)
            else:
                return visitor.visitChildren(self)




    def iterateBlock(self):

        localctx = FoostacheParser.IterateBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_iterateBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(FoostacheParser.OPEN)
            self.state = 244
            self.match(FoostacheParser.ITERATE)
            self.state = 245
            self.path()
            self.state = 246
            self.indexRange()
            self.state = 247
            self.match(FoostacheParser.CLOSE)
            self.state = 248
            self.statements()
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 249
                    self.iterateClause() 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 255
            self.match(FoostacheParser.OPEN)
            self.state = 256
            self.match(FoostacheParser.END)
            self.state = 257
            self.match(FoostacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(FoostacheParser.INTEGER, 0)

        def indexRangeB(self):
            return self.getTypedRuleContext(FoostacheParser.IndexRangeBContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_indexRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexRange" ):
                listener.enterIndexRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexRange" ):
                listener.exitIndexRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexRange" ):
                return visitor.visitIndexRange(self)
            else:
                return visitor.visitChildren(self)




    def indexRange(self):

        localctx = FoostacheParser.IndexRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_indexRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 259
                self.match(FoostacheParser.INTEGER)


            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 262
                self.indexRangeB()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexRangeBContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(FoostacheParser.COLON, 0)

        def INTEGER(self):
            return self.getToken(FoostacheParser.INTEGER, 0)

        def indexRangeC(self):
            return self.getTypedRuleContext(FoostacheParser.IndexRangeCContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_indexRangeB

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexRangeB" ):
                listener.enterIndexRangeB(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexRangeB" ):
                listener.exitIndexRangeB(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexRangeB" ):
                return visitor.visitIndexRangeB(self)
            else:
                return visitor.visitChildren(self)




    def indexRangeB(self):

        localctx = FoostacheParser.IndexRangeBContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_indexRangeB)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(FoostacheParser.COLON)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 266
                self.match(FoostacheParser.INTEGER)


            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 269
                self.indexRangeC()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexRangeCContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(FoostacheParser.COLON, 0)

        def INTEGER(self):
            return self.getToken(FoostacheParser.INTEGER, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_indexRangeC

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexRangeC" ):
                listener.enterIndexRangeC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexRangeC" ):
                listener.exitIndexRangeC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexRangeC" ):
                return visitor.visitIndexRangeC(self)
            else:
                return visitor.visitChildren(self)




    def indexRangeC(self):

        localctx = FoostacheParser.IndexRangeCContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_indexRangeC)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(FoostacheParser.COLON)
            self.state = 273
            self.match(FoostacheParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterateClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iterateBeforeClause(self):
            return self.getTypedRuleContext(FoostacheParser.IterateBeforeClauseContext,0)


        def iterateAfterClause(self):
            return self.getTypedRuleContext(FoostacheParser.IterateAfterClauseContext,0)


        def iterateBetweenClause(self):
            return self.getTypedRuleContext(FoostacheParser.IterateBetweenClauseContext,0)


        def iterateElseClause(self):
            return self.getTypedRuleContext(FoostacheParser.IterateElseClauseContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_iterateClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterateClause" ):
                listener.enterIterateClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterateClause" ):
                listener.exitIterateClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterateClause" ):
                return visitor.visitIterateClause(self)
            else:
                return visitor.visitChildren(self)




    def iterateClause(self):

        localctx = FoostacheParser.IterateClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_iterateClause)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.iterateBeforeClause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.iterateAfterClause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.iterateBetweenClause()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 278
                self.iterateElseClause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterateBeforeClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def BEFORE(self):
            return self.getToken(FoostacheParser.BEFORE, 0)

        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_iterateBeforeClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterateBeforeClause" ):
                listener.enterIterateBeforeClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterateBeforeClause" ):
                listener.exitIterateBeforeClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterateBeforeClause" ):
                return visitor.visitIterateBeforeClause(self)
            else:
                return visitor.visitChildren(self)




    def iterateBeforeClause(self):

        localctx = FoostacheParser.IterateBeforeClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_iterateBeforeClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(FoostacheParser.OPEN)
            self.state = 282
            self.match(FoostacheParser.BEFORE)
            self.state = 283
            self.match(FoostacheParser.CLOSE)
            self.state = 284
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterateAfterClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def AFTER(self):
            return self.getToken(FoostacheParser.AFTER, 0)

        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_iterateAfterClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterateAfterClause" ):
                listener.enterIterateAfterClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterateAfterClause" ):
                listener.exitIterateAfterClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterateAfterClause" ):
                return visitor.visitIterateAfterClause(self)
            else:
                return visitor.visitChildren(self)




    def iterateAfterClause(self):

        localctx = FoostacheParser.IterateAfterClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_iterateAfterClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(FoostacheParser.OPEN)
            self.state = 287
            self.match(FoostacheParser.AFTER)
            self.state = 288
            self.match(FoostacheParser.CLOSE)
            self.state = 289
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterateBetweenClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def BETWEEN(self):
            return self.getToken(FoostacheParser.BETWEEN, 0)

        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_iterateBetweenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterateBetweenClause" ):
                listener.enterIterateBetweenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterateBetweenClause" ):
                listener.exitIterateBetweenClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterateBetweenClause" ):
                return visitor.visitIterateBetweenClause(self)
            else:
                return visitor.visitChildren(self)




    def iterateBetweenClause(self):

        localctx = FoostacheParser.IterateBetweenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_iterateBetweenClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(FoostacheParser.OPEN)
            self.state = 292
            self.match(FoostacheParser.BETWEEN)
            self.state = 293
            self.match(FoostacheParser.CLOSE)
            self.state = 294
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterateElseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(FoostacheParser.OPEN, 0)

        def ELSE(self):
            return self.getToken(FoostacheParser.ELSE, 0)

        def CLOSE(self):
            return self.getToken(FoostacheParser.CLOSE, 0)

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def getRuleIndex(self):
            return FoostacheParser.RULE_iterateElseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterateElseClause" ):
                listener.enterIterateElseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterateElseClause" ):
                listener.exitIterateElseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterateElseClause" ):
                return visitor.visitIterateElseClause(self)
            else:
                return visitor.visitChildren(self)




    def iterateElseClause(self):

        localctx = FoostacheParser.IterateElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_iterateElseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(FoostacheParser.OPEN)
            self.state = 297
            self.match(FoostacheParser.ELSE)
            self.state = 298
            self.match(FoostacheParser.CLOSE)
            self.state = 299
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.filterName = None # Token

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.OPEN)
            else:
                return self.getToken(FoostacheParser.OPEN, i)

        def FILTER(self):
            return self.getToken(FoostacheParser.FILTER, 0)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(FoostacheParser.CLOSE)
            else:
                return self.getToken(FoostacheParser.CLOSE, i)

        def statements(self):
            return self.getTypedRuleContext(FoostacheParser.StatementsContext,0)


        def END(self):
            return self.getToken(FoostacheParser.END, 0)

        def ID(self):
            return self.getToken(FoostacheParser.ID, 0)

        def getRuleIndex(self):
            return FoostacheParser.RULE_filterBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterBlock" ):
                listener.enterFilterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterBlock" ):
                listener.exitFilterBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterBlock" ):
                return visitor.visitFilterBlock(self)
            else:
                return visitor.visitChildren(self)




    def filterBlock(self):

        localctx = FoostacheParser.FilterBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_filterBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(FoostacheParser.OPEN)
            self.state = 302
            self.match(FoostacheParser.FILTER)
            self.state = 303
            localctx.filterName = self.match(FoostacheParser.ID)
            self.state = 304
            self.match(FoostacheParser.CLOSE)
            self.state = 305
            self.statements()
            self.state = 306
            self.match(FoostacheParser.OPEN)
            self.state = 307
            self.match(FoostacheParser.END)
            self.state = 308
            self.match(FoostacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




