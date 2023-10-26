def validUTF8(data):
    byts_remaining = 0
    for item in data:
        binary_char = format(item, '08b')
        if byts_remaining == 0:
            if binary_char.startswith("0"):
                continue
            elif binary_char.startswith("110"):
                byts_remaining = 1
            elif binary_char.startswith("1110"):
                byts_remaining = 2
            elif binary_char.startswith("11110"):
                byts_remaining = 3
            else:
                return False, "Invalid start byte"
        else:
            if binary_char.startswith("10"):
                byts_remaining -= 1
                continue
            return False, "Invalid continuation byte"
    
    if byts_remaining > 0:
        return False, "Incomplete UTF-8 sequence"
    
    return True, "Valid UTF-8 sequence"
