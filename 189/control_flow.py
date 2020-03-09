IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    
    def _have_digits(name):
        digits = "0123456789"
        result = False
        for ch in name:
            if ch in digits:
                result = True
                break
        return result
    
    
    count = 0
    for name in names:
        if (name.startswith(QUIT_CHAR) or
            count >= MAX_NAMES):
            break
        else:
            if (name.startswith(IGNORE_CHAR) or
                _have_digits(name)):
                continue
            count += 1
            yield name
