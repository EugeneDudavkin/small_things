# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Add-on info
bl_info = {
    "name": "Object Data (multi)",
    "author": "APEC",
    "version": (0, 0, 2),
    "blender": (2, 93, 0),
    "location": "Select - Select Linked (multi)",
    "description": "Select Linked - Object Data for multiple selected objects", 
    "doc_url": "",
    "tracker_url": "",      
    "category": "Object" # Menu, Object, Collection, etc.
}

import bpy

###########################################################################################
##################################    Operators    ########################################
########################################################################################### 

class OBJECT_OT_select_linked_multi(bpy.types.Operator):
    bl_idname = "object.select_linked_multi"
    bl_label = "Object Data (multi)"
    #bl_description = "Select Linked (multi)"
    
    def execute(self, context):
        active_object = bpy.context.view_layer.objects.active

        for ob in context.selected_objects:
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.select_linked(extend=True, type='OBDATA')
        
        bpy.context.view_layer.objects.active = active_object
        return {'FINISHED'}

###########################################################################################
#####################################    UI    ############################################
########################################################################################### 

class VIEW3D_MT_select_linked_multi(bpy.types.Menu):
    bl_label = "Select Linked (multi)"
    bl_idname = "VIEW3D_MT_select_linked_multi"
    
    def draw(self, context):
        layout = self.layout
        
        layout.operator("object.select_linked_multi")

def add_menu(self, context):
    layout = self.layout
    #layout.separator()
    layout.menu(VIEW3D_MT_select_linked_multi.bl_idname)

def add_menu_single(self, context):
    self.layout.operator("object.select_linked_multi")
   
###########################################################################################
##################################### Register ############################################
########################################################################################### 	

def register(): 
    bpy.utils.register_class(OBJECT_OT_select_linked_multi)
    bpy.utils.register_class(VIEW3D_MT_select_linked_multi)
       
    # to appear at the top of menu list
    #bpy.types.VIEW3D_MT_select_object.prepend(add_menu)
    #bpy.types.VIEW3D_MT_select_object.prepend(add_menu_single)
    
    # to appear at the bottom of menu list
    bpy.types.VIEW3D_MT_select_object.append(add_menu)    
    #bpy.types.VIEW3D_MT_select_object.append(add_menu_single)    
    
def unregister():    
    bpy.utils.unregister_class(OBJECT_OT_select_linked_multi)
    bpy.utils.unregister_class(VIEW3D_MT_select_linked_multi)
    
    bpy.types.VIEW3D_MT_select_object.remove(add_menu)
    #bpy.types.VIEW3D_MT_select_object.remove(add_menu_single)
    
if __name__ == "__main__":
    register()