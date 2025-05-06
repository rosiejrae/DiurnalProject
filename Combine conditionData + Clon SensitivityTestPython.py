Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ==== Create epochByUnit table ====
... all_units = pd.unique(pd.concat([BL_aves['unitID'], FS_aves['unitID'], Clon5_aves['unitID']]))
... epoch_by_unit = pd.DataFrame({'unitID': all_units})
... 
... # Add shared metadata
... epoch_by_unit['lightCycle'] = light_cycle
... epoch_by_unit['estrusPhase'] = estrus_phase
... 
... # Helper to get firing rate from a table
... def get_FR(unitID, df):
...     match = df[df['unitID'] == unitID]
...     return float(match['FiringRate']) if not match.empty else 0
... 
... # Loop to populate firing rates
... epoch_by_unit['BLFR'] = epoch_by_unit['unitID'].apply(lambda uid: get_FR(uid, BL_aves))
... epoch_by_unit['FSFR'] = epoch_by_unit['unitID'].apply(lambda uid: get_FR(uid, FS_aves))
... epoch_by_unit['ClonFR'] = epoch_by_unit['unitID'].apply(lambda uid: get_FR(uid, Clon5_aves))
... 
... # ==== Handle NaNs (replace with 0) ====
... epoch_by_unit = epoch_by_unit.fillna(0)
... 
... # ==== Change from baseline ====
... epoch_by_unit['changeFromBL'] = (
...     (epoch_by_unit['ClonFR'] - epoch_by_unit['BLFR']) / epoch_by_unit['BLFR']
... ).replace([np.inf, -np.inf], 0)  # protect against division by 0
... 
... # ==== Identify clonidine-sensitive units (>= 50% decrease) ====
... clon_sens_epoch_by_unit = epoch_by_unit[epoch_by_unit['changeFromBL'] <= -0.5].copy()
... 
... # Save to .mat
