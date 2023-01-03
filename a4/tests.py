"""
This is just a file i made with some public and private key pairs that can be used to check
that certain messages encrypt and decrypt properly using the block method I programmed in
a4_part3.py
"""


# TODO delete these keys, just using them for testing with 'hi'
# [1922208, 1607228, 2160456, 1453557] after rsa encryption step
# rsa_encrypt_block(public_key5, 'hi')
# k = 1
private_key5 = (13, 11, 89)
public_key5 = (143, 89)

# TODO delete these keys, just using them for testing with 'hello there!'
# [13413, 13932, 14240, 14952, 13042, 12961] before rsa encryption step
# [1258, 10622, 5593, 11081, 14617, 17083] after rsa encryption step
# rsa_encrypt_block(public_key2, 'hello there!')
# k = 2
private_key2 = (139, 149, 5215)
public_key2 = (20711, 3607)

# TODO delete these keys later, just using them for testing with 'Hello David and Tom!!'
# rsa_encrypt_block(public_key, 'Hello David and Tom!!')
# 128^k <= n Must be satisfied
# k = 3
private_key = (7907, 7919, 3331951)
public_key = (62615533, 2265891)

# TODO delete these keys, just using them for testing with 'i am lost'
# [1922208, 1607228, 2160456, 1453557] after rsa encryption step
# rsa_encrypt_block(public_key3, 'i am lost')
# rsa_decrypt_block(private_key3, [1505923, 1667708, 574033])
# k = 3
private_key3 = (1601, 1447, 1584407)
public_key3 = (2316647, 418343)

# TODO delete these keys, just using them for testing with 'this algorithm is cool!!'
# [1922208, 1607228, 2160456, 1453557] after rsa encryption step
# rsa_encrypt_block(public_key4, 'this algorithm is cool!!')
# k = 3
private_key4 = (6959, 6961, 25944739)
public_key4 = (48441599, 7924459)

# TODO delete these keys, just using them for testing with 'this algorithm is cool!!'
# [1922208, 1607228, 2160456, 1453557] after rsa encryption step
# rsa_encrypt_block(public_key6, '\x00\x00lawnmowers are useless \x00\x00\x00 in the winter in canada')
# k = 4
private_key6 = (19207, 19211, 113652017)
public_key6 = (368985677, 245514293)
