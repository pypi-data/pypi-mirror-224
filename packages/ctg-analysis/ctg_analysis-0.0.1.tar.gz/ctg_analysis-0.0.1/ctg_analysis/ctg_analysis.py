#!/usr/bin/env python
# coding: utf-8

# # Preprocessing and auxiliary functions.

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import scipy
import numpy as np
import scipy
from scipy import signal
import BaselineRemoval
from BaselineRemoval import BaselineRemoval
from scipy.interpolate import interp1d


# In[ ]:


def signal_loss(sequence, value=0):
    """
    Calculates the signal loss percentage of a given sequence.
    
    The signal loss represents the proportion of values in the sequence that are less than or equal to the specified `value`.
    
    Args:
        sequence (list or np.ndarray): The FHR/toco sequence values.
        value (int, optional): The minimum permitted value in the signal. Defaults to 0.
        
    Returns:
        float: The signal loss percentage.
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: If `value` is negative.
        
    Example:
        >>> signal_loss([1, 2, 3, 4, 0, 0, 2], 1)
        0.57
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray) , f"Object {sequence} is not a list nor an array."
    assert value >= 0, "The minimum permitted value in the signal must be positive or equal to 0."
    
    i = 0
    loss = 0
    while i < len(sequence):
        if sequence[i] <= value:
          loss += 1
        i += 1        
    return round(loss / len(sequence), 2)


# In[ ]:


def pad(sequence, freq=4, t=120):
    """
    Pads the input sequence to ensure all sequences have the same length.
    
    The sequences' length are padded to ensure they all have the same temporal duration when doing the analysis.
    
    Args:
        sequence (list or np.ndarray): The sequence to pad.
        freq (floar, optional): The frequency of the signal in Hz. Defaults to 4.
        t (float, optional): The total duration time of the sequences in minutes. Defaults to 120, which means 
                             28800 points for a standard 4Hz signal.
    Returns:
        np.ndarray: The padded sequence.
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: If the frequency of the signal is not a positive non-zero number.
        AssertionError: If the temporal length of the sequence is not positive and greater than 0.
        AssertionError: If the length of the desired output sequence is smaller than the initial one.
        
    Note:
        The padding is done with the mean value of the whole sequence.
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray) , f"Object {sequence} is not a list nor an array."
    assert freq > 0, "The frequence of the signal must be a positive non-zero number."
    assert t > 0, f"The length of the sequence {t} must be positive and greater than 0."
    size = int(t * 60 * freq)
    assert len(sequence) <= size, f"Pad function can not output a sequence smaller than the initial one."
    
    if len(sequence) < size:
        # Pad the sequence with the mean value of the whole sequence (to be revised).
        return np.pad(sequence, ((size - len(sequence)), 0), mode = 'mean')
    else:
        return sequence


# In[ ]:


def epoch_calc(sequence, freq=4, epoch=3.75):
    """
    Resamples the input signal per epoch.
    
    Given a signal with an initial frequency of `freq` Hz, this function converts it to a signal with a frequency of 
    (1 / (freq * epoch)) Hz. This conversion should be performed after the preprocessing and padding steps.
    
    Args:
        sequence (list or np.ndarray): The FHR or tocometry sequence of values.
        freq (float, optional): The frequency of the signal in Hz. Defaults to 4.
        epoch (float, optional): The seconds equivalent to one epoch. Defaults to 3.75s.
        
    Returns:
        list: The resampled FHR/tocometry signal at a frequency of (1 / (freq * epoch)) Hz.
    
    Raises:
        AssertionError: If the  input sequence is not a list or an ndarray.
        AssertionError: If the frequency of the signal is not a positive non-zero number.
        AssertionError: If the epoch value is not a positive non-zero number expressing the seconds that one epoch lasts.
    
    Example:
        >>> epoch_calc([1, 2, 3, 4, 5, 6, 7, 8], freq=4, epoch=1)
        [2.5, 6.5]
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray) , f"Object {sequence} is not a list nor an array."
    assert freq > 0, "The frequence of the signal must be a positive non-zero number."
    assert epoch > 0, f"{epoch} must be a positive non-zero number expressing the seconds that one epoch lasts."
    epoch = int(epoch * freq)
    # Convert the sequence value to integers.
    sequence = [int(x) for x in sequence]
    mean = []
    i = 0
    while i < len(sequence):
        mean_int = np.mean(sequence[i:i+epoch])
        mean.append(mean_int)
        i += epoch
    return mean


# In[ ]:


def moving_average(sequence, size=5):
    """
    Applied a moving average smoothing measure to the input signal or sequence.
    
    The moving average smooths the input signal using a sliding window of the specified `size`.
    
    Args:
        sequence (list or np.ndarray): The values from the signal we want to smooth.
        size (int, optional): The size of the window to perform the moving average. Defaults to 5.
        
    Returns:
        list: The smoothed signal after applying the moving average.
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: If the `size` parameter is not an integer greater than 0.
    
    Example:
        >>> moving_average([1, 2, 3, 4, 5, 6, 7, 8], size=5)
        [2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 6.5, 7.0]
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray) , f"Object {sequence} is not a list nor an array."
    assert isinstance(size, int) and size > 0, f"{size} must be a integer greater than 0."    
    
    seq_final = sequence.copy()
    i = 0
    l = size // 2
    while i < len(sequence):
        seq_final[i] = np.mean(sequence[max(0, i-l) : min(len(sequence), i+l+1)])
        i += 1
    return seq_final


# In[ ]:


def gap_detection(sequence, freq=4):
    """
    Detects and interpolates small gaps in a sequence of FHR values.
    
    The function identifies 0-valued segments in the FHR sequence that last less than 15 seconds (a total of 15*freq points).
    When such segments are found, linear interpolation is applied between their extremes. This is the first part of the 
    preprocessing methodology.
       
    Args:
        sequence (list or np.ndarray): Sequence of FHR values.
        freq (float, optional): The frequency of the signal in Hz. Defaults to 4.
        
    Returns: 
        np.ndarray: Sequence of FHR values interpolated in the small gaps.
    
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: IF the frequency of the signal is not a positive non-zero number.
    
    Example:
        >>> gap_detection([120, 0, 0, 0, 135, 136, 0, 0, 0, 0, 0, 145, 0, 0, 150], freq=4)
        array([120., 123.75, 127.5, 131.25, 135., 136., 137.5, 139., 140.5, 142., 143.5, 145., 146.67, 148.33, 150.])
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert freq > 0, "The frequence of the signal must be a positive non-zero number."
    # Gap Detection
    decision = np.array([1] * len(sequence))
    seq = np.array(sequence)
    x = np.arange(len(seq))
    count = 0
    i = 0
    while i < len(seq):
        if seq[i] != 0:
            if count <= 15 * freq:
                decision[i-count:i] = [0] * count
            count = 0
        else:
            # A 0 value has been found.
            count += 1
        i += 1
        
    # Interpolating small gaps.
    condition = decision == 1
    # Keep the values where there are no small gaps.
    filtered_values = seq[condition]
    filtered_x = x[condition]
    # Do the linear interpolation on the filtered values.
    interp = scipy.interpolate.interp1d(filtered_x, filtered_values)
    x_final = np.arange(filtered_x[0], filtered_x[-1] + 1)
    seq_final = interp(x_final)
    
    return seq_final


# In[ ]:


def stable_points(sequence):
    """
    Identifies stable segments and unstable points in a sequence of FHR values. 
    
    This function aims to find the stable segments (coded with 1) and also locate the unstable points (coded with 2).
    It is desgined to be applied after the `gap_detection` function and before the `interpol_unstables` one.

    Stable segments: Time series of five adjacent samples with the differences among them less than 10bpm.
  
    Unstable points: first sample of the two adjacent points where the difference is higher than 25bpm.

    Args: 
        sequence (list or np.ndarray): Sequence of FHR values.
        
    Returns: 
        list: "Hot-encoder" kind of list where:
            - = 0 if the point is neither stable nor unstable, 
            - = 1 if point is part of a stable segment, and 
            - = 2 if the point is unstable.
            
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
    
    Example:
        >>> stable_points(([120, 123, 153, 128, 129, 130, 129, 135, 137, 163, 150]))
        [0, 0, 2, 1, 1, 1, 1, 1, 1, 2, 0]
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    
    stable = [0] * len(sequence)
    seq = np.array(sequence)
    i = 1
    count = 1
    
    while i < len(seq):
        diff = np.absolute(seq[i] - seq[i-1])
        if diff <= 10 and seq[i] > 0:
            count += 1
            i += 1            
            # To consider the extreme cases where the stable segments
            # lasts until the end of the sequence.
            if i == len(seq) - 1:
                stable[i-count:len(seq)] = [1] * (count+1)
        
        elif diff >= 25:
            stable[i] = 2
            # If it comes from a stable period, update the information.
            if count >= 5 and seq[i] >= 0:
                stable[i-count:i] = [1] * count
            i += 1
            count = 1
        
        elif (diff > 10 and diff < 25) or (diff == 0 and seq[i] == 0):
            # If it comes from a stable period, update the information.
            if count >= 5 and seq[i] >= 0:
                stable[i-count:i] = [1] * count
            i += 1
            count = 1

    return stable


# In[ ]:


def interpol_unstables(sequence, stable):
    """
    Linearly interpolates the segments found between an unstable point and the beginning of the next stable period.
    
    This function is designed to be applied after the `gap_detection` and `stable_points` functions, and before the
    `outlier_interpol` one.
  
    Args:
        sequence (list or np.ndarray): The sequence of FHR values.
        stable (list): A list that has 1 in the positions where the sequence is stable, 2 in the positions where the 
                       sequence is unstable and 0, otherwise.
                       
    Returns:
        np.ndarray: The linearly interpolated signal in the unstable segments.
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: If the lengths of `sequence` and `stable` are different.
    
    Example:
        >>> sequence = [120, 123, 153, 128, 129, 130, 129, 135, 137, 163, 150]
        >>> stable = [0, 0, 2, 1, 1, 1, 1, 1, 1, 2, 0]
        >>> interpol_unstables(sequence, stable)
        array([120., 123., 125.5, 128., 129., 130., 129., 135., 137., 143.5, 150.])
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert len(sequence) == len(stable), f"Object {sequence} and object {stable} have different lengths."
    
    saved = np.array([0] * len(sequence))
    i = 0
    keep = True
    while i < len(sequence):
        if stable[i] == 2:
            keep == False
            
        elif stable[i] == 1 and keep == False and sequence[i] > 0:
            keep == True
            saved[i] = 1
            
        elif (stable[i] == 1 or stable[i] == 0) and (keep == True) and sequence[i] > 0:
            saved[i] = 1
            
        i += 1
    # Interpolating unstable segments.
    condition = saved == 1
    # Keep the interesting values.
    filtered_values = np.array(sequence)[condition]
    filtered_x = np.arange(len(sequence))[condition]
    # Interpolate linearlly 
    interp = scipy.interpolate.interp1d(filtered_x, filtered_values)
    x_final = np.arange(filtered_x[0], filtered_x[-1] + 1)
    seq_final = interp(x_final)
    
    return seq_final


# In[ ]:


def outlier_interpol(sequence, inter='linear'):
    """
    Applies linear/spline interpolation to the points that are considered physiologically inconsistent (<50bpm and >200bpm).
    
    This function is designed to be applied after the `interpol_unstables` function but before the `epoch_calc` and 
    `moving_average` methods. 

    Args: 
        sequence (list or np.ndarray): Sequence of FHR values.
        inter (str, optional): The type of interpolation to be used. Can be 'linear' for linear interpolation or 'spline' for
                               spline interpolation. Defaults to 'linear'.
                               
    Returns: 
        np.ndarray: The final sequence of FHR values without outliers.
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: IF the interpolation type is not 'linear' or 'spline'.
        
    Example:
        >>> sequence = [120, 123, 153, 128, 129, 45, 20, 135, 210, 163, 150]
        >>> outlier_interpol(sequence, inter='linear')
        array([120., 123., 153., 128., 129., 131., 133., 135., 149., 163., 150.])
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert inter == 'linear' or inter == 'spline', "Only linear and spline interpolation are supported."
    
    # Collect the points of interest in other to do the
    # linear interpolation. 
    interpolation_x = []
    interpolation_y = []  
    i = 0  
    while i < len(sequence):
        # Take those points physiologicallly faisables. 
        if sequence[i] >= 200 or sequence[i] <= 50:
            i += 1
        else:
            interpolation_x.append(i)
            interpolation_y.append(sequence[i])
            i += 1
    
    # Create the interpolation object, can be linear or spline.
    if inter == 'linear':
        x = np.array(interpolation_x)
        y = np.array(interpolation_y)    
        interp = scipy.interpolate.interp1d(x, y)
        x_final = np.arange(x[0], x[-1] + 1)
    elif inter == 'spline':
        x = np.array(interpolation_x)
        y = np.array(interpolation_y)
        interp = scipy.interpolate.CubicSpline(x, y)
        x_final = np.arange(x[0], x[-1] + 1)


    # Generate points in the interpolated curve
    seq_final = interp(x_final)
    # Assure that the interpolated values that are going to be used
    # are in the correct physiological interval. 
    seq_final = np.clip(seq_final, 50, 200)

    return seq_final


