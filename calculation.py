# coding: utf-8

def convert_base(num, to_base=10, from_base=10):
    """ 
    num : std - Чило для перевода
    to_base : int - Конечная с/с
    from_base : int - Начальная с/с
    """
    # Cначала преобразует в десятичное число
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # Преобразовывает из десятичной в 'to_base'
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
