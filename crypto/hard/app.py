from Crypto.PublicKey import RSA
from Crypto.Util.number import getPrime, bytes_to_long
import binascii

tower1 = getPrime(512)
tower2 = tower1 + 4  # Sentinels stand near
walls = tower1 * tower2
lock = 65537
keyhole = (tower1 - 1) * (tower2 - 1)
unlock = pow(lock, -1, keyhole)

fortress = RSA.construct((walls, lock, unlock, tower1, tower2))
with open("sentinel.pem", "wb") as f:
    f.write(fortress.publickey().export_key())

treasure = b"CIR{T0P_T34R_5TUFF}"
vault = pow(bytes_to_long(treasure), lock, walls)
with open("locked_vault.txt", "w") as f:
    f.write(binascii.hexlify(vault.to_bytes((vault.bit_length() + 7) // 8, 'big')).decode())