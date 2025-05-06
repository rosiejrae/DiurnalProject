Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import numpy as np
import scipy.io as sio

# ==== Experiment Info ====
animal_num = 206797
weight = 326
estrus_phase = 'M'
light_cycle = 'D'

bl_done = 15
BL_sec = bl_done * 60

fs_start = 16
FsStart_sec = fs_start * 60

fs_done = fs_start + 5
FsDone_sec = fs_done * 60

clon_inject = 21.5
ClonInject_sec = clon_inject * 60

clon25 = clon_inject + 25
clon25_sec = clon25 * 60

clon30 = clon_inject + 30
clon30_sec = clon30 * 60

# Save experiment info
... exp_info = {'animalNum': animal_num}
... sio.savemat(f'expInfo{animal_num}.mat', exp_info)
... 
... # ==== Preprocessing ====
... col_heads = ["channel", "unit", "timestamp", "energy", "Area", "PeakFWHM", "ValleyFWHM", "PeakValley", "Waveforms"]
... 
... # Example placeholder: concatenate SPK01-SPK16 numpy arrays
... # Assuming these are already loaded as NumPy arrays with shape (N, 9)
... # Replace these with your actual data variables
... SPK_list = [SPK01, SPK02, SPK03, SPK04, SPK05, SPK06, SPK07, SPK08,
...             SPK09, SPK10, SPK11, SPK12, SPK13, SPK14, SPK15, SPK16]
... data_array = np.vstack(SPK_list)
... 
... data = pd.DataFrame(data_array[:, :9], columns=col_heads)
... 
... # Convert estrus and light cycle to full-length columns
... data['animalNum'] = animal_num
... data['estrusPhase'] = estrus_phase
... data['lightCycle'] = light_cycle
... 
... # Create unitID
... data['channel'] = data['channel'].astype(int)
... data['unit'] = data['unit'].astype(int)
... data['unitID'] = data.apply(lambda row: f"{animal_num}_{row['channel']}_{row['unit']}", axis=1)
... 
... # Create main Data table
... Data = data[['unitID', 'estrusPhase', 'lightCycle', 'timestamp']].copy()
... Data['timestamp'] = pd.to_numeric(Data['timestamp'])
... 
... # Save waveform data
... waveform_data = data.iloc[:, [2, 4, 5, 6]]  # timestamp, Area, PeakFWHM, ValleyFWHM
... waveform_file = f'waveFormData{animal_num}.mat'
... sio.savemat(waveform_file, {'waveformData': waveform_data.to_numpy()})
... 
... # Save data table
... data_file = f'Data{animal_num}.mat'
