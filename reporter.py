def get_report(temp, moist):
    full_report = ""
    # Moisture level interpretation
    moist_level = "🪴  I'm feeling GOOD!\n"
    would_be_watered = ""

    if moist < 20:
        moist_level = "⛱️  Soil is too dry! Water Me please!\n"
        notification_mode = True
    elif moist > 40:
        moist_level = "️🌊  Soil is too wet. I need less water!\n"
    full_report += moist_level
    full_report += f"💧 {moist:.2f}% (should be 20%-40%)\n"

    full_report += f"🌡️  {temp:.2f}°C"
    return full_report


x = {'indoor': [(27.0, 30.0)], 'outdoor': [(15.27, 100.0)]}