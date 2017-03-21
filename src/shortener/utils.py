import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for i in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    # This line is the same as the four lines above, just condensed
    return ''.join(random.choice(chars) for _ in range(size))