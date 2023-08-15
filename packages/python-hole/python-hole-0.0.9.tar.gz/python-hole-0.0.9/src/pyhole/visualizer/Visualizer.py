import pkgutil
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element

from ..PatternMatch import PatternMatch


def remove_overlap(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = []

    for start, end in sorted_intervals:
        if not merged or start > merged[-1][1]:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))

    return merged


def match_to_hml(matcher: PatternMatch, code: str, pattern: str) -> ElementTree:
    template = load_template()
    code_div = template.find(".//*[@id='code']")

    matches = {}
    patterns = {}
    for pattern_node, code_node in matcher.matches:
        if not hasattr(code_node, "lineno"):
            continue
        if not hasattr(code_node, "col_offset") or not hasattr(code_node, "end_col_offset"):
            continue

        # Add red to line
        if code_node.lineno - 1 not in matches:
            matches[code_node.lineno - 1] = []
        matches[code_node.lineno - 1].append((code_node.col_offset, code_node.end_col_offset))

        # Add pattern line
        if code_node.lineno - 1 not in patterns:
            patterns[code_node.lineno - 1] = pattern_node

    code_line = code.splitlines(False)
    for i, line in enumerate(code_line):
        pre = ET.SubElement(code_div, "pre")

        if i in matches:
            start = 0
            match_i = remove_overlap(matches[i])
            for match in remove_overlap(match_i):
                text = ET.SubElement(pre, "span")
                text.text = line[start:match[0]]
                b = ET.SubElement(pre, "b")
                b.text = line[match[0]:match[1]]
                start = match[1]
            text = ET.SubElement(pre, 'span')
            text.text = line[start:]
        else:
            pre.text = line

    pattern_line = pattern.splitlines(False)
    pattern_div = template.find(".//*[@id='pattern']")
    for i, _ in enumerate(code_line):
        pre = ET.SubElement(pattern_div, "pre")

        text = ""
        if i in matcher.pattern_match:
            line = matcher.pattern_match[i].lineno
            txt = pattern_line[line - 1]
            text += txt
        else:
            text += '\t'

        if i + 1 in matcher.line_skip_matches:
            text += "{"

        if i + 1 in matcher.line_skip_matches.values():
            text += "}"

        pre.text = text

    return ElementTree(template)


def __str_to_pre(string):
    pre = ET.Element("pre")
    pre.text = string
    return pre


def load_template() -> Element:
    data = pkgutil.get_data(__name__, "template.html")
    template = ET.fromstring(data)
    return template
