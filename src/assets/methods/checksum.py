import hmac
import hashlib


class checksum:
    def __init__(self):
        pass
    
    def get_checksum(self, encrypted_data, key):
        return hmac.new(key, encrypted_data, hashlib.sha3_256).hexdigest()
    
    def check(self, encrypted_data, key, received_signature):
        return hmac.compare_digest(
            self.get_checksum(encrypted_data, key),
            received_signature
        )