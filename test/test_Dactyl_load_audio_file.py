import unittest


class TestDactyl_load_audio_file(unittest.TestCase):

    def setUp(self):
        dactyl = Dactyl()

    def test_load_mono(self):
        dactyl.load_audio_file("./examples/sine_mono.wav")

    def test_load_stereo(self):
        dactyl.load_audio_file("./examples/sine_stereo.wav")

