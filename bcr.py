from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *
from _Framework.EncoderElement import EncoderElement
from typing import List
import Live


class Bcr(ControlSurfaceComponent):
    def __init__(self, *a, **k):
        super(Bcr, self).__init__(*a, **k)
        self._channel = 15
        self._buttons: List[List[ButtonElement]] = [
            [ButtonElement(False, MIDI_CC_TYPE, self._channel, 65),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 66),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 67),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 68),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 69),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 70),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 71),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 72)],
            [ButtonElement(False, MIDI_CC_TYPE, self._channel, 73),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 74),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 75),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 76),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 77),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 78),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 79),
             ButtonElement(False, MIDI_CC_TYPE, self._channel, 80)]]
        self.bot_knobs: List[List[EncoderElement]] = [
            [EncoderElement(MIDI_CC_TYPE, self._channel, 97, Live.MidiMap.MapMode.absolute),  # red
             EncoderElement(MIDI_CC_TYPE, self._channel, 89, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 81, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 98, Live.MidiMap.MapMode.absolute),  # blue
             EncoderElement(MIDI_CC_TYPE, self._channel, 90, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 82, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 99, Live.MidiMap.MapMode.absolute),  # yellow
             EncoderElement(MIDI_CC_TYPE, self._channel, 91, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 83, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 100, Live.MidiMap.MapMode.absolute),  # green
             EncoderElement(MIDI_CC_TYPE, self._channel, 92, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 84, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 101, Live.MidiMap.MapMode.absolute),  # orange
             EncoderElement(MIDI_CC_TYPE, self._channel, 93, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 85, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 102, Live.MidiMap.MapMode.absolute),  # purple
             EncoderElement(MIDI_CC_TYPE, self._channel, 94, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 86, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 103, Live.MidiMap.MapMode.absolute),  # white
             EncoderElement(MIDI_CC_TYPE, self._channel, 95, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 87, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 104, Live.MidiMap.MapMode.absolute),  # brown
             EncoderElement(MIDI_CC_TYPE, self._channel, 96, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 88, Live.MidiMap.MapMode.absolute)], ]
        self._top_knobs: List[List[EncoderElement]] = [ # no correct values for midi map!
            [EncoderElement(MIDI_CC_TYPE, self._channel, 82, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 83, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 84, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 85, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 86, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 87, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 88, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 89, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 82, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 83, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 84, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 85, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 86, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 87, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 88, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 89, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 82, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 83, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 84, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 85, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 86, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 87, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 88, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 89, Live.MidiMap.MapMode.absolute)],
            [EncoderElement(MIDI_CC_TYPE, self._channel, 82, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 83, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 84, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 85, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 86, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 87, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 88, Live.MidiMap.MapMode.absolute),
             EncoderElement(MIDI_CC_TYPE, self._channel, 89, Live.MidiMap.MapMode.absolute)]]
