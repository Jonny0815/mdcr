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
from _Framework.SubjectSlot import SlotManager, subject_slot
from _Framework.EncoderElement import EncoderElement
from _Framework.ToggleComponent import ToggleComponent
from .ToggleButton import ToggleButton
from functools import partial
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
            self._active_tracks: Dict[int, Live.Track.Track] = {14: None,  # 14 red
                                                                9: None,  # 9 blue
                                                                3: None,  # 3 yellow
                                                                19: None,  # 19 green
                                                                15: None,  # 15 orange
                                                                66: None,  # 66 purple
                                                                13: None,  # 13 white
                                                                16: None  # 16 brown
                                                                }
            self.mixer = MixerComponent(num_tracks, num_returns, is_enabled=True, auto_name=True)
            self.session = SessionComponent(num_tracks, 4)
            self.session.set_offsets(0, 0)
            self.session.set_mixer(self.mixer)
            self.mixer.set_track_offset(0)
            self.song().view.selected_track = self.song().tracks[0]
            self._bcf: Bcf = Bcf(self)
            self._bcr: Bcr = Bcr(self)
            # self._fcb: Fcb = Fcb(self)
            # self.mixer.channel_strip(0).set_volume_control(EncoderElement(MIDI_CC_TYPE, 8, 1, Live.MidiMap.MapMode.absolute))
            # self.mixer.channel_strip(0).set_volume_control(self._bcf.faders[0])
            # self.test_listener.subject = self._bcf._buttons[1][0]
            #self.mixer.channel_strip(0).set_mute_button(ToggleButton(True, MIDI_CC_TYPE, 8, 73, c_instance))
            #self.mixer.channel_strip(0).set_mute_button(self._bcf._buttons[1][0])
            self.show_message("did it?")
            self.set_highlighting_session_component(self.session)
            self.init_clip_listeners()
            self.song().add_tracks_listener(self.handle_new_track)

    def init_clip_listeners(self):
        song: Live.Song.Song = self.song()
        for i in range(len(song.tracks)):
            for j in range(len(song.tracks[i].clip_slots)):
                if song.tracks[i].clip_slots[j].has_clip:
                    # song.tracks[i].clip_slots[j].clip.add_playing_status_listener(self.handle_clip_launch)
                    song.tracks[i].clip_slots[j].clip.add_playing_status_listener(
                        partial(self.handle_clip_launch, song.tracks[i].clip_slots[j].clip))

    def handle_new_track(self):
        self.show_message("new track added")

    def handle_clip_launch(self, clip: Live.Clip.Clip):
        self.show_message("hello from handle clip launch: " + str(clip.color_index))
        track: Live.Track.Track = clip.canonical_parent.canonical_parent
        if clip.color_index in self._active_tracks:  # anything wrong with clip coloring?
            if self._active_tracks[clip.color_index] == track:  # same clip? return
                if not clip.is_playing:
                    index: int = self.get_track_index(track)
                    self.mixer.channel_strip(index).set_volume_control(None)
                    self.mixer.channel_strip(index).set_mute_button(None)
                    self.mixer.channel_strip(index).set_solo_button(None)
                    self._active_tracks[clip.color_index] = None
                return
            else:

                self._active_tracks[clip.color_index] = track
                index: int = self.get_track_index(track)
                self.show_message("trying to map track " + str(index) + " to " + str(track))
                self.log_message("trying to map track " + str(index) + " to " + str(track))
                with self.component_guard():
                    self.mixer.channel_strip(index).set_volume_control(
                        self._bcf.get_volume_control(clip))
                    self.mixer.channel_strip(index).set_mute_button(self._bcf.get_arm_button(clip))
                    self.mixer.channel_strip(index).set_solo_button(self._bcf.get_cue_button(clip))

        self.show_message(
            "track: " + str(self._active_tracks[clip.color_index]) + " has color: " + str(clip.color_index))

    def get_track_index(self, track: Live.Track.Track) -> int:
        tracks = self.song().tracks
        for i in range(len(tracks)):
            if tracks[i] == track:
                return i

    @subject_slot("value")
    def test_listener(self, value):
        self.show_message("test listener with value: " + str(value))
        if value == 127:
            self.song().tracks[0].mute = 0
        if value == 0:
            self.song().tracks[0].mute = 127

    def disconnect(self):
        super(Mdcr, self).disconnect()
