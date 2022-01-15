#!/usr/bin/python


CMD_TERM = "!EOF!"

# stdout the cmd on the input text
def cmd_view(cmd, input_text):
    if not cmd:
        print(input_text)
    elif not input_text:
        print(cmd)
    else:
        print("%s<<%s\n%s\n%s"%(cmd, CMD_TERM, input_text, CMD_TERM));

