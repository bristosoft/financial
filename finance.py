"""
Summary: This module includes business formulas of all types.
Organization: bristoSOFT 
Author: Kirk A Jackson, Chief Software Designer
"""
# Imports
import math

# TIME VALUE OF MONEY


def    fv(pv, i, n):
    """ This function is for the future value of money
    over a period of time.
    pv = Initial Investment (1000)
    i = interest rate as decimal (.0675)
    n = the number of compound periods (20)
    Example: fv(1000, .0675, 20)
    """
    return pv * ((1 + i) ** n)

def    fvcc(pv, i, t):
    """ This function is for the future value of money
    over a period of time using continuous compounding.
    pv = Initial Investment (1000)
    i = interest rate as decimal (.0675)
    n = time periods in months, years etc (20)
    Example: fvcc(1000, .0675, 20)
    """
    return pv * (math.e ** (t*i))

def    pv(fv, i, n):
    """ This function is for the present value of money
    over a period of time.
    fv = Initial Investment (1000)
    i = interest rate as decimal (.0675)
    n = the number of compound periods (20)
    Example: pv(1000, .0675, 20)
    """
    return fv/((1 + i) ** n)

def    pva(a, i, n):
    """ This function is for the present value of money
    invested per period at the end of the month over a 
    period of time. 
    a = Periodic Investment (1000)
    i = interest rate as decimal (.0675)
    n = the number of compound periods (20)
    Example: pva(1000, .0675, 20)
    """
    return (a / i) * (1 - (1/(1 + i) ** n))

def    fva(a, i, n):
    """ This function is for the future value of money
    over a period of time.
    a = Periodic Investment (1000)
    i = interest rate as decimal (.0675)
    n = the number of compound periods (20)
    Example: fv(1000, .0675, 20)
    """
    return a * (((1 + i) ** n - 1)/ i)

def    fvga(a, i, g, n):
    """ This function is for the future value of an annuity
    with growth rate.  It is the future value of a growing
    stream of periodic investments.
    a = Periodic Investment (1000)
    i = interest rate as decimal (.0675)
    g = the growth rate (.05)
    n = the number of compound periods (20)
    Example: fv(1000, .0675, .05, 20)
    """
    return a * ((((1 + i) ** n) - (((1 + g) ** n)))/(i - g))

# ACCOUNTANCY

# Depreciation

def    sl(c, s, l):
    """ This accountancy function computes straight line
    depreciation for an asset purchase for cash with
    a known life span and salvage value.
    c = historical cost or price paid (1000)
    s = the expected salvage proceeds at disposal
    l = expected useful life of the fixed asset
    Example: sl(1000, 350, 10)
    """
    return (c - s)/l

def    syd(c, s, l):
    """ This accountancy function computes sum of the years
    digits depreciation for an asset purchased for cash
    with a known life span and salvage value.  The depreciation
    is returned as a list in python.
    c = historcal cost or price paid
    s = the expected salvage proceeds
    l = expected useful life of the fixed asset
    Example: syd(1000, 100, 5)
    """
    return [(c-s) * (x/(l*(l+1)/2)) for x in range(l,0,-1)]

def    dbal(c, s, r, l):
    """ This accountancy function computes declining balance
    depreciation for an asset purchased for cash with
    a known life span and salvage value.  The depreciation
    is returned as a list in Python.
    c = historcal cost or price paid
    s = the expected salvage proceeds
    r = declining percetage rate(ie 1, 1.2, 1.75 or double 2)
    l = expected useful life of the fixed asset
    Example: dbal(1000, 100, 1.5, 5) for 150% declining
    Example: dbal(1000, 100, 2, 5) for double declining
    """
    ad = 0
    res = []
    for x in range(l):
        if x == (l -1):
            dexp = (c - s -ad)
        else: 
            dexp = (((c)/l)/(c) * r) * (c - ad)
        res.append(dexp)
        ad = ad + dexp
    return res
        
# CAPITAL BUDGETING

def    ror (endv, iv):
    """ This capital budgeting function computes the rate of
    return on an investment for one period only.
    iv = initial investment value
    endv = total value at the end of the period
    Example: ror(100000, 129,500)
    """
    return (endv - iv)/iv 

def    npv(ico, nci, r, n):
    """ This capital budgeting function computes the net present
    value on a cash flow generating investment.
    ico = Initial Capital Outlay
    nci = net cash inflows per period
    r = discounted rate
    n = number of periods
    Example: npv(100000, 15000, .03, 10)
    """
    pv_nci = 0
    for x in range(n):
        pv_nci = pv_nci + (nci/((1 + r) ** (x + 1)))
    return pv_nci - ico
