import bpy
import subprocess


class HoudiniPanel(bpy.types.Panel):
    bl_idname = "Houdini_Panel"
    bl_label = "Houdini Tools"  # This is the name of the tab displayed in n-bar
    bl_category = "Houdini"  # This is the name of the tab displayed in n-bar
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.send_to_houdini", text="Send to Houdini")


class SendToHoudini(bpy.types.Operator):
    bl_idname = "object.send_to_houdini"
    bl_label = "Send to Houdini"

    def execute(self, context):
        fbx_path = "C:/Users/Harshaan/Desktop/hoo.fbx"
        bpy.ops.export_scene.fbx(filepath=fbx_path, use_selection=True)

        houdini_path = "C:/Program Files/Side Effects Software/Houdini 19.5.640/bin/houdinifx.exe"
        cmd = [houdini_path, fbx_path]

        return {'FINISHED'}


def register():
    bpy.utils.register_class(HoudiniPanel)
    bpy.utils.register_class(SendToHoudini)


def unregister():
    bpy.utils.unregister_class(HoudiniPanel)
    bpy.utils.unregister_class(SendToHoudini)


if __name__ == "__main__":
    register()
