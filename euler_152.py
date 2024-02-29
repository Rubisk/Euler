from fractions import Fraction
import copy
import sys
import pytest
import math
import itertools as it
from euler_util import slow_factor, is_prime_slow
from collections import Counter

squares = []

large_sums = [tuple(), (13, 39, 52), (7, 14, 21), (7, 28, 35), (7, 63, 70), (14, 28, 42), (14, 56, 70), (21, 35, 56), (21, 42, 63), (7, 28, 42, 56), (14, 35, 56, 63), (7, 21, 28, 42, 70), 
(14, 21, 35, 63, 70), (7, 14, 28, 35, 56, 70), (7, 14, 28, 42, 63, 70), (7, 21, 28, 35, 42, 63), (7, 21, 35, 56, 63, 70), (14, 21, 28, 35, 42, 56), (14, 21, 42, 56, 63, 70), (28, 35, 42, 56, 63, 70), 
(7, 14, 21, 28, 35, 42, 56, 63, 70), (15, 20), (30, 40), (45, 60), (60, 80), (5, 10, 15, 30), (5, 10, 40, 45), (5, 10, 40, 80), (5, 20, 40, 60), (10, 15, 45, 80), (10, 20, 30, 60), (15, 20, 30, 40), 
(15, 20, 45, 60), (15, 20, 60, 80), (30, 40, 45, 60), (30, 40, 60, 80), (5, 10, 15, 20, 40, 45), (5, 10, 15, 20, 40, 80), (5, 10, 15, 30, 45, 60), (5, 10, 15, 30, 60, 80), (5, 10, 40, 45, 60, 80), 
(10, 15, 30, 40, 45, 80), (15, 20, 30, 40, 45, 60), (15, 20, 30, 40, 60, 80), (5, 10, 15, 20, 40, 45, 60, 80), (5, 7, 28, 35), (5, 7, 15, 20, 28, 35), (5, 7, 28, 30, 35, 40), (5, 7, 28, 35, 45, 60),
(5, 7, 28, 35, 60, 80), (7, 10, 20, 28, 35, 45), (7, 10, 20, 28, 35, 80), (7, 15, 28, 30, 35, 45), (7, 15, 28, 30, 35, 80), (7, 28, 35, 40, 45, 80), (5, 7, 10, 15, 28, 35, 45, 80), 
(5, 7, 10, 20, 28, 30, 35, 60), (5, 7, 15, 20, 28, 30, 35, 40), (5, 7, 15, 20, 28, 35, 45, 60), (5, 7, 15, 20, 28, 35, 60, 80), (5, 7, 28, 30, 35, 40, 45, 60), (5, 7, 28, 30, 35, 40, 60, 80), 
(7, 10, 20, 28, 30, 35, 40, 45), (7, 10, 20, 28, 30, 35, 40, 80), (7, 10, 20, 28, 35, 45, 60, 80), (7, 15, 20, 28, 35, 40, 45, 80), (7, 15, 28, 30, 35, 45, 60, 80), (5, 7, 10, 15, 28, 30, 35, 40, 45, 80), (5, 7, 15, 20, 28, 30, 35, 40, 45, 60), (5, 7, 15, 20, 28, 30, 35, 40, 60, 80), (7, 10, 20, 28, 30, 35, 40, 45, 60, 80), (7, 10, 63, 70), (5, 7, 15, 60, 63, 70), (7, 10, 15, 20, 63, 70), (7, 10, 30, 40, 63, 70), (7, 10, 45, 60, 63, 70), (7, 10, 60, 63, 70, 80), (7, 15, 40, 45, 63, 70), (7, 15, 40, 63, 70, 80), (7, 20, 30, 45, 63, 70, 80), (5, 7, 10, 20, 40, 60, 63, 70), (5, 7, 15, 30, 40, 60, 63, 70), (7, 10, 15, 20, 30, 40, 63, 70), (7, 10, 15, 20, 45, 60, 63, 70), (7, 10, 15, 20, 60, 63, 70, 80), (7, 10, 30, 40, 45, 60, 63, 70), (7, 10, 30, 40, 60, 63, 70, 80), (7, 15, 40, 45, 60, 63, 70, 80), (7, 10, 15, 20, 30, 40, 45, 60, 63, 70), (7, 10, 15, 20, 30, 40, 60, 63, 70, 80), (10, 14, 56, 70), (5, 14, 15, 56, 60, 70), (10, 14, 15, 20, 56, 70), (10, 14, 30, 40, 56, 70), (10, 14, 45, 56, 60, 70), (10, 14, 56, 60, 70, 80), (14, 15, 40, 45, 56, 70), (14, 15, 40, 56, 70, 80), (14, 20, 30, 45, 56, 70, 80), (5, 10, 14, 20, 40, 56, 60, 70), (5, 14, 15, 30, 40, 56, 60, 70), (10, 14, 15, 20, 30, 40, 56, 70), (10, 14, 15, 20, 45, 56, 60, 70), (10, 14, 15, 20, 56, 60, 70, 80), (10, 14, 30, 40, 45, 56, 60, 70), (10, 14, 30, 40, 56, 60, 70, 80), (14, 15, 40, 45, 56, 60, 70, 80), (10, 14, 15, 20, 30, 40, 45, 56, 60, 70), (10, 14, 15, 20, 30, 40, 56, 60, 70, 80), (5, 21, 35, 56), (5, 15, 20, 21, 35, 56), (5, 21, 30, 35, 40, 56), (5, 21, 35, 45, 56, 60), (5, 21, 35, 56, 60, 80), (10, 20, 21, 35, 45, 56), (10, 20, 21, 35, 56, 80), (15, 21, 30, 35, 45, 56), (15, 21, 30, 35, 56, 80), (21, 35, 40, 45, 56, 80), (5, 10, 15, 21, 35, 45, 56, 80), (5, 10, 20, 21, 30, 35, 56, 60), (5, 15, 20, 21, 30, 35, 40, 56), (5, 15, 20, 21, 35, 45, 56, 60), (5, 15, 20, 21, 35, 56, 60, 80), (5, 21, 30, 35, 40, 45, 56, 60), (5, 21, 30, 35, 40, 56, 60, 80), (10, 20, 21, 30, 35, 40, 45, 56), (10, 20, 21, 30, 35, 40, 56, 80), (10, 20, 21, 35, 45, 56, 60, 80), (15, 20, 21, 35, 40, 45, 56, 80), (15, 21, 30, 35, 45, 56, 60, 80), (5, 10, 15, 21, 30, 35, 40, 45, 56, 80), (5, 15, 20, 21, 30, 35, 40, 45, 56, 60), (5, 15, 20, 21, 30, 35, 40, 56, 60, 80), (10, 20, 21, 30, 35, 40, 45, 56, 60, 80), (5, 14, 35, 56, 63), (5, 14, 15, 20, 35, 56, 63), (5, 14, 30, 35, 40, 56, 63), (5, 14, 35, 45, 56, 60, 63), (5, 14, 35, 56, 60, 63, 80), (10, 14, 20, 35, 45, 56, 63), (10, 14, 20, 35, 56, 63, 80), (14, 15, 30, 35, 45, 56, 63), (14, 15, 30, 35, 56, 63, 80), (14, 35, 40, 45, 56, 63, 80), (5, 10, 14, 15, 35, 45, 56, 63, 80), (5, 10, 14, 20, 30, 35, 56, 60, 63), (5, 14, 15, 20, 30, 35, 40, 56, 63), (5, 14, 15, 20, 35, 45, 56, 60, 63), (5, 14, 15, 20, 35, 56, 60, 63, 80), (5, 14, 30, 35, 40, 45, 56, 60, 63), (5, 14, 30, 35, 40, 56, 60, 63, 80), (10, 14, 20, 30, 35, 40, 45, 56, 63), (10, 14, 20, 30, 35, 40, 56, 63, 80), (10, 14, 20, 35, 45, 56, 60, 63, 80), (14, 15, 20, 35, 40, 45, 56, 63, 80), (14, 15, 30, 35, 45, 56, 60, 63, 80), (5, 10, 14, 15, 30, 35, 40, 45, 56, 63, 80), (5, 14, 15, 20, 30, 35, 40, 45, 56, 60, 63), (5, 14, 15, 20, 30, 35, 40, 56, 60, 63, 80), (10, 14, 20, 30, 35, 40, 45, 56, 60, 63, 80), (7, 10, 21, 28, 42, 70), (5, 7, 15, 21, 28, 42, 60, 70), (7, 10, 15, 20, 21, 28, 42, 70), (7, 10, 21, 28, 30, 40, 42, 70), (7, 10, 21, 28, 42, 45, 60, 70), (7, 10, 21, 28, 42, 60, 70, 80), (7, 15, 21, 28, 40, 42, 45, 70), (7, 15, 21, 28, 40, 42, 70, 80), (7, 20, 21, 28, 30, 42, 45, 70, 80), (5, 7, 10, 20, 21, 28, 40, 42, 60, 70), (5, 7, 15, 21, 28, 30, 40, 42, 60, 70), (7, 10, 15, 20, 21, 28, 30, 40, 42, 70), (7, 10, 15, 20, 21, 28, 42, 45, 60, 70), (7, 10, 15, 20, 21, 28, 42, 60, 70, 80), (7, 10, 21, 28, 30, 40, 42, 45, 60, 70), (7, 10, 21, 28, 30, 40, 42, 60, 70, 80), (7, 15, 21, 28, 40, 42, 45, 60, 70, 80), (7, 10, 15, 20, 21, 28, 30, 40, 42, 45, 60, 70), (7, 10, 15, 20, 21, 28, 30, 40, 42, 60, 70, 80), (5, 10, 14, 21, 35, 63, 70), (14, 20, 21, 35, 40, 63, 70), (14, 21, 30, 35, 60, 63, 70), (5, 10, 14, 15, 20, 21, 35, 63, 70), (5, 10, 14, 21, 30, 35, 40, 63, 70), (5, 10, 14, 21, 35, 45, 60, 63, 70), (5, 10, 14, 21, 35, 60, 63, 70, 80), (5, 14, 15, 21, 35, 40, 45, 63, 70), (5, 14, 15, 21, 35, 40, 63, 70, 80), (10, 14, 15, 21, 30, 35, 45, 63, 70), (10, 14, 15, 21, 30, 35, 63, 70, 80), (10, 14, 21, 35, 40, 45, 63, 70, 80), (14, 15, 20, 21, 30, 35, 60, 63, 70), (14, 20, 21, 35, 40, 45, 60, 63, 70), (14, 20, 21, 35, 40, 60, 63, 70, 80), (5, 14, 20, 21, 30, 35, 45, 63, 70, 80), (5, 10, 14, 15, 20, 21, 30, 35, 40, 63, 70), (5, 10, 14, 15, 20, 21, 35, 45, 60, 63, 70), (5, 10, 14, 15, 20, 21, 35, 60, 63, 70, 80), (5, 10, 14, 21, 30, 35, 40, 45, 60, 63, 70), (5, 10, 14, 21, 30, 35, 40, 60, 63, 70, 80), (5, 14, 15, 21, 35, 40, 45, 60, 63, 70, 80), (10, 14, 15, 20, 21, 35, 40, 45, 63, 70, 80), (10, 14, 15, 21, 30, 35, 45, 60, 63, 70, 80), (5, 10, 14, 15, 20, 21, 30, 35, 40, 45, 60, 63, 70), (5, 10, 14, 15, 20, 21, 30, 35, 40, 60, 63, 70, 80), (5, 7, 10, 14, 28, 35, 56, 70), (7, 14, 20, 28, 35, 40, 56, 70), (7, 14, 28, 30, 35, 56, 60, 70), (5, 7, 10, 14, 15, 20, 28, 35, 56, 70), (5, 7, 10, 14, 28, 30, 35, 40, 56, 70), (5, 7, 10, 14, 28, 35, 45, 56, 60, 70), (5, 7, 10, 14, 28, 35, 56, 60, 70, 80), (5, 7, 14, 15, 28, 35, 40, 45, 56, 70), (5, 7, 14, 15, 28, 35, 40, 56, 70, 80), (7, 10, 14, 15, 28, 30, 35, 45, 56, 70), (7, 10, 14, 15, 28, 30, 35, 56, 70, 80), (7, 10, 14, 28, 35, 40, 45, 56, 70, 80), (7, 14, 15, 20, 28, 30, 35, 56, 60, 70), (7, 14, 20, 28, 35, 40, 45, 56, 60, 70), (7, 14, 20, 28, 35, 40, 56, 60, 70, 80), (5, 7, 14, 20, 28, 30, 35, 45, 56, 70, 80), (5, 7, 10, 14, 15, 20, 28, 30, 35, 40, 56, 70), (5, 7, 10, 14, 15, 20, 28, 35, 45, 56, 60, 70), (5, 7, 10, 14, 15, 20, 28, 35, 56, 60, 70, 80), (5, 7, 10, 14, 28, 30, 35, 40, 45, 56, 60, 70), (5, 7, 10, 14, 28, 30, 35, 40, 56, 60, 70, 80), (5, 7, 14, 15, 28, 35, 40, 45, 56, 60, 70, 80), (7, 10, 14, 15, 20, 28, 35, 40, 45, 56, 70, 80), (7, 10, 14, 15, 28, 30, 35, 45, 56, 60, 70, 80), (5, 7, 10, 14, 15, 20, 28, 30, 35, 40, 45, 56, 60, 70), (5, 7, 10, 14, 15, 20, 28, 30, 35, 40, 56, 60, 70, 80), (7, 10, 14, 28, 42, 63, 70), (5, 7, 14, 15, 28, 42, 60, 63, 70), (7, 10, 14, 15, 20, 28, 42, 63, 70), (7, 10, 14, 28, 30, 40, 42, 63, 70), (7, 10, 14, 28, 42, 45, 60, 63, 70), (7, 10, 14, 28, 42, 60, 63, 70, 80), (7, 14, 15, 28, 40, 42, 45, 63, 70), (7, 14, 15, 28, 40, 42, 63, 70, 80), (7, 14, 20, 28, 30, 42, 45, 63, 70, 80), (5, 7, 10, 14, 20, 28, 40, 42, 60, 63, 70), (5, 7, 14, 15, 28, 30, 40, 42, 60, 63, 70), (7, 10, 14, 15, 20, 28, 30, 40, 42, 63, 70), (7, 10, 14, 15, 20, 28, 42, 45, 60, 63, 70), (7, 10, 14, 15, 20, 28, 42, 60, 63, 70, 80), (7, 10, 14, 28, 30, 40, 42, 45, 60, 63, 70), (7, 10, 14, 28, 30, 40, 42, 60, 63, 70, 80), (7, 14, 15, 28, 40, 42, 45, 60, 63, 70, 80), (7, 10, 14, 15, 20, 28, 30, 40, 42, 45, 60, 63, 70), (7, 10, 14, 15, 20, 28, 30, 40, 42, 60, 63, 70, 80), (5, 7, 21, 28, 35, 42, 63), (5, 7, 15, 20, 21, 28, 35, 42, 63), (5, 7, 21, 28, 30, 35, 40, 42, 63), (5, 7, 21, 28, 35, 42, 45, 60, 63), (5, 7, 21, 28, 35, 42, 60, 63, 80), (7, 10, 20, 21, 28, 35, 42, 45, 63), (7, 10, 20, 21, 28, 35, 42, 63, 80), (7, 15, 21, 28, 30, 35, 42, 45, 63), (7, 15, 21, 28, 30, 35, 42, 63, 80), (7, 21, 28, 35, 40, 42, 45, 63, 80), (5, 7, 10, 15, 21, 28, 35, 42, 45, 63, 80), (5, 7, 10, 20, 21, 28, 30, 35, 42, 60, 63), (5, 7, 15, 20, 21, 28, 30, 35, 40, 42, 63), (5, 7, 15, 20, 21, 28, 35, 42, 45, 60, 63), (5, 7, 15, 20, 21, 28, 35, 42, 60, 63, 80), (5, 7, 21, 28, 30, 35, 40, 42, 45, 60, 63), (5, 7, 21, 28, 30, 35, 40, 42, 60, 63, 80), (7, 10, 20, 21, 28, 30, 35, 40, 42, 45, 63), (7, 10, 20, 21, 28, 30, 35, 40, 42, 63, 80), (7, 10, 20, 21, 28, 35, 42, 45, 60, 63, 80), (7, 15, 20, 21, 28, 35, 40, 42, 45, 63, 80), (7, 15, 21, 28, 30, 35, 42, 45, 60, 63, 80), (5, 7, 10, 15, 21, 28, 30, 35, 40, 42, 45, 63, 80), (5, 7, 15, 20, 21, 28, 30, 35, 40, 42, 45, 60, 63), (5, 7, 15, 20, 21, 28, 30, 35, 40, 42, 60, 63, 80), (7, 10, 20, 21, 28, 30, 35, 40, 42, 45, 60, 63, 80), (5, 7, 10, 21, 35, 56, 63, 70), (7, 20, 21, 35, 40, 56, 63, 70), (7, 21, 30, 35, 56, 60, 63, 70), (5, 7, 10, 15, 20, 21, 35, 56, 63, 70), (5, 7, 10, 21, 30, 35, 40, 56, 63, 70), (5, 7, 10, 21, 35, 45, 56, 60, 63, 70), (5, 7, 10, 21, 35, 56, 60, 63, 70, 80), (5, 7, 15, 21, 35, 40, 45, 56, 63, 70), (5, 7, 15, 21, 35, 40, 56, 63, 70, 80), (7, 10, 15, 21, 30, 35, 45, 56, 63, 70), (7, 10, 15, 21, 30, 35, 56, 63, 70, 80), (7, 10, 21, 35, 40, 45, 56, 63, 70, 80), (7, 15, 20, 21, 30, 35, 56, 60, 63, 70), (7, 20, 21, 35, 40, 45, 56, 60, 63, 70), (7, 20, 21, 35, 40, 56, 60, 63, 70, 80), (5, 7, 20, 21, 30, 35, 45, 56, 63, 70, 80), (5, 7, 10, 15, 20, 21, 30, 35, 40, 56, 63, 70), (5, 7, 10, 15, 20, 21, 35, 45, 56, 60, 63, 70), (5, 7, 10, 15, 20, 21, 35, 56, 60, 63, 70, 80), (5, 7, 10, 21, 30, 35, 40, 45, 56, 60, 63, 70), (5, 7, 10, 21, 30, 35, 40, 56, 60, 63, 70, 80), (5, 7, 15, 21, 35, 40, 45, 56, 60, 63, 70, 80), (7, 10, 15, 20, 21, 35, 40, 45, 56, 63, 70, 80), (7, 10, 15, 21, 30, 35, 45, 56, 60, 63, 70, 80), (5, 7, 10, 15, 20, 21, 30, 35, 40, 45, 56, 60, 63, 70), (5, 7, 10, 15, 20, 21, 30, 35, 40, 56, 60, 63, 70, 80), (5, 14, 21, 28, 35, 42, 56), (5, 14, 15, 20, 21, 28, 35, 42, 56), (5, 14, 21, 28, 30, 35, 40, 42, 56), (5, 14, 21, 28, 35, 42, 45, 56, 60), (5, 14, 21, 28, 35, 42, 56, 60, 80), (10, 14, 20, 21, 28, 35, 42, 45, 56), (10, 14, 20, 21, 28, 35, 42, 56, 80), (14, 15, 21, 28, 30, 35, 42, 45, 56), (14, 15, 21, 28, 30, 35, 42, 56, 80), (14, 21, 28, 35, 40, 42, 45, 56, 80), (5, 10, 14, 15, 21, 28, 35, 42, 45, 56, 80), (5, 10, 14, 20, 21, 28, 30, 35, 42, 56, 60), (5, 14, 15, 20, 21, 28, 30, 35, 40, 42, 56), (5, 14, 15, 20, 21, 28, 35, 42, 45, 56, 60), (5, 14, 15, 20, 21, 28, 35, 42, 56, 60, 80), (5, 14, 21, 28, 30, 35, 40, 42, 45, 56, 60), (5, 14, 21, 28, 30, 35, 40, 42, 56, 60, 80), (10, 14, 20, 21, 28, 30, 35, 40, 42, 45, 56), (10, 14, 20, 21, 28, 30, 35, 40, 42, 56, 80), (10, 14, 20, 21, 28, 35, 42, 45, 56, 60, 80), (14, 15, 20, 21, 28, 35, 40, 42, 45, 56, 80), (14, 15, 21, 28, 30, 35, 42, 45, 56, 60, 80), (5, 10, 14, 15, 21, 28, 30, 35, 40, 42, 45, 56, 80), (5, 14, 15, 20, 21, 28, 30, 35, 40, 42, 45, 56, 60), (5, 14, 15, 20, 21, 28, 30, 35, 40, 42, 56, 60, 80), (10, 14, 20, 21, 28, 30, 35, 40, 42, 45, 56, 60, 80), (10, 14, 21, 42, 56, 63, 70), (5, 14, 15, 21, 42, 56, 60, 63, 70), (10, 14, 15, 20, 21, 42, 56, 63, 70), (10, 14, 21, 30, 40, 42, 56, 63, 70), (10, 14, 21, 42, 45, 56, 60, 63, 70), (10, 14, 21, 42, 56, 60, 63, 70, 80), (14, 15, 21, 40, 42, 45, 56, 63, 70), (14, 15, 21, 40, 42, 56, 63, 70, 80), (14, 20, 21, 30, 42, 45, 56, 63, 70, 80), (5, 10, 14, 20, 21, 40, 42, 56, 60, 63, 70), (5, 14, 15, 21, 30, 40, 42, 56, 60, 63, 70), (10, 14, 15, 20, 21, 30, 40, 42, 56, 63, 70), (10, 14, 15, 20, 21, 42, 45, 56, 60, 63, 70), (10, 14, 15, 20, 21, 42, 56, 60, 63, 70, 80), (10, 14, 21, 30, 40, 42, 45, 56, 60, 63, 70), (10, 14, 21, 30, 40, 42, 56, 60, 63, 70, 80), (14, 15, 21, 40, 42, 45, 56, 60, 63, 70, 80), (10, 14, 15, 20, 21, 30, 40, 42, 45, 56, 60, 63, 70), (10, 14, 15, 20, 21, 30, 40, 42, 56, 60, 63, 70, 80), (5, 10, 28, 35, 42, 56, 63, 70), (20, 28, 35, 40, 42, 56, 63, 70), (28, 30, 35, 42, 56, 60, 63, 70), (5, 10, 15, 20, 28, 35, 42, 56, 63, 70), (5, 10, 28, 30, 35, 40, 42, 56, 63, 70), (5, 10, 28, 35, 42, 45, 56, 60, 63, 70), (5, 10, 28, 35, 42, 56, 60, 63, 70, 80), (5, 15, 28, 35, 40, 42, 45, 56, 63, 70), (5, 15, 28, 35, 40, 42, 56, 63, 70, 80), (10, 15, 28, 30, 35, 42, 45, 56, 63, 70), (10, 15, 28, 30, 35, 42, 56, 63, 70, 80), (10, 28, 35, 40, 42, 45, 56, 63, 70, 80), (15, 20, 28, 30, 35, 42, 56, 60, 63, 70), (20, 28, 35, 40, 42, 45, 56, 60, 63, 70), (20, 28, 35, 40, 42, 56, 60, 63, 70, 80), (5, 20, 28, 30, 35, 42, 45, 56, 63, 70, 80), (5, 10, 15, 20, 28, 30, 35, 40, 42, 56, 63, 70), (5, 10, 15, 20, 28, 35, 42, 45, 56, 60, 63, 70), (5, 10, 15, 20, 28, 35, 42, 56, 60, 63, 70, 80), (5, 10, 28, 30, 35, 40, 42, 45, 56, 60, 63, 70), (5, 10, 28, 30, 35, 40, 42, 56, 60, 63, 70, 80), (5, 15, 28, 35, 40, 42, 45, 56, 60, 63, 70, 80), (10, 15, 20, 28, 35, 40, 42, 45, 56, 63, 70, 80), (10, 15, 28, 30, 35, 42, 45, 56, 60, 63, 70, 80), (5, 10, 15, 20, 28, 30, 35, 40, 42, 45, 56, 60, 63, 70), (5, 10, 15, 20, 28, 30, 35, 40, 42, 56, 60, 63, 70, 80), (5, 7, 10, 14, 21, 28, 35, 42, 56, 63, 70), (7, 14, 20, 21, 28, 35, 40, 42, 56, 63, 70), (7, 14, 21, 28, 30, 35, 42, 56, 60, 63, 70), (5, 7, 10, 14, 15, 20, 21, 28, 35, 42, 56, 63, 70), (5, 7, 10, 14, 21, 28, 30, 35, 40, 42, 56, 63, 70), (5, 7, 10, 14, 21, 28, 35, 42, 45, 56, 60, 63, 70), (5, 7, 10, 14, 21, 28, 35, 42, 56, 60, 63, 70, 80), (5, 7, 14, 15, 21, 28, 35, 40, 42, 45, 56, 63, 70), (5, 7, 14, 15, 21, 28, 35, 40, 42, 56, 63, 70, 80), (7, 10, 14, 15, 21, 28, 30, 35, 42, 45, 56, 63, 70), (7, 10, 14, 15, 21, 28, 30, 35, 42, 56, 63, 70, 80), (7, 10, 14, 21, 28, 35, 40, 42, 45, 56, 63, 70, 80), (7, 14, 15, 20, 21, 28, 30, 35, 42, 56, 60, 63, 70), (7, 14, 20, 21, 28, 35, 40, 42, 45, 56, 60, 63, 70), (7, 14, 20, 21, 28, 35, 40, 42, 56, 60, 63, 70, 80), (5, 7, 14, 20, 21, 28, 30, 35, 42, 45, 56, 63, 70, 80), (5, 7, 10, 14, 15, 20, 21, 28, 30, 35, 40, 42, 56, 63, 70), (5, 7, 10, 14, 15, 20, 21, 28, 35, 42, 45, 56, 60, 63, 70), (5, 7, 10, 14, 15, 20, 21, 28, 35, 42, 56, 60, 63, 70, 80), (5, 7, 10, 14, 21, 28, 30, 35, 40, 42, 45, 56, 60, 63, 70), (5, 7, 10, 14, 21, 28, 30, 35, 40, 42, 56, 60, 63, 70, 80), (5, 7, 14, 15, 21, 28, 35, 40, 42, 45, 56, 60, 63, 70, 80), (7, 10, 14, 15, 20, 21, 28, 35, 40, 42, 45, 56, 63, 70, 80), (7, 10, 14, 15, 21, 28, 30, 35, 42, 45, 56, 60, 63, 70, 80), (5, 7, 10, 14, 15, 20, 21, 28, 30, 35, 40, 42, 45, 56, 60, 63, 70), (5, 7, 10, 14, 15, 20, 21, 28, 30, 35, 40, 42, 56, 60, 63, 70, 80)]

