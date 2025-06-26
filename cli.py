import sys
from unitflex.core import convert

if len(sys.argv) != 5:
    print("Использование: cli.py <domain> <from_unit> <to_unit> <value>")
    sys.exit(1)

domain, from_unit, to_unit, value = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])

try:
    result = convert(domain, from_unit, to_unit, value)
    print(f"{value} {from_unit} = {result} {to_unit}")
except ValueError as e:
    print(f"Ошибка: {e}")
    sys.exit(1)