def respon(input):
    user_input = str(input).lower()

    if user_input in ('hello','hi'):
        return "hey how's it"

    if user_input in ('who are you?'):
        return "im nama_bot"

    return "Ga ngerti ah"