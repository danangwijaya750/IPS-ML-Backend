import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import StandardScaler

# List of reference WAPs
wap_str = ""

# example
# separate each wap mac with ';'
# "90:3a:72:45:ee:a8;90:3a:72:45:ee:ac;90:3a:72:25:d9:88;90:3a:72:05:ee:dc;90:3a:72:45:ee:dc;90:3a:72:05:ee:88;d8:38:fc:3b:09:88;60:d0:2c:3b:56:ec;90:3a:72:45:ec:28;C3:52:58:A0:C9:AD;90:3a:72:05:eb:08;60:d0:2c:3b:56:e8;90:3a:72:46:03:68;60:d0:2c:7b:57:dc;90:3a:72:05:ee:ac;b0:be:76:41:c6:82;90:3a:72:45:ee:78;f0:3e:90:30:45:08;90:3a:72:06:03:68;90:3a:72:05:ec:2c;d8:38:fc:3b:14:88;90:3a:72:46:03:6c;60:d0:2c:7b:57:d8;90:3a:72:45:ed:98;90:3a:72:05:ec:28;90:3a:72:05:ee:8c;90:3a:72:05:ed:98;90:3a:72:45:ee:d8;90:3a:72:45:eb:0c;90:3a:72:05:ee:a8;90:3a:72:06:03:6c;90:3a:72:05:ee:d8;90:3a:72:05:ee:78;84:18:3a:34:01:08;90:3a:72:45:ee:88;90:3a:72:05:eb:0c;f0:3e:90:30:45:0c;D0:EB:B8:F7:B2:13;90:3a:72:45:ee:8c;60:d0:2c:7b:59:08;60:d0:2c:7b:56:ec;90:3a:72:45:eb:08;d8:38:fc:3b:14:8c;90:3a:72:45:ec:2c;90:3a:72:45:f0:58;90:3a:72:25:d9:8c;90:3a:72:05:f0:58;80:03:84:74:ed:c0;d8:38:fc:3b:0e:48;d8:38:fc:3b:09:8c;FA:9B:B2:5A:1B:C1;60:d0:2c:7b:56:e8"

def prepare_input(input_data):
    """
    Prepare input data for prediction by aligning and normalizing RSSI values.

    Args:
        input_data (str): Input RSSI data as a string in the format "mac,rssi;mac,rssi;...".

    Returns:
        pd.DataFrame: DataFrame with normalized RSSI values aligned with reference WAPs.
    """
    wap_arr = wap_str.split(";")
    input_data = input_data.split(";")
    rssis = ""
    for j in wap_arr:
        rssi = "100"
        count = 0
        for k in input_data:
            count += 1
            if k.split(",")[0] == j and count < len(wap_arr):
                rssi = k.split(",")[1]
                break
        rssis = rssis + "" + rssi + ";"
    rssi_arr = rssis.split(";")
    del rssi_arr[-1]
    normalized = normalization([rssi_arr])
    return normalized

def normalization(input_data):
    """
    Normalize the RSSI values using the `normalize_signal` function.

    Args:
        input_data (list): List of RSSI values.

    Returns:
        pd.DataFrame: DataFrame with normalized RSSI values aligned with reference WAPs.
    """
    col_names = wap_str.split(";")
    df = pd.DataFrame(input_data, columns=col_names)
    for i in df:
        df[i] = df[i].apply(normalize_signal)
    return df

def normalize_signal(num):
    """
    Normalize a signal value using a specified range.

    Args:
        num (float): Signal value to be normalized.

    Returns:
        float: Normalized signal value within a specified range.
    """
    sig_min = -105
    sig_max = 0
    tar_min = 0.25
    tar_max = 1.0
    no_sig = 100
    ans = 0
    num = float(num)
    if math.isclose(num, no_sig, rel_tol=1e-3):
        return 0
    else:
        ans = normalize(num, sig_min, sig_max, tar_min, tar_max)
        return ans

def normalize(x, xmin, xmax, a, b):
    """
    Normalize a value within a specified range.

    Args:
        x (float): Value to be normalized.
        xmin (float): Minimum value of the original range.
        xmax (float): Maximum value of the original range.
        a (float): Minimum value of the new range.
        b (float): Maximum value of the new range.

    Returns:
        float: Normalized value within the new range.
    """
    numerator = x - xmin
    denominator = xmax - xmin
    multiplier = b - a
    ans = (numerator / denominator) * multiplier + a
    return ans

def output_mapping():
    """
    Map the predicted output to a meaningful representation.

    Returns:
        str: Mapped output.
    """
    output = ""
    # Add mapping logic here if needed
    return output