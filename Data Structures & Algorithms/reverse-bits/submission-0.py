class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        # int("1010", 2)  # binary → decimal
        # int("1010", 10) # decimal → decimal
        # int("A", 16)    # hexadecimal → decimal
        rev_binary = binary[::-1]
        decimal = int(rev_binary, 2)

        return decimal