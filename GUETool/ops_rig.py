import bpy

from bpy.types import Operator


class GUE_OT_fix_rig_scale(Operator):
    bl_label = "Fix Rig Scale for UE"
    bl_idname = "object.fix_rig_scale"

    def execute(self, context):

        if bpy.context.object.type == "ARMATURE":

            # Getting every child of the armature and clearing their parent
            children = list(bpy.context.object.children)
            with bpy.context.temp_override(selected_editable_objects=children):
                bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")

            # Fixing the scale
            bpy.ops.object.transform_apply(location=True,
                                           rotation=True,
                                           scale=True
                                           )
            bpy.ops.transform.resize(value=(100, 100, 100))
            bpy.ops.object.transform_apply(location=True,
                                           rotation=True,
                                           scale=True
                                           )
            bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))

            # Re-adding object as children to the armature
            with bpy.context.temp_override(selected_editable_objects=children):
                bpy.ops.object.parent_set(type='ARMATURE')

            self.report({"INFO"}, "Operation is done successfully")

        else:
            self.report({"ERROR"}, "Selected object is not an armature")

        return {"FINISHED"}


classes = [GUE_OT_fix_rig_scale]


def register():

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
