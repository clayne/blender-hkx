import bpy

class ArmatureProperties(bpy.types.PropertyGroup):
    skeleton_path: bpy.props.StringProperty(
        name="Skeleton",
        description="Path to the HKX skeleton file",
        subtype='FILE_PATH')

class ArmaturePanel(bpy.types.Panel):
    """Panel for the Armature properties window"""
    bl_label = "HKX Export"
    bl_idname = "DATA_PT_io_hkx"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    
    @classmethod
    def poll(cls, context):
        return (context.object and context.object.type == 'ARMATURE')
    
    def draw(self, context):
        self.layout.prop(context.object.data.iohkx, "skeleton_path")

def register():
    bpy.utils.register_class(ArmatureProperties)
    bpy.utils.register_class(ArmaturePanel)
    bpy.types.Armature.iohkx = bpy.props.PointerProperty(type=ArmatureProperties)

def unregister():
    del bpy.types.Armature.iohkx
    bpy.utils.unregister_class(ArmaturePanel)
    bpy.utils.unregister_class(ArmatureProperties)