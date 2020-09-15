from decimal import Decimal
import cmath


def is_perfect_square(n, *, complex=False):
    if isinstance(n, (int, float, type(0j), Decimal)):
        if complex:
            complex_root = cmath.sqrt(n)
            r_exp = Decimal(complex_root.real).as_tuple().exponent
            i_exp = Decimal(complex_root.imag).as_tuple().exponent
            return r_exp == 0 and i_exp == 0
        else:
            if n >= 0:
                return Decimal(n).sqrt().as_tuple().exponent == 0
            else:
                return False
    else:
        raise TypeError()