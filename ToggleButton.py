# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/ButtonElement.py
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
import Live
from _Framework.InputControlElement import InputControlElement, MIDI_CC_TYPE
from _Framework.Skin import Skin, SkinColorMissingError
from _Framework.Util import nop


class ButtonValue(object):
    u"""
    Basic type for button values, so global constants are symbolically
    different from integers.
    """
    midi_value = 0

    def __init__(self, midi_value=None, *a, **k):
        super(ButtonValue, self).__init__(*a, **k)
        if midi_value is not None:
            self.midi_value = midi_value

    def __int__(self):
        return self.midi_value

    def __eq__(self, other):
        try:
            return id(self) == id(other) or self.midi_value == other
        except NotImplementedError:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __bool__(self):
        return self != OFF_VALUE


ON_VALUE = ButtonValue(127)
OFF_VALUE = ButtonValue(0)


class Color(ButtonValue):
    u"""
    Basic interface for showing a color.
    """

    def draw(self, interface):
        u"""
        Draws the color into the interface.  Depending on the color
        type, interface might be required special capabilities.
        """
        interface.send_value(self.midi_value)


class DummyUndoStepHandler(object):

    def begin_undo_step(self):
        pass

    def end_undo_step(self):
        pass


class ButtonElementMixin(object):
    u"""
    Mixin for sending values to button-like control-elements elements.
    """

    def set_light(self, is_turned_on):
        if is_turned_on:
            self.turn_on()
        else:
            self.turn_off()

    def turn_on(self):
        self.send_value(ON_VALUE)

    def turn_off(self):
        self.send_value(OFF_VALUE)


class ToggleButton(InputControlElement, ButtonElementMixin):
    u"""
    Class representing a button a the controller
    """

    class ProxiedInterface(InputControlElement.ProxiedInterface, ButtonElementMixin):
        is_momentary = nop
        is_pressed = nop

    def __init__(self, is_momentary, msg_type, channel, identifier, skin=Skin(),
                 undo_step_handler=DummyUndoStepHandler(), *a, **k):
        super(ToggleButton, self).__init__(msg_type, channel, identifier, *a, **k)
        self.__is_momentary = bool(is_momentary)
        self._last_received_value = -1
        self._toggle = 0
        self._undo_step_handler = undo_step_handler
        self._skin = skin


    def is_momentary(self):
        u""" returns true if the buttons sends a message on being released """
        return self.__is_momentary

    def message_map_mode(self):
        assert self.message_type() is MIDI_CC_TYPE
        return Live.MidiMap.MapMode.absolute

    def is_pressed(self):
        return self.__is_momentary and int(self._last_received_value) > 0

    def set_light(self, value):
        self._set_skin_light(value)

    def _set_skin_light(self, value):
        try:
            color = self._skin[value]
            color.draw(self)
        except SkinColorMissingError:
            super(ToggleButton, self).set_light(value)

    # this is broken! rework this! do not use
    def receive_value(self, value):
        self.canonical_parent.show_message(str(value))
        if self._toggle == 1:
            self._toggle = 0
            super(ToggleButton, self).receive_value(0)
        else:
            self._toggle = 1
            super(ToggleButton, self).receive_value(1)

    def disconnect(self):
        super(ToggleButton, self).disconnect()
        self._undo_step_handler = None
