import ast
import operator as op
import math
import sys

# Supported operators mapping
_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.FloorDiv: op.floordiv,
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}

# Allowed names from the math module
_ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}


def _eval(node):
    """Recursively evaluate an AST node representing a mathematical expression."""
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError(f"Unsupported constant: {node.value!r}")
    if isinstance(node, ast.Name):
        if node.id in _ALLOWED_NAMES:
            return _ALLOWED_NAMES[node.id]
        raise ValueError(f"Unknown identifier: {node.id}")
    if isinstance(node, ast.BinOp):
        if type(node.op) not in _OPERATORS:
            raise ValueError(f"Unsupported binary operator: {node.op}")
        return _OPERATORS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp):
        if type(node.op) not in _OPERATORS:
            raise ValueError(f"Unsupported unary operator: {node.op}")
        return _OPERATORS[type(node.op)](_eval(node.operand))
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Only function names are allowed")
        func_name = node.func.id
        if func_name not in _ALLOWED_NAMES:
            raise ValueError(f"Use of function '{func_name}' is not allowed")
        args = [_eval(arg) for arg in node.args]
        return _ALLOWED_NAMES[func_name](*args)
    raise ValueError(f"Unsupported expression: {ast.dump(node)}")


def evaluate(expr: str) -> float:
    """Safely evaluate a mathematical expression."""
    tree = ast.parse(expr, mode="eval")
    return float(_eval(tree))


def main(argv: list[str]) -> int:
    """Entry point for command-line usage."""
    if len(argv) > 1:
        expression = " ".join(argv[1:])
    else:
        expression = input("Enter expression: ")
    try:
        result = evaluate(expression)
        print(result)
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
