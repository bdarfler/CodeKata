import hashlib
import binascii


class BloomFilter(object):
    def __init__(self, filename=None):
        self.step = 3
        self.bit_array = [False] * pow(2, (8 * self.step))
        if filename:
            with open(filename) as f:
                for word in f:
                    self.insert(word.strip())

    @staticmethod
    def bytes2int(bytes):
        return int(binascii.hexlify(bytes), 16)

    def hashes(self, string):
        hash_val = hashlib.sha512(string.encode()).digest()
        return [self.bytes2int(hash_val[i:i + self.step]) for i in range(0, len(hash_val) - 1, self.step)]

    def insert(self, string):
        for hash_val in self.hashes(string.lower()):
            self.bit_array[hash_val] = True

    def contains(self, string):
        for hash_val in self.hashes(string.lower()):
            if not self.bit_array[hash_val]:
                return False
        return True