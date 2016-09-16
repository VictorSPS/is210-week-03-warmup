#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports values from task 13 to test equality.

.. hint::

    You can access task_12 data in the following example type:

.. code:: python

    print task_12.FLOATVAL
"""

import task_12
if task_12.DECVAL == task_12.FLOATVAL:
    FRAC_DEC_EQUAL = 'True'
else:
    FRAC_DEC_EQUAL = 'Not True'
print FRAC_DEC_EQUAL
if task_12.DECVAL != task_12.FLOATVAL:
    DEC_FLOAT_INEQUAL = 'True'
else:
    DEC_FLOAT_INEQUAL = 'Not True'
print DEC_FLOAT_INEQUAL
