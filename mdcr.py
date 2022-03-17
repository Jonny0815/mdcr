import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.DeviceComponent import DeviceComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.SliderElement import SliderElement
from _Framework.TransportComponent import TransportComponent
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.SessionComponent import SessionComponent
from _Framework.EncoderElement import *
from _Framework.SliderElement import SliderElement
from _Framework.SubjectSlot import SlotManager
from functools import partial
from Launchpad.ConfigurableButtonElement import ConfigurableButtonElement
import time
from itertools import chain
from _Framework.Util import find_if
import collections

from typing import Dict

from .bcf import Bcf
from .bcr import Bcr
from .fcb import Fcb


class Mdcr(ControlSurface):
    def __init__(self, c_instance):
        super(Mdcr, self).__init__(c_instance)
        with self.component_guard():
            self.current_track_offset = 0
            self.current_scene_offset = 0
            num_tracks = 8
            num_returns = 2
            self._active_tracks: Dict[int, Live.Track.Track] = {}
            self.mixer = MixerComponent(num_tracks, num_returns, is_enabled=True, auto_name=True)
            self.session = SessionComponent(num_tracks, 4)
            self.session.set_offsets(0, 0)
            self.session.set_mixer(self.mixer)
            self.mixer.set_track_offset(0)
            self.song().view.selected_track = self.song().tracks[0]
            self._bcf: Bcf = Bcf(self)
            self._bcr: Bcr = Bcr(self)
            #self._fcb: Fcb = Fcb(self)
            # self.mixer.channel_strip(0).set_volume_control(EncoderElement(MIDI_CC_TYPE, 8, 1, Live.MidiMap.MapMode.absolute))
            self.mixer.channel_strip(0).set_volume_control(self._bcf.faders[0])
            self.show_message("did it?")
            self.set_highlighting_session_component(self.session)
            self.init_clip_listeners()


    def init_clip_listeners(self):
        song: Live.Song.Song = self.song()
        for i in range(len(song.tracks)):
            for j in range(len(song.tracks[i].clip_slots)):
                if song.tracks[i].clip_slots[j].has_clip:
                    song.tracks[i].clip_slots[j].clip.add_playing_status_listener(
                        partial(self.handle_clip_launch, song.tracks[i].clip_slots[j].clip))

    def handle_clip_launch(self, clip: Live.Clip.Clip):
        self.show_message("test + " + str(clip.color_index))
        self._active_tracks[clip.color_index] = clip.canonical_parent.canonical_parent
        self.show_message("track: " + str(self._active_tracks[clip.color_index]))

    def disconnect(self):
        super(Mdcr, self).disconnect()
