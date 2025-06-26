_TO_METERS = {
    'kilometers': 1000,
    'miles': 1609.344,
}

def convert_distance(from_unit: str, to_unit: str, value: float) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    valid_units = _TO_METERS.keys()
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Unsupported distance unit: {from_unit} or {to_unit}")

    if from_unit == to_unit:
        return value

    meters = value * _TO_METERS[from_unit]
    return round(meters / _TO_METERS[to_unit], 4)
