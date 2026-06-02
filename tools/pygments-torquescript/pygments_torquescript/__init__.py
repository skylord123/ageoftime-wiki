"""A Pygments lexer for TorqueScript, the embedded scripting language used by
the Torque Game Engine (and *Age of Time*).

The token model mirrors the IDEA-TorqueScriptLanguage flex lexer: TorqueScript
keywords, ``$global`` / ``%local`` variables, single-quoted *tagged* strings,
the ``SPC`` / ``TAB`` / ``NL`` string-concatenation operators, and the usual
C-style comments, numbers, and operators.

Standard Pygments token types are used throughout so that mkdocs-material's
syntax-highlight colors (``--md-code-hl-*``) apply without extra CSS.
"""

from pygments.lexer import RegexLexer, words
from pygments.token import (
    Comment, Keyword, Name, Number, Operator, Punctuation, String, Text,
    Whitespace,
)

__all__ = ["TorqueScriptLexer"]

# Keywords from the flex grammar (excluding true/false, handled as constants,
# and switch$/foreach$, handled by a dedicated rule below).
_KEYWORDS = (
    "new", "if", "else", "switch", "do", "while", "for", "foreach", "in",
    "case", "or", "default", "break", "continue", "assert", "return",
    "function", "datablock", "singleton", "package", "namespace", "Parent",
)


class TorqueScriptLexer(RegexLexer):
    name = "TorqueScript"
    aliases = ["torquescript", "torque", "tscript"]
    # Intentionally no *.cs / *.gui filename mapping: those extensions collide
    # with C# and other languages, and we only highlight explicit fences.
    filenames = []
    mimetypes = []
    url = "https://github.com/skylord123/ageoftime-wiki"

    tokens = {
        "root": [
            (r"\s+", Whitespace),

            # Comments
            (r"//[^\n]*", Comment.Single),
            (r"/\*", Comment.Multiline, "block_comment"),

            # Strings: "..." normal, '...' tagged
            (r'"', String.Double, "string_double"),
            (r"'", String.Single, "string_single"),

            # Numbers
            (r"0[xX][0-9a-fA-F]+", Number.Hex),
            (r"(\d+\.\d*|\.\d+)([eE][+-]?\d+)?", Number.Float),
            (r"\d+[eE][+-]?\d+", Number.Float),
            (r"\d+", Number.Integer),

            # Variables: $Global / $Foo::Bar and %local / %this
            (r"\$[A-Za-z_][A-Za-z0-9_]*(::[A-Za-z0-9_]+)*", Name.Variable.Global),
            (r"%[A-Za-z_][A-Za-z0-9_]*(::[A-Za-z0-9_]+)*", Name.Variable),

            # String-concatenation keyword operators
            (words(("SPC", "TAB", "NL"), suffix=r"\b"), Operator.Word),

            # $-suffixed keywords (must precede the plain `switch`/`foreach`)
            (r"(switch|foreach)\$", Keyword),

            (words(("true", "false"), suffix=r"\b"), Keyword.Constant),
            (words(_KEYWORDS, suffix=r"\b"), Keyword),

            # A bare identifier immediately followed by `(` is a call/definition
            (r"[A-Za-z_][A-Za-z0-9_]*(?=\s*\()", Name.Function),
            (r"[A-Za-z_][A-Za-z0-9_]*", Name),

            # Operators & punctuation
            (r"::", Operator),
            (r"!\$=|\$=|<<=|>>=|==|!=|<=|>=|&&|\|\||<<|>>|\+\+|--|-->|->|"
             r"[-+*/%=<>!~&|\^@?:]", Operator),
            (r"[{}\[\]();,.]", Punctuation),

            # Fallback: don't emit Error tokens for stray bytes (e.g. the
            # \x01 tagged-string markers the engine bakes into $MSGCB names).
            (r".", Text),
        ],
        "block_comment": [
            (r"[^*]+", Comment.Multiline),
            (r"\*/", Comment.Multiline, "#pop"),
            (r"\*", Comment.Multiline),
        ],
        "string_double": [
            (r'[^"\\]+', String.Double),
            (r"\\.", String.Escape),
            (r'"', String.Double, "#pop"),
        ],
        "string_single": [
            (r"[^'\\]+", String.Single),
            (r"\\.", String.Escape),
            (r"'", String.Single, "#pop"),
        ],
    }
