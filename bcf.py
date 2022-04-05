from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *
from _Framework.EncoderElement import EncoderElement
from _Framework.ToggleComponent import ToggleComponent
from .ToggleButton import ToggleButton
from typing import List
import Live


def translate_color_index(color_index: int) -> int:
    color_table = {14: 0,  # 14 red
                   9: 1,  # 9 blue
                   3: 2,  # 3 yellow
                   19: 3,  # 19 green
                   15: 4,  # 15 orange
                   66: 5,  # 66 purple
                   13: 6,  # 13 white
                   16: 7}  # 16 brown
    return color_table[color_index]


class Bcf(ControlSurfaceComponent):
    def __init__(self, *a, **k):
        super(Bcf, self).__init__(*a, **k)
        is_momentary = True
        self._buttons: List[List[ToggleButton]] = [[ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 65),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 66),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 67),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 68),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 69),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 70),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 71),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 72)],
                                                   [ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 73),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 74),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 75),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 76),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 77),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 78),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 79),
                                                    ToggleButton(is_momentary, MIDI_CC_TYPE, 8, 80)]]
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

    def get_volume_control(self, clip: Live.Clip.Clip) -> EncoderElement:
        return self.faders[translate_color_index(clip.color_index)]

    def get_arm_button(self, clip: Live.Clip.Clip) -> ButtonElement:
        return self._buttons[1][translate_color_index(clip.color_index)]

    def get_cue_button(self, clip: Live.Clip.Clip) -> ButtonElement:
        return self._buttons[0][translate_color_index(clip.color_index)]

    def on_selected_scene_changed(self):
        self.canonical_parent.show_message("Hello from bcf")
