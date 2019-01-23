# Copyright (C) 2019 Enikeishik <enikeishik@gmail.com>.
# All rights reserved.
#
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


bl_info = {
    "name": "Origin to select",
    "description": "Moves origin of selected object into selected part (v/e/f) of object",
    "author": "enikeishik",
    "category": "Mesh",
}


import bpy


class OriginToSelect(bpy.types.Operator):
    """Origin of selected moving script"""
    bl_idname = "mesh.origin_to_select"
    bl_label = "Move origin to select"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                cursor3d_location = bpy.context.scene.cursor_location.copy()
                
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
                bpy.ops.view3d.snap_cursor_to_selected(ctx)
                
                bpy.ops.object.mode_set(mode='OBJECT')
                
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                
                bpy.context.scene.cursor_location = cursor3d_location
                
                bpy.ops.object.mode_set(mode='EDIT')
                
                break
        
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OriginToSelect.bl_idname)


def register():
    bpy.utils.register_class(OriginToSelect)
    bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OriginToSelect)


if __name__ == "__main__":
    register()
