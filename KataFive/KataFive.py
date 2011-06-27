import hashlib
import binascii

class BloomFilter:

    def __init__(self):
        self.step = 3
        self.bit_array = [False]*pow(2,(8*self.step))
    
    def bytes2int(self, bytes):
        return int(binascii.hexlify(bytes), 16) 
    
    def hashes(self, string):
        hash_val = hashlib.sha512(string.encode()).digest()
        return [self.bytes2int(hash_val[i:i+self.step]) for i in range(0, len(hash_val) - 1, self.step)]    
    
    def insert(self, string):
        for hash_val in self.hashes(string):
            self.bit_array[hash_val] = True
        
    def contains(self, string):
        for hash_val in self.hashes(string):
            if not self.bit_array[hash_val]: return False
        return True