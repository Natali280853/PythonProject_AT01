def remainder(a, b):
    """Возвращает остаток от деления a на b.
       Если b равно 0, вызывает ValueError.
    """
    if b == 0:
        raise ValueError("Деление на ноль недопустимо.")
    return a % b