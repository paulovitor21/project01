import hashlib

def generate_hash(model_suffix, org, date):
    """
    Gera um hash único com base em campos específicos.
    """
    hash_input = f"{model_suffix}|{org}|{date}"
    return hashlib.md5(hash_input.encode()).hexdigest()
