import pytest


def test_exercise_1_variables_and_types(tb):
    name = tb.ref("name")
    age = tb.ref("age")
    is_student = tb.ref("is_student")

    assert isinstance(name, str) and name.strip()
    assert isinstance(age, int) and not isinstance(age, bool)
    assert isinstance(is_student, bool)


def test_exercise_2_gst_arithmetic(tb):
    price = tb.ref("price")
    gst_rate = tb.ref("gst_rate")

    assert tb.ref("gst_amount") == pytest.approx(price * gst_rate)
    assert tb.ref("total_price") == pytest.approx(price + price * gst_rate)


def test_exercise_3_string_manipulation(tb):
    full_name = tb.ref("full_name")
    first, last = full_name.split()

    assert tb.ref("title_name") == full_name.title()
    assert tb.ref("initials") == (first[0] + last[0]).upper()
    assert tb.ref("name_length") == len(full_name.replace(" ", ""))


def test_exercise_4_profile_message(tb):
    out = tb.cell_output_text(9)
    name = tb.ref("name")
    price = tb.ref("price")

    assert name in out
    assert f"{price:.2f}" in out
