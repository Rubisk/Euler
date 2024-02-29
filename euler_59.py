import sys
import pytest
import copy

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTRUVWXYZ() "

def decrypt(key, string):
    # key = [ord(c) for c in key]
    decrypted = ""
    assert len(key) == 3
    for i in range(len(string)):
        c = chr(string[i] ^ key[i % 3])
        decrypted += c
    return decrypted


def find_possible_keys(string, key_length, ascii_min, ascii_max):
    keys = []
    for i in range(key_length):
        character = string[i]
        keys.append([])
        for j in range(ascii_min, ascii_max):
            if chr(character ^ j) in ALLOWED_CHARS:
                keys[i].append(j)
    print keys
    to_return = [[x] for x in keys[0]]
    for x in range(1, key_length):
        new_to_return = []
        for key in keys[x]:
            for t in to_return:
                t = copy.copy(t)
                t.append(key)
                new_to_return.append(t)
        to_return = new_to_return
    return to_return


def decrypt_file(filename, *args):
    string = [int(x) for x in open(filename).read().split(',')]
    z = find_possible_keys(string, *[int(x) for x in args])
    for x in z:
        d = decrypt(x, string[:15])
        if all([c in ALLOWED_CHARS for c in d]):
            print decrypt(x, string)

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        decrypt_file(*sys.argv[1:])