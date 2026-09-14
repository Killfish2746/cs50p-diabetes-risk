import sys


def main():
    print("=" * 45)
    print("      سامانه ارزیابی ریسک ابتلا به دیابت      ")
    print("=" * 45)

    try:
        age = int(input("سن شما (سال): "))
        weight = float(input("وزن شما (کیلوگرم): "))
        height = float(input("قد شما (متر، مثلا 1.75): "))
        glucose = float(input("سطح قند خون ناشتا (mg/dL): "))
        has_family_history = (
            input("آیا سابقه دیابت در خانواده دارید؟ (بله/خیر): ")
            .strip()
            .lower()
            in ["بله", "yes", "y"]
        )

        bmi = calculate_bmi(weight, height)
        glucose_status = classify_glucose(glucose)
        risk_result = assess_diabetes_risk(bmi, glucose_status, age, has_family_history)

        print("\n" + "-" * 30)
        print("نتایج غربالگری:")
        print(f"• شاخص توده بدنی (BMI): {bmi:.1f}")
        print(f"• وضعیت قند خون: {glucose_status}")
        print(f"• سطح ریسک کلی: {risk_result}")
        print("-" * 30)

    except ValueError as e:
        sys.exit(f"خطای ورودی نامعتبر: {e}")


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """محاسبه شاخص توده بدنی (BMI)"""
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("وزن و قد باید اعداد مثبت باشند.")
    return round(weight_kg / (height_m**2), 2)


def classify_glucose(glucose_level: float) -> str:
    """دسته‌بندی سطح قند خون ناشتا بر اساس استانداردهای بالینی"""
    if glucose_level <= 0:
        raise ValueError("مقدار قند خون باید عددی مثبت باشد.")
    elif glucose_level < 70:
        return "Hypoglycemia (افت قند خون)"
    elif 70 <= glucose_level <= 99:
        return "Normal (طبیعی)"
    elif 100 <= glucose_level <= 125:
        return "Prediabetes (پیش‌دیابت)"
    else:
        return "Diabetes (مشکوک به دیابت)"


def assess_diabetes_risk(
    bmi: float, glucose_status: str, age: int, family_history: bool
) -> str:
    """سنجش سطح ریسک بر اساس امتیازدهی بالینی"""
    if age < 0 or bmi <= 0:
        raise ValueError("سن یا BMI نامعتبر است.")

    score = 0

    # امتیازدهی بر اساس وضعیت قند خون
    if glucose_status == "Diabetes (مشکوک به دیابت)":
        score += 5
    elif glucose_status == "Prediabetes (پیش‌دیابت)":
        score += 3

    # امتیازدهی بر اساس BMI
    if bmi >= 30:
        score += 3
    elif bmi >= 25:
        score += 1

    # امتیاز سن
    if age >= 45:
        score += 2

    # سابقه خانوادگی
    if family_history:
        score += 2

    # برآورد نهایی
    if score >= 6:
        return "High Risk (خطر بالا - نیاز به مراجعه فوری به پزشک)"
    elif 3 <= score < 6:
        return "Moderate Risk (خطر متوسط - اصلاح رژیم و پایش سالانه)"
    else:
        return "Low Risk (کم‌خطر)"


if __name__ == "__main__":
    main()
