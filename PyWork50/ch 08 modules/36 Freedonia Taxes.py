"""
Sales tax on purchases in Freedonia depends on where the purchase was made, as
well as the time of the purchase. Freedonia has four provinces, each of which charges
its own percentage of tax:
 Chico: 50%
 Groucho: 70%
 Harpo: 50%
 Zeppo: 40%

The tax percentage is always multiplied by the hour at which the purchase was made.
At midnight (i.e., when the 24-hour clock is 0), there’s no sales tax. From 12 noon until
1 p.m., only 50% (12/24) of the tax applies. And from 11 p.m. until midnight, 95.8%
(i.e., 23/24) of the tax applies.

Your job is to implement that Python module, freedonia.py. It should provide a
function, calculate_tax, that takes three arguments:
the amount of the purchase,
the province in which the purchase took place,
and the hour (an integer, from 0–24) at which it happened.

The calculate_tax function should return the final price, as float.
Thus, if I were to invoke calculate_tax(500, 'Harpo', 12)
a $500 purchase in Harpo province (with 50%) tax would normally be $750.
However, because the purchase was done at 12 noon, the tax is only half of its maximum, or
$125, for a total of $625.

If the purchase were made at 9 p.m. (i.e, 21:00 on a 24-hour
clock), then the tax would be 87.5% of its full rate, or 43.75%, for a total price of
$718.75.

Moreover, I want you to write this solution using two separate files.
* The calculate_tax function, as well as any supporting data and functions,
should reside in the file freedonia.py, a Python module.
* The program that calls calculate_tax should be in a file called use_freedonia.py,
which then uses import to load the function.
"""