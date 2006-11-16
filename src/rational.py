import pymbolic.primitives as primitives
import pymbolic.traits as traits




class Rational(primitives.Expression):
    def __init__(self, numerator, denominator=1):
        d_unit = traits.traits(denominator).get_unit(denominator)
        numerator /= d_unit
        denominator /= d_unit
        self.Numerator = numerator
        self.Denominator = denominator

    def _num(self):
        return self.Numerator
    numerator = property(_num)

    def _den(self):
        return self.Denominator
    denominator = property(_den)

    def __nonzero__(self):
        return bool(self.Numerator)

    def __neg__(self):
        return Rational(-self.Numerator, self.Denominator)

    def __eq__(self):
        if not isinstance(other, Rational):
            other = Rational(other)

        return self.Numerator == other.Numerator and \
               self.Denominator == other.Denominator

    def __add__(self, other):
        if not isinstance(other, Rational):
            newother = Rational(other)

        try:
            t = traits.common_traits(self.Denominator, newother.Denominator)
            newden = t.lcm(self.Denominator, newother.Denominator)
            newnum = self.Numerator * newden/self.Denominator + \
                     newother.Numerator * newden/newother.Denominator
            gcd = t.gcd(newden, newnum)
            return Rational(newnum/gcd, newden/gcd)
        except traits.NoTraitsError:
            return primitives.Expression.__add__(self, other)
        except traits.NoCommonTraitsError:
            return primitives.Expression.__add__(self, other)

    __radd__ = __add__

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        return (-self).__radd__(other)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            newother = Rational(other)

        try:
            t = traits.common_traits(self.Numerator, newother.Numerator,
                                     self.Denominator, newother. Denominator)
            gcd_1 = t.gcd(self.Numerator, newother.Denominator)
            gcd_2 = t.gcd(newother.Numerator, self.Denominator)

            new_num = self.Numerator/gcd_1 * newother.Numerator/gcd_2
            new_denom = self.Denominator/gcd_2 * newother.Denominator/gcd_1

            if not (new_denom-1):
                return new_num

            return Rational(new_num, new_denom)
        except traits.NoTraitsError:
            return primitives.Expression.__mul__(self, other)
        except traits.NoCommonTraitsError:
            return primitives.Expression.__mul__(self, other)

    __rmul__ = __mul__

    def __div__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)

        return self.__mul__(Rational(other.Denominator, other.Numerator))

    def __rdiv__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)

        return Rational(self.Denominator, self.Numerator).__rmul__(other)

    def __pow__(self, other):
        return Rational(self.Denominator**other, self.Numerator**other)

    def __float__(self):
        return float(self.Numerator) / flaot(self.Denominator)

    def __getinitargs__(self):
        return (self.Numerator, self.Denominator)

    def reciprocal(self):
        return Rational(self.Denominator, self.Numerator)

    def invoke_mapper(self, mapper, *args, **kwargs):
        return mapper.map_rational(self, *args, **kwargs)




if __name__ == "__main__":
    one = Rational(1)
    print 3 + 1/(1 - 3/(one + 17))
    print one/3 + 2*one/3
    print one/3 + 2*one/3 + 0*one/1771
