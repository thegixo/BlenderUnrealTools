# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

from . import ops_rig
from . import ui_panel

bl_info = {
    "name": "Gixo's UnrealEngine Tool",
    "description": "A tool for Unreal Engine users.",
    "author": "Gixo",
    "version": (0, 0, 5),
    "blender": (2, 80, 0),
    "location": "3D View > Tools",
    "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

modules = [ops_rig, ui_panel]


def register():

    for module in modules:
        module.register()


def unregister():

    for module in modules:
        module.unregister()


if __name__ == "__main__":
    register()