# In[ ]:


def fhr_preprocess(sequence, freq=4, inter='linear', t=120):
    """
    Integrates the three steps of the proposed preprocessing methodology and the final padding:
        1) Small gap detection + Linear Interpolation.
        2) Unstable segments detection + Linear Interpolation.
        3) Outlier detection + Linear/Spline Interpolation.
        4) Padding until the sequence has the desired length.
    
    This function preprocesses the input FHR sequence of values according to the proposed methodology. It performs small gap
    detection with linear interpolation, detects unstable segments, and applies outlier detection with either linear or
    spline interpolation.
    
    Args:
        sequence (list or np.ndarray): The FHR sequence of values to be preprocessed.
        freq (float, optional): The frequency of the signal. Defaults to 4 Hz.
        inter (str, optional): The interpolation methodology to be used. Can be 'linear' or 'spline'. Defaults to 'linear'.
        t (float, optional): The final time of the sequences in minutes. Defaults to 120 minutes.
        
    Returns:
        np.ndarray: The preprocessed FHR sequence after padding. 
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: If the frequency of the signal is not a positive non-zero number.
        AssertionError: If the interpolation type is not 'linear' or 'spline'.
        AssertionError: IF the final time of the sequences is not a positive non-zero number.
        
    Example:
        >>> sequence = [120, 0, 0, 0, 135, 136, 0, 0, 0, 0, 0, 145, 0, 0, 150]
        >>> fhr_preprocess(sequence, freq=4, t=0.08)
        array([137.73, 137.73, 137.73, 137.73, 120., 123.75, 127.5, 131.25, 135.,
        136., 137.5, 139., 140.5, 142., 143.5, 145., 146.67, 148.33, 150.])
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert freq > 0, "The frequence of the signal must be a positive non-zero number."
    assert inter == 'linear' or inter == 'spline', 'Only linear or spline interpolation are supported.'
    assert t > 0, "The final time of the sequences must be a positive non-zero number."
    
    # Proposed Preprocessing Method.
    # 1) Small gap detection.
    sequence = gap_detection(sequence, freq=freq)
    # 2) Unstable segments detection.
    stable = stable_points(sequence)
    sequence = interpol_unstables(sequence, stable)
    # 3) Outlier detection.
    sequence = outlier_interpol(sequence, inter)
    # Padding.
    sequence = pad(sequence, freq=freq, t=t)
    return sequence


# In[ ]:


def toco_preprocess(toco, freq=4, t=120):
    """
    Implements the chosen methodology to preprocess the tocometry signal sampled at `freq`Hz.
    
    This function applies the following steps to preprocess the tocometry signal:
        1) Baseline Removal with the use of AIRPLS algorithm (can be found in references).
        2) Padding until the the sequence has the desired length.  
    
    Args:
        toco (list or np.ndarray): The original tocometry sequence of values at 4Hz.
        freq (float, optional): The frequency of the signal. Defaults to 4Hz.
        t (float, optional): The final time of the sequences in minutes. Defaults to 120 minutes.
        
    Returns:
        np.ndarray: the processed tocometry sequence.
        
    Raises:
        AssertionError: If the input tocometry signal is not a list or an ndarray.
        AssertionError: If the frequency of the signal is not a positive non-zero number.
        AssertionError: If the final time of the sequences is not a positive non-zero number.
        
    Note:
        The AIRPLS algorithm is used for baseline removal, as referred to in the references.
        
    Example:
        See ZhangFit() in the Baseline Removal Python library.         
    """
    assert isinstance(toco, list) or isinstance(toco, np.ndarray), f"Object {toco} is not a list nor an array."
    assert freq > 0, "The frequence of the signal must be a positive non-zero number."
    assert t > 0, "The final time of the sequences must be a positive non-zero number."
    # Baseline Removal Algorithm.
    baseObj = BaselineRemoval(toco)
    toco = baseObj.ZhangFit()
    # Padding.
    toco = pad(toco, freq=freq, t=t)
    return toco


# # Baseline

# In[ ]:


def erode(sequence, w):
    """
    Applies the erosion operation to reduce the values in the sequence and smooth out local peaks or outliers within the window.
    
    The erosion operation involves sliding a structuring element (also known as a kernel or a window) over the input signal or
    image and replacing each element with the minimum value within the corresponding neighborhood defined by the structuring
    element.
    
    This function is primarily used for the baseline computation according to the Cazares' algorithm.
    
    Args:
        sequence (list or np.ndarray): The FHR values sampled per epoch.
        w (int): The size of the sliding window when applying the erosion.
        
    Returns:
        list: The sequence after having applied the erosion operation.
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: If the size of the sliding window is not a positive integer (greater than 0).
    
    Example:
        >>> fhr_values = [120, 130, 135, 140, 130, 145, 150, 120, 115]
        >>> erode(fhr_values, w=2)
        [120, 120, 120, 130, 130, 120, 115, 115, 115]
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert w > 0, f"The size {w} of the sliding window must be positive (greater than 0)."
    
    s = [0] * len(sequence)
    for i in range(len(sequence)):
        s[i] = min(sequence[max(0, i-w) : min(len(sequence), i+w+1)])
    return s


# In[ ]:


def dilate(sequence, w):
    """
    Applies the dilation operation to reduce the values in the sequences and smooth out local peaks or outliers within the window.
    
    The dilation operation involves sliding a structuring element (also known as kernel or window) over the input signal or image
    and replacing each element with the maximum value within the corresponding neighborhood defined by the structuring element.
    
    This function is primarily used for the baseline computation according to the Cazares' algorithm.
    
    Args:
        sequence (list or np.ndarray): The FHR values sampled per epoch.
        w (int): The size of the sliding window when applying the dilation.
        
    Returns:
        list: The sequence after having applied the dilation operation.
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: If the size of the sliding window is not a positive integer (greater than 0).
    
    Example:
        >>> fhr_values = [120, 130, 135, 140, 130, 145, 150, 120, 115]
        >>> dilate(fhr_values, w=2)
        [135, 140, 140, 145, 150, 150, 150, 150, 150]
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert w > 0, f"The size {w} of the sliding window must be positive (greater than 0)."
    
    s = [0] * len(sequence)
    for i in range(len(sequence)):
        s[i] = max(sequence[max(0, i-w) : min(len(sequence), i+w+1)])
    return s


# In[ ]:


def opens(sequence, w):
    """
    Applies the erosion and dilation operations sequentially to a given sequence.
    
    This function first applies the erosion operation to reduce the values in the sequence and smooth out local peaks or outliers 
    within the window. Then, it applies the dilation operation to further enhance the smoothed sequence.
    
    The erosion operation involves sliding a structuring element (also known as kernel or window) over the input signal or image
    and replacing each element with the minimum value within the corresponding neighborhood defined by the structuring element.
    
    The dilation operation involves sliding a structuring element over the input signal or image and replacing each element with
    the maximum value within the corresponding neighborhood defined by the structuring element.
    
    This function is primarily used for the baseline computation according to the Cazares' algorithm.
    
    Args:
        sequence (list or np.ndarray): The FHR values sampled per epoch.
        w (int): The size of the sliding window when applying both operations.
        
    Returns:
        list: The sequence after having applied erosion, and then dilation.
        
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: IF the size of the sliding window is not a positive integer (greater than 0).
        
    Example:
        >>> fhr_values = [120, 130, 135, 140, 130, 145, 150, 120, 115] 
        >>> opens(fhr_values, w=2)
        [120, 130, 130, 130, 130, 130, 130, 120, 115]
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert w > 0, f"The size {w} of the sliding window must be positive (greater than 0)."
    
    return dilate(erode(sequence, w), w)


# In[1]:


