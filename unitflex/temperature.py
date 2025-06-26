def convert_temperature(from_unit: str, to_unit: str, value: float) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    valid_units = {'celsius', 'fahrenheit'}
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Unsupported temperature unit: {from_unit} or {to_unit}")

    if from_unit == to_unit:
        return value

    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5 / 9

    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return celsius * 9 / 5 + 32
