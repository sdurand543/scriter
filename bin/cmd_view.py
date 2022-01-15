#!/usr/bin/python

# stdout the cmd on the input text
def cmd_view(cmd, input_text):
    if not cmd:
        print(input_text)
    elif not input_text:
        print(cmd)
    else:
        print("%s<<EOF\n%s\nEOF"%(cmd, input_text));

