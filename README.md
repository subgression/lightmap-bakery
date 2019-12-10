# lightmap-bakery
- Python tool that allow to bake lightmaps for multiple blender files using cycles rendering engine
- It will always create a new UVMap called 'lightmap' before unwrapping so it won't screw up any textured materials
- Works well even if the entire scene is built using the Blender rendering engine
- Works only on static object (atm) because the script needs to join all the meshes before creating the lightmap

# Why using lightmap-bakery?
I'm currently using this script to bake multiple maps for a mobile game i'm working on without having to join the mesh, switch manually to cycles and setting up the bake procedure (Adding the texture atlas on all the materials in the scene, generating the lightmap, etc...), with this script i can bake all the maps that i need while working on other stuff, I just simply create the bake_file and than let the script handle the rest

# Usage
- Edit (or create) the bake_file.xml that the script will use to find all the .blend files to bake
- Run `python batch_bake.py`
- Have a cup of :coffee:
- Profit

# Nodes
+ `lightmapper_samples`: The number of samples used by the cycles rendering engine
+ `atlas_size`: The size of the lightmapper atlas
+ `path`: The path for the blender file to bake
+ `atlas_path`: The path where the atlas lightmap will be saved
+ `baked_path`: The path where the baked
