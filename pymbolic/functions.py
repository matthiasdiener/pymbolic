from __future__ import division, absolute_import

__copyright__ = "Copyright (C) 2009-2013 Andreas Kloeckner"

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


import pymbolic.primitives as primitives


def sin(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "sin"), (x,))


def cos(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "cos"), (x,))


def tan(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "tan"), (x,))


def log(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "log"), (x,))


def exp(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "exp"), (x,))


def sinh(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "tanh"), (x,))


def cosh(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "cosh"), (x,))


def tanh(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "sinh"), (x,))


def expm1(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "expm1"), (x,))


def fabs(x):
    return primitives.Call(
            primitives.Lookup(primitives.Variable("math"), "fabs"), (x,))


def sgn(x):
    return primitives.Quotient(x,
            primitives.Call(
                primitives.Lookup(primitives.Variable("math"), "fabs"), (x,)))
