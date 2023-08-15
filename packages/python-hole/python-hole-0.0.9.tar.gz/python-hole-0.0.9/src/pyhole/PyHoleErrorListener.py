from antlr4.error.ErrorListener import ErrorListener


class Python3ErrorListener(ErrorListener):
    def __init__(self, output):
        self.output = output
        self._symbol = ''
        self._line = -1

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offending_symbol.text
        self._line = line
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        
    @property
    def symbol(self):
        return self._symbol

    @property
    def line(self):
        return self._line
