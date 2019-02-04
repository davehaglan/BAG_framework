# -*- coding: utf-8 -*-

"""This module defines generators that tests wiring API."""

from typing import Dict, Any

from bag.util.cache import Param
from bag.layout.template import TemplateBase, TemplateDB


class TestWire00(TemplateBase):
    def __init__(self, temp_db: TemplateDB, params: Param, **kwargs: Any) -> None:
        TemplateBase.__init__(self, temp_db, params, **kwargs)

    @classmethod
    def get_params_info(cls) -> Dict[str, str]:
        return {}

    def draw_layout(self) -> None:
        # Metal 4 is horizontal, Metal 5 is vertical
        hm_layer = 4
        vm_layer = 5

        warr1 = self.add_wires(hm_layer, 0, 100, 300)
        # print WireArray object
        print(warr1)
        # print lower, middle, and upper coordinate of wire.
        print(warr1.lower, warr1.middle, warr1.upper)
        # print TrackID object associated with WireArray
        print(warr1.track_id)
        # add a horizontal wire on track 1, from X=0.1 to X=0.3,
        # coordinates specified in resolution units
        self.add_wires(hm_layer, 1, 100, 300)
        # add a horizontal wire on track 2.5, from X=0.2 to X=0.4
        self.add_wires(hm_layer, 2.5, 200, 400)
        # add a horizontal wire on track 4, from X=0.2 to X=0.4, with 2 tracks wide
        self.add_wires(hm_layer, 4, 200, 400, width=2)

        # add 3 parallel vertical wires starting on track 6 and use every other track
        warr4 = self.add_wires(vm_layer, 6, 100, 400, num=3, pitch=2)
        print(warr4)

        # set the size of this template
        top_layer = vm_layer
        num_h_tracks = 6
        num_v_tracks = 11
        # size is 3-element tuple of top layer ID, number of top
        # vertical tracks, and number of top horizontal tracks
        self.size = top_layer, num_v_tracks, num_h_tracks
        # print bounding box of this template
        print(self.bound_box)
        # add a M7 rectangle to visualize bounding box in layout
        self.add_rect(('M7', ''), self.bound_box)


class TestVia00(TemplateBase):
    def __init__(self, temp_db: TemplateDB, params: Param, **kwargs: Any) -> None:
        TemplateBase.__init__(self, temp_db, params, **kwargs)

    @classmethod
    def get_params_info(cls):
        return {}

    def draw_layout(self):
        # Metal 4 is horizontal, Metal 5 is vertical
        hm_layer = 4
        vm_layer = 5

        warr1 = self.add_wires(hm_layer, 0, 0, 400)
        warr2 = self.add_wires(vm_layer, 2, 0, 400)
        self.connect_to_track_wires(warr1, warr2)

        warr3 = self.add_wires(hm_layer, 10, 0, 400, num=3, pitch=2)
        self.connect_to_track_wires(warr2, warr3)

        self.add_pin('foo', warr2)