def hash_func(name: str):
    """DJB2 hash function"""
    hash_value = 5381

    for char in name:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    
    return hash_value & 0xFFFFFFFF