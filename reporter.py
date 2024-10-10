def get_report(temp, moist):
    full_report = []
    # Moisture level interpretation
    moist_level = "🪴  I'm feeling GOOD!"
    would_be_watered = ""

    if moist < 20:
        moist_level = "⛱️  Soil is too dry! Water Me please!"
        notification_mode = True
    elif moist > 40:
        moist_level = "️🌊  Soil is too wet. I need less water!"
    full_report.append(moist_level)
    full_report.append(f"🌡️  {temp:.2f}°C")
    return full_report


{'indoor': [(27.0, 30.0)], 'outdoor': [(15.27, 100.0)]}