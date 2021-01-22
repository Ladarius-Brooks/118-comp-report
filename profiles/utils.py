import uuid 

def get_irregular_code():
    code = str(uuid.uuid4())[:8].replace('-','').lower()
    return code