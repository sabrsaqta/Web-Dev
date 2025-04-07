def squirrel_party(nuts, is_weekend):
    if is_weekend and nuts >= 40:
        return True
    elif not is_weekend and nuts in range(40,61):
        return True
    return False