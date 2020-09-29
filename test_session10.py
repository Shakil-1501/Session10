import pytest , os , inspect , re , random,session10
from decimal import Decimal
import math
import random


def test_dict_approach():
    c,d,e=session10.dict_approach_for_solution()
    assert type(d) is int


def test_numed_tuple_approach():
    c,d,e,f=session10.named_tuple_approach_fo_solution()
    assert type(d) is int


def test_stock_exchange():
    c,d,e=session10.stock_exchange_creation()
    assert type(d) is float