# Mac Homework macros
# This macro layer uses HotKey macros to open apps
# The browser shortcuts (row 1-2) are specifically Arc shortcuts but most work on any mac browser

from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


app = {  # REQUIRED dict, must be named 'app'
    "name": "Homework",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xF9ED69, "New Tab", [Keycode.COMMAND, "t"]),
        (0xF9ED69, "Split", [Keycode.CONTROL, Keycode.SHIFT, "="]),
        (0xF9ED69, "Refresh", [Keycode.COMMAND, "r"]),
        # 2nd row ----------
        (0xF08A5D, "Close", [Keycode.COMMAND, "w"]),
        (0xF08A5D, "Restore", [Keycode.COMMAND, Keycode.SHIFT, "t"]),
        (0xF08A5D, "Find", [Keycode.COMMAND, 'f']),  #
        # 3rd row ----------
        (0xB83B5E, "<<", [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0xB83B5E, "Play/Pause", [[ConsumerControlCode.PLAY_PAUSE]]),
        (0xB83B5E, ">>", [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # 4th row ----------
        (
            0x6A2C70,
            "New Doc",
            [
                Keycode.CONTROL,
                Keycode.SHIFT,
                "=",
                -Keycode.CONTROL,
                -Keycode.SHIFT,
                "docs.new\n",
            ],
        ),
        (
            0x6A2C70,
            "GPT",
            [
                Keycode.CONTROL,
                Keycode.SHIFT,
                "=",
                -Keycode.CONTROL,
                -Keycode.SHIFT,
                "chat.openai.com\n",
            ],
        ),
        (0x6A2C70, "Notion", [Keycode.CONTROL, Keycode.COMMAND, Keycode.SHIFT, "n"]),
        # Encoder button ---
        (
            0x000000,
            "",
            [
                Keycode.CONTROL,
                Keycode.COMMAND,
                Keycode.ALT,
                Keycode.SHIFT,
                "m",
                -Keycode.CONTROL,
                -Keycode.COMMAND,
                -Keycode.ALT,
                -Keycode.SHIFT,
                Keycode.COMMAND,
                "l",
            ],
        ),  # Apple Music Hotkey, opens to current song's album
    ],
}
