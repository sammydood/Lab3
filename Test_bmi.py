import lab2_submodule.lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(70, 1.75)  # BMI ≈ 22.86
    assert (result == 0)


def test_bmi_under_weight():
    result = bmi.calculate_bmi(45, 1.75)  # BMI ≈ 14.69
    assert (result == -1)


def test_bmi_over_weight():
    result = bmi.calculate_bmi(90, 1.75)  # BMI ≈ 29.39
    assert (result == 1)


print(bmi)
