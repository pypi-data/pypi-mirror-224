# Generated from Python3.g4 by ANTLR 4.7.2

import re
from ast import *

from .HoleAST import *
from .antlr.Python3Parser import Python3Parser
from .antlr.Python3Visitor import Python3Visitor

# Bind operator to their classes
operators = {
    'and': And,
    'or': Or,
    '+': UAdd,
    '-': USub,
    '*': Mult,
    '@': MatMult,
    '/': Div,
    '%': Mod,
    '**': Pow,
    '<<': LShift,
    '>>': RShift,
    '|': BitOr,
    '^': BitXor,
    '&': BitAnd,
    '//': FloorDiv,
    '~': Invert,
    'not': Not,
    '==': Eq,
    '!=': NotEq,
    '<': Lt,
    '<=': LtE,
    '>': Gt,
    '>=': GtE,
    'is': Is,
    'is not': IsNot,
    'in': In,
    'not in': NotIn,
    '+=': Add,
    '-=': Sub,
    '*=': Mult,
    '@=': MatMult,
    '/=': Div,
    '%=': Mod,
    '&=': BitAnd,
    '|=': BitOr,
    '^=': BitXor,
    '<<=': LShift,
    '>>=': RShift,
    '**=': Pow,
    '//=': FloorDiv
}


def set_lineno(obj, ctx):
    start = ctx.start.line
    end = ctx.stop.line
    if isinstance(obj, (stmt, HoleAST)):
        obj.lineno = start
        obj.lineno_end = end


# This class defines a complete generic visitor for a parse tree produced by Python3Parser.

