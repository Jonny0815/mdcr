from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from Launchpad.ConfigurableButtonElement import ConfigurableButtonElement
from _Framework.InputControlElement import *
from _Framework.EncoderElement import EncoderElement
from typing import List
import Live


class Fcb(ControlSurfaceComponent):
    def __init__(self, *a, **k):
        super(Fcb, self).__init__(*a, **k)
        self._channel = 0
        self._buttons: List[ConfigurableButtonElement] = [
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 0),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 1),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 2),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 3),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 4),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 5),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 6),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 7),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 8),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 9),
            ConfigurableButtonElement(False, MIDI_CC_TYPE, self._channel, 10)]
        self._pedal_left = EncoderElement(MIDI_CC_TYPE, self._channel, 7, Live.MidiMap.MapMode.absolute)
        self._pedal_right = EncoderElement(MIDI_CC_TYPE, self._channel, 27)