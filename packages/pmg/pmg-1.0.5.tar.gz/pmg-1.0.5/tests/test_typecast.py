from hypothesis import given
import hypothesis.strategies as st
import pmg.typecast

@given(st.one_of(st.booleans(), st.dates(), st.datetimes(), st.integers(), st.decimals(allow_nan=False), st.floats(allow_nan=False), st.text()))
def test_box(value):
    boxed_value = pmg.typecast.box(value) 
    assert value == pmg.typecast.unbox(boxed_value, type(value).__name__)