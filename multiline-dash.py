SCRIPT_NAME    = "multiline-dash"
SCRIPT_AUTHOR  = "eyJhb <eyjhbb@gmail.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPLv3"
SCRIPT_DESC    = "Replaces dashdash (--) with a two newlines instead symbol"

import_ok = True

try:
   import weechat as w
except:
   print "Script must be run under weechat. http://www.weechat.org"
   import_ok = False

def convert_dash_to_newline(data, modifier, modifier_data, string):
    string = string.replace(" -- ", "--")
    return string.replace("--", "\n\n")

if __name__ == "__main__" and import_ok:
    if w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
                  SCRIPT_DESC, "", "utf-8"):

        w.hook_modifier("input_text_for_buffer", "convert_dash_to_newline", "")
