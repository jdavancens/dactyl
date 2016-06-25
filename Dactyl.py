# -*- coding: utf-8 -*-

import numpy
from pymongo import MongoClient()

class Dactyl(object):
    '''
    '''

    __slots__ = (
            "_audio_data",
            "_sample_rate",
            "_duration_in_seconds"
    )

    def __init__(self):
        ''' Initializes the fingerprinter. Creates a new database of none
        exists.
        '''
        pass

    def _downmix(self):
        ''' Downmixes stereo audio file to mono.
        '''
        pass

    def _downsample(self, new_rate, antialiasing=True):
        ''' Resamples the audio at a lower frequency (must be mono)
        '''
        pass

    def _hpf(self, cutoff, resonance=0):
        ''' Applies a high pass filter to audio
        '''
        pass

    def _lpf(self, cutoff, resonance=0):
        ''' Applies a low pass filter to audio (for antialiasing when
        downsampling.
        '''
        pass

    def db_create_collection(self, name):
        ''' Creates a new MongoDB database collection.
        '''
        pass

    def db_delete_collection(self, name):
        ''' Deletes a collection from the database
        '''
        pass

    def db_insert_fingerprint(self):
        ''' Inserts a new entry in to the current collection
            Raises error if no fingerprint has been made.
        '''
        pass

    def db_load_collection(self, name):
        ''' Loads a collection.
            Raises an error if none found.
        '''
        pass

    def load_audio_file(self, file_name, sampling_rate=11025,
            antialiasing=True, lpf=True):
        ''' Loads an audio file
            Returns number of channels, sampling rate, and duration in seconds.
        '''
       try:
           true_sampling_rate, data = wav.read(file_name)
       except:
           raise ValueError('File does not exist')
           # downmix to mono
       if data.shape[0] > 1:
           data = sum(data)
           # normalize
           data = data / data.max()
           # downsample
           if true_sampling_rate > sampling_rate:
               data = self._resample(data, true_sampling_rate, sampling_rate)
           # apply low pass filter for antialiasing
           if antialiasing:
               data = self._lpf(data, sampling_rate)


    def db_query_fingerprint(self):
        ''' Queries database for a matching fingerprint.
            Returns closest match.
        '''
        pass
