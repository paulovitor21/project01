import hashlib

def generate_hash(temp_id, status, group, item, arrival_1):
    """
    Gera um hash único com base em campos específicos.
    """
    # Garantir que todos os valores sejam strings

    # Concatenar os campos com um separador para evitar colisões
    hash_input = f"{temp_id}|{status}|{group}|{item}|{arrival_1}"
    return hashlib.md5(hash_input.encode()).hexdigest()
