import re

from preprocessing.PREP import PREP

def default(text):
    ret = ""
    if text == None:
        return ret
    var_cnt = 0
    delimited = re.split("((?:```[^`]*```)|(?:`[^`]*`))", text)
    for match in delimited:
        if not match:
            continue
        if re.match("(```[^`]*```)", match):
            cmd = match[3:-3].strip()
            ret += "%s\n"%(cmd)
        elif re.match("(`[^`]*`)", match):
            cmd = match[1:-1].strip()
            ret += "printf \"%s\" \"$(%s)\"\n"%('%s', cmd)
        else:
            ret += "printf \"%s\"\n"%(match)
    ret += "printf '\\n'"
    return ret

default_preprocessor = PREP \
(
    'default',
    'executes inline and standalone commands while catting input',
    default,
)
