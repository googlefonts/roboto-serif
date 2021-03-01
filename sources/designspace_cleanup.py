"""
Create a GF Compliant designspace
"""
import sys
from fontTools.designspaceLib import DesignSpaceDocument, InstanceDescriptor

WEIGHT = {
    100: "Thin",
    200: "ExtraLight",
    300: "Light",
    400: "Regular",
    500: "Medium",
    600: "SemiBold",
    700: "Bold",
    800: "ExtraBold",
    900: "Black",
}


if len(sys.argv) != 2:
    print("Usage: python designspace_cleanup.py mydesignspace.designspace")
    sys.exit(1)

designspace_file = sys.argv[1]

ds = DesignSpaceDocument()
ds.read(designspace_file)

is_italic = "Italic" in designspace_file or any(a.tag in ["ital", "slnt"] for a in ds.axes)
dflt_coords = {a.name: a.default for a in ds.axes}
wght_axis = next((a for a in ds.axes if a.tag == "wght"), None)
wght_min = wght_axis.minimum
wght_max = wght_axis.maximum


new_instances = []
for wght in range(int(wght_min), int(wght_max)+100, 100):
    i = InstanceDescriptor()
    i.familyName = "Roboto Serif"
    location = dflt_coords
    location["weight"] = wght

    if is_italic:
        i.styleName = f"{WEIGHT[wght]} Italic"
    else:
        i.styleName = f"{WEIGHT[wght]}"
    i.location = location
    new_instances.append(i)


ds.instances = new_instances
ds.write(designspace_file)
print("Updated designspace")