class PyHoleVisitor(Python3Visitor):

    def __init__(self):
        super().__init__()
        self.context = Load()

    def aggregateResult(self, aggregate, next_result):
        if aggregate is None:
            return next_result
        elif isinstance(aggregate, list):
            aggregate.append(next_result)
            return aggregate
        elif next_result is None:
            return aggregate
        else:
            return [aggregate, next_result]

    def visitChildren(self, ctx):
        children = super().visitChildren(ctx)
        if not isinstance(children, list):
            set_lineno(children, ctx)
        # print(type(ctx).__name__ + " " + str(children))
        return children

    # Visit a parse tree produced by Python3Parser#single_input.
    def visitSingle_input(self, ctx: Python3Parser.Single_inputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#file_input.
    def visitFile_input(self, ctx: Python3Parser.File_inputContext):
        body = []
        stmts = ctx.stmt()
        n = len(stmts)
        for i in range(n):
            c = stmts[i]
            child_result = c.accept(self)
            body.append(child_result)

        return Module(body, [])

    # Visit a parse tree produced by Python3Parser#eval_input.
    def visitEval_input(self, ctx: Python3Parser.Eval_inputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#decorator.
    def visitDecorator(self, ctx: Python3Parser.DecoratorContext):
        name = ctx.dotted_name().accept(self)
        if '.' in name:
            name = name.split('.')
            attr = name.pop()
            while len(name) > 0:
                attr = Attribute(Name(name.pop(), self.context), attr, self.context)
            name = attr
        if ctx.OPEN_PAREN() is not None:
            args = ctx.arglist().accept(self) if ctx.arglist() is not None else []
            return Call(name, args, [])
        return Name(name, self.context)

    # Visit a parse tree produced by Python3Parser#decorators.
    def visitDecorators(self, ctx: Python3Parser.DecoratorsContext):
        return list(map(lambda x: x.accept(self), ctx.decorator()))

    # Visit a parse tree produced by Python3Parser#decorated.
    def visitDecorated(self, ctx: Python3Parser.DecoratedContext):
        decorator = ctx.decorators().accept(self)
        decorated = ctx.getChild(1).accept(self)
        decorated.decorator_list = decorator
        return decorated

    # Visit a parse tree produced by Python3Parser#async_funcdef.
    def visitAsync_funcdef(self, ctx: Python3Parser.Async_funcdefContext):
        funcdef = ctx.funcdef()
        name = funcdef.NAME().accept(self)
        args = funcdef.parameters().accept(self)
        returns = funcdef.test().accept(self) if funcdef.test() is not None else None
        suite = funcdef.suite().accept(self)

        return AsyncFunctionDef(name, args, suite, [], returns=returns)

    # Visit a parse tree produced by Python3Parser#funcdef.
    def visitFuncdef(self, ctx: Python3Parser.FuncdefContext):
        if ctx.NAME() is not None:
            name = ctx.NAME().accept(self)
        else:
            name = ctx.simple_hole().accept(self)
        args = ctx.parameters().accept(self)

        returns = ctx.test().accept(self) if ctx.test() is not None else None

        suite = ctx.suite().accept(self)

        return FunctionDef(name, args, suite, [], returns=returns)

    # Visit a parse tree produced by Python3Parser#parameters.
    def visitParameters(self, ctx: Python3Parser.ParametersContext):
        args = ctx.typedargslist()
        return args.accept(self) if args is not None else arguments(posonlyargs=[], args=[], kwonlyargs=[],
                                                                    kw_defaults=[], defaults=[])

    # Visit a parse tree produced by Python3Parser#typedargslist.
    def visitTypedargslist(self, ctx: Python3Parser.TypedargslistContext):
        args = []
        defaults = []
        kwonlyargs = []
        kw_defaults = []
        vararg = None
        kwarg = None
        kw = False

        childs = list(ctx.getChildren())
        while len(childs) > 0:
            c = childs.pop(0)
            if type(c).__name__ == 'TfpdefContext':
                kwonlyargs.append(c.accept(self))
                if kw:
                    kw_defaults.append(None)
            elif type(c).__name__ == 'TestContext':
                if kw:
                    kw_defaults.pop()
                kw_defaults.append(c.accept(self))
            elif c.accept(self) == '*':
                kw = True
                vararg = childs.pop(0).accept(self)
                if vararg == ',':
                    vararg = None
                args = kwonlyargs[::]
                defaults = kw_defaults[::]
                kwonlyargs = []
                kw_defaults = []

            elif c.accept(self) == '**':
                kwarg = childs.pop(0).accept(self)

        if not kw:
            args = kwonlyargs[::]
            defaults = kw_defaults[::]
            kwonlyargs = []
            kw_defaults = []

        return arguments(posonlyargs=[], args=args, vararg=vararg, kwonlyargs=kwonlyargs, kw_defaults=kw_defaults,
                         kwarg=kwarg, defaults=defaults)

    # Visit a parse tree produced by Python3Parser#tfpdef.
    def visitTfpdef(self, ctx: Python3Parser.TfpdefContext):
        if ctx.expr_hole() is not None:
            return ctx.expr_hole().accept(self)
        val = ctx.NAME().accept(self)
        type_val = ctx.test().accept(self) if ctx.test() is not None else None
        return arg(val, annotation=type_val)

    # Visit a parse tree produced by Python3Parser#varargslist.
    def visitVarargslist(self, ctx: Python3Parser.VarargslistContext):
        args = []
        defaults = []
        kwonlyargs = []
        kw_defaults = []
        vararg = None
        kwarg = None
        kw = False

        childs = list(ctx.getChildren())
        while len(childs) > 0:
            c = childs.pop(0)
            if type(c).__name__ == 'VfpdefContext':
                kwonlyargs.append(c.accept(self))
                if kw:
                    kw_defaults.append(None)
            elif type(c).__name__ == 'TestContext':
                if kw:
                    kw_defaults.pop()
                kw_defaults.append(c.accept(self))
            elif c.accept(self) == '*':
                kw = True
                vararg = childs.pop(0).accept(self)
                if vararg == ',':
                    vararg = None
                args = kwonlyargs[::]
                defaults = kw_defaults[::]
                kwonlyargs = []
                kw_defaults = []

            elif c.accept(self) == '**':
                kwarg = childs.pop(0).accept(self)

        if not kw:
            args = kwonlyargs[::]
            defaults = kw_defaults[::]
            kwonlyargs = []
            kw_defaults = []

        return arguments(posonlyargs=[], args=args, vararg=vararg, kwonlyargs=kwonlyargs, kw_defaults=kw_defaults,
                         kwarg=kwarg, defaults=defaults)

    # Visit a parse tree produced by Python3Parser#vfpdef.
    def visitVfpdef(self, ctx: Python3Parser.VfpdefContext):
        return arg(ctx.NAME().accept(self))

    # Visit a parse tree produced by Python3Parser#stmt.
    def visitStmt(self, ctx: Python3Parser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#simple_stmt.
    def visitSimple_stmt(self, ctx: Python3Parser.Simple_stmtContext):
        vals = list(map(lambda x: x.accept(self), ctx.small_stmt()))
        return vals if len(vals) > 1 else vals[0]

    # Visit a parse tree produced by Python3Parser#small_stmt.
    def visitSmall_stmt(self, ctx: Python3Parser.Small_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#expr_stmt.
    def visitExpr_stmt(self, ctx: Python3Parser.Expr_stmtContext):

        if ctx.ASSIGN(0) is not None:
            targets = self.visitChildren(ctx)
            value = targets.pop()
            targets = list(filter(lambda x: x != '=', targets))
            return Assign(targets, value)

        target = ctx.testlist_star_expr(0).accept(self)

        if ctx.annassign() is not None:
            values = ctx.annassign().accept(self)
            if len(values) == 1:
                return AnnAssign(target, values[0])
            else:
                return AnnAssign(target, values[0], values[1])

        if ctx.augassign() is not None:
            op = ctx.augassign().accept(self)
            val = ctx.getChild(2).accept(self)
            return AugAssign(target, op, val)

        return Expr(target)

    # Visit a parse tree produced by Python3Parser#annassign.
    def visitAnnassign(self, ctx: Python3Parser.AnnassignContext):
        values = []
        tests = ctx.test()

        for i in range(len(tests)):
            c = tests[i]
            child_result = c.accept(self)
            values.append(child_result)

        return values

    # Visit a parse tree produced by Python3Parser#testlist_star_expr.
    def visitTestlist_star_expr(self, ctx: Python3Parser.Testlist_star_exprContext):
        values = self.visitChildren(ctx)
        if not isinstance(values, list):
            return values
        values = list(filter(lambda x: x != ',', values))
        return Tuple(values, self.context)

    # Visit a parse tree produced by Python3Parser#augassign.
    def visitAugassign(self, ctx: Python3Parser.AugassignContext):
        op = ctx.getChild(0).accept(self)
        clazz = operators[op]

        return clazz()

    # Visit a parse tree produced by Python3Parser#del_stmt.
    def visitDel_stmt(self, ctx: Python3Parser.Del_stmtContext):
        self.context = Del()
        exprs = ctx.exprlist().accept(self)
        if not isinstance(exprs, Tuple):
            exprs = [exprs]
        else:
            exprs = exprs.elts
        self.context = Load()
        return Delete(exprs)

    # Visit a parse tree produced by Python3Parser#pass_stmt.
    def visitPass_stmt(self, ctx: Python3Parser.Pass_stmtContext):
        return Pass()

    # Visit a parse tree produced by Python3Parser#flow_stmt.
    def visitFlow_stmt(self, ctx: Python3Parser.Flow_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#break_stmt.
    def visitBreak_stmt(self, ctx: Python3Parser.Break_stmtContext):
        return Break()

    # Visit a parse tree produced by Python3Parser#continue_stmt.
    def visitContinue_stmt(self, ctx: Python3Parser.Continue_stmtContext):
        return Continue()

    # Visit a parse tree produced by Python3Parser#return_stmt.
    def visitReturn_stmt(self, ctx: Python3Parser.Return_stmtContext):
        if ctx.testlist() is None:
            return Return()
        value = ctx.testlist().accept(self)
        return Return(value)

    # Visit a parse tree produced by Python3Parser#yield_stmt.
    def visitYield_stmt(self, ctx: Python3Parser.Yield_stmtContext):
        value = ctx.yield_expr().accept(self)
        return Expr(value)

    # Visit a parse tree produced by Python3Parser#raise_stmt.
    def visitRaise_stmt(self, ctx: Python3Parser.Raise_stmtContext):
        tests = ctx.test()
        if len(tests) == 0:
            return Raise()
        exc = tests[0].accept(self)
        if len(tests) == 2:
            cause = tests[1].accept(self)
            return Raise(exc, cause)

        return Raise(exc)

    # Visit a parse tree produced by Python3Parser#import_stmt.
    def visitImport_stmt(self, ctx: Python3Parser.Import_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#import_name.
    def visitImport_name(self, ctx: Python3Parser.Import_nameContext):
        names = ctx.dotted_as_names().accept(self)
        return Import(names)

    # Visit a parse tree produced by Python3Parser#import_from.
    def visitImport_from(self, ctx: Python3Parser.Import_fromContext):
        module = ctx.dotted_name().accept(self)
        import_as = ctx.import_as_names()
        names = import_as.accept(self) if import_as is not None else [alias("*")]
        return ImportFrom(module, names, 0)

    # Visit a parse tree produced by Python3Parser#import_as_name.
    def visitImport_as_name(self, ctx: Python3Parser.Import_as_nameContext):
        names = ctx.NAME()
        name = names[0].accept(self)
        if len(names) == 2:
            al = names[1].accept(self)
            return alias(name, al)
        return alias(name)

    # Visit a parse tree produced by Python3Parser#dotted_as_name.
    def visitDotted_as_name(self, ctx: Python3Parser.Dotted_as_nameContext):
        name = ctx.dotted_name().accept(self)
        asname_node = ctx.NAME()
        if asname_node is not None:
            asname = asname_node.accept(self)
            return alias(name, asname)
        return alias(name)

    # Visit a parse tree produced by Python3Parser#import_as_names.
    def visitImport_as_names(self, ctx: Python3Parser.Import_as_namesContext):
        return list(map(lambda x: x.accept(self), ctx.import_as_name()))

    # Visit a parse tree produced by Python3Parser#dotted_as_names.
    def visitDotted_as_names(self, ctx: Python3Parser.Dotted_as_namesContext):
        return list(map(lambda x: x.accept(self), ctx.dotted_as_name()))

    # Visit a parse tree produced by Python3Parser#dotted_name.
    def visitDotted_name(self, ctx: Python3Parser.Dotted_nameContext):
        names = list(map(lambda x: x.accept(self), ctx.NAME()))
        return '.'.join(names)

    # Visit a parse tree produced by Python3Parser#global_stmt.
    def visitGlobal_stmt(self, ctx: Python3Parser.Global_stmtContext):
        names = []
        name = ctx.NAME()
        for i in range(len(name)):
            c = name[i]
            child_result = c.accept(self)
            names.append(child_result)

        return Global(names)

    # Visit a parse tree produced by Python3Parser#nonlocal_stmt.
    def visitNonlocal_stmt(self, ctx: Python3Parser.Nonlocal_stmtContext):
        names = []
        name = ctx.NAME()
        for i in range(len(name)):
            c = name[i]
            child_result = c.accept(self)
            names.append(child_result)

        return Nonlocal(names)

    # Visit a parse tree produced by Python3Parser#assert_stmt.
    def visitAssert_stmt(self, ctx: Python3Parser.Assert_stmtContext):
        tests = ctx.test()
        test = tests[0].accept(self)
        if len(tests) == 2:
            msg = tests[1].accept(self)
            return Assert(test, msg)
        return Assert(test)

    # Visit a parse tree produced by Python3Parser#compound_stmt.
    def visitCompound_stmt(self, ctx: Python3Parser.Compound_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#async_stmt.
    def visitAsync_stmt(self, ctx: Python3Parser.Async_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#if_stmt.
    def visitIf_stmt(self, ctx: Python3Parser.If_stmtContext):
        tests = ctx.test()
        suites = ctx.suite()
        if len(suites) > len(tests):
            cur_suite = suites.pop().accept(self)
        else:
            cur_suite = []
        while len(tests) > 0:
            cur_test = tests.pop().accept(self)
            body = suites.pop().accept(self)
            ifstmt = If(cur_test, body, cur_suite)
            cur_suite = [ifstmt]

        return cur_suite[0]

    # Visit a parse tree produced by Python3Parser#while_stmt.
    def visitWhile_stmt(self, ctx: Python3Parser.While_stmtContext):
        test = ctx.test().accept(self)
        suite = ctx.suite(0).accept(self)

        if ctx.ELSE() is None:
            return While(test, suite, [])

        else_body = ctx.suite(1).accept(self)
        return While(test, suite, else_body)

    # Visit a parse tree produced by Python3Parser#for_stmt.
    def visitFor_stmt(self, ctx: Python3Parser.For_stmtContext):
        target = ctx.exprlist().accept(self)
        ite = ctx.testlist().accept(self)
        body = ctx.suite(0).accept(self)
        orelse = ctx.suite(1).accept(self) if ctx.suite(1) is not None else []
        return For(target, ite, body, orelse)

    # Visit a parse tree produced by Python3Parser#try_stmt.
    def visitTry_stmt(self, ctx: Python3Parser.Try_stmtContext):
        suites = ctx.suite()
        suites.reverse()
        body = suites.pop().accept(self)

        handlers = []
        clauses = ctx.except_clause()
        for i in range(len(clauses)):
            c = clauses[i]
            child_result = c.accept(self)
            handler = child_result
            handler.body = suites.pop().accept(self)
            handlers.append(handler)

        if len(handlers) == 0:
            final = suites.pop().accept(self)
            return Try(body, handlers, [], final)

        if len(suites) == 0:
            return Try(body, handlers, [], [])

        next_body = suites.pop().accept(self)
        if ctx.ELSE() is None:
            return Try(body, handlers, [], next_body)
        elif ctx.FINALLY() is None:
            return Try(body, handlers, next_body, [])
        else:
            final_body = suites.pop().accept(self)
            return Try(body, handlers, next_body, final_body)

    # Visit a parse tree produced by Python3Parser#with_stmt.
    def visitWith_stmt(self, ctx: Python3Parser.With_stmtContext):
        items = list(map(lambda x: x.accept(self), ctx.with_item()))
        body = ctx.suite().accept(self)
        return With(items, body)

    # Visit a parse tree produced by Python3Parser#with_item.
    def visitWith_item(self, ctx: Python3Parser.With_itemContext):
        ctx_expr = ctx.test().accept(self)
        if ctx.expr() is None:
            return withitem(ctx_expr)

        opt_vars = ctx.expr().accept(self)
        return withitem(ctx_expr, opt_vars)

    # Visit a parse tree produced by Python3Parser#except_clause.
    def visitExcept_clause(self, ctx: Python3Parser.Except_clauseContext):
        if ctx.test() is None:
            return ExceptHandler()

        test = ctx.test().accept(self)
        if ctx.NAME() is None:
            return ExceptHandler(test)

        name = ctx.NAME().accept(self)
        return ExceptHandler(test, name)

    # Visit a parse tree produced by Python3Parser#suite.
    def visitSuite(self, ctx: Python3Parser.SuiteContext):
        if ctx.simple_stmt() is not None:
            stmt = ctx.simple_stmt().accept(self)
            return stmt if isinstance(stmt, list) else [stmt]

        body = []
        stmts = ctx.stmt()
        for i in range(len(stmts)):
            c = stmts[i]
            child_result = c.accept(self)
            if child_result is not None:
                if isinstance(child_result, list):
                    body.extend(child_result)
                else:
                    body.append(child_result)
            else:
                print(type(c))

        return body

    # Visit a parse tree produced by Python3Parser#tests.
    def visitTest(self, ctx: Python3Parser.TestContext):
        if ctx.IF() is not None:
            body = ctx.or_test(0).accept(self)
            test = ctx.or_test(1).accept(self)
            orelse = ctx.test().accept(self)
            return IfExp(test, body, orelse)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#test_nocond.
    def visitTest_nocond(self, ctx: Python3Parser.Test_nocondContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#lambdef.
    def visitLambdef(self, ctx: Python3Parser.LambdefContext):
        args = ctx.varargslist()
        args = args.accept(self) if args is not None else arguments([], [], None, [], [], None, [])
        body = ctx.test().accept(self)
        return Lambda(args, body)

    # Visit a parse tree produced by Python3Parser#lambdef_nocond.
    def visitLambdef_nocond(self, ctx: Python3Parser.Lambdef_nocondContext):
        args = ctx.varargslist().accept(self)
        body = ctx.test_nocond().accept(self)
        return Lambda(args, body)

    # Visit a parse tree produced by Python3Parser#or_test.
    def visitOr_test(self, ctx: Python3Parser.Or_testContext):
        ors = ctx.and_test()
        n = len(ors)
        if n == 1:
            return self.visitChildren(ctx)

        vals = list(map(lambda x: x.accept(self), ors))
        return BoolOp(Or(), vals)

    # Visit a parse tree produced by Python3Parser#and_test.
    def visitAnd_test(self, ctx: Python3Parser.And_testContext):
        ands = ctx.not_test()
        n = len(ands)
        if n == 1:
            return self.visitChildren(ctx)

        vals = list(map(lambda x: x.accept(self), ands))
        return BoolOp(And(), vals)

    # Visit a parse tree produced by Python3Parser#not_test.
    def visitNot_test(self, ctx: Python3Parser.Not_testContext):
        test = ctx.not_test()
        if test is None:
            return self.visitChildren(ctx)
        return UnaryOp(Not(), test.accept(self))

    # Visit a parse tree produced by Python3Parser#comparison.
    def visitComparison(self, ctx: Python3Parser.ComparisonContext):
        exprs = ctx.expr()
        if len(exprs) == 1:
            return self.visitChildren(ctx)

        tests = ctx.comp_op()
        test = []
        expr = []
        n = len(tests)
        for i in range(n):
            c = tests[i]
            child_result = c.accept(self)
            test.append(child_result)

            c = exprs[i + 1]
            child_result = c.accept(self)
            expr.append(child_result)

        left = exprs[0].accept(self)

        return Compare(left, test, expr)

    # Visit a parse tree produced by Python3Parser#comp_op.
    def visitComp_op(self, ctx: Python3Parser.Comp_opContext):
        op = self.visitChildren(ctx)
        if isinstance(op, list):
            op = ' '.join(op)
        clazz = operators[op]

        return clazz()

    # Visit a parse tree produced by Python3Parser#star_expr.
    def visitStar_expr(self, ctx: Python3Parser.Star_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#expr.
    def visitExpr(self, ctx: Python3Parser.ExprContext):
        expr = ctx.xor_expr()
        if len(expr) == 1:
            return self.visitChildren(ctx)

        left = expr.pop(0).accept(self)
        while len(expr) > 0:
            right = expr.pop(0).accept(self)
            left = BinOp(left, BitOr(), right)

        return left

    # Visit a parse tree produced by Python3Parser#xor_expr.
    def visitXor_expr(self, ctx: Python3Parser.Xor_exprContext):
        expr = ctx.and_expr()
        if len(expr) == 1:
            return self.visitChildren(ctx)

        left = expr.pop(0).accept(self)
        while len(expr) > 0:
            right = expr.pop(0).accept(self)
            left = BinOp(left, BitXor(), right)

        return left

    # Visit a parse tree produced by Python3Parser#and_expr.
    def visitAnd_expr(self, ctx: Python3Parser.And_exprContext):
        expr = ctx.shift_expr()
        if len(expr) == 1:
            return self.visitChildren(ctx)

        left = expr.pop(0).accept(self)
        while len(expr) > 0:
            right = expr.pop(0).accept(self)
            left = BinOp(left, BitAnd(), right)

        return left

    def visitMulti_expr(self, ctx):
        children = list(ctx.getChildren())
        left = children.pop(0).accept(self)
        while len(children) > 0:
            op_sign = children.pop(0).accept(self)
            op = operators.get(op_sign)()
            right = children.pop(0).accept(self)
            left = BinOp(left, op, right)

        return left

    # Visit a parse tree produced by Python3Parser#shift_expr.
    def visitShift_expr(self, ctx: Python3Parser.Shift_exprContext):
        return self.visitMulti_expr(ctx)

    # Visit a parse tree produced by Python3Parser#arith_expr.
    def visitArith_expr(self, ctx: Python3Parser.Arith_exprContext):
        children = list(ctx.getChildren())
        left = children.pop(0).accept(self)
        while len(children) > 0:
            op_sign = children.pop(0).accept(self)
            op = Add() if op_sign == "+" else Sub()
            right = children.pop(0).accept(self)
            left = BinOp(left, op, right)

        return left

    # Visit a parse tree produced by Python3Parser#term.
    def visitTerm(self, ctx: Python3Parser.TermContext):
        return self.visitMulti_expr(ctx)

    # Visit a parse tree produced by Python3Parser#factor.
    def visitFactor(self, ctx: Python3Parser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        op_sign = ctx.getChild(0).accept(self)
        op = operators.get(op_sign)()
        expr = ctx.getChild(1).accept(self)

        return UnaryOp(op, expr)

    # Visit a parse tree produced by Python3Parser#power.
    def visitPower(self, ctx: Python3Parser.PowerContext):
        return self.visitMulti_expr(ctx)

    # Visit a parse tree produced by Python3Parser#atom_expr.
    def visitAtom_expr(self, ctx: Python3Parser.Atom_exprContext):
        ret = ctx.atom().accept(self)

        trailers = ctx.trailer()
        for i in range(len(trailers)):
            trail = trailers[i].accept(self)

            if isinstance(trail, Call):
                trail.func = ret
                ret = trail
            else:
                trail.value = ret
                ret = trail

        return ret

    @staticmethod
    def replace_escaped_chars(string):
        # Define a dictionary mapping escaped characters to their corresponding values
        escape_dict = {
            "\\n": "\n",
            "\\r": "\r",
            "\\t": "\t",
            "\\\\": "\\",
            "\\'": "'",
            '\\"': '"'
            # Add more escape sequences here as needed
        }
        # Create a regular expression pattern that matches any escaped character
        escape_pattern = re.compile("|".join(re.escape(key) for key in escape_dict.keys()))
        # Replace all escaped characters with their corresponding values
        return escape_pattern.sub(lambda match: escape_dict[match.group()], string)

    def cleanup_string(self, string):
        # remove potential '\' at the end of each line
        regex = r"\\\n"
        string = re.sub(regex, "", string, 0, re.MULTILINE)

        if string.startswith('"""') or string.startswith("'''"):
            string = string[3:-3]
            string = self.replace_escaped_chars(string)
        elif string.startswith('"') or string.startswith("'"):
            string = string[1:-1]
            string = self.replace_escaped_chars(string)
        elif string.startswith('b'):
            string = string[2:-1]
            string = bytes(string, 'utf-8')

        return string

    # Visit a parse tree produced by Python3Parser#atom.
    def visitAtom(self, ctx: Python3Parser.AtomContext):
        if ctx.NAME() is not None:
            return Name(ctx.NAME().accept(self), self.context)

        if ctx.NUMBER() is not None:
            num = ctx.NUMBER().accept(self).lower()
            if '.' in num or 'e' in num:
                return Constant(float(num))
            base = 10
            if len(num) > 2 and num[0] == '0':
                b = num[1]
                if b == 'b':
                    base = 2
                elif b == 'o':
                    base = 8
                elif b == 'x':
                    base = 16
            return Constant(int(num, base))

        if len(ctx.STRING()) > 0:
            if len(ctx.STRING()) == 1:
                string = ctx.STRING(0).accept(self)
                string = self.cleanup_string(string)
            else:
                strings = [self.cleanup_string(s.accept(self)) for s in ctx.STRING()]
                string = ''.join(strings)

            return Constant(string)

        if ctx.ELLIPSIS() is not None:
            return Constant(...)

        if ctx.NONE() is not None:
            return Constant(None)

        if ctx.TRUE() is not None:
            return Constant(True)

        if ctx.FALSE() is not None:
            return Constant(False)

        if ctx.OPEN_PAREN() is not None:
            if ctx.testlist_comp() is not None:
                val = ctx.testlist_comp().accept(self)
                if isinstance(val, List):
                    val = val.elts
                elif isinstance(val, ListComp):
                    return GeneratorExp(elt=val.elt, generators=val.generators)
            elif ctx.yield_expr() is not None:
                val = ctx.yield_expr().accept(self)
            else:
                val = []
            if isinstance(val, list):
                return Tuple(elts=val, ctx=self.context)
            return val

        if ctx.OPEN_BRACK() is not None:
            val = ctx.testlist_comp().accept(self) if ctx.testlist_comp() is not None else List(elts=[],
                                                                                                ctx=self.context)
            if not isinstance(val, List) and not isinstance(val, ListComp):
                val = List(elts=[val], ctx=self.context)
            return val

        if ctx.OPEN_BRACE() is not None:
            val = ctx.dictorsetmaker().accept(self) if ctx.dictorsetmaker() is not None else Dict(keys=[], values=[])
            return val

        return self.visitChildren(ctx)

    # Visit a parse tree pro duced by Python3Parser#testlist_comp.
    def visitTestlist_comp(self, ctx: Python3Parser.Testlist_compContext):
        if ctx.comp_for() is not None:
            comp = ctx.comp_for().accept(self)
            elt = ctx.getChild(0).accept(self)
            return ListComp(elt=elt, generators=comp)
        vals = self.visitChildren(ctx)
        if isinstance(vals, list):
            vals = list(filter(lambda x: x != ',', vals))
            return List(elts=vals, ctx=self.context)
        return vals

    # Visit a parse tree produced by Python3Parser#trailer.
    def visitTrailer(self, ctx: Python3Parser.TrailerContext):
        if ctx.subscriptlist() is not None:
            val = ctx.subscriptlist().accept(self)
            return Subscript(value=None, slice=val, ctx=self.context)

        if ctx.NAME() is not None:
            val = ctx.NAME().accept(self)
            return Attribute(value=None, attr=val, ctx=self.context)

        if ctx.arglist() is not None:
            allargs = ctx.arglist().accept(self)

            # Filter args and keywords
            keywords = list(filter(lambda x: isinstance(x, keyword), allargs))
            args = list(filter(lambda x: x not in keywords, allargs))

            return Call(args=args, keywords=keywords)

        return Call(args=[], keywords=[])

    # Visit a parse tree produced by Python3Parser#subscriptlist.
    def visitSubscriptlist(self, ctx: Python3Parser.SubscriptlistContext):
        if ctx.getChildCount() > 1:
            return Tuple(list(map(lambda x: x.accept(self), ctx.subscript())), self.context)
        else:
            return ctx.subscript(0).accept(self)

    # Visit a parse tree produced by Python3Parser#subscript.
    def visitSubscript(self, ctx: Python3Parser.SubscriptContext):
        if ctx.COLON() is not None:
            lower = None
            step = ctx.sliceop().accept(self) if ctx.sliceop() is not None else None

            if ctx.getChild(0) == ctx.test(0):
                lower = ctx.test(0).accept(self)
                upper = ctx.test(1).accept(self) if len(ctx.test()) > 1 else None
            else:
                upper = ctx.test(0).accept(self) if len(ctx.test()) > 0 else None

            return Slice(lower=lower, upper=upper, step=step)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#sliceop.
    def visitSliceop(self, ctx: Python3Parser.SliceopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#exprlist.
    def visitExprlist(self, ctx: Python3Parser.ExprlistContext):
        vals = self.visitChildren(ctx)
        if isinstance(vals, list):
            vals = list(filter(lambda x: x != ',', vals))
            return Tuple(elts=vals, ctx=self.context)
        return vals

    # Visit a parse tree produced by Python3Parser#testlist.
    def visitTestlist(self, ctx: Python3Parser.TestlistContext):
        vals = list(map(lambda x: x.accept(self), ctx.test()))
        return Tuple(vals, self.context) if len(vals) > 1 else vals[0]

    # Visit a parse tree produced by Python3Parser#dictorsetmaker.
    def visitDictorsetmaker(self, ctx: Python3Parser.DictorsetmakerContext):
        if len(ctx.COLON()) > 0:
            # we have a dict
            if ctx.comp_for() is not None:
                # we have a dict comprehension
                comp = ctx.comp_for().accept(self)
                keys = ctx.test(0).accept(self)
                values = ctx.test(1).accept(self)
                return DictComp(key=keys, value=values, generators=comp)

            tests = list(map(lambda x: x.accept(self), ctx.test()))
            keys = tests[::2]
            values = tests[1::2]
            return Dict(keys=keys, values=values)
        else:
            # we have a set
            if ctx.comp_for() is not None:
                # we have a set comprehension
                comp = ctx.comp_for().accept(self)
                elt = ctx.test().accept(self)
                return SetComp(elt=elt, generators=comp)

            vals = self.visitChildren(ctx)
            if not isinstance(vals, list):
                vals = [vals]
            else:
                vals = list(filter(lambda x: x != ',', vals))
            return Set(elts=vals)

    # Visit a parse tree produced by Python3Parser#classdef.
    def visitClassdef(self, ctx: Python3Parser.ClassdefContext):
        name = ctx.NAME().accept(self)
        args = ctx.arglist()
        args = args.accept(self) if args is not None else []
        body = ctx.suite().accept(self)
        return ClassDef(name, args, [], body, [])

    # Visit a parse tree produced by Python3Parser#arglist.
    def visitArglist(self, ctx: Python3Parser.ArglistContext):
        return list(map(lambda x: x.accept(self), ctx.argument()))

    # Visit a parse tree produced by Python3Parser#argument.
    def visitArgument(self, ctx: Python3Parser.ArgumentContext):
        if ctx.STAR() is not None:
            return Starred(value=ctx.test(0).accept(self), ctx=self.context)

        if ctx.POWER() is not None:
            return keyword(value=ctx.test(0).accept(self))

        if ctx.ASSIGN() is not None:
            key = ctx.test(0).accept(self)
            key = key.id if isinstance(key, Name) else key.value
            return keyword(arg=key, value=ctx.test(1).accept(self))

        if ctx.comp_for() is not None:
            generator = ctx.comp_for().accept(self)
            elt = ctx.test(0).accept(self)
            return GeneratorExp(elt=elt, generators=generator)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#comp_iter.
    def visitComp_iter(self, ctx: Python3Parser.Comp_iterContext):
        vals = self.visitChildren(ctx)
        return vals

    # Visit a parse tree produced by Python3Parser#comp_for.
    def visitComp_for(self, ctx: Python3Parser.Comp_forContext):
        target = ctx.exprlist().accept(self)
        iter_val = ctx.or_test().accept(self)
        is_async = 1 if ctx.ASYNC() is not None else 0

        ret = []
        ifs = []
        next_comp = ctx.comp_iter()
        if next_comp is not None:
            next_comp = next_comp.accept(self)
            for comp in next_comp:
                if isinstance(comp, comprehension):
                    ret.append(comp)
                else:
                    ifs.append(comp)
        return [comprehension(target=target, iter=iter_val, ifs=ifs, is_async=is_async)] + ret

    # Visit a parse tree produced by Python3Parser#comp_if.
    def visitComp_if(self, ctx: Python3Parser.Comp_ifContext):
        test = ctx.test_nocond().accept(self)
        next_comp = ctx.comp_iter().accept(self) if ctx.comp_iter() is not None else []

        return [test] + next_comp

    # Visit a parse tree produced by Python3Parser#encoding_decl.
    def visitEncoding_decl(self, ctx: Python3Parser.Encoding_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#yield_expr.
    def visitYield_expr(self, ctx: Python3Parser.Yield_exprContext):
        if ctx.yield_arg() is not None:
            return ctx.yield_arg().accept(self)
        return Yield(None)

    # Visit a parse tree produced by Python3Parser#yield_arg.
    def visitYield_arg(self, ctx: Python3Parser.Yield_argContext):
        if ctx.FROM() is not None:
            return YieldFrom(ctx.test().accept(self))
        return Yield(ctx.testlist().accept(self))

    def visitTerminal(self, node):
        txt = node.getText()
        if txt.isspace():
            return None
        return txt

    # Visit a parse tree produced by Python3Parser#expr_hole.
    def visitExpr_hole(self, ctx: Python3Parser.Expr_holeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#simple_hole.
    def visitSimple_hole(self, ctx: Python3Parser.Simple_holeContext):
        hole = SimpleHole()
        set_lineno(hole, ctx)
        return hole

    # Visit a parse tree produced by Python3Parser#double_hole.
    def visitDouble_hole(self, ctx: Python3Parser.Double_holeContext):
        hole = DoubleHole()
        set_lineno(hole, ctx)
        return hole

    # Visit a parse tree produced by Python3Parser#compound_hole.
    def visitCompound_hole(self, ctx: Python3Parser.Compound_holeContext):
        return self.visitChildren(ctx)

    def visitVar_hole(self, ctx: Python3Parser.Var_holeContext):
        name = ctx.NAME().accept(self)
        hole = VarHole(name)
        set_lineno(hole, ctx)
        return hole

    def visitSimple_compound_hole(self, ctx: Python3Parser.Simple_compound_holeContext):
        body = ctx.suite().accept(self)
        hole = CompoundHole(body)
        set_lineno(hole, ctx)
        return hole

    def visitMultiple_compound_hole(self, ctx: Python3Parser.Multiple_compound_holeContext):
        body = ctx.suite().accept(self)
        hole = MultipleCompoundHole(body)
        set_lineno(hole, ctx)
        return hole

    def visitStrict_mode(self, ctx: Python3Parser.Strict_modeContext):
        body = self.visitChildren(ctx)
        hole = StrictMode(body, True)
        set_lineno(hole, ctx)

        end_hole = StrictMode(None, False)
        set_lineno(hole, ctx)
        return [hole, end_hole]


del Python3Parser
