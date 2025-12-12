# aquarium_blender.py
# Starter script for Blender: creates camera, lights, and simple placeholder objects
# Usage: open new Blender scene, open this script in Text Editor, Run Script.

import bpy, json, math
from mathutils import Vector, Euler

# ---- helper ----
def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def add_cube(name, size, loc, material=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = (size[0]/2, size[1]/2, size[2]/2)
    if material:
        if material not in bpy.data.materials:
            mat = bpy.data.materials.new(material)
        else:
            mat = bpy.data.materials[material]
        obj.data.materials.append(mat)
    return obj

# ---- clear ----
clear_scene()

# ---- scene setup ----
# units: metric, meters
bpy.context.scene.unit_settings.system = 'METRIC'
bpy.context.scene.unit_settings.length_unit = 'METERS'

# camera
cam_data = bpy.data.cameras.new("Cam")
cam = bpy.data.objects.new("Camera", cam_data)
bpy.context.collection.objects.link(cam)
cam.location = ( -1.5, -4.0, 1.6 )
cam.rotation_euler = Euler((math.radians(70), 0, math.radians(20)), 'XYZ')
bpy.context.scene.camera = cam

# light
light_data = bpy.data.lights.new("Sun", type='AREA')
light = bpy.data.objects.new("Sun", light_data)
bpy.context.collection.objects.link(light)
light.location = (0, -3, 4)
light.data.energy = 500

# create aquarium box (internal dimensions from JSON)
# Default units: meters; aquarium in JSON is in cm, so convert
aq_w = 1.20  # m (120 cm)
aq_d = 0.40  # m
aq_h = 0.50  # m
# create glass box (thin)
glass = add_cube("Aquarium_Box", (aq_w, aq_d, aq_h), (0.0, 0.0, aq_h/2))

# material glass
glass_mat = bpy.data.materials.new("GlassMat")
glass_mat.use_nodes = True
nodes = glass_mat.node_tree.nodes
nodes.clear()
output = nodes.new(type='ShaderNodeOutputMaterial')
glass_shader = nodes.new(type='ShaderNodeBsdfGlass')
glass_shader.inputs['Color'].default_value = (0.85, 0.93, 1.0, 1.0)
glass_shader.inputs['Roughness'].default_value = 0.05
glass_mat.node_tree.links.new(glass_shader.outputs[0], output.inputs[0])
glass.data.materials.append(glass_mat)

# placeholder rock cave
rock = add_cube("Rock_Cave", (0.40, 0.22, 0.20), ( -0.3, 0.0, 0.10 ), material="RockMat")
rock_mat = bpy.data.materials.new("RockMat")
rock_mat.diffuse_color = (0.8,0.75,0.65,1)
rock.data.materials.clear()
rock.data.materials.append(rock_mat)

# placeholder roots
r1 = add_cube("Root_Left", (0.22,0.08,0.45), (-0.45, 0.05, 0.22), material="WoodMat")
r2 = add_cube("Root_Center", (0.45,0.09,0.18), (0.0, 0.0, 0.18), material="WoodMat")
r3 = add_cube("Root_Right", (0.30,0.08,0.22), (0.45, -0.05, 0.2), material="WoodMat")
wood = bpy.data.materials.new("WoodMat")
wood.diffuse_color = (0.22,0.12,0.06,1)
for o in [r1,r2,r3]:
    o.data.materials.clear()
    o.data.materials.append(wood)

# done
print("Starter scene created. Replace placeholders with real meshes and import aquarium_scene.json for exact positions.")