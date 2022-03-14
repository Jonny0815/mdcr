from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from Launchpad.ConfigurableButtonElement import ConfigurableButtonElement
from _Framework.InputControlElement import *
from _Framework.EncoderElement import EncoderElement
from typing import List
import Live


class Bcf(ControlSurfaceComponent):
    def __init__(self, *a, **k):
        super(Bcf, self).__init__(*a, **k)
        self._buttons: List[List[ConfigurableButtonElement]] = [[ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 65),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 66),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 67),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 68),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 69),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 70),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 71),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 72)],
                                                                [ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 73),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 74),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 75),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 76),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 77),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 78),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 79),
                                                                 ConfigurableButtonElement(False, MIDI_CC_TYPE, 8, 80)]]
        self.faders: List[EncoderElement] = [EncoderElement(MIDI_CC_TYPE, 8, 1, Live.MidiMap.MapMode.absolute),
                                              EncoderElement(MIDI_CC_TYPE, 8, 2, Live.MidiMap.MapMode.absolute),
                                              EncoderElement(MIDI_CC_TYPE, 8, 3, Live.MidiMap.MapMode.absolute),
                                              EncoderElement(MIDI_CC_TYPE, 8, 4, Live.MidiMap.MapMode.absolute),
                                              EncoderElement(MIDI_CC_TYPE, 8, 5, Live.MidiMap.MapMode.absolute),
                                              EncoderElement(MIDI_CC_TYPE, 8, 6, Live.MidiMap.MapMode.absolute),
                                              EncoderElement(MIDI_CC_TYPE, 8, 7, Live.MidiMap.MapMode.absolute),
                                              EncoderElement(MIDI_CC_TYPE, 8, 8, Live.MidiMap.MapMode.absolute)]
        self._knobs: List[List[EncoderElement]] = [[EncoderElement(MIDI_CC_TYPE, 8, 82, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 83, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 84, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 85, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 86, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 87, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 88, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 89, Live.MidiMap.MapMode.absolute)],
                                                   [EncoderElement(MIDI_CC_TYPE, 8, 82, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 83, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 84, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 85, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 86, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 87, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 88, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 89, Live.MidiMap.MapMode.absolute)],
                                                   [EncoderElement(MIDI_CC_TYPE, 8, 82, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 83, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 84, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 85, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 86, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 87, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 88, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 89, Live.MidiMap.MapMode.absolute)],
                                                   [EncoderElement(MIDI_CC_TYPE, 8, 82, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 83, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 84, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 85, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 86, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 87, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 88, Live.MidiMap.MapMode.absolute),
                                                    EncoderElement(MIDI_CC_TYPE, 8, 89, Live.MidiMap.MapMode.absolute)]]
