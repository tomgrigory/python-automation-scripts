import re
def rearrange_name(name):
    result = re.search(r"^([\w ,-]), ([\w .-]*)$")
    if result is None:
        result = ""
    return (f"{result[2], result[1]}")


rearrange_name("shibu", "kannnadevan")
