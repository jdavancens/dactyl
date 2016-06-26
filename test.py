import unittest
import test.test_Dactyl_load_audio_file

def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(test.test_Dactyl_load_audio_file.TestDactyl_load_audio_file))
    return s

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
