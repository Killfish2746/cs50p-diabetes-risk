import pytest
from project import calculate_bmi, classify_glucose, assess_diabetes_risk


def test_calculate_bmi():
    # تست حالت عادی
    assert calculate_bmi(70, 1.75) == 22.86
    assert calculate_bmi(90, 1.80) == 27.78

    # تست مقادیر غیرمجاز
    with pytest.raises(ValueError):
        calculate_bmi(0, 1.75)
    with pytest.raises(ValueError):
        calculate_bmi(70, -1.5)


def test_classify_glucose():
    # افت قند
    assert classify_glucose(65) == "Hypoglycemia (افت قند خون)"
    # بازه نرمال
    assert classify_glucose(85) == "Normal (طبیعی)"
    # پیش‌دیابت
    assert classify_glucose(110) == "Prediabetes (پیش‌دیابت)"
    # دیابت
    assert classify_glucose(140) == "Diabetes (مشکوک به دیابت)"

    # مقدار منفی
    with pytest.raises(ValueError):
        classify_glucose(-10)


def test_assess_diabetes_risk():
    # ریسک بالا
    assert (
        assess_diabetes_risk(31.0, "Diabetes (مشکوک به دیابت)", 50, True)
        == "High Risk (خطر بالا - نیاز به مراجعه فوری به پزشک)"
    )

    # ریسک پایین
    assert assess_diabetes_risk(21.0, "Normal (طبیعی)", 25, False) == "Low Risk (کم‌خطر)"

    # ورودی نامعتبر سن
    with pytest.raises(ValueError):
        assess_diabetes_risk(22.0, "Normal (طبیعی)", -5, False)
