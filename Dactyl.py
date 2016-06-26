# -*- coding: utf-8 -*-


import numpy
import librosa
#from pymongo import MongoClient

class Dactyl(object):
    '''
    '''

    __slots__ = (
            "_audio_data",
            "_sample_rate",
            "_duration_in_seconds",
    )

    def __init__(self):
        ''' Initializes the fingerprinter. Creates a new database of none
        exists.
        '''
        self._audio_data = None
        self._sample_rate = None
        self._duration_in_seconds = None
        self._peaks = None

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

    def find_peaks(self, n_fft=2048, tau=10, kappa=10):
        ''' Extracts a fingerprint from the loaded audio data. Stores value
            internally as a integer hash code.
        '''
        # compute stft
        if self._audio_data is None:
            raise ValueError("No audio data loaded.")
        S = librosa.stft(self._audio_data, n_fft)
        # find peaks
        n_frames = S.shape[0]
        n_bins = S.shape[1]
        peaks = []
        for n in range(n_frames):
            for k in range(n_bins):
                p = S[n][k]
                is_peak = True
                # search neigborhood
                for i in range(tau):
                    for j in range(kappa):
                        n_ = n + i - tau//2
                        k_ = k + j - kappa//2
                        if 0 <= n_ < n_frames and 0 < k_ < n_bins and (n != n_ and k != n_):
                            p_ = S[n_][k_]
                            if abs(p_) < abs(p):
                                is_peak = False
                if is_peak:
                    peaks.append((n, k))
        return peaks

    def make_fingerprint(self, peaks):
        pass



    def load_audio_file(self,
                        file_name,
                        sample_rate=11025,
                        hpf_frequency=None,
                        duration
                        ):
        ''' Loads an audio file into memory as an Numpy array.
        '''

        # convert to absolute path
        import os.path
        file_name = os.path.abspath(file_name)

        # load data into a numpy array (downsample, convert to mono)
        try:
            data, sample_rate = librosa.load(file_name, sample_rate)
        except:
            raise ValueError('File does not exist')

        n_samples = data.shape[0]

        # set class attributes
        self._audio_data = data
        self._sample_rate = sample_rate
        self._duration_in_seconds = n_samples / sample_rate

    def db_query_fingerprint(self):
        ''' Queries database for a matching fingerprint.
            Returns closest match.
        '''
        pass
