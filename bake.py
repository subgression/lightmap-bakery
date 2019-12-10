import bpy
import bmesh
import sys
import argparse

# Reading argv
parser = argparse.ArgumentParser()
parser.add_argument("--s")
parser.add_argument("--lms")
parser.add_argument("--ap")
parser.add_argument("--bp")
parser.add_argument("-b")
parser.add_argument("-P")
args = parser.parse_args()

# Setting the right atlas and lightmappare values
atlas_size = args.s
lightmapper_samples = args.lms
bpy.data.scenes["Scene"].cycles.samples = int(lightmapper_samples)
atlas_size = int(atlas_size)
atlas_path = args.ap
bake_path = args.bp

print("# Starting bake process")

for ob in bpy.data.objects:
    if ob.type == 'MESH':
        ob.select = True
        bpy.context.scene.objects.active = ob
    else:
        ob.select = False

print("# Joining meshes")
bpy.ops.object.join()

print("# Creating texture atlas")
atlas = bpy.data.images.new("atlas", atlas_size, atlas_size)

print("# Switching to Cycles rendering engine")
bpy.context.scene.render.engine = 'CYCLES'

print("# Getting all materials")
selected_mesh = bpy.context.selected_objects
all_mat = bpy.data.materials
all_mat_count = len(all_mat)
print("# Found " + str(all_mat_count) + " materials to bake")

print ("# Generating Lightmap UV on channel 2")
#bpy.ops.mesh.uv_texture_add()
lm = selected_mesh[0].data.uv_textures.new("lightmap")
lm.active = True

print ("# Unwrapping LightmapUVs using Lightmap pack")
bpy.ops.object.editmode_toggle()

bm = bmesh.from_edit_mesh(selected_mesh[0].data)
for f in bm.faces:
    f.select = True

bpy.ops.uv.lightmap_pack(
    PREF_IMG_PX_SIZE=2048,
    PREF_BOX_DIV=48,
    PREF_MARGIN_DIV=0.3
)
bpy.ops.object.editmode_toggle()

print ("# Switching materials to nodes")
for mat in all_mat:
    mat.use_nodes = True
    matnodes = mat.node_tree.nodes
    #new texture
    tex = matnodes.new('ShaderNodeTexImage')
    tex.image = atlas
    tex.select = True
    mat.node_tree.nodes.active = tex

print("# Starting bake")
bpy.ops.object.bake(type='COMBINED')

print("# Packing and saving image")
atlas.pack(as_png=True)
atlas.filepath = atlas_path
atlas.file_format = "PNG"
atlas.save()

print("# Saving blend file as new one")
bpy.ops.wm.save_as_mainfile(filepath=bake_path)
