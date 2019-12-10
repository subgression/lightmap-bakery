import sys
import os
import xml.dom.minidom

blender_file_path = "/Applications/Blender/blender.app/Contents/MacOS/blender"
bake_file = xml.dom.minidom.parse("./bake_file.xml")
files_to_bake = bake_file.getElementsByTagName("file")

print("N. of files to bake: " + str(len(files_to_bake)))
for fb in files_to_bake:
    file_path = str(fb.getElementsByTagName("path")[0].firstChild.nodeValue)
    lightmapper_samples = str(fb.getElementsByTagName("lightmapper_samples")[0].firstChild.nodeValue)
    atlas_size = str(fb.getElementsByTagName("atlas_size")[0].firstChild.nodeValue)
    atlas_path = str(fb.getElementsByTagName("atlas_path")[0].firstChild.nodeValue)
    baked_path = str(fb.getElementsByTagName("baked_path")[0].firstChild.nodeValue)
    print("Preparing bake for file: " + file_path)
    print("Atlas size: " + atlas_size)
    print("Lighmapper samples: " + lightmapper_samples)
    print("Atlas path: " + atlas_path)
    print("Baked blend file path" + baked_path)
    cmd = blender_file_path + " -b " + file_path + " -P bake.py --s " + atlas_size + " --lms " + lightmapper_samples + " --ap " + atlas_path + " --bp " + baked_path
    os.system(cmd)