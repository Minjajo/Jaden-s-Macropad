print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.row_pins = (board.GP7, board.GP8, board.GP9, board.GP10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [ # Start of the map
    [ # Layer 0 (The default layer)
        KC.N7,   KC.N8,   KC.N9,   KC.PSLS,  
        KC.N4,   KC.N5,   KC.N6,   KC.PAST,  
        KC.N1,   KC.N2,   KC.N3,   KC.PMNS,  
        KC.N0,   KC.DOT,  KC.PENT, KC.PPLS,  
    ]
]

rgb = RGB(
    pixel_pin=board.GP6,     
    num_pixels=16,           
    rgb_order=(1, 0, 2),    
    val_limit=100,           
    hue_default=0,           
    sat_default=255,         
    val_default=50,          
)

if __name__ == '__main__':
    keyboard.go()
