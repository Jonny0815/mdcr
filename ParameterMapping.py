from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *
from _Framework.EncoderElement import EncoderElement
from _Framework.SubjectSlot import *
from typing import List
import Live


class ParameterMapping(ControlSurfaceComponent):
    def __init__(self, track_id: int, device_id: int, parameter_id: int, *a, **k):
        super(ParameterMapping, self).__init__(*a, **k)
        self.track_id: int = track_id
        self.device_id: int = device_id
        self.parameter_id: int = parameter_id

    @subject_slot("value")
    def parameter_listener(self, value):
        self.song().tracks[self.track_id].devices[self.device_id].parameters[self.parameter_id].value = value

    def assign_encoder(self, encoder: EncoderElement):
        self.parameter_listener.subject = encoder
