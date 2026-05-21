import bpy
import os

EXPORT_PATH = os.path.expanduser("~/SilkRoadRPG/Assets/")

def export_selected_mesh(subfolder="Characters"):
    obj = bpy.context.active_object
    if not obj:
        print("No object selected!")
        return
    path = os.path.join(EXPORT_PATH, subfolder, obj.name + ".fbx")
    bpy.ops.export_scene.fbx(
        filepath=path,
        use_selection=True,
        mesh_smooth_type='FACE',
        use_mesh_modifiers=True,
        bake_anim=True,
        axis_forward='-Z',
        axis_up='Y',
        global_scale=1.0
    )
    print(f"Exported: {path}")

export_selected_mesh()
