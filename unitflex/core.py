def convert(domain: str, from_unit: str, to_unit: str, value: float) -> float:
    domain = domain.lower()

    if domain not in {'temperature', 'distance', 'currency'}:
        raise ValueError(f"Unsupported domain: {domain}")

    if domain == 'temperature':
        from .temperature import convert_temperature
        return convert_temperature(from_unit, to_unit, value)

    elif domain == 'distance':
        from .distance import convert_distance
        return convert_distance(from_unit, to_unit, value)

    elif domain == 'currency':
        from .currency import convert_currency
        return convert_currency(from_unit, to_unit, value)
