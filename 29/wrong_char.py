def get_index_different_char(chars):
    index = None
    if len(chars) > 1:
        alnum = (str(chars[0]).isalnum()
                 and str(chars[-1]).isalnum())
        for idx, ch in enumerate(chars):
            if not str(ch).isalnum() == alnum:
                index = idx
                break       
        
    return index
