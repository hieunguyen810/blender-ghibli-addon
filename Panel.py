bl_info = {
    "name":"Ghibli",
    "author":"Hieunguyen810",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "description":"Ghibli style low poly grass, plants, flower",
    "location": "View3D",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh"
}

import bpy 
import os 

model_directory = "/home/hieunguyen/Documents/Blender_ghibli_addon/model/"

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        file_loc = model_directory + "daisy.obj"
        imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
        return {'FINISHED'}

class MainPanel(bpy.types.Panel):
    bl_label = "Ghibli"
    bl_idname = "MainPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ghibli"
    
    def draw (self, context):
        layout = self.layout
        row = layout.row()
        row.label(text = "Daisy", icon = 'CUBE')
        row.operator("mesh.primitive_cube_add")
        
class FlowerPanel(bpy.types.Panel):
    bl_label = "Flower"
    bl_idname = "FlowerPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Object"
    bl_parent_id = "MainPanel"
    bl_options = {'DEFAULT_CLOSED'}
    def import_object (self):
#        file_loc = "/home/hieunguyen/Documents/Blender/daisy.obj"
#        imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
        bpy.ops.file.make_paths_absolute()
        return {'FINISHED'}
    def draw (self, context):
        layout = self.layout
        row = layout.row()
        row.label(text = "Daisy", icon = 'FREEZE')
        row.operator(SimpleOperator.bl_idname, text = "Add")
        
   
classes = (MainPanel, FlowerPanel, SimpleOperator)   
     
def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
