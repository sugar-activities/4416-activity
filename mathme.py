#!/usr/bin/env python
#-*-coding: utf-8 -*-
# Copyright (C) 2011, Hiram Jeronimo Perez <worg@linuxmail.org>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging
from random import randint, randrange
from gettext import gettext as _

import gtk
import mynum

from sugar.activity import activity
from sugar import env


try:
    from sugar.graphics.toolbarbox import ToolbarBox
    from sugar.graphics.toolbarbox import ToolbarButton
    from sugar.activity.widgets import ActivityToolbarButton
    from sugar.activity.widgets import StopButton
    NEW_TOOLBARS = True
except ImportError:
    from sugar.activity.activity import ActivityToolbox
    NEW_TOOLBARS = False

log = logging.getLogger('MathMe')
log.setLevel(logging.DEBUG)
logging.basicConfig()


class MathMe(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self._name = handle

        self._main_view = gtk.VBox()

        self.num = mynum.Numbers()
        
        if NEW_TOOLBARS:
            toolbar_box = ToolbarBox()
            
            separator = gtk.SeparatorToolItem()
            separator.props.draw = False
            separator.set_expand(True)
            toolbar_box.toolbar.insert(separator, -1)
            separator.show()
               
            stop_button = StopButton(self)
            stop_button.props.accelerator = '<Ctrl><Shift>Q'
            toolbar_box.toolbar.insert(stop_button, -1)
            stop_button.show()

            self.set_toolbar_box(toolbar_box)
            toolbar_box.show()

        else:
            toolbox = ActivityToolbox(self)
            self.set_toolbox(toolbox)
            toolbox.show()

        if self.num.widget.parent:
            self.num.widget.parent.remove(self.num.widget)
            
        self._main_view.pack_start(self.num.widget)
        
        self.num.widget.show()
        self._main_view.show()
        self.set_canvas(self._main_view)
        self.show_all()
        
