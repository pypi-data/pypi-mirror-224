import ast

from .HoleAST import iter_child_nodes


class AstWalker:
    def __init__(self, tree):
        self.tree = tree
        self._node = None
        self._set_node(tree, None)

    def _set_node(self, tree, parent):
        self._node = _Node(tree, parent)

    def next(self):
        nxt = self.next_child()
        if nxt is not None:
            return nxt

        nxt = self.next_sibling()
        if nxt is not None:
            return nxt

        nxt = self.next_parent()
        if nxt is not None:
            return nxt

        return None

    def select_specific_child(self, field):
        self._node.children = getattr(self._node.node, field, [])

    def select_body_children(self):
        children = []
        for name, vals in ast.iter_fields(self._node.node):
            if isinstance(vals, list) and len(vals) > 0 and isinstance(vals[0], ast.stmt):
                children.extend(vals)
        self._node.children = children

    def next_child(self):
        nxt = self._node.next_child()
        if nxt is None:
            return None
        self._set_node(nxt, self._node)
        return nxt

    def next_parent(self):
        parent = self._node.parent
        if parent is None:
            return None
        next_parent = parent.parent
        if next_parent is None:
            return None
        next_child = next_parent.next_child()
        while next_child is None:
            parent = next_parent
            if parent is None:
                return None
            next_parent = parent.parent
            if next_parent is None:
                return None
            next_child = next_parent.next_child()

        self._set_node(next_child, next_parent)
        return next_child

    def next_sibling(self):
        parent = self._node.parent
        if parent is None:
            return None
        next_child = parent.next_child()
        if next_child is None:
            return None
        self._set_node(next_child, parent)
        return next_child


def _is_load_store(obj):
    return not (isinstance(obj, ast.Store) or isinstance(obj, ast.Load))


class _Node:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent
        self.children = list(filter(_is_load_store, iter_child_nodes(node)))
        self.child_index = 0

    def next_child(self):
        if len(self.children) <= self.child_index:
            return None
        next_child = self.children[self.child_index]
        self.child_index += 1
        return next_child
