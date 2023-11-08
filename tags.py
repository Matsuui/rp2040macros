# Mac Finder Tags macros
# Up to 7 tags can be used. These 7 tags are selected in the finder settings as your favorite tags.
# The 'Finder' macro uses HotKeys to open finder.


from adafruit_hid.keycode import Keycode


app = {  # REQUIRED dict, must be named 'app'
    "name": "Tags",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, "Favorites", [Keycode.CONTROL, "1"]),
        (0xFFA500, "2", [Keycode.CONTROL, "2"]),
        (0xFFFF00, "3", [Keycode.CONTROL, "3"]),
        # 2nd row ----------
        (0x00FF00, "4", [Keycode.CONTROL, "4"]),
        (0x0000FF, "5", [Keycode.CONTROL, "5"]),
        (0x800080, "6", [Keycode.CONTROL, "6"]),
        # 3rd row ----------
        (0x808080, "7", [Keycode.CONTROL, "7"]),
        (0x000000, "", [Keycode.CONTROL, ]),
        (0x00FFFF, "Finder", [Keycode.CONTROL, Keycode.COMMAND, Keycode.ALT, Keycode.SHIFT, "f"]),
        # 4th row ----------
        (0xFF0000, "Favorites", [Keycode.CONTROL, "1"]),
        (0xFF0000, "L", [Keycode.LEFT_ARROW]),
        (0x00FF00, "R", [Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, ]),
    ],
}
