import unittest
from Dactyl import Dactyl
import numpy as np
class TestDactyl_load_audio_file(unittest.TestCase):

    def setUp(self):
        self.dactyl = Dactyl()

    def test_load_mono(self):
        import os.path
        self.dactyl.load_audio_file("./example/sine_440_mono.wav")
        expected_sr = 11025
        expected_dur = 10.0
        # correctly downsampled
        actual_sr = self.dactyl._sample_rate
        self.assertEqual(expected_sr, actual_sr)
        # correct duration
        actual_dur = self.dactyl._duration_in_seconds
        self.assertEqual(expected_dur, actual_dur)
        # is a numpy array
        self.assertTrue( isinstance(self.dactyl._audio_data, np.ndarray) )
        # is mono
        self.assertEqual(len(self.dactyl._audio_data.shape), 1)

    def test_load_stereo(self):
        import os.path
        self.dactyl.load_audio_file("./example/sine_440_stereo.wav")
        expected_sr = 11025
        expected_dur = 10.0
        # correctly downsampled
        actual_sr = self.dactyl._sample_rate
        self.assertEqual(expected_sr, actual_sr)
        # correct duration
        actual_dur = self.dactyl._duration_in_seconds
        self.assertEqual(expected_dur, actual_dur)
        # is a numpy array
        self.assertTrue( isinstance(self.dactyl._audio_data, np.ndarray) )
        # is mono
        self.assertEqual(len(self.dactyl._audio_data.shape), 1)
