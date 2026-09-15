import ast
import io
import sys
import tokenize
from pathlib import Path

def get_docstring_spans(source):
    tree = ast.parse(source)
    spans = set()

    def add_docstring(node):
        if not getattr(node, "body", None):
            return
        first = node.body[0]
        if isinstance(first, ast.Expr):
            value = first.value
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                spans.add((first.lineno, first.end_lineno))

    add_docstring(tree)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            add_docstring(node)

    return spans

def clean_source(source):
    docstrings = get_docstring_spans(source)
    lines = source.splitlines(keepends=True)
    removed_lines = set()

    for start, end in docstrings:
        removed_lines.update(range(start - 1, end))

    comment_tokens = []
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)

    for token in tokens:
        if token.type == tokenize.COMMENT:
            line_index = token.start[0] - 1
            if not source.splitlines()[line_index][:token.start[1]].strip():
                removed_lines.add(line_index)
            else:
                comment_tokens.append(token)

    result = []
    previous_was_removed = False

    for index, line in enumerate(lines):
        if index in removed_lines:
            previous_was_removed = True
            continue

        if previous_was_removed and not line.strip():
            continue

        result.append(line)
        previous_was_removed = False

    source = "".join(result)

    if comment_tokens:
        lines = source.splitlines(keepends=True)
        cleaned_lines = []

        for line in lines:
            try:
                line_tokens = tokenize.generate_tokens(io.StringIO(line).readline)
                comment_start = None

                for token in line_tokens:
                    if token.type == tokenize.COMMENT:
                        comment_start = token.start[1]
                        break

                if comment_start is not None:
                    line = line[:comment_start].rstrip() + "\n"

            except tokenize.TokenError:
                pass

            cleaned_lines.append(line)

        source = "".join(cleaned_lines)

    return source

def clean_file(path):
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".py":
        raise ValueError("The input file must be a Python .py file.")

    source = path.read_text(encoding="utf-8")
    cleaned = clean_source(source)

    output_path = path.with_name(f"{path.stem}_clean{path.suffix}")
    output_path.write_text(cleaned, encoding="utf-8")

    return output_path

def main():
    if len(sys.argv) != 2:
        print("Usage: python cleanpy.py <python_file>")
        return 1

    try:
        output = clean_file(sys.argv[1])
        print(f"Cleaned file: {output}")
        return 0
    except (SyntaxError, UnicodeError, OSError, ValueError) as error:
        print(f"Error: {error}")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())