CMD_TERM = "!EOF!"

def cmd_view(cmd, input_text):
    """
    stdout the cmd on the input text
    """
    if not cmd:
        print(input_text)
    else:
        if input_text:
            print("%s<<%s\n%s\n%s"%(cmd, CMD_TERM, input_text, CMD_TERM))
        else:
            print("%s<<%s\n%s"%(cmd, CMD_TERM, CMD_TERM))
        


