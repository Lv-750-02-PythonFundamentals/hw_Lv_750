def correct_tail(body, tail):
    last_letter = body[len(body) - 1:len(body)]
    if last_letter == tail:
        return True
    else:
        return False
