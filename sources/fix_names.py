# TODO Drop this and update designspace + ufos sources properly
from fontTools.ttLib import TTFont
import os

fonts_dir = os.path.join(os.path.dirname(__file__), "..", "fonts", "variable")
version = 1.004
license = "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL"

# Roman
roman = TTFont(os.path.join(fonts_dir, "RobotoSerif[GRAD,opsz,wdth,wght].ttf"))
roman_name = roman['name']
roman_name.setName("Roboto Serif 20pt", 1, 3, 1, 0x409)
roman_name.setName("Regular", 2, 3, 1, 0x409)
roman_name.setName(f"{version};COMM;RobotoSerif-20ptRegular", 3, 3, 1, 0x409)
roman_name.setName("Roboto Serif 20pt Regular", 4, 3, 1, 0x409)
roman_name.setName("RobotoSerif-20ptRegular", 6, 3, 1, 0x409)
roman_name.setName(license, 13, 3, 1, 0x409)
roman_name.setName("Roboto Serif", 16, 3, 1, 0x409)
roman_name.setName("20pt Regular", 17, 3, 1, 0x409)

# Italic
italic = TTFont(os.path.join(fonts_dir, "RobotoSerif-Italic[GRAD,opsz,wdth,wght].ttf" ))
italic_name = italic['name']
italic_name.setName("Roboto Serif 20pt", 1, 3, 1, 0x409)
italic_name.setName("Italic", 2, 3, 1, 0x409)
italic_name.setName(f"{version};COMM;RobotoSerifNormalItalic-Regular", 3, 3, 1, 0x409)
italic_name.setName("Roboto Serif 20pt Italic", 4, 3, 1, 0x409)
italic_name.setName("RobotoSerif-20ptItalic", 6, 3, 1, 0x409)
italic_name.setName(license, 13, 3, 1, 0x409)
italic_name.setName("Roboto Serif", 16, 3, 1, 0x409)
italic_name.setName("20pt Italic", 17, 3, 1, 0x409)


roman.save(roman.reader.file.name)
italic.save(italic.reader.file.name)
print("Done fixing names")
