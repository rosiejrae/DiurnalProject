Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ==== Identify non-clonidine-sensitive units (change >= -0.5) ====
... non_clon_epoch_by_unit = epoch_by_unit[epoch_by_unit['changeFromBL'] >= -0.5].copy()
... 
... # Extract full spike data for those units
... non_clon_sen_spikes = Data[Data['unitID'].isin(non_clon_epoch_by_unit['unitID'])].copy()
... 
... # Optional: if you're working with specific subsets (e.g., "unitID5" and "unitID15")
... # you must define them as lists or pull them from somewhere else
... # e.g. unitID5 = clon_sens_epoch_by_unit.sample(5) or a predefined list
... 
... # Get epoch-specific spikes
... EX_non_clon_bl_spikes = BL_spikes[BL_spikes['unitID'].isin(non_clon_epoch_by_unit['unitID'])].copy()
... EX_non_fs_clon_spikes = FS_spikes[FS_spikes['unitID'].isin(non_clon_epoch_by_unit['unitID'])].copy()
... EX_non_clon30_spikes = cloninject_spikes[cloninject_spikes['unitID'].isin(non_clon_epoch_by_unit['unitID'])].copy()
... 
... # If using `adj_raster_spikes` from above to assign dummy lightCycle values
... adj_raster_spikes['lightCycle'] = 'X'  # for example or visualization
... 
... # Pull specific subset of unitIDs for examples
... # Assuming unitID5 and unitID15 are lists of IDs, e.g.:
... # unitID5 = ['206797_5_1', '206797_6_1', ...]
... # unitID15 = ['206797_15_1', ...]
... 
... # Filter the adjusted raster spike table
... non_clon_spikes_5 = adj_raster_spikes[adj_raster_spikes['unitID'].isin(unitID5)].copy()
... non_clon_spikes_15 = adj_raster_spikes[adj_raster_spikes['unitID'].isin(unitID15)].copy()
... 
... # Save those if needed
... # sio.savemat(f'nonClonSpikes5_{animal_num}.mat', {'nonClonSpikes5': non_clon_spikes_5.to_dict("list")})
# sio.savemat(f'nonClonSpikes15_{animal_num}.mat', {'nonClonSpikes15': non_clon_spikes_15.to_dict("list")})
