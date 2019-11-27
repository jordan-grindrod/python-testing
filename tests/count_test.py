import pytest
from applications import count

def test_count_zeros():
	assert count.count([0,0,0],0)==3

def test_count_string():
	assert count.count(["a","a","a"],"a")==3

def test_count_minus():
	assert count.count([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert count.count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2

def test_count_bigNum():
	assert count.count([100000,200000,368574,468790,567582,60000,612345,54536,46667,377789,2789,109], 368574)==1
