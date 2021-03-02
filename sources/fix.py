from glob import glob
from ufoLib2 import Font

sources = glob("*.ufo")

for source in sources:
    source = Font(source)
#    if not source.info.openTypeOS2Selection:
#        source.info.openTypeOS2Selection = []
#    if 7 not in source.info.openTypeOS2Selection:
#        source.info.openTypeOS2Selection.append(7)
    delattr(source.info, "openTypeNameLicense")

#    source.info.openTypeOS2TypoAscender = 1900
#    source.info.openTypeOS2TypoLineGap = -500
#    source.info.openTypeOS2TypoDescender = 0
#
#    source.info.openTypeHheaAscender = 1900
#    source.info.openTypeHheaDescender = -500
#    source.info.openTypeHheaLineGap = 0
    source.save()
