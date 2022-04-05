from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *
from _Framework.EncoderElement import EncoderElement
from typing import List
import Live


class Fcb(ControlSurfaceComponent):
    def __init__(self, *a, **k):
        super(Fcb, self).__init__(*a, **k)
        self._channel = 0
        self._buttons: List[ButtonElement] = [
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 0),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 1),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 2),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 3),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 4),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 5),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 6),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 7),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 8),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 9),
            ButtonElement(False, MIDI_CC_TYPE, self._channel, 10)]
        self._pedal_left = EncoderElement(MIDI_CC_TYPE, self._channel, 7, Live.MidiMap.MapMode.absolute)
        self._pedal_right = EncoderElement(MIDI_CC_TYPE, self._channel, 27)
