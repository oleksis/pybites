def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    result = 0
    if not (isinstance(value, int)
            or isinstance(value, float)):
        raise TypeError("value need be int or float")
    
    fmt = fmt.lower()
    
    if fmt not in("cm", "in"):
        raise ValueError("fmt in cm or in")
        
    if fmt == "cm":
        result = value * 2.54
    else:
        result = value / 2.54
    
    return round(result, 4)
