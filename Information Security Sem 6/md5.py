def simplified_md5(message):
    # Define initial hash values
    a = 0x01234567
    b = 0x89abcdef
    c = 0xfedcba98
    d = 0x76543210

    # Process each byte of the message
    for byte in message:
        # Update hash values with a simple XOR operation
        a ^= byte
        b ^= byte
        c ^= byte
        d ^= byte
    
        #permutation step
        c=b
        d=c
        a=d
        b=a^c^d

    # Concatenate the hash values
    digest = (a << 96) | (b << 64) | (c << 32) | d
    return digest.to_bytes(16, 'little')

# Example usage:
message = b"Hello, world!"
hashed_message = simplified_md5(message)
print(hashed_message.hex())