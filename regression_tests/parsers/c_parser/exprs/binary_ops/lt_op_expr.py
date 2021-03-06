"""
    A less than operator (``<``).
"""

from regression_tests.parsers.c_parser.exprs.binary_ops.binary_op_expr import BinaryOpExpr


class LtOpExpr(BinaryOpExpr):
    """A less than operator (``<``)."""

    def is_lt_op(self):
        """Returns ``True``."""
        return True

    def __str__(self):
        return '{} < {}'.format(self.lhs, self.rhs)
