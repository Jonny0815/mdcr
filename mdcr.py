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
import json

from typing import Dict, List, Optional

from .ParameterMapping import ParameterMapping
from .bcf import Bcf
from .bcr import Bcr
from .fcb import Fcb

session: Optional[SessionComponent] = None
mixer: Optional[MixerComponent] = None


class Mdcr(ControlSurface):
    def __init__(self, c_instance):
        super(Mdcr, self).__init__(c_instance)
        self.Song: Live.Song.Song = self.song()
        with self.component_guard():
            self.clip_id_counter: int = 0
            self.current_track_offset = 0
            self.current_scene_offset = 0
            num_tracks = len(self.song().tracks)
            num_returns = len(self.song().return_tracks)
            self._knob_mappings: Dict[int, List[ParameterMapping]] = {}  # clip_id | list[pm]
            self._active_tracks: Dict[int, Optional[Live.Track.Track]] = {14: None,  # 14 red
                                                                          9: None,  # 9 blue
                                                                          3: None,  # 3 yellow
                                                                          19: None,  # 19 green
                                                                          15: None,  # 15 orange
                                                                          66: None,  # 66 purple
                                                                          13: None,  # 13 white
                                                                          16: None  # 16 brown
                                                                          }
            global mixer
            mixer = MixerComponent(num_tracks, num_returns, is_enabled=True, auto_name=True)
            global session
            session = SessionComponent(1, 1)
            session.set_offsets(0, 0)
            session.set_mixer(mixer)
            mixer.set_track_offset(0)
            self.Song.view.selected_track = self.Song.tracks[0]
            self._bcf: Bcf = Bcf(self)
            self._bcr: Bcr = Bcr(self)
            # self._fcb: Fcb = Fcb(self)
            # self.mixer.channel_strip(0).set_volume_control(EncoderElement(MIDI_CC_TYPE, 8, 1, Live.MidiMap.MapMode.absolute))
            # self.mixer.channel_strip(0).set_volume_control(self._bcf.faders[0])
            # self.test_listener.subject = self._bcf._buttons[1][0]
            # self.mixer.channel_strip(0).set_mute_button(ToggleButton(True, MIDI_CC_TYPE, 16, 73, c_instance))
            # self.mixer.channel_strip(0).set_mute_button(self._bcf._buttons[1][0])
            # self.test_listener.subject = EncoderElement(MIDI_CC_TYPE, 15, 84, Live.MidiMap.MapMode.absolute)
            self.set_highlighting_session_component(session)
            self.init_clip_listeners()
            self._tracks: List[Live.Track.Track] = self.Song.tracks
            self._scenes: List[Live.Scene.Scene] = self.Song.scenes
            self.Song.add_tracks_listener(self.handle_tracks_change)
            self.Song.add_scenes_listener(self.handle_scenes_change)
            # self.song().view.add_selected_parameter_listener(self.test_selected_param)

    def init_clip_listeners(self):
        i_debug = 0
        j_debug = 0
        song: Live.Song.Song = self.song()
        for i in range(len(song.tracks)):
            i_debug = i
            for j in range(len(song.tracks[i].clip_slots)):
                j_debug = j
                if song.tracks[i].clip_slots[j].has_clip:  # add listener for all clips
                    #clip_id: int = self.get_clip_id(song.tracks[i].clip_slots[j].clip)
                    #if clip_id > self.clip_id_counter:  # update clip_id_counter to max clip id in set
                        #self.clip_id_counter = clip_id
                    song.tracks[i].clip_slots[j].clip.add_playing_status_listener(
                        partial(self.handle_clip_launch, song.tracks[i].clip_slots[j].clip))
                else:
                    song.tracks[i].clip_slots[j].add_has_clip_listener(
                        partial(self.handle_new_clip, song.tracks[i].clip_slots[j]))
        self.log_message()

    def handle_scenes_change(self):
        self.show_message("scenes changed")

    def handle_tracks_change(self):
        self.show_message("new track added")

    def test_selected_param(self):
        self.show_message("param " + str(self.song().view.selected_parameter))

    def handle_new_clip(self, clip_slot: Live.ClipSlot.ClipSlot):
        if clip_slot.has_clip:
            #self.clip_id_counter += 1
            #clip_slot.clip.name += "|" + str(self.clip_id_counter)
            clip_slot.add_playing_status_listener(partial(self.handle_clip_launch, clip_slot.clip))

    def handle_clip_launch(self, clip: Live.Clip.Clip):
        track: Live.Track.Track = clip.canonical_parent.canonical_parent
        if clip.color_index in self._active_tracks.keys():
            if self._active_tracks[clip.color_index] == track:  # same track? return
                if not clip.is_playing:
                    index: int = self.get_track_index(track)

                    mixer.channel_strip(index).set_volume_control(None)
                    #togglebutton is broken
                    #mixer.channel_strip(index).set_mute_button(None)
                    #mixer.channel_strip(index).set_solo_button(None)
                    #self.song().tracks[index].devices[0].parameters[0].value = 0
                    self._active_tracks[clip.color_index] = None
                return
            else:

                self._active_tracks[clip.color_index] = track
                index: int = self.get_track_index(track)
                with self.component_guard():
                    #self.song().tracks[index].devices[0].parameters[0].value = 1
                    mixer.channel_strip(index).set_volume_control(
                        self._bcf.get_volume_control(clip))
                    #togglebutton is broken
                    #mixer.channel_strip(index).set_mute_button(self._bcf.get_arm_button(clip))
                    #mixer.channel_strip(index).set_solo_button(self._bcf.get_cue_button(clip))
                    parameterlist = [ParameterMapping(index, 0, 1),  # fix for first 3 params
                                     ParameterMapping(index, 0, 2),
                                     ParameterMapping(index, 0, 3)]
                    self._bcr.map_encoders(clip, parameterlist)

    def get_track_index(self, track: Live.Track.Track) -> int:
        tracks = self.song().tracks
        for i in range(len(tracks)):
            if tracks[i] == track:
                self.show_message(str(i))
                return i

    def get_clip_id(self, clip: Live.Clip.Clip) -> int:  # extract clip id from name
        try:
            _, clip_id = str(clip.name).split("|")

        except ValueError:
            #clip.name = str(clip.name + "|" + str(self.clip_id_counter))
            #clip_id = self.clip_id_counter
            #self.clip_id_counter += 1
            clip_id = ""

        return int(clip_id)

    @subject_slot("value")
    def test_listener(self, value):  # mapped to some button in init, look there for usage
        self.song().tracks[3].devices[0].parameters[1].value = value

    def disconnect(self):
        super(Mdcr, self).disconnect()
