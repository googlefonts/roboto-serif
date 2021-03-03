from glob import glob
from ufoLib2 import Font

sources = glob("*.ufo")

for source in sources:
    source = Font(source)

    if not source.info.openTypeOS2Selection:
        source.info.openTypeOS2Selection = []
    if 7 not in source.info.openTypeOS2Selection:
        source.info.openTypeOS2Selection.append(7)

    if "openTypeOS2CodePageRanges":
        delattr(source.info, "openTypeOS2CodePageRanges")

    if "openTypeNameLicense":
        delattr(source.info, "openTypeNameLicense")

    if "openTypeOS2UnicodeRanges":
        delattr(source.info, "openTypeOS2UnicodeRanges")

    source.info.openTypeOS2TypoAscender = 750
    source.info.openTypeOS2TypoDescender = -250
    source.info.openTypeOS2TypoLineGap = 50

    source.info.openTypeHheaAscender = 750
    source.info.openTypeHheaDescender = -250
    source.info.openTypeHheaLineGap = 50
    source.save()
