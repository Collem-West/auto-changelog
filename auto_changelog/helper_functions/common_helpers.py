def words_in_message(msg: str, words: list) -> bool:
    """
    Checks ignored words in commit message

    :param msg: commit message
    :param words: list of ignored words
    """
    for word in words:
        if word.lower() in msg.lower():
            return True

    return False
