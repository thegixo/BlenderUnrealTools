import bpy

from bpy.types import Panel


class GUE_PT_gue_tool_ui(Panel):
    bl_label = "GUE Tool"
    bl_idname = "gue_tool_ui"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GUE Tool"
    bl_context = "objectmode"

    @classmethod
    def poll(self, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.label(text="Rig Operations")
        col.operator("object.fix_rig_scale")


classes = [GUE_PT_gue_tool_ui]


def register():

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
