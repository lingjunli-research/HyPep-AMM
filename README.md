# HyPep-AMM

HyPep is produced and maintained by the Lingjun Li Research Group at the University of Wisconsin-Madison. This program is designed for accurate mass matching of neuropeptides at both precursor and fragment levels. This program is still in progress, and a GUI will be available in a future release.

For use currently:
1. Make all edits to the user_input.py file only, specifically lines 10-23
2. From the command prompt, run user_output.py. All output files will be reported in the the folder specified in Step 1.

Example input files are provided. Here are the names with the accomanying lines for the user_input.py script:

topFD (line 11): 2021_0817_Brain_1_frac.mzrt
raw_converter (line 12): Brain_1_untarget_ms2_output_list
db (line 13): Database
SHS_results (line 14): Brain_SHS
ion_list (line 15): Ion_Lists

*An ion list is required to be generated for each database sequence, once it is detected within the accurate mass matching
