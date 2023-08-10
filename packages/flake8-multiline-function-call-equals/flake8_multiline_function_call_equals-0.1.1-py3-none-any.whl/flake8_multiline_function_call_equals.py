import ast
import importlib.metadata


class Visitor(ast.NodeVisitor):

    def __init__(self):
        self.problems = []

        # messages / Error codes
        self.errors = {100: "EQA100 Too many whitespaces in single-line function call",
                       101: "EQA101 Too many whitespaces in multiline function call",
                       102: "EQA102 Too few whitespaces in multiline function call",
                       103: "EQA103 Empty line in multiline function call",
                       104: "EQA104 Multiple arguments on the same line in multiline function call",
                       105: "EQA105 First argument does not start on the call line in multiline function call",
                       106: "EQA106 Closing paren is on the same line as the last argument",
                       106: "EQA107 Closing paren is on the same line as the last argument",
                       }

    def visit_Call(self, node):
        sofar = node.col_offset+len(node.func.id) + 1  # 1 for the paren
        for keyword in node.keywords:
            if keyword.arg is None:
                continue

            if node.end_lineno - node.lineno == 0:  # single-line call
                self.processSingleLineCall(keyword, sofar)
                sofar = keyword.value.end_col_offset
                sofar += 2  # comma and space

            else:  # multiline call
                self.processMultiLineCall(keyword, node.col_offset+len(node.func.id)+1)  # +1 for the paren

                args = node.args + node.keywords
                for k1,k2 in zip(args, args[1:]):  # check for empty lines
                    if getattr(k2.value, 'lineno', getattr(k2, 'lineno', None)) > getattr(k1.value, 'end_lineno', getattr(k1, 'end_lineno', None))+1:
                        self.problems.append((k2.value.lineno-1, 0, self.errors[103]))
                        continue
        
                    if getattr(k2.value, 'lineno', getattr(k2, 'lineno', None)) == getattr(k1.value, 'end_lineno', getattr(k1, 'end_lineno', None)):
                        self.problems.append((getattr(k2.value, 'lineno', getattr(k2, 'lineno', None)), 0, self.errors[104]))
                        continue


        if node.end_lineno - node.lineno != 0:  # multiline function call
            # ensure the first argument is on the same line as the function call
            args = node.args + node.keywords
            n = args[0]
            if getattr(n.value, 'lineno', getattr(n, 'lineno', None)) > node.lineno:
                self.problems.append((node.keywords[0].value.lineno, node.keywords[0].value.col_offset, self.errors[105]))

            # ensure that the close-paren is on its own line
            if node.end_lineno == getattr(args[-1].value, 'end_lineno', getattr(args[-1], 'end_lineno', None)):
                self.problems.append((node.end_lineno, node.end_col_offset, self.errors[106]))

            # no blank lines before the closing paren
            if args:
                larg = args[-1]
                largLine = getattr(larg.value, 'end_lineno', getattr(larg, 'end_lineno', None))
            
                if node.end_lineno > largLine + 1:
                    self.problems.append((node.end_lineno, 0, self.errors[103]))

        self.generic_visit(node)

    def processSingleLineCall(self, keyword, startCol):
        arg = keyword.arg
        val = keyword.value

        if val.col_offset > startCol + len(arg) + 1:  # +1 for the `=`
            self.problems.append((keyword.value.lineno, startCol, self.errors[100]))


    def processMultiLineCall(self, keyword, startCol):
        arg = keyword.arg
        val = keyword.value

        if val.col_offset > startCol + len(arg) + 3:  # 3 because ` = `
            self.problems.append((val.lineno, startCol, self.errors[101]))
            return

        if val.col_offset < startCol + len(arg) + 3:  # 3 because ` = `
            self.problems.append((val.lineno, startCol, self.errors[102]))


class Plugin:
    name = __name__
    version = importlib.metadata.version(__name__)

    def __init__(self, tree):
        self._tree = tree

    def run(self):
        v = Visitor()
        v.visit(self._tree)
        for line, col, msg in v.problems:
            yield line, col, msg, type(self)
