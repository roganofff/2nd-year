CODES = ('+7', '8')
LOCAL_LENGTH = 10
REGION_CODE_LENGTH = 3

def is_phone_number(phone: str) -> bool:
    """Check if the given phone is valid.
    
    Args:
        phone - phone number.

    Returns:
        bool - validity of phone number.
    """
    for code in CODES:
        if phone.startswith(code):
            local = phone[len(code):]
            return len(local) == LOCAL_LENGTH and local.isdigit() 

    return False


def get_region(phone: str, database: str='region_codes.txt') -> str:
    """Get region by code given in .txt file.

    Args:
        phone: str - phone number,
        database: str - database of region codes.

    Returns:
        str - region code or exception if the code is undefined.
    """
    if not is_phone_number(phone):
        raise Exception('Invalid phone number given.')
    with open(database, 'r') as db_file:
        lines = db_file.readlines()
    lines = [line.replace('\n', '').split('|') for line in lines]

    regions = dict(lines)
    for code in CODES:
        if phone.startswith(code):
            phone = phone[len(code):]
            break
    return regions.get(phone[:REGION_CODE_LENGTH]) or f'{phone[:REGION_CODE_LENGTH]} not defined in given database'