def find_prime_combinations(prime, upper, extra=0):
    """
    Finds all sets of numbers <= upper such that
    a) All numbers are divisible by prime
    b) No numbers are divisible by any other prime q >= prime
    c) The denominator of the sum of the reciprocal squares is not divisible by any prime q >= prime
    """
    numbers = [prime * n for n in range(1, int(upper / prime + 1))]
    sums = []
    for n in numbers:
        if max(slow_factor(n)) > prime:
            numbers.remove(n)
    set_count = 0
    for count in range(1, len(numbers) + 1):
        for combination in it.combinations(numbers, count):
            set_count += 1
            total = extra + sum([Fraction(1, x ** 2) for x in combination])
            if max(slow_factor(total.denominator)) < prime:
                sums.append(combination)
    return sums

def find_large_sums(large_lower_bound, upper):
    """
    Finds all sums where all terms are divisible by a prime
    """
    n = upper
    all_results = [tuple()]
    while n > large_lower_bound:
        new_results = []
        if is_prime_slow(n):
            for combination in all_results:
                extra = sum([Fraction(1, x ** 2) for x in combination])
                combinations = find_prime_combinations(n, upper, extra)
                combinations = [tuple(set(x).union(set(combination))) for x in combinations]
                combinations = [tuple(sorted(x)) for x in combinations]
                new_results += combinations
            all_results += new_results
            print(all_results, n)
        n -= 1
    return all_results

def find_small_sums(prime_bound, upper, extra=0):
    """
    Finds all sets of numbers <= upper such that
    a) All numbers are divisible by prime
    b) No numbers are divisible by any other prime q >= prime
    c) The denominator of the sum of the reciprocal squares is not divisible by any prime q >= prime
    """
    numbers = [x for x in range(2, upper + 1) if max(slow_factor(x)) <= prime_bound]
    totals = []
    set_count = 0
    for count in range(1, len(numbers) + 1):
        print(count)
        for combination in it.combinations(numbers, count):
            set_count += 1
            total = extra + sum([Fraction(1, x ** 2) for x in combination])
            totals.append(total)
    return totals


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main([__file__])
    else:
        count = 0
        results = [sum([Fraction(1, x ** 2) for x in combination]) if combination else 0 for combination in list(set(large_sums))]
        print(len(large_sums), len(set(large_sums)))
        set_results = set(results)
        for x in find_small_sums(3, 80):
            if Fraction(1, 2) - x in set_results:
                print(x)
                count += Counter(results)[Fraction(1, 2) - x]
                print("COUNT", count)

        