def closes(sequence, w):
    """
    Applies the dilation and erosion operations sequentially to a given sequence.
    
    This function first applies the dilation operation to reduce the values in the sequence and smooth out local peaks or
    outliers within the window. Then, it applies the erosion operation to further enhance the smoothed sequence.
    
    The dilation operation involves sliding a structuring element (also known as kernel or window) over the input signal
    or image and replacing each element with the maximum value within the corresponding neighborhood defined by the
    structuring element.
    
    The erosion operation involves sliding a structuring element over the input signal or image and replacing each element
    with the minimum valuue within the corresponding neighborhood defined by the structuring element.
    
    This function is primarily used for the baseline computation according to the Cazares' algorithm.
    
    Args:
        sequence (list or np.ndarray): The FHR values sampled per epoch.
        w (int): The size of the sliding window when applying both operations.
        
    Returns:
        list: The sequence after having applied dilation, and then erosion.
    
    Raises:
        AssertionError: If the input sequence is not a list or an ndarray.
        AssertionError: If the size of the sliding window is not a positive integer (greater than 0).
        
    Example:
        >>> fhr_values = [120, 130, 135, 140, 130, 145, 150, 120, 115]
        >>> closes(fhr_values, w=2)
        [135, 135, 135, 140, 140, 145, 150, 150, 150]
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert w > 0, f"The size {w} of the sliding window must be positive (greater than 0)."
    
    return erode(dilate(sequence, w), w)


# In[ ]:


def compute_freq(subseq):
    """
    Computes the most frequent FHR values within the subsequence and their frequencies.
    
    This function takes a subsequence of FHR values and computes the 50 most frequently
    ocurring FHR values and their corresponding frequencies within the subsequence.
    
    It is primarily used for the baseline computation according to the SisPorto's algorithm.

    Args: 
        subseq (list): The FHR values sequence.

    Returns:
        tuple: A tuple containing two lists - `max_values` and `h`.
            - max_values (list): A vector of the maximum 50 most repeated FHR values.
            - h (list): A vector within the frequency of each of the corresponding FHR values.
    
    Raises:
        AssertionError: If the input subseq is not a list.
        
    Example:
        >>> fhr_subseq = [120, 130, 135, 120, 130, 130, 120, 130, 135]
        >>> compute_freq(fhr_subseq)
        ([130, 120, 135], [0.44, 0.33, 0.22])
    """
    assert isinstance(subseq, list), f"Object {subseq} must be a list."
    
    res = []
    l = len(subseq)

    # Create a set of all the different values that are found in the sequence
    values = set(subseq)

    # For each of this values, count the number of them in the set and also
    # compute the frequence.
    for x in values:
        count = subseq.count(x)
        freq = count / l
        # Interested in maximum 50 values and only if the frequence is 
        # greater than a certain value.
        if freq >= 0:
            res += [[x, freq]]
        
    # We sort the values in descendent order in relation to their frequence.
    res = sorted(res, key=lambda x: x[1], reverse=True)

    # Make sure we just take the first 50 values. 
    if len(res) >= 50:
        res = res[:50]
#     else:
#         res = res + [res[-1]] * (50-len(res))

    # First component will be the most repeated FHR values.
    max_values = [x[0] for x in res]

    # Second component will be the frequence itself.
    h = [round(x[1],2) for x in res]
    return max_values, h


# In[ ]:


def abnormal_stv(subseq):
    """
    Identifies points with abnormal STV (Short Term Variability) in a given FHR sequence.
    
    This function analyzes a subsequence of FHR values and identifies points with abnormal
    Short Term Variability (STV). A point is considered abnormal if the difference between
    its adjacent FHR signals is less than 1bpm.
    
    It is primarily used for the baseline computation according to the SisPorto's algorithm.

    Args:
      subseq (list): The sequence of the FHR values.

    Returns:
      float: A number between 0 and 100 expressing the percentage of abnormal STV points 
             within the analyzed sequence.
             
    Raises:
        AssertionError: IF the input subseq is not a list.
    
    Example:
        >>> fhr_subseq = [120, 125, 130, 130, 128, 120, 120, 120]
        >>> abnormal_stv(fhr_subseq)
        14.29
    """
    assert isinstance(subseq, list), f"Object {subseq} must be a list."
    
    abnormal = 0
    i = 1
    # Idea: fix a point i a then compare the difference between the 
    # previous and the following value in the subsequence. 
    while i < len(subseq) - 1:
        # If difference between this two is lower than 1 bpm, the i point will
        # be considered as an abnormal stv point.  
        if np.abs(subseq[i+1] - subseq[i-1]) < 1:
            abnormal += 1    
        i += 1  
    # Return the number of abnormal STV points divided by the lenght of the 
    # sequence. 
    abnormal_stv = ( abnormal / i ) * 100

    return round(abnormal_stv, 2)


# In[ ]:


def SisPortoBase(subseq):
    '''
    Computes the FHR baseline according to the SisPorto2.0 algorithm criteria.
    
    This function takes a subsequence of FHR values and computes the FHR baseline
    according to the criteria exposed in the paper of the SisPorto2.0 algorithm.

    Args:
        subseq (list): The sequence of the FHR values.
      
    Returns:
        int: A scalar number indicating the baseline of the subsequence.
      
    Raises:
        AssertionError: If the input subseq is not a list.
    
    Example:
        >>> fhr_subseq = [120, 130, 135, 130, 125, 120, 130, 130]
        >>> SisPortoBase(fhr_subseq)
        130        
    '''
    assert isinstance(subseq, list), f"Object {subseq} must be a list."
    
    # Find the stable points in the subsequence in particular
    stable = stable_points(subseq)
    fhr_stables = [value for value, flag in zip(subseq, stable) if flag==1]
    fhr_stables = [int(x) for x in fhr_stables]
    # Computation of the most frequent FHR values and their explicit frequence.
    max_values, h = compute_freq(fhr_stables)

    # Computation of the abnormal STV points in the sequence.
    aSTV = abnormal_stv(subseq)

    # Take the first component as the initial BL value. 
    BL = max_values[0]

    # SisPorto2.0 Baseline Algorithm (see references).
    if BL >= 110:
        if BL > 152:
            for i in range(1, len(max_values)):
                if 110 <= max_values[i] and max_values[i] < BL and h[i] > 1.6 * aSTV * h[0]:
                    BL = max_values[i]
            return BL

        else:
            if aSTV < 20:
                F = 4
            elif 20 <= aSTV and aSTV < 30:
                F = 2
            elif 30 <= aSTV and aSTV < 40:
                F = 1
            elif 40 <= aSTV and aSTV < 60:
                F = 1/2
            elif aSTV >= 60:
                F = 1
    
            for i in range(1, len(max_values)):
                if 110 <= max_values[i] and max_values[i] < BL and h[i] > F * aSTV * h[0]:
                    BL = max_values[i]    
            return BL

    else:
        for i in range(1, len(max_values)):
            if max_values[i] > 110 and h[i] > 1/3 * (1 - aSTV) * h[0]:
                BL = max_values[i]
                return BL

        for i in range(1, len(max_values)):
            if max_values[i] < BL and h[i] > aSTV * h[0]:
                BL = max_values[i]    
        return BL


# In[ ]:


def baselevelreference(hbi):
    """
    Calculates a baseline reference value based on the conditions in the article "Computer
    analysis of antepartum fetal heart rate: 1. Baseline Determination" (1990) by S.Boudet.
    
    This function takes a sequence of heart beat intervals (HBI) and calculates a baseline
    reference value based on the conditions imposed in the article by S.Boudet. The 
    calculated baseline reference is used for further analysis in antepartum fetal heart
    rate monitoring. 
    
    Args:
        hbi (list or np.ndarray): The sequence of heart beat intervals.
        
    Returns:
        int: The estimated baseline reference.
        
    Raises:
        AssertionError: If the input hbi is not a list or ndarray.
        
    Example:
        >>> hbi_sequence = [350, 380, 395, 410, 420, 450, 480]
        >>> baselevelreference(hbi_sequence)
        410
    """
    assert isinstance(hbi, list) or isinstance(hbi, np.ndarray), f"Object {hbi} is not a list nor an array."
    
    hbi = [round(i) for i in hbi] 
    histogram = np.zeros(300)
    
    for i in range(len(hbi)):
        # If current heart beat interval is not NaN and falls within the range of 301 and 600,
        # the corresponding index in histogram is incremented by 1.
        if (not np.isnan(hbi[i])) and (hbi[i] > 300) and (hbi[i] <= 600):
            histogram[int(hbi[i])-300-1] += 1
    
    # Ensure that histogram represents the relative frequencies.
    histogram /= np.sum(histogram)
    cshist = np.cumsum(histogram)
    
    # Cumulative sum is less than or equal to 0.875 and the values are greater than their
    # neighboring elements.
    mask = (cshist <= 0.875) & np.concatenate(([0, 0, 0, 0, 0], (histogram[5:-1] > histogram[6:]) &
                                              (histogram[5:-1] > histogram[4:-2]) & 
                                              (histogram[5:-1] > histogram[3:-3]) & 
                                              (histogram[5:-1] > histogram[2:-4]) & 
                                              (histogram[5:-1] > histogram[1:-5]) & 
                                              (histogram[5:-1] > histogram[:-6]), [0]))
    
    # Estimated baseline reference: if any indices satisfy the mask conditions, last index in
    # the masked array is selected, and 300 is added to it.
    # If no indices satisfy the mask conditions, the index of the maximum value in the histogram
    # is selected, representing the most common heart beat interval.
    p = np.where(mask)[0][-1] + 300 if np.any(mask) else np.argmax(histogram)
    
    return p


# In[ ]:


def baselineloop(hbi):
    """
    Obtains reference values for a given sequence, taking a 64-minute window as reference.
    Used as part of the baseline computation according to the Mantel's algorithm.
    
    This function calculates reference values for a given sequence of heart base intervals (HBI)
    by taking a 64-minute window (corresponding to 240 samples in the sequence) as reference.
    The calculated reference values are used for baseline computation in the Mantel's algorithm.
    
    Args:
        hbi (list or np.ndarray): The sequence of heart beat interval values.
        
    Returns:
        np.ndarray: The final reference values for the initial sequence.
        
    Raises:
        AssertionError: If the input hbi is not a list or ndarray.
    """
    assert isinstance(hbi, list) or isinstance(hbi, np.ndarray), f"Object {hbi} is not a list nor an array."
    
    blsupport = np.array([0] * len(hbi))
    
    # Suppose 10-min window which is 10min*24points = 240 samples.    
    if len(hbi) < 240:
        blsupport[:] = baselevelreference(hbi)
    else:
        for i in range(0, len(hbi)-240+1, 240):
            blsupport[i:i+240] = baselevelreference(hbi[i:i+240])
            
    return blsupport


# In[ ]:


def filterpass(B, P):
    """
    Applies the filter pass as described by R.Mantel in his article "Computer analysis of antepartum
    fetal heart rate: 1. Baseline Determination" (1990).
    
    Used as part of the baseline computation.
    
    This function filters the initial sequence B using the reference sequence P, following the filter
    pass algorithm proposed by R.Mantel. The filtered signal B is adjusted considering the difference
    between B and P for each corresponding sample, while ensuring that the difference is within a 
    threshold of 60. 
    
    Args:
        B (list or np.ndarray): The initial sequence to be filtered.
        P (list or np.ndarray): The reference sequence used for filtering.
        
    Returns:
        list or np.ndarray: The filtered signal B according to the reference P.
        
    Raises:
        AssertionError: If either input B or P is not a list or numpy array.
    """
    assert isinstance(B, list) or isinstance(B, np.ndarray), f"Object {B} is not a list nor an array."
    assert isinstance(P, list) or isinstance(P, np.ndarray), f"Object {P} is not a list nor an array."
    
    # Backward dummy
    B0 = P[1]
    for i in range(len(B)-1, -1, -1):
        if abs(B[i] - P[i]) <= 60:
            B0 = 0.95 * B0 + 0.05 * B[i]
            
    # Forward pass
    if abs(B[0] - P[0]) <= 60:
        B[0] = 0.95 * B0 + 0.05 * B[0]
    else:
        B[0] = B0
    
    for i in range(1, len(B)):
        if abs(B[i] - P[i]) <= 60:
            B[i] = 0.95 * B[i-1] + 0.05 * B[i]
        else:
            B[i] = B[i-1]
    
    # Backward Pass
    for i in range(len(B)-2, -1, -1):
        B[i] = 0.95 * B[i+1] + 0.05 * B[i]
        
    return B


# In[ ]:


def trimRR(A, B, U, L):
    """
    Applies the trim function as described by R.Mantel in his article "Computer analysis of antepartum
    fetal heart rate: 1. Baseline Determination" (1990).
    
    Used as part of the baseline computation.
    
    This function trims the initial sequence B based on the comparison with reference sequence A using
    upper and lower frontier thresholds U and L, respectively. Segments in B that violate the frontier
    constraints will be trimmed to match the corresponding segments in A.
    
    Args:
        A (list or np.ndarray): The initial sequence to trim.
        B (list or np.ndarray): The initial reference sequence to trim B.
        U (float or int): The upper frontier threshold when trimming.
        L (float or int): The lower frontier threshold when trimming.
        
    Returns:
        list or np.ndarray: The sequence B after the trim function has been applied.
    
    Raises:
        AssertionError: If either input A or B is not a list or np.ndarray.
        AssertionError: If U or L is not a positive value.
    """
    assert isinstance(A, list) or isinstance(A, np.ndarray), f"Object {A} is not a list nor an array."
    assert isinstance(B, list) or isinstance(B, np.ndarray), f"Object {B} is not a list nor an array."
    assert U > 0, f"Upper frontier {U} when trimming must be positive (greater than 0)."
    assert L > 0, f"Lower frontier {L} when trimming must be positive (greater than 0)."
    
    # Keep track of the points in the sequence that should be trimmed.
    blpoints = np.ones(len(A))
    A = np.array([60000. / x for x in A])
    B = np.array([60000. / x for x in B])
    i = 0
    while i < len(A):
        if A[i] > B[i] + U:
            # Upper frontier violation. Identify starting index (d) and ending index (f) of
            # the violated segment in the A and B sequence.
            d = np.where(A[:i] < B[:i])[0][-1] + 1 if np.any(A[:i] < B[:i]) else 0
            f = np.where(A[d:] < B[d:])[0][0] + d - 1 if np.any(A[d:] < B[d:]) else i - 1
            # The segment (d, f) should be trimmed.
            blpoints[d:f+1] = 0
            i = f + 1
        elif A[i] < B[i] - L:
            # Lower frontier violation. Identify starting index (d) and ending index (f) of
            # the violated segment in the A and B sequence.
            d = np.where(A[:i] > B[:i])[0][-1] + 1 if np.any(A[:i] > B[:i]) else 0
            f = np.where(A[d:] > B[d:])[0][0] + d - 1 if np.any(A[d:] > B[d:]) else i - 1
            # The segment (d, f) should be trimmed.
            blpoints[d:f+1] = 0
            i = f + 1
        else:
            i += 1
    
    # All points marked as 1 are replaced by the corresponding values from the A sequence.
    B[blpoints == 1] = A[blpoints == 1]
    B = 60000. / B
    
    return B            


# In[ ]:


def resamp(x, factor, l, lin=None):
    """
    Resamples the input array x with a given resampling factor and target length l.
    
    This function performs resampling of the input array x, where the resampling factor
    determines how many points will be generated between each pair of adjacent points
    in the original array. The target length l defines the desired length of the final
    resampled sequence.
    
    Args:
        x (np.ndarray): The array to resample.
        factor (int or float): The resampling factor.
        l (int): The target length of the final sequence.
        lin (bool, optional): if True, resampling will generate factor+1 equally spaced 
                              points in between the initial points. If False, basic linear 
                              interpolation is applied. If None, the default behavior is 
                              used (linear interpolation).
                              
    Returns:
        np.ndarray: The resampled sequence.
        
    Raises:
        AssertionError: If input x is not a numpy array.
        AssertionError: If `factor` or `l` is not a positive value.
        AssertionError: If `lin` is not a boolean or None.
    
    Example:
        >>> input_array = np.array([1, 2, 3])
        >>> resampling_factor = 2
        >>> target_length = 6
        >>> resamp(input_array, resampling_factor, target_length, lin=True)
        array([1.5, 2., 2.5, 3., 0., 0.])
    """
    assert isinstance(x, np.ndarray), f"Object {x} should be an array."
    assert factor > 0, f"Resampling factor {factor} should be positive (greater than 0)."
    assert l > 0, f"Length of the sequence {l} should be positive (greater than 0)."
    assert lin == True or lin == None, f"Object {lin} is a boolean."
    
    if lin is not None:
        y = np.zeros(len(x) * factor)
        for i in range(len(x) - 1):
            pt = np.linspace(x[i], x[i+1], factor + 1)
            y[(i * factor) : (i * factor) + factor] = pt[1:]
    else:
        y = scipy.interpolate.interp1d(np.arange(len(x)), x, kind='linear')(np.linspace(0, len(x)-1, len(x)*factor))
        
    y = np.append(y, np.full(l - len(y), y[-1]))
    return y


# In[1]:


def enveloppe(x):
    """
    Computes the upper and lower envelope of the given signal x.
    
    This function computes the upper and lower envelope of the input signal x. The upper envelope
    represents the peaks or local maximum points in the signal, while the lower envelope represents
    the valleys or local minimum points.
    
    This computation is used as part of the baseline computation in the Lu's algorithm.
    
    Args:
        x (np.ndarray): The input signal for which upper and lower envelopes are computed.
        
    Returns:
        tuple: A tuple containing two np.ndarray - `eu` and `el`.
            - eu (np.ndarray): The upper envelope of the signal.
            - el (np.ndarray): The lower envelope of the signal.
        
    Raises:
        AssertionError: If input x is not a numpy array.
    """
    assert isinstance(x, list) or isinstance(x, np.ndarray), f"Object {x} is not a list nor an array."
    
    # The indices where x is greater than the previous subsequent elements. (Local Maximum)
    upoints = np.concatenate(([0], np.where((x[1:-1] >= x[:-2]) & (x[1:-1] > x[2:]))[0] + 1, [len(x) -1]))
    # The indices where x is lower than the previous subsequent elements. (Local Minimum)
    lpoints = np.concatenate(([0], np.where((x[1:-1] <= x[:-2]) & (x[1:-1] < x[2:]))[0] + 1, [len(x) -1]))
    
    upoints = np.array([int(m) for m in upoints])
    lpoints = np.array([int(m) for m in lpoints])
    
    # Create the interpolation objects.
    eu_func = interp1d(upoints, x[upoints], kind='slinear')
    el_func = interp1d(lpoints, x[lpoints], kind='slinear')
    
    # Interpolate the desired interval.
    eu = eu_func(np.arange(len(x)))
    el = el_func(np.arange(len(x)))
    
    return eu, el


# In[ ]:


def linearinterpolation(x, y, xx):
    """
    Applies basic linear interpolation to the given function values.
    
    This function performs basic linear interpolation using the provided points (x, y)
    and applies it to the desired interval xx.
    
    Args:
        x (np.ndarray): Points where information is provided.
        y (np.ndarray): Function values that are provided.
        xx (np.ndarray): The desired interval to interpolate our function.
        
    Returns:
        np.ndarray: The final linearlly interpolated function.
    
    Raises:
        AssertionError: In inputs x, y, or xx are not numpy arrays.
    
    Example:
        >>> x = np.array([0, 1, 2, 3])
        >>> y = np.array([1, 2, 3, 4])
        >>> xx = np.array([0.5, 1.5, 2.5])
        >>> linearinterpolation(x, y, xx)
        array([1.5, 2.5, 3.5])
    """
    assert isinstance(x, list) or isinstance(x, np.ndarray), f"Object {x} is not a list nor an array."
    assert isinstance(y, list) or isinstance(y, np.ndarray), f"Object {y} is not a list nor an array."
    assert isinstance(xx, list) or isinstance(xx, np.ndarray), f"Object {xx} is not a list nor an array."
    
    yy = np.zeros_like(xx)
    yy[:x[0]] = y[0]
    for i in range(len(x) - 1):
        yy[x[i] : x[i+1] + 1] = np.linspace(y[i], y[i+1], x[i+1] - x[i] + 1)
    yy[x[-1]:] = y[-1]
    return yy


# In[ ]:


def exclude(x, factor):
    """
    Perform exclusion of certain segments from the given signal.
    
    This function is used as part of the baseline computation in the Lu's algorithm.
    It excludes certain segments from the input sequence x based on the provided factor.
    
    Args:
        x (np.ndarray): The sequence from which certain segments will be excluded.
        factor (int or float): Corresponds to the frequency of the signal.
        
    Returns:
        np.ndarray: The initial sequence after the segment removal (baseline).
        
    Raises:
        AssertionError: If the input x is not a np.ndarray or list.
        AssertionError: If the factor is not positive (greater than 0).        
    """
    
    assert isinstance(x, list) or isinstance(x, np.ndarray), f"Object {x} is not a list nor an array."
    assert factor > 0, f"The element {factor} must be positive (greater than 0)."
    
    # The indices where x is increasing.
    upoints = np.where((x[1:-1] >= x[:-2]) & (x[1:-1] > x[2:]))[0] + 1
    # The indices where x is decreasing.
    lpoints = np.where((x[1:-1] <= x[:-2]) & (x[1:-1] < x[2:]))[0] + 1
    points = np.sort(np.concatenate(([0], upoints, lpoints, [len(x) - 1])))
    # Absolute differences between consecutive values of x. Magnitude of change
    # between adjacent segments. 
    D = np.abs(x[points[1:]] - x[points[:-1]])
    # Define a threshold for the differences.
    Dlim = np.mean(D) + 0.5 * np.std(D)
    truepoints = (D < Dlim)
    truepoints = np.logical_or(np.concatenate(([True], truepoints)), np.concatenate((truepoints, [True])))
    
    CP = []
    winstartlist = np.arange(0, len(x) - 20 * 240 / factor, 2 * 240 / factor)
    workinginterval = np.array([winstartlist + 9 * 240 / factor, winstartlist + 11 * 240 / factor])
    workinginterval[0, 0] = 0
    workinginterval[1, -1] = len(x)
    
    for i in range(len(winstartlist)):
        winstart = winstartlist[i]
        p = points[np.logical_and(truepoints, np.logical_and(points > winstart, points <= winstart + 20 * 240 / factor))]
        ME = np.mean(x[p])
        ST = np.std(x[p])
        pinterval = points[np.logical_and(truepoints, np.logical_and(points > workinginterval[0, i], points <= workinginterval[1,i]))]
        CP = np.concatenate((CP, pinterval[np.abs(x[pinterval] - ME) < ST]))
        
    CP = np.array([int(m) for m in CP])
    baseline = linearinterpolation(CP, x[CP], np.arange(len(x)))
    baseline = moving_average(baseline)
    
    return baseline


# In[ ]:


def mantel_tmin(subsamphbi, epoch=2.5, t=10, freq=4):
    """
    Compute the baseline of the FHR signal as described by R.Mantel in his article
    "Computer analysis of antepartum fetal heart rate: 1. Baseline Determination" (1990).
    
    This function calculated the averaged baseline of the FHR (Fetal Heart Rate) signal
    over a specified time interval t using the method proposed by Mantel.
    
    Args:
        subsamphbi (list or np.ndarray): The HBI signal sampled per epoch.
        epoch (float): The duration in seconds of each epoch. Default is 2.5 seconds.
        t (float): The time in minutes for which the baseline is computed. Default is 10 minutes.
        freq (int or float): The frequency of the FHR signal in Hz. Default is 4Hz.
        
    Returns:
        list: The averaged baseline of the FHR signal each t minutes.
    
    Raises:
        AssertionError: If the input subsamphbi is not a list or np.ndarray.
        AssertionError: If epoch is not positive (greater than 0).
        AssertionError: If `t` is not positive (greater than 0).
        AssertionError: If the parameters are not chosen to divide the whole sequence equally.
        
    Example:
        >>> subsamphbi = [350, 380, 395, 410, 420, 450, 480, 450, 420, 410, 395, 410]
        >>> epoch = 2.5
        >>> t = 0.125
        >>> freq = 4
        >>> mantel_tmin(subsamphbi, epoch, t, freq)
        [143, 143, 143, 143]
    """
    assert isinstance(subsamphbi, list) or isinstance(subsamphbi, np.ndarray), f"Object {subsamphbi} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert t > 0, f"The analysis time {t} must be positive (greater than 0)."
    r = len(subsamphbi) % ((60 * t) / epoch)
    assert r == 0, f"The parameters must be chosen in order to divide equally the whole sequence."

    epoch = int(freq * epoch)
    blsupport = baselineloop(subsamphbi)
    
    bl = filterpass(subsamphbi, blsupport)
    
    bl = trimRR(subsamphbi, bl, 20, 20)
    bl = filterpass(bl, blsupport)
    bl = trimRR(subsamphbi, bl, 15, 20)
    bl = filterpass(bl, blsupport)
    bl = trimRR(subsamphbi, bl, 10, 20)
    bl = filterpass(bl, blsupport)
    bl = trimRR(subsamphbi, bl, 5, 20)
    bl = filterpass(bl, blsupport)

    baselinefhr = 60000./bl

    baseline = resamp(baselinefhr, epoch, len(subsamphbi) * epoch)

    base = []
    for i in range((len(subsamphbi) * epoch) // (int((60 * freq) * t))):
        base += [int(np.mean(baseline[int(i * t * (60 * freq)) : int((i+1) * t * (60 * freq))]))]
    return base


# In[1]:


def cazares_tmin(subseq, epoch=3.75, t=10, freq=4):
    """
    Compute the baseline of the FHR signal as described by S.Cazares in his article
    "Automated Identification of Abnormal Patterns in the Intrapartum Cardiotocogram" (PhD 2002).
    
    This function calculates the averaged baseline of the FHR (Fetal Heart Rate) signal
    over a specified time interval t using the method proposed by Cazares.
    
    Args:
        subseq (list or np.ndarray): The FHR signal sampled per epoch.
        epoch (float): The duration in seconds of each epoch Default is 3.75 seconds.
        t (float): The time in minutes for which the baseline is computed. Default is 10 minutes.
        freq (int or float): The frequency of the signal in Hz. Default is 4Hz.
        
    Returns:
        list: The averaged baseline of the FHR signal each t minutes.
        
    Raises:
        AssertionError: If the input `subseq` is not a np.ndarray or list.
        AssertionError: If `epoch` is not positive (greater than 0).
        AssertionError: If `t` is not positive (greater than 0).
        AssertionError: If the parameters are not chosen to divide the whole sequence equally.
        AssertionError: If `freq` is not positive (greater than 0).
        
    Example:
        >>> subseq = [120, 118, 115, 120, 125, 130, 125, 120]
        >>> epoch = 3.75
        >>> t = 0.5
        >>> freq = 4
        >>> cazares_tmin(subseq, epoch, t, freq)
        [115, 115]
    """
    assert isinstance(subseq, list) or isinstance(subseq, np.ndarray), f"Object {subseq} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert t > 0, f"The analysis time {t} must be positive (greater than 0)."
    r = len(subseq) % ((60 * t) / epoch)
    assert r == 0, f"The parameters must be chosen in order to divide equally the whole sequence."
    assert freq > 0, f"The frequency {freq} of the signal must be positive (greater than 0)."
    
    epoch = int(freq * epoch)
    baseline = moving_average(closes(opens(subseq, 19), 137), 65)
    base = []
    for i in range(len(subseq) // (int(((60 * freq) // epoch) * t))):
        base += [int(np.mean(baseline[int(i * t * ((60 * freq) // epoch)) : int((i+1) * t * ((60 * freq) // epoch))]))]        
    return base


# In[ ]:


def sisporto_tmin(sequence, epoch=3.75, t=10, freq=4):
    """
    Compute the baseline for the FHR signal each t minutes using the SisPorto Algorithm.
    
    The SisPorto Algorithm calculates the averaged baseline of the FHR (Fetal Heart Rate)
    signal over a specified time interval t with moving windows. In case the baseline
    difference between the current window and the previous one is greater than 15bpm, a
    weighted mean is computed (60% of the previous window + 40% of the present window).
    This allows tracking the tendency and making the computation of the baseline less
    sensitive to accelerations or decelerations.
  
    Args:
        sequence (list or np.ndarray): The mean value of the FHR signal per epoch.
        epoch (float): The duration in seconds of each epoch. Default is 3.75 seconds.
        t (float): The time in minutes for which the baseline is computed. Default is 10 minutes.
        freq (int or float): The frequency of the signal in Hz. Default is 4 Hz.
        
    Returns:
        list: The averaged baseline of the FHR signal each t minutes.
        
    Raises:
        AssertionError: If the input sequence is not a np.ndarray or list.
        AssertionError: If `epoch` is not positive (greater than 0).
        AssertionError: If `t` is not positive and not an integer divisor of the whole sequence.
        AssertionError: If `freq` is not positive (greater than 0).
        
    Example:
        >>> subseq = [120, 118, 115, 120, 125, 130, 125, 120]
        >>> epoch = 3.75
        >>> t = 0.5
        >>> freq = 4
        >>> sisporto_tmin(subseq, epoch, t, freq)
        [115, 125]
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    r = len(sequence) % int((60 * t ) / epoch)
    assert t > 0 and r == 0, f"The time of analysis {t} must be positive and an integer divisor of the whole sequence."
    assert freq > 0, f"The frequency {freq} of the signal must be positive (greater than 0)."
    
    epoch = int(epoch * freq)
    i = 0
    # We compute the number of windows we will have in the analysis.
    m = int(len(sequence) // (((60 * freq) // epoch) * t))
    baseline = []
    while i < m:
        subseq = sequence[int(i * ((60 * freq) // epoch) * t): int((i+1) * ((60 * freq) // epoch) * t)]
        base = SisPortoBase(subseq)
        baseline.append(base)    
        i += 1

    for i in range(1, m):
        if np.absolute(baseline[i-1] - baseline[i]) >= 15:
            baseline[i] = int(0.6*baseline[i-1] + 0.4*baseline[i]) 
            
    return baseline


# In[ ]:


def lu_tmin(sequence, epoch=1, t=10, freq=4):
    """
    Compute the baseline of the FHR signal using the method described by Y.Lu in his article
    "Nonlinear baseline estimation of FHR signal using empirical mode decomposition".
    
    The method employs empirical mode decomposition to estimate the baseline of the FHR (Fetal
    Heart Rate) signal. It iteratively computes the mean of the upper and lower enveloppes and
    subtracts it from the original signal until the difference between consecutive estimates
    becomes sufficiently small. 
    
    Args:
        sequence (list or np.ndarray): the mean value of the FHR signal per epoch.
        epoch (float): the duration in seconds of each epoch. Default is 1 second.
        t (float): the time in minutes for which the baseline is computed. Default is 10 minutes.
        freq (int or float): The frequency of the signal in Hz. Default to 4 Hz. 
        
    Returns:
        list: The averaged baseline of the FHR signal each t minutes.
        
    Raises:
        AssertionError: If the input sequence is not a list or np.ndarray.
        AssertionError: If `epoch` is not positive (greater than 0).
        AssertionError: If `t` is not positive (greater than 0).
        AssertionError: If the length of the sequence is not divisible by (60 * t) / epoch.
        AssertionError: If `freq` is not positive (greater than 0).
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert t > 0, f"The analysis time {t} must be positive (greater than 0)."
    r = len(sequence) % int((60 * t) / epoch)
    assert r == 0, f"The parameters must be chosen in order to divide equally the whole sequence."
    assert freq > 0, f"The frequency {freq} of the signal must be positive (greater than 0)."
    
    l = len(sequence) * epoch * freq
    d = np.array(sequence)
    r = np.zeros((9, len(sequence)))
    c = np.zeros((8, len(sequence)))
    
    for j in range(8):
        SD = 1
        while SD > 0.1:
            eu, el = enveloppe(d)
            # Compute the mean of upper and lower envelopes.
            m = (eu + el) / 2
            dprev = d
            # A new estimation of the baseline.
            d = d - m
            SD = np.sum((dprev - d) ** 2) / np.sum(dprev ** 2)
        
        c[j, :] = d
        r[j + 1, :] = r[j, :] - c[j, :]
        d = sequence - np.sum(c, axis=0)
    # The baseline signal is calculated as the sum of the third to eight rows
    # of c and the last row of r.
    baseline = np.sum(c[2:, :], axis=0) + r[j + 1, :]
    baseline = exclude(baseline, freq)
    baseline = resamp(baseline, freq, l) 
    
    base = []
    for i in range(len(baseline) // (((60 * freq) // epoch) * t)):
        base += [np.mean(baseline[i * t * ((60 * freq) // epoch) : (i+1) * t * ((60 * freq) // epoch)])]
    
    return base


# In[ ]:


def baseline(sequence, mode='sisporto', epoch=3.75, t=10, freq=4, preprocess=False, inter='linear', duration=120):
    """
    Compute the baseline of the FHR signal using the selected algorithm.
    
    The function supports multiple baseline computation algorithms ('sisporto', 'cazares', 'mantel', 'lu'). The selected algorithm
    is applied to the provided FHR sequence.
    
    Optionally, the sequence can be preprocessed before baseline computation using linear/spline interpolation.

    Args:
        sequence (list or np.ndarray): The sequence of FHR values.
        mode (str): The baseline algorithm ('sisporto', 'cazares', 'mantel', 'lu'). Default is 'sisporto'.
        epoch (float): The duration in seconds of a given epoch. Default is 3.75 seconds for 'sisporto' and 'cazares',
                       and 2.5 seconds for 'mantel' and 1 second for 'lu'.
        t (float): The time in minutes for which the baseline is computed. Default is 10 minutes.
        freq (int or float): The frequency of the signal in Hz. Default is 4Hz.
        preprocess (bool):  A boolean variable indicating whether to apply preprocess or not to the input sequence.
        inter (str): If preprocess is True, the type of interpolation used to preprocess the data. It can be whether 'linear' or 'spline'.
        duration (int): If preprocess is True, the final length of the sequence after preprocessing has been applied.
        
    Returns:
        tuple: A tuple containing two list - `FHRbase` and `baseline_t`.
            - FHRbase: the baseline for each of the points in the sequence computed by the chosen algorithm.
            - baseline_t: the averaged baseline of the FHR signal each t minutes.
            
    Raises:
        AssertionError: If the input sequence is not a list or np.ndarray.
        AssertionError: If mode is not one of the supported baseline algorithms.
        AssertionError: If `epoch` is not positive (greater than 0).
        AssertionError: If `t` is not positive (greater than 0) and an integer divisor of the whole sequence.
        AssertionError: If `freq` is not positive (greater than 0).
        AssertionError: If `preprocess` is not a boolean variable.
        AssertionError: If `inter` is not `linear` or `spline`.
        AssertionError: If `duration` is not an integer.
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert mode == 'sisporto' or mode == 'cazares' or mode == 'mantel' or mode == 'lu', f"The algorithm {mode} is not supported."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    r = len(sequence) % (((60 * freq * t)))
    assert t > 0 and r == 0, f"The time of analysis {t} must be positive and an integer divisor of the whole sequence."
    assert freq > 0, f"The frequency {freq} of the signal must be positive (greater than 0)."
    assert isinstance(preprocess, bool), f"Object {preprocess} must be a boolean variable."
    assert inter == 'linear' or inter == 'spline', "Only linear and spline interpolation are supported."
    assert isinstance(duration, int), f"Object {duration} must be an integer."
    
    if preprocess != False:
        sequence = fhr_preprocess(sequence, inter='linear', freq=4, duration=120)
    # Compute the baseline for t he treated signal for a window of 10 minutes
    # taking into account the previous and the next epoch
    if mode == 'sisporto':
        assert epoch == 3.75, "Epochs are composed of 3.75s in SisPorto's algorithm"
        sequence = epoch_calc(sequence, freq=freq, epoch=epoch)
        sequence = moving_average(sequence)
        baseline_t = sisporto_tmin(sequence, epoch, t)

    elif mode == 'cazares':
        assert epoch == 3.75, "Epochs are composed of 3.75s in Cazares' algorithm"
        sequence = epoch_calc(sequence, freq=freq, epoch=epoch)
        sequence = moving_average(sequence)
        baseline_t = cazares_tmin(sequence, epoch, t)

    elif mode == 'mantel':
        assert epoch == 2.5, "Epochs are composed of 10 points in Mantel's approach"
        sequence = epoch_calc([round(60000./x) for x in sequence], epoch=2.5, freq=4) # Heart Beat Interval
        sequence = moving_average(sequence)
        baseline_t = mantel_tmin(sequence, epoch, t)
        
    elif mode == 'lu':
        assert epoch == 1, "Epochs are composed of 4 points in Lu's approach"
        sequence = epoch_calc(sequence, epoch=1, freq=4)
        sequence = moving_average(sequence)
        baseline_t = np.array(lu_tmin(sequence, epoch=epoch, t=t))
        baseline_t = (baseline_t * np.std(sequence)) + np.mean(sequence)
        
    FHRbase = []
    m = int(len(sequence) // (((60 * freq) // (freq*epoch)) * t))
    for i in range(m):
        FHRbase += [baseline_t[i]] * (int((60 * freq) // (freq*epoch))) * (t)       

    return FHRbase, baseline_t


# # Other important features.

# In[ ]:


def intersections(sequence, FHRbase):
    """
    Find the intersection points between the FHR sequences and the FHR baseline.
    
    This function identifies the indices at which the FHR sequences intersect
    with the FHR baseline. An intersection occurs when the FHR value in the 
    sequence crosses the corresponding value in the baseline.
    
    Args:
        sequence (list or np.ndarray): The sequence of FHR values per epoch.
        FHRbase (list or np.ndarray): The baseline of the FHR sequence.
        
    Returns:
        list: A list containing the indices of the intersection points.
        
    Raises:
        AssertionError: If the input arguments are not lists or np.ndarrays.
        
    Example:
        >>> sequence = [120, 130, 125, 140, 150]
        >>> FHRbase = [123, 130, 127, 135, 150]
        >>> intersections(sequence, FHRbase)
        [1, 4]        
    """    
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert isinstance(FHRbase, list) or isinstance(FHRbase, np.ndarray), f"Object {FHRbase} is not a list nor an array."
    
    intersection = []
    i = 0
    # Find the intersections 
    while i < len(sequence):
        if sequence[i] == FHRbase[i]:
            intersection += [i]
        elif i > 1 and i < len(sequence) and (
            (sequence[i-1] < FHRbase[i-1] and sequence[i] > FHRbase[i]) or (
            sequence[i-1] > FHRbase[i-1] and sequence[i] < FHRbase[i])):
            intersection += [i-1, i]
        i += 1
    return intersection


# In[ ]:


def decelerations(sequence, FHRbase, epoch=3.75, t=10, freq=4):
    """
    Obtain the decelerations from the FHR sequences in relation to the FHR baseline.
    
    Decelerations are defined as decreases in the FHR below the baseline, of more than
    15bpm in amplitude, and lasting more than 15 seconds. There are two types of decelerations:
        1) Normal decelerations: lasting between 15 seconds and 2 minutes.
        2) Big decelerations: lasting more than 2 minutes.
        
    This function identifies the decelerations in the FHR sequence with respect to the FHR baseline.
    It calculates the number of normal decelerations and big decelerations ocurring in each t-minute window.
    It also computes the total number of decelerations, the total duration of decelerations, the total duration
    of reperfustion time, and the total area covered by the decelerations.
    
    Args:
        sequence (list or np.ndarray): The sequence of FHR values per epoch.
        FHRbase (list or np.ndarray): The baseline value of the sequence per epoch.
        epoch (float): The duration in seconds of a given epoch. Default is 3.75 seconds.
        t (int): The time in minutes for each feature analysis window. Default is 10 minutes.
        freq (int): The frequency of the original non-preprocessed signal in Hz. Default is 4Hz.
                
    Returns:
        dict: A dictionary containing the following entries:
            - 'decelerations': The number of normal decelerations each t minutes.
            - 'big_decelerations': The number of big decelerations each t minutes.
            - 'total_decelerations': The total number of decelerations.
            - 'location': A list containing a 40 in the positions where decelerations are taking place.
            - 'decel_info': A list containing a 40 in the positions where normal decelerations are taking place and 
                            a 45 where big decelerations are taking place.
            - 'reperfusion_time': The total duration (minutes) during which the fetus mantained a baseline state without any deceleration.
            - 'deceleration_time': The total duration(minutes) of the period during which the fetus displayed decelerations.
            - 'deceleration_area': The total area (minutes*bpm) covered by all the decelerations. 
                                   Each area was calculated after being approximated by a triangle.
            - 'deceleration_area_t': The total area (minutes*bpm) covered by the decelerations each t minutes.
            - 'reperfusion_time_t': The reperfusion time (minutes) each t minutes.
            
    Raises:
        AssertionError: If the input arguments do not meet the specified conditions.
    """
    
    assert isinstance(sequence, np.ndarray) or isinstance(sequence, list), f"Object {sequence} is not a list nor an array."
    assert isinstance(FHRbase, np.ndarray) or isinstance(FHRbase, list), f"Object {FHRbase} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert freq > 0, f"The frequency of the original signal must be positive (greater than 0)."
    
    sequence = np.array(sequence)
    FHRbase = np.array(FHRbase)
    min_ep = int((60 * freq) // (freq * epoch))
    r = len(sequence) % (t * min_ep)
    assert t > 0 and r == 0, f"The time of analysis {t} must be positive and an integer divisor of the whole sequence."
    
    # Define the variables-
    location = np.array([-10] * len(sequence))
    decel_info = np.array([-10] * len(sequence))
    decel = []
    big_decel = []
    dec_area = 0
    dec_time = 0
    reperfusion_time = 0
    min_position_loc = []
    dec_area_t = []
    reperfusion_time_t = []
    
    # The first step is to find the intersections between the sequence
    # and the baseline of the signal. 
    intersection = intersections(sequence, FHRbase)
    intersection = [0] + intersection + [len(sequence)-1]
    
    # Now we start with the deceleration counting.
    i = 1
    period = 0
    while i < len(intersection):
        x3 = intersection[i-1]
        x4 = intersection[i]
        interval = [sequence[m] for m in np.arange(x3, x4+1)]
        min_position = interval.index(min(interval)) + x3
        duree = (x4 - x3) * epoch
        min_position_loc.append(min_position)
        
        if (FHRbase[min_position] - sequence[min_position] >= 15):
            if duree >= 15 and duree < 120:
                location[x3:x4+1] = 40
                decel_info[x3:x4+1] = 40

            elif duree >= 120:
                location[x3:x4+1] = 40
                decel_info[x3:x4+1] = 45
            
            decel += [min_position]
            dec_area += (duree * (FHRbase[min_position] - sequence[min_position])) / 2
            dec_time += duree
            
        else:
            reperfusion_time += duree
          
        # Keep the values each t min in another separate vector.
        
        if x4 >= period * t * min_ep:
                if period == 0:
                    dec_area_t.append(dec_area)
                    reperfusion_time_t.append(reperfusion_time)
                else:
                    dec_area_t.append((dec_area - sum(dec_area_t)) / 60)
                    reperfusion_time_t.append((reperfusion_time - sum(reperfusion_time_t)) / 60)
                    
                period += 1
                    
        if i == len(intersection) - 1 and len(dec_area_t) < 12:
            dec_area_t.append((dec_area - sum(dec_area_t)) / 60)          
       
        if i == len(intersection) - 1 and len(reperfusion_time_t) < 12:
            reperfusion_time_t.append((reperfusion_time - sum(reperfusion_time_t)) / 60)
            
        i += 1 
        
    # Once deceleration peaks are found, we distribute them in the windows.
    windows = int(len(sequence) // (min_ep * t))
    dec_normal = [0] * windows
    dec_long = [0] * windows
    for x in decel:
        m = int(x // (min_ep * t))
        if decel_info[x] == 40:
            dec_normal[m] += 1
        elif decel_info[x] == 45:
            dec_long[m] += 1
            
    # Deceleration Report.
    #print('##################### DECELERATION REPORT #####################')
    #print(f'Decelerations per analysis window ({t}-min): {dec_normal}')
    #print(f'Big decelerations per analysis window ({t}-min): {dec_long}')
    #print(f'Total number of decelerations during 2h: {sum(dec_normal) + sum(dec_long)}')
    #print(f'Total reperfusion time (in minutes): {reperfusion_time / 60:0.2f} min')
    #print(f'Total deceleration time (in minutes): {dec_time / 60:0.2f} min')
    #print(f'Total deceleration area (min*bpm): {dec_area / 60:0.2f} min*bpm')
    
    
    
    return {'decelerations': dec_normal,
            'big_decelerations': dec_long,
            'total_decelerations': sum(dec_normal) + sum(dec_long),
           'location': location,
           'decel_info': decel_info,
            'reperfusion_time': reperfusion_time / 60,
            'deceleration_time': dec_time / 60,
           'deceleration_area': dec_area / 60,
           'deceleration_area_t': dec_area_t,
           'reperfusion_time_t': reperfusion_time_t}


# In[ ]:


def accelerations(sequence, FHRbase, location, epoch=3.75, t=10, freq=4):
    """
    Obtain the accelerations from the FHR sequences in relation to the FHR baseline.
    
    Accelerations are defined as increases in the FHR above the baseline, of more than
    15bpm in amplitude, and lasting more than 15 seconds. There are two type of accelerations:
        1) Normal accelerations: lasting between 15 seconds and 2 minutes.
        2) Big accelerations: lasting more than 2 minutes.
        
    This function identifies the accelerations in the FHR sequence with respect to the FHR baseline.
    It calculates the number of normal accelerations and big accelerations occurring in each t-minute window.
    It also computes the total number of accelerations.
    
    Args:
        sequence (list or np.ndarray): The sequence of FHR values per epoch.
        FHRbase (list or np.ndarray): The baseline value of the sequence per epoch.
        location (list or np.ndarray): A list containing information about where the decelerations are
                                       found (all those positions with value 40).
        epoch (float): The duration in seconds of a given epoch. Default is 3.75 seconds.
        t (int): The time in minutes in which the feature analysis will be done. Default is 10 minutes.
        freq (int): The frequency of the original non-preprocessed signal in Hz. Default is 4Hz.
        
    Returns:
        dict: A dictionary containing the following entries:
            - 'accelerations': The number of accelerations each t minutes.
            - 'big_accelerations': The number of big accelerations each t minutes.
            - 'total_accelerations': The total number of accelerations, both normal and big.
            - 'location': A list containing a 192 in the positions where accelerations are
                          happening, and a 40 in the positions where decelerations are.
            - 'acel_info': A list containing a 190 in the index where normal accelerations 
                           are; and a 194, where big accelerations are. 
                           
    Raises:
        AssertionError: If the input argument do not meet the specified conditions.              
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert isinstance(FHRbase, list) or isinstance(FHRbase, np.ndarray), f"Object {FHRbase} is not a list nor an array."
    assert isinstance(location, list) or isinstance(location, np.ndarray), f"Object {location} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert freq > 0, f"The frequency of the initial signal must be positive (greater than 0)."
    min_ep = int((60 * freq) // (freq * epoch))
    r = len(sequence) % (t * min_ep)
    assert t > 0 and r == 0, f"The time of analysis {t} must be positive and an integer divisor of the whole sequence."
    #######################################################################################################################
    ac = []
    acel_info = np.array([-10] * len(sequence))
    # The first step is to find the intersections between the sequence
    # and the baseline of the signal. 
    intersection = intersections(sequence, FHRbase)
    intersection = [0] + intersection + [len(sequence)-1]
    
    # Now we start with the acceleration counting.
    i = 1
    while i < len(intersection):
        x3 = intersection[i-1]
        x4 = intersection[i]
        interval = [sequence[m] for m in np.arange(x3, x4+1)]
        max_position = interval.index(max(interval)) + x3
        duree = (x4 - x3) * epoch
        if (sequence[max_position] - FHRbase[max_position] >= 15):
            if duree >= 15 and duree < 120: #and ((x3 - 8) not in end_decel) :
                ac.append(max_position)
                location[x3:x4+1] = 192
                acel_info[x3:x4+1] = 190
            elif duree >= 120: #and ((x3 - 8) not in end_decel):
                ac.append(max_position)
                location[x3:x4+1] = 192
                acel_info[x3:x4+1] = 194
        i += 1
    
    ###########################################################################
    # We convert the image to prepare it for the analysis each 10 minutes.
    windows = int(len(sequence) // (min_ep * t))
    accelerations = [0] * windows
    big_accelerations = [0] * windows
    for x in ac:
        m = int(x // (min_ep * t))
        if acel_info[x] == 190:
            accelerations[m] += 1
        elif acel_info[x] == 194:
            big_accelerations[m] += 1
            
    # Acceleration Report.
    #print('##################### ACCELERATION REPORT #####################')
    #print(f'Accelerations per analysis window ({t}-min): {accelerations}')
    #print(f'Big accelerations per analysis window ({t}-min): {big_accelerations}')
    #print(f'Total number of accelerations during 2h: {sum(accelerations) + sum(big_accelerations)}')
    
    return {'accelerations': accelerations,
            'big_accelerations': big_accelerations,
            'total_accelerations': sum(accelerations) + sum(big_accelerations),
           'location': location,
           'acel_info': acel_info}


# In[ ]:


def short_term(sequence, location, epoch=3.75, t=10, freq=4):    
    """
    Calculate the short-term variability of the FHR signal averaged over each t-minute window.
    
    Short-term variability (STV) is calculated for each minute by averaging the absolute difference in the FHR of
    consecutive epochs. Minutes that contain less than 50% valid epochs or are part of a deceleration are excluded.

    Args:
        sequence (list or np.ndarray): The mean value of the FHR signal per epoch.
        location (list or np.ndarray): A list containing information about when the decelerations are found.
                                       If location[i] == 40, it indicates a deceleration in the epoch i.
        epoch (float): The duration in seconds of a given epoch. Default is 3.75 seconds.
        t (int): The analysis time (in minutes). Default is 10 minutes.
        freq (int): The frequency of the non-preprocessed signal in Hz. Default is 4Hz.

    Returns:
        list: The short-term variability averaged each t minutes.
        
    Raises:
        AssertionError: If the input arguments do not meet the specified conditions.
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {FHRbase} is not a list nor an array."
    assert isinstance(location, list) or isinstance(location, np.ndarray), f"Object {location} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert freq > 0, f"The frequency of the initial signal must be positive (greater than 0)."
    min_ep = int((60 * freq) // (freq * epoch))
    r = len(sequence) % (t * min_ep)
    assert t > 0 and r == 0, f"The time of analysis {t} must be positive and an integer divisor of the whole sequence."
    ########################################################################################################################
    
    STVmin = []
    m = 0
    while m < len(sequence) - 1:
        i = 0
        Te = 0
        n = 1
        while n < min_ep and Te < 9000:
            
            # We take into account whether the points come from a deceleration or not
            # in a given epoch.
            # If they come from a deceleration, we set Te=9999 and exit this minute
            # immediately.
            if ((location[m + n] == 40 or location[m + n -1] == 40)):
                Te = 9999
            elif sequence[m + n]!=0 and sequence[m + n - 1]!= 0:
                Te += np.abs((60000/sequence[m + n]) - (60000/sequence[m + n - 1]))
                i += 1
            n += 1
            
        if i >= 8 and Te > 0 and Te < 9000:            
            STVmin.append(Te / i)
        elif Te == 9999:
            STVmin.append(-1)
        else:
            STVmin.append(-1)

        m += min_ep
  
    # Having computed the short-term variability for each minute, we take the 
    # value that interests us, which is the mean value in the t-minute window.
    m = 0
    STV_tmin = []
    windows = len(sequence) / (min_ep * t)
    while m < windows:
        
        # We want to take into account minutes where at least >50% of the epochs
        # were not in a deceleration.
        values = [num for num in STVmin[t*m:t*(1+m)] if num >= 0]
        if len(values) > 0:
            STV_tmin_ = np.mean(values)
        else:
            STV_tmin_ = 0
        STV_tmin.append(round(STV_tmin_, 2))
        m += 1
        
    # STV Report.
    #print('##################### STV #####################')
    #print(f'Short-Time Variability per analysis window ({t}-min): {STV_tmin}')
    #print(f'Total Short-Time Variability during 2h: {np.mean([num for num in STVmin if num >= 0]):0.2f}')
    
    return STV_tmin


# In[ ]:


def long_term(sequence, epoch=3.75, t=10, freq=4):
    """
    Calculate the long-term variability (LTV) of the FHR signal averaged over each t-minute window.
    
    LTV is computed for each t-minute window by obtaining the absolute difference between the
    maximum and minimum FHR values for each minute. The LTV is then averaged for each t-minute
    window. Minutes that contain less than 50% valid epochs are excluded from the calculation.
    
    Args:
        sequence (list or np.ndarray): The FHR signal computed per epoch.
        epoch (float): The duration in seconds of a given epoch. Default is 3.75 seconds.
        t (int): The analysis time (in minutes). Default is 10 minutes.
        freq (int): The frequency of the non-preprocessed signal in Hz. Default is 4Hz.
        
    Returns: 
        list: The averaged long-term variability each t minutes.
        
    Raises:
        AssertionError: If the input arguments do not meet the specified conditions.
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert freq > 0, f"The frequency of the initial signal must be positive (greater than 0)."
    min_ep = int((60*freq) // (freq * epoch))
    r = len(sequence) % (t * min_ep)
    assert t > 0 and r == 0, f"The time of analysis {t} must be positive and an integer divisor of the whole sequence."
    ########################################################################################################################
    
    LTV = []
    m = 0
    Te = 0
    i = 0
    while m < len(sequence) - 1:
        # A minute is composed of 16 epochs. We compute the maximum 
        # and the minimum values of the analyzed minute.
        ma = max(sequence[m : m + min_ep])
        mi = min(sequence[m : m + min_ep])
        if ma != 0 and mi != 0:
            Te += abs((60000 / mi) - (60000 / ma))
            i += 1
        # We go for the next minute.
        m += min_ep
        if i > 0:
            LTV.append(Te / i)
            Te = 0
            i = 0
        else:
            LTV.append(0)
            Te = 0
    
    m = 0
    LTV_tmin = []
    windows = len(sequence) // (min_ep * t)
    while m < windows:
        
        # We want to take into account minutes where at least >50% of the epochs
        # were not in a deceleration.
        values = [num for num in LTV[t*m:t*(1+m)] if num >= 0]
        if len(values) > 0:
            LTV_tmin_ = np.mean(values)
        else:
            LTV_tmin_ = 0
        LTV_tmin.append(round(LTV_tmin_,2))
        m += 1
    
    # LTV Report.
    #print('##################### LTV #####################')
    #print(f'Long-Time Variability per analysis window ({t}-min): {LTV_tmin}')
    #print(f'Total short-time variability during 2h: {np.mean([num for num in LTV if num >= 0]):0.2f}')
    return LTV_tmin


# In[ ]:


def peaks_toco(toco, epoch=3.75, t=10, freq=4):
    """
    Locate the peaks of the tocometry computed per epochs.
    
    The function uses the find_peaks function from the scipy.signal module to identify the peaks
    of the tocometry signal computed per epochs. The peaks are coded as one-hot vector where
    a '1' indicates the position of a peak in the tocometry signal.
    
    Args:
        toco (list or np.ndarray): The sequence of values from the tocometry per epoch.
        epoch (float): The duration in seconds of a given epoch. Default is 3.75 seconds.
        t (int): The analysis time (in minutes). Default is 10 minutes.
        freq (int): The frequency of the initial non-preprocessed signal in Hz. Default is 4Hz.
        
    Returns:
        tuple: A tuple containing the following elements:
            loc (np.ndarray): The location of the tocometry peaks.
            count (list): The count vector of toco peaks each t minutes.
    
    Raises:
        AssertionError: If the input arguments do not meet the specified conditions.
    """
    assert isinstance(toco, list) or isinstance(toco, np.ndarray), f"Object {toco} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert freq > 0, f"The frequency of the initial signal must be positive (greater than 0)."
    min_ep = (60 * freq) // (freq * epoch)
    r = len(toco) % (t * min_ep)
    assert t > 0 and r == 0, f"The time of analysis {t} must be positive and an integer divisor of the whole sequence."
    ###################################################################################################################
    
    toco = np.array(toco)
    loc, _ = signal.find_peaks(toco, width=6, height=10)
    count = []
    c = 0
    m = 0
    while m < len(toco) / (min_ep * t):
        start = m * min_ep * t
        end = (m + 1) * min_ep * t
        for x in loc:
            if x >= start and x < end:
                c += 1
        count += [c]
        c = 0
        m += 1
        
    return loc, count


# # Early, late and variable decelerations.

# In[ ]:


def find_decel_peaks(sequence, location):
    """
    Find the deceleration peaks of the FHR signal.
    
    The function uses the find_peaks function from the scipy.signal module to locate the peaks
    of the negative of the FHR signal after applying the moving average. It then checks whether
    the identified peaks correspond to decelerations by analyzing the corresponding 'location'
    information, which is coded with a value of 40 for decelerations.
    
    Args:
        sequence (list or np.ndarray): The sequence of FHR values per epoch and after the moving average.
        location (list or np.ndarray): The coded information of the sequence, where '40' indicates decelerations.

    Returns:
        list: A binary vector where '1' indicates the location of the deceleration peaks.
        
    Raises: 
        AssertionError: If the input arguments do not meet the specified conditions.
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert isinstance(location, list) or isinstance(location, np.ndarray), f"Object {location} is not a list nor an array."
    #######################################################################################################################
    
    decel_peak_loc = [0] * len(sequence)
    seq_neg = [-x for x in sequence]
    peaks, _ = signal.find_peaks(seq_neg, width=4, prominence=3)
    
    # We check whether there is a deceleration going on in that peak.  We will 
    # only consider the normal deceleration peak. 
    valid_peaks = [location[x] == 40 for x in peaks]
    decel_peaks = [x for i, x in enumerate(peaks) if valid_peaks[i]]
    
    for x in decel_peaks:
        decel_peak_loc[x] = 1
        
    return decel_peak_loc


# In[ ]:


def classify_decelerations(sequence, toco, location, epoch=3.75, duration=120, t=10, freq=4):
    """
    Find and classsify different types of decelerations in the FHR signal in relation to the peaks of tocometry.
    
    The function locates the nadir of each deceerations and determines whether it corresponds to an early,
    late, or variable deceleration based on the time between the beginning of the deceleration and the nadir,
    as well as the position of the peaks of the tocometry with respecto to the nadir. The criteria is the following:
        1) Variable: If the time between the beginning of the deceleration and the nadir is less than 30 seconds.
        2) Late: if the tocometry peak is found in the 15s before the nadir 
          (> or =15 sec), the deceleration will be classified as late
          deceleration.
        - of the tocometry peak is found <15 sec before the nadir, the
          deceleration will be classified as early deceleration.    
    
    Inputs:
        - sequence: the sequence of FHR values per epoch.
        - toco: the sequence of tocometry values per epoch.
        - location: list with a 40 in the positions where normal decelerations
                    are found.
        - epoch: the duration in seconds of a given epoch, 3.75s by default.
        - duration: total temporal duration in minutes of the sequence, 120min by default.
        - t: the temporal analysis window duration in minutes, 10min by default.
        - freq: the frequenct of the initial non-preprocessed signal in Hz,
                4Hz by default.
    Outputs:
        - early: the number of early decelerations each t minutes.
        - late: the number of late decelerations each t minutes.
        - variable: the number of variable decelerations each t minutes.
        - category: a number-of-windows size list where the number in each position
                    represents the type of decelerations that are going on in that
                    specific period. 
        - early_loc: the indices where early decelerations are detected.
        - late_loc: the indices where late decelerations are detected.
        - variable_loc: the indices where variable decelerations are detected.
        - dic: a dictionary whose keys are the positions of the different decelerations
               and whose entries are the "type of deceleration", "slope" (pente) and 
               "distance between the tocometry peak and the deceleration peak" (latence).
        
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert isinstance(toco, list) or isinstance(toco, np.ndarray), f"Object {toco} is not a list nor an array."
    assert isinstance(location, list) or isinstance(location, np.ndarray), f"Object {location} is not a list nor an array."
    assert len(sequence) == len(toco), f"Lengths from {seq} and {toco} must be equal."
    assert epoch > 0, f"The epoch duration must be positive (greater than 0)."
    assert duration > 0 and isinstance(duration,int), f"Object {duration} must be an integer greater than 0."
    assert t > 0 and isinstance(duration,int), f"Object {t} must be an integer greater than 0."
    assert freq > 0, f"The frequency of the initial signal must be positive greater than 0."
    min_ep = (60 * freq) // (freq * epoch)
    r = duration % t
    assert r == 0, f"The time {t} must be a divisor of the duration {duration}."
    ########################################################################################################################
    # Find the deceleration and tocometry peaks. 
    decel_peak_loc = find_decel_peaks(sequence, location)
    loc, count = peaks_toco(toco)
    toco_peak_loc = np.array([0] * len(sequence))
    for x in loc:
        toco_peak_loc[x] = 1
    
    # Initialize the variables.
    early_loc = []
    late_loc = []
    variable_loc = []
    distance = []
    dic = {}
    
    # Algorithm.
    i = 0
    p = 0
    while i < len(sequence):
        if (40 in location[i:]) and (1 in decel_peak_loc[i:]):
            inicio_dec = location[i:].tolist().index(40)
            final_dec = decel_peak_loc[i:].index(1)
            pente = (final_dec - inicio_dec) * epoch
            if pente < 30:
                variable_loc += [i + final_dec]
                dic[i + final_dec] = {
                            'type': 'variable',
                            'pente': pente
                        }
            else:
                if 1 in toco_peak_loc[i + final_dec - 32 : i + final_dec + 1]:
                    arr = toco_peak_loc[i + final_dec - 32 : i + final_dec + 1]
                    reversed_toco = np.flip(arr)
                    index = len(arr) - 1 - np.where(reversed_toco == 1)[0][0]
                    latence = (32 - index) * epoch
                    if latence < 15:
                        early_loc += [i + final_dec]
                        dic[i + final_dec] = {
                            'type': 'early',
                            'pente': pente,
                            'latence': latence
                        }
                    else:
                        late_loc += [i + final_dec]
                        dic[i + final_dec] = {
                            'type': 'late',
                            'pente': pente,
                            'latence': latence
                        }
            
            if -10 in location[i + final_dec:]:
                i += final_dec + location[i + final_dec:].tolist().index(-10)
            else:
                i = len(sequence)
                
        else:
            i = len(sequence)
      
    ########################################################################################################
    # Having located the index of each type of deceleration, we now count them
    # dividing the count for each t minutes and we also create the variable
    # category.
    early = [0] * (duration // t)
    late = [0] * (duration // t)
    variable = [0] * (duration // t)
    m = 0
    category = []
    while m < duration // t:
        start = m * min_ep * t 
        end = (m + 1) * min_ep * t
        for x in early_loc:
            if x >= start and x < end:
                early[m] += 1
        for y in late_loc:
            if y >= start and y < end:
                late[m] += 1
        for z in variable_loc:
            if z >= start and z < end:
                variable[m] += 1
        suma = early[m] + late[m] + variable[m]
        if suma > 0:
            l = late[m] / suma
            e = early[m] / suma
            v = variable[m] / suma
            decel = [e, v, l]
            cat = decel.index(max(decel))
            if cat == 0:
                category += [cat]
            elif cat == 1:
                category += [cat]
            elif cat == 2:
                category += [cat]
        else:
            category += [-1]
        m += 1
    ########################################################################################################
    
    # Deceleration Classification. 
    #print('##################### DECELERATION CLASSIFICATION #####################')
    #print(dic)
    
    return early, late, variable, category, early_loc, late_loc, variable_loc, dic 


# # Last Deceleration

# In[ ]:


def last_deceleration(sequence, FHRbase, location):
    """
    Compute descriptive characteristics of the last deceleration in the analyzed sequence.
    
    The function find the beginning and end indices of the last deceleration in the sequence.
    It then computes various characteristics of the deceleration, such as amplitude, duration,
    drop duration, slope, area covered by the deceleration, and baseline FHR during the last deceleration.
    
    Args:
        sequence (list or np.ndarray): The FHR values in bpm.
        FHRbase (list or np.ndarray): The baseline FHR values in bpm.
        location (list or np.ndarray): A list with value 40 at the indices of decelerations.

    Returns:
        dict: A dictionary with the following entries:
            - 'begin': The index where last deceleration begins.
            - 'end': The index where last deceleration ends.
            - 'amplitude': The amplitude of the deceleration in bpm.
            - 'duration': The duration of the deceleration in seconds.
            - 'drop': Duration until reaching the deceleration peak in seconds.
            - 'slope': Amplitude / drop.
            - 'area': The area covered by deceleration (approximated by a triangle).
            - 'FHR': The baseline during last deceleration in bpm.
    
    Raises:
        AssertionError: If the input arguments do not meet the specified conditions.
    """
    assert isinstance(sequence, list) or isinstance(sequence, np.ndarray), f"Object {sequence} is not a list nor an array."
    assert isinstance(FHRbase, list) or isinstance(FHRbase, np.ndarray), f"Object {FHRbase} is not a list nor an array."
    assert isinstance(location, list) or isinstance(location, np.ndarray), f"Object {location} is nit a list nor an array."
    
    # Find the end and the début of the last deceleration.
    location = location.tolist()
    if 40 in location[:-481:-1]:
        end = location[:-481:-1].index(40)
        begin = location[-end-1::-1].index(-10)    
        begin = len(sequence) - begin - end
        assert location[begin] == 40
        end = len(sequence) - end - 1
        assert location[end] == 40
    
        # Find the minimum of the deceleration and its position.
        minimum = min(sequence[begin:end+1])
        minimum_index = sequence[begin:end+1].index(minimum)
    
        # Compute the different characteristics of the deceleration.
        amplitude = FHRbase[begin+minimum_index] - sequence[begin+minimum_index]
        duration = (end - begin) * 3.75
        drop = minimum_index * 3.75
        slope = amplitude / drop
        area = (duration * amplitude) / (2)
        FHRbase = np.mean(FHRbase[begin:end+1])
    else:
        begin = 0
        end = 0
        amplitude = 0
        duration = 0
        drop = 0
        slope = 0
        area = 0
        FHRbase = 0
    
    return {'begin': begin,
           'end': end,
           'amplitude': round(amplitude, 2),
           'duration': round(duration, 2),
           'drop': round(drop,2),
           'slope': round(slope, 2),
            'area': round(area, 2),
           'FHR': round(FHRbase, 2)}


# # Feature Extraction

# In[1]:


def features_extraction_dic(seq, toco, epoch=3.75, duration=120, time=10, freq=4):
    """
    Extract various features from the CTG (Cardiotocography) signal.
    
    The function computes the baseline, the number of decelerations, and accelerations
    (both normal and long), the short-term variability, the long-term variability, and
    the number of tocometry peaks each t minutes. It also determines the early, late,
    and variable decelerations according to specific definitions.
    
    Args:
        seq (list or np.ndarray): The sequence of FHR values without preprocessing.
        toco (list or np.ndarray): The sequence of tocometry values without preprocessing.
        epoch (float): The time duration in seconds of a given epoch. Default is 3.75 seconds.
        duration (int): The duration in minutes of the analyzed signals. Default is 120 minutes.
        time (int): The analysis time in minutes when doing feature extraction. Default is 10 minutes.
        freq (int): The frequency of the initial non-preprocessed signal in Hz. Default is 4Hz.
        
    Returns:
        dict: A dictionary with various entries containing the extracted features:
            - 'baseline': The baseline FHR values in bpm.
            - 'normal_dec': The number of normal decelerations each t minutes.
            - 'long_dec': The number of long decelerations each t minutes.
            - 'normal_ac': The number of normal accelerations each t minutes.
            - 'long_ac': The number of long accelerations each t minutes.
            - 'stv': The short-term variability each t minutes.
            - 'ltv': The long-term variability each t minutes.
            - 'peaks': The number of tocometry peaks each t minutes.
            - 'early_dec': The number of early decelerations each t minutes.
            - 'late_dec': The number of late decelerations each t minutes.
            - 'variable_dec': The number of variable decelerations each t minutes.
            - 'category': A list where the number in each positions represents the type
                          of decelerations that are going on in that specific period.
            - 'deceleration_area': The area covered by decelerations (approximated by a triangle).
            - 'reperfusion_time': The duration in minutes of the non-deceleration periods.
            - 'signal_loss': The percentage of signal loss due to preprocessing.
    
    Raises:
        AssertionError: If the input arguments do not meet the specified conditions.
    """
    assert isinstance(seq, list) or isinstance(seq, np.ndarray), f"Object {seq} is not a list nor an array."
    assert isinstance(toco, list) or isinstance(toco, np.ndarray), f"Object {toco} is not a list nor an array."
    assert epoch > 0, f"The epoch duration must be positive, greater than 0."
    assert duration > 0, "The duration of the signals must be positive."
    assert time > 0, "The analysis time must be positive."
    assert freq > 0, f"The frequency of the initial signal must be positive greater than 0."
    ############################################################################################################3
    
    # Number of windows (packs of features) we will compute. 
    windows = int(duration / time) 
    # Extraction of the FHR and tocometry sequences.
    #seq = signal['seq'][number]
    #toco = signal['toco'][number]
    loss = signal_loss(seq)
    # Preprocessing for the FHR sequences (28800-point signal). 
    seq = fhr_preprocess(seq, freq=freq, inter='linear', t=duration)
    toco = toco_preprocess(toco, freq=freq, t=duration)    
    # Compute the signals per epoch and apply the moving average window.
    seq_ep = epoch_calc(seq, freq=freq, epoch=epoch)
    toco_ep = epoch_calc(toco, freq=freq, epoch=epoch)
    seq_ep_av = moving_average(seq_ep)
    toco_ep_av = moving_average(toco_ep)
    
    # Decelerations, Accelerations, STV, LTV, UC. For the baseline, decelerations and 
    # acelerations we will use the averaged sequence per epochs.
    FHRbase, base = baseline(seq, mode='sisporto', epoch=epoch, t=time, freq=freq)
    dec = decelerations(seq_ep_av, FHRbase, epoch=epoch, t=time, freq=freq)
    loc1 = dec['location']
    loc2 = dec['decel_info']
    ac = accelerations(seq_ep_av, FHRbase, loc1, epoch=epoch, t=time, freq=freq)
    dec_normal, dec_long = dec['decelerations'], dec['big_decelerations']
    ac_normal = ac['accelerations']
    ac_long = ac['big_accelerations']
    # Once we have defined the decelerations with the previous sequence, we will compute
    # the STV and LTV with the seq_stv_ltv sequence. 
    stv = short_term(seq_ep, loc1, epoch=epoch, t=time, freq=freq)
    ltv = long_term(seq_ep, epoch=epoch, t=time, freq=freq)
    # Tocometry peaks and early/late decelerations.
    loc, peak = peaks_toco(toco_ep_av, epoch=epoch, t=time, freq=freq)
    early, late, variable, category, early_loc, late_loc, variable_loc, dic = classify_decelerations(seq_ep_av, toco_ep_av, loc2, epoch=epoch, duration=duration, t=time, freq=freq)
    
    # We create the new feature dictionary.
    return {'baseline': base,
           'normal_dec': dec_normal,
           'long_dec': dec_long,
           'normal_ac': ac_normal,
           'long_ac': ac_long,
           'stv': stv,
           'ltv': ltv,
           'peaks': peak,
           'early_dec': early,
           'late_dec': late,
           'variable_dec': variable,
           'category': category,
            'deceleration_area': dec['deceleration_area'],
            'reperfusion_time': dec['reperfusion_time'] ,
           'signal_loss': round(loss,2)
           }


# In[ ]:


def ctg_analysis(seq, toco, epoch=3.75, t=10, mode='sisporto', inter='linear', duration=120, freq=4):
    """
    Graphic analysis of the CTG (cardiotocography) signal and feature extraction.
    
    The function analyzes the CTG signal provided by 'seq' and 'toco' sequences and computes various
    features, including the baseline, the number of decelerations, and accelerations (both normal
    and long), short-term variability (STV), long-term variability (LTV), and the number of tocometry
    peaks each t minutes. It also classifies the decelerations into early, late and variable types 
    based on the specified criteria. The analysis results are displayed in a graphical form for easy 
    visualization.
    
    Args:
        seq (list or np.ndarray): The fetal heart rate sequence to be analyzed.
        toco (list or np.ndarray): The tocometry sequence to be analyzed.
        epoch (float): The time duration of the epochs in seconds. Default is 3.75 seconds. 
        t (int): The duration of the temporal windows of analysis in minutes. Default is 10 minutes.
        mode (str): The chosen algorithm to compute the baseline from the signal. Default is 'sisporto'.
        inter (str): The type of interpolation when removing the signal outliers. Default is 'linear'.
        duration (int): The total temporal duration of the analyzed signals in minutes. Default is 120 minutes.
        freq (int): The frequency of the signal in Hz. Default is 4Hz.
        
    Returns:
        None: This function displays a graphic with all the CTG's feature analysis.
        
    Raises:
        AssertionError: If the input arguments do not meet the specified conditions.
    """
    assert isinstance(seq, list) or isinstance(seq, np.ndarray), f"Object {seq} is not a list nor an array."
    assert isinstance(toco, list) or isinstance(toco, np.ndarray), f"Object {toco} is not a list nor an array."
    assert epoch >= 0, "The number of the row must be a positive integer."
    assert isinstance(t, int) and t > 0, "The temporal duration of the analysis window must be a positive integer."
    assert mode == 'sisporto' or mode == 'cazares' or mode == 'mantel' or mode == 'lu', "Only sisporto, cazares, mantel and lu algorithms are supported."
    assert inter == 'linear' or inter == 'spline', "Only linear and spline interpolation are supported."
    
    print('##################### ANALYSIS CHARACTERISTICS #####################')
    print(f'Frequency of the signal: {freq}Hz')
    print(f'Epoch temporal duration: {epoch}s')
    print(f'Analysis temporal windows: {t}s')
    print(f'Baseline Algorithm: {mode.upper()}')   
    
    
    # We first get the direct data from the arguments.
    windows = int(120 // t)
    min_ep = int(240 // (freq * epoch))
    # Check that signal loss is less than 30%.
    assert signal_loss(seq) <= 0.3, "The signal loss is higher than 30%."
    
    # Preprocessing for the FHR signal.
    seq = fhr_preprocess(seq, freq=freq, inter=inter, t=duration)
    # Preprocessing for the toco signal.
    toco = toco_preprocess(toco, freq=freq, t=duration)
    assert len(seq) == duration * 60 * freq, "The FHR is not 28800-point long."
    assert len(toco) == duration * 60 * freq, "The toco is not 28800-point long."
            
    # Computation of the signal per epochs.
    seq_ep = epoch_calc(seq, freq=freq, epoch=epoch)
    toco_ep = epoch_calc(toco, freq=freq, epoch=epoch)
    assert len(seq_ep) == int(len(seq) / (freq*epoch)), "The FHRep is not 1920-point long."
    assert len(toco_ep) == int(len(toco) / (freq*epoch)), "The toco_ep is not 1920-point long."
    
    # Final smoothing with an average moving window.
    seq_ep_s = moving_average(seq_ep)
    toco_ep_s = moving_average(toco_ep)
    
    # Feature extraction: baseline.
    FHRbase, base = baseline(seq, mode=mode, epoch=epoch, t=t, freq=freq)
    # Feature extraction: decelerations.
    dec = decelerations(seq_ep_s, FHRbase, epoch=epoch, t=t, freq=freq)
    loc1 = dec['location']
    loc2 = dec['decel_info']
    dec_normal, dec_long = dec['decelerations'], dec['big_decelerations']
    # Feature extraction: accelerations.
    ac = accelerations(seq_ep_s, FHRbase, loc2, epoch=epoch, t=t, freq=freq)
    ac_normal = ac['accelerations']
    ac_long = ac['big_accelerations']
    code = ac['location']
    # Feature extraction: STV.
    stv = short_term(seq_ep, loc1, epoch=epoch, t=t, freq=freq)
    ltv = long_term(seq_ep, epoch=epoch, t=t, freq=freq)
    # Compute the tocometry peaks.
    loc, count = peaks_toco(toco_ep_s, epoch=epoch, t=t, freq=freq)
    # Early and late decelerations.
    early, late, variable, category,early_loc, late_loc, variable_loc, dic = classify_decelerations(
        seq_ep_s, toco_ep_s, loc2, epoch=epoch, duration=120, t=t, freq=freq)
    ###################################################################################################
    # PLOT ############################################################################################
    fig, axes = plt.subplots(1, 1, figsize=(30,10))
    # Plot the two signals we want to analyze and compare.
    axes.plot(seq_ep_s)
    axes.plot(toco_ep_s)
    for i in range(windows):
        # The black grid to separate each window of analysis.
        axes.axvline(i * min_ep * t, color='gray', linestyle='-')
        # Plot the baseline for each period.
        base_t = int(base[i])
        axes.plot(np.arange(i * min_ep * t, (i+1) * min_ep * t), min_ep * t * [base_t], color = 'green')
        axes.plot(np.arange(i * min_ep * t, (i+1) * min_ep * t), min_ep * t * [base_t + 15], color = 'gray')
        axes.plot(np.arange(i * min_ep * t, (i+1) * min_ep * t), min_ep * t * [base_t - 15], color = 'gray')
        
        # Plot the different features from the signal.
        n_dec = dec_normal[i]
        l_dec = dec_long[i]
        n_ac = ac_normal[i]
        l_ac = ac_long[i]
        stv_n = stv[i]
        ltv_n = ltv[i]
        peaks_n = count[i]
        e = early[i]
        l = late[i]
        v = variable[i]
        c = category[i]
        axes.text(i * min_ep * t, y = -10, s=f'Base={base_t}', fontsize='large')
        axes.text(i * min_ep * t, y = -15, s=f'Normal Dec={n_dec}', fontsize='large')
        axes.text(i * min_ep * t, y = -20, s=f'Long Dec={l_dec}', fontsize='large')
        axes.text(i * min_ep * t, y = -25, s=f'Normal Ac={n_ac}', fontsize='large')
        axes.text(i * min_ep * t, y = -30, s=f'Long Ac={l_ac}', fontsize='large')
        axes.text(i * min_ep * t, y = -35, s=f'STV={stv_n:0.2f}', fontsize='large')
        axes.text(i * min_ep * t, y = -40, s=f'LTV={ltv_n:0.2f}', fontsize='large')
        axes.text(i * min_ep * t, y = -45, s=f'Peaks={peaks_n}', fontsize='large')
        axes.text(i * min_ep * t, y = -50, s=f'Early={e}', fontsize='large')
        axes.text(i * min_ep * t, y = -55, s=f'Late={l}', fontsize='large')
        axes.text(i * min_ep * t, y = -60, s=f'Variables={v}', fontsize='large')
        axes.text(i * min_ep * t, y = -65, s=f'Category={c}', fontsize='large')
        axes.set_ylim(-70)
        axes.set_xlim(0, len(seq_ep))
        
        # Plot the early and late decelerations.
        for i in early_loc:
            axes.axvline(i, ymin=0.3, ymax=0.7, color='lime')
        for i in late_loc:
            axes.axvline(i, ymin=0.3, ymax=0.7, color='brown')
        for i in variable_loc:
            axes.axvline(i, ymin=0.3, ymax=0.7, color='darkcyan')
        
        # Plot the acceleration and deceleration periods.
        for i in range(len(code)):
            if code[i] == 40 or code[i] == 45:
                axes.plot(i, FHRbase[i], '.', color='red')
            elif code[i] == 192:
                axes.plot(i, FHRbase[i], '.', color='darkgreen')
        
        # Title of the graphic.
    plt.title(f'Feature Analysis ({mode} baseline)', fontsize=18)

