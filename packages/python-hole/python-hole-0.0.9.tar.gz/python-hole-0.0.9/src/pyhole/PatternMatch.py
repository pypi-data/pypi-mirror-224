from .HoleAST import HoleAST


class PatternMatch:
    def __init__(self):
        self.matches = []
        self.line_skip_matches = {}
        self.pattern_match = {}
        self.links: list[Link] = []

    def add_match(self, pattern, code):
        self.matches.append((pattern, code))

    def add_line_skip_match(self, start, end):
        self.line_skip_matches[start] = end

    def add_pattern_match(self, line, pattern):
        self.pattern_match[line-1] = pattern

    def match(self, code, pattern):
        self.links.append(Link(code, pattern))


class Link:
    def __init__(self, code_node, pattern_node):
        self._code_node = code_node
        self._pattern_node = pattern_node

    @property
    def code_node(self):
        return self._code_node

    @property
    def pattern_node(self):
        return self._pattern_node

    @property
    def code_line(self):
        if hasattr(self._code_node, "lineno"):
            return self._code_node.lineno
        return None

    @property
    def pattern_line(self):
        if hasattr(self._pattern_node, "lineno"):
            return self._pattern_node.lineno

    def __str__(self):
        if isinstance(self._pattern_node, HoleAST):
            return f"({type(self._code_node).__name__}, {self._pattern_node})"
        else:
            return f"({type(self._code_node).__name__}, {type(self._pattern_node).__name__})"

    def __repr__(self):
        return repr(str(self))
