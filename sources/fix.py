from glob import glob
from defcon import Font

sources = glob("*.ufo")

for source in sources:
    source = Font(source)
    import pdb
    pdb.set_trace()
    if not source.info.openTypeOS2Selection:
        source.info.openTypeOS2Selection = []
    if 7 not in source.info.openTypeOS2Selection:
        source.info.openTypeOS2Selection.append(7)

    source.info.openTypeOS2TypoAscender = 1900
    source.info.openTypeOS2TypoLineGap = -500
    source.info.openTypeOS2TypoDescender = 0

    source.info.openTypeHheaAscender = 1900
    source.info.openTypeHheaDescender = -500
    source.info.openTypeHheaLineGap = 0
    source.save()
    print(source.info.openTypeOS2Selection)
