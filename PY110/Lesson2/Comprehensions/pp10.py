import secrets

def generate_uuid():
    hex_string  = secrets.token_hex(16)
    uuid = f'{hex_string[:8]}-{hex_string[8:12]}-{hex_string[12:16]}-{hex_string[16:20]}-{hex_string[20:]}'  # 8-4-4-4-12
    return uuid

# Alternative:
# 
# import random
# 
# def generate_uuid():
#     hex_chars = '0123456789abcdef'
#     uuid_structure = [8, 4, 4, 4, 12]
#     uuid = []
#
#     for length in uuid_structure:
#         random_sequence = [random.choice(hex_chars) for _ in range(length)]
#         uuid.append(''.join(random_sequence))
#    
#     return '-'.join(uuid)
#

print(generate_uuid())
print(generate_uuid())
