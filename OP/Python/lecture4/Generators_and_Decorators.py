"""A module with functions for processing basic calculus."""

def get_pow(number: int, power: int = 2) -> int:
    """Evaluate a power of a given number. Power defaults to 2.
    
    Args:
        number: int - a given number to process
        power: int - a desired power, defaults to 2
        
    Returns:
        int - a power of a given number
    """
    return number ** power


help(get_pow)
print(get_pow.__annotations__)