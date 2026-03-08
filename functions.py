import sounddevice as sd
import numpy as np 
import parselmouth 
from vocalRanges import VocalRanges, vocalRangesMean

def recording():
    '''
    Record audio input and return the inverse of numpy array to be processed in parselmouth
    
    Return: 
        numpy array: [channel, sampleing rate]
    '''
    SAMPLERATE = 48000

    sd.default.samplerate = SAMPLERATE
    sd.default.channels = 1

    print("Recording...")
    sound = sd.rec(int(5*SAMPLERATE))
    sd.wait()
    print("Done")
    
    sound = sound.T
    return sound 

def soundToMedianFrequency(file):
    '''
    Take in .wav file, tranfer to parselmouth format, extract the frequencies, 
    filter out 0s, and return median of frequency array. 

    Args: 
        String: file name 
    
    Return: 
        Float: median of frequncy array.     


    '''
    sound = parselmouth.Sound(file)
    pitch = sound.to_pitch()
    frequencies = pitch.selected_array['frequency']
    f0 = frequencies[frequencies > 0]
    medianF0 = np.median(f0)
    return medianF0

def soundToSustainedFrequency(file, k=2):
    '''
    Estimate the sustained frequency by: 
    1. Find the median of the entire array
    2. find median of the array
    3 compute distance of each value from the median 
    4. calculate MAD (median of absolute deviation)
    5. scale to calculate robust sigma NOTE: Don't really know how does that work yet
    6. Keep frequencies that are only 2 - 3 sigma away from the median 
    7. calculate mean of remaining frequencies 

    Arg:
        file (string): .wav file filename
        k (int): number of sigma to keep frequencies. Default at 2

    Return:
        int: sustained frequency 

    '''
    # 
    
    sound = parselmouth.Sound(file)
    pitch = sound.to_pitch()
    frequencies = pitch.selected_array['frequency']

    # Remove 0s
    f0 = frequencies[frequencies > 0]
    
    # find median and MAD
    median = np.median(f0)
    mad = np.median(np.abs(f0 - median))

    # calculate robust sigma 
    
    robustSigma = 1.4826 * mad
    filtered = f0[np.abs(f0 - median) <= k * robustSigma]

    return np.mean(filtered)


def possibleRange(high, low):
    '''
    Given the highest and lowest frequency, return possibilities of vocal ranges. 

    Arg: 
        high (float): highest frequency
        low (float): lowest frequency

    return: 
        list: a list of possibilities in string datatype
    '''
    possibility = []
    for voiceType, (minimum, maximum) in VocalRanges.items():
        if low >= minimum and high <= maximum and high >= minimum: 
            possibility.append(voiceType)
        
    return possibility

def possibleRangeForMedian(possibilities, middle):
    '''
    Given a list of possibilities, find the vocal range that the median is closest to the input 

    Arg:
        possibilities (list): a list of possible vocal ranges in string datatype
        middle (float): frequency 
    
    Return:
        string: estimated vocal range as a string 
    '''
    possibilityDict = {}
    for possibility in possibilities: 
        possibilityDict[possibility] = np.abs(vocalRangesMean[possibility] - middle)
    result = min(possibilityDict, key=possibilityDict.get)
    return result
        
    


