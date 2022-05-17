# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:28:20 2022

@author: lawashburn
"""

import os

output_folder = r"C:\Users\lawashburn\Documents\HyPep1.0\HyPep_Simple_ASMS_Results\20220506\Target_CoG1" #folder in which all output directories will be generated
topFD_path = r"C:\Users\lawashburn\Documents\HyPep1.0\HyPep_Simple_ASMS_Results\20220407\Target_Raw_Files\TopFD_output\2022_0318_CoG_SIM_TR1_frac.mzrt.csv" #path to topFD output
raw_converter_path =  r"C:\Users\lawashburn\Documents\HyPep1.0\HyPep_Simple_ASMS_Results\20220407\Target_Raw_Files\Formatted\CoG_1_ms2_output_list.txt" #path to RawConverter output
db_path = r"C:\Users\lawashburn\Documents\HyPep1.0\HyPep_Simple_ASMS_Results\20220503\Database\Database.csv" #crustaecean NP db path
SHS_results_path = r"C:\Users\lawashburn\Documents\HyPep1.0\HyPep_Simple_ASMS_Results\20220503\Database\priority_list.csv"
ion_list_directory_path = r"C:\Users\lawashburn\Documents\HyPep1.0\HyPep_Simple_ASMS_Results\20220429\ion_lists_unformatted"

sample_name = 'Target_CoG1'
promex_cutoff = -10
precursor_error_cutoff = 20 #ppm
fragment_error_cutoff = 0.02
precursor_charges = [1,2,3,4,5,6,7,8]
fragment_charges = [1,2,3,4]
number_loops = 5

topFD_rawconverter_combined_out_path = output_folder + '\\' + 'topFD_rawconverter_combined'
prelim_AMM_out_path = output_folder + '\\' + 'prelim_AMM_results'
AMM_v_SHS_out_path = output_folder + '\\' + 'AMM_v_SHS'
target_inclusion_list_path = output_folder + '\\' + 'inclusion_lists'
formatted_ion_list_path = output_folder + '\\' + 'ion_list_formatted'
formatted_ion_list_report_path = output_folder + '\\' + 'ion_list_formatted\\final_directory'
filtered_fragment_list_path = output_folder + '\\' + 'filtered_fragment_lists'
filtered_fragment_list_report_path = output_folder + '\\' + 'filtered_fragment_lists\\final_directory'
non0_precursor_fragment_matches_out = output_folder + '\\' + 'non0_precursor_fragment_matches'
assign0_working_directory_path = output_folder + '\\assign_charge_0\\working_directory'
assign0_final_directory_path = output_folder + '\\assign_charge_0\\final_directory'
combined_fragments_out = output_folder + '\\' + 'combined_fragment_matches'
sequence_working_directory_path = output_folder + '\\sequence_assign\\working_directory'
sequence_final_directory_path = output_folder + '\\sequence_assign\\final_directory'
looping_working_directory_path = output_folder + '\\scan_loop_assign\\working_directory'
looping_final_directory_path = output_folder + '\\scan_loop_assign\\working_directory'

if not os.path.exists(topFD_rawconverter_combined_out_path):
    os.makedirs(topFD_rawconverter_combined_out_path)
if not os.path.exists(prelim_AMM_out_path):
    os.makedirs(prelim_AMM_out_path)
if not os.path.exists(AMM_v_SHS_out_path):
    os.makedirs(AMM_v_SHS_out_path) 
if not os.path.exists(formatted_ion_list_path):
    os.makedirs(formatted_ion_list_path) 
if not os.path.exists(formatted_ion_list_report_path):
    os.makedirs(formatted_ion_list_report_path)     
if not os.path.exists(target_inclusion_list_path):
    os.makedirs(target_inclusion_list_path) 
if not os.path.exists(filtered_fragment_list_path):
    os.makedirs(filtered_fragment_list_path) 
if not os.path.exists(filtered_fragment_list_report_path):
    os.makedirs(filtered_fragment_list_report_path) 
if not os.path.exists(non0_precursor_fragment_matches_out):
    os.makedirs(non0_precursor_fragment_matches_out) 
if not os.path.exists(assign0_working_directory_path):
    os.makedirs(assign0_working_directory_path)
if not os.path.exists(assign0_final_directory_path):
    os.makedirs(assign0_final_directory_path)
if not os.path.exists(combined_fragments_out):
    os.makedirs(combined_fragments_out)
if not os.path.exists(sequence_working_directory_path):
    os.makedirs(sequence_working_directory_path)
if not os.path.exists(sequence_final_directory_path):
    os.makedirs(sequence_final_directory_path)
if not os.path.exists(looping_working_directory_path):
    os.makedirs(looping_working_directory_path)
if not os.path.exists(looping_final_directory_path):
    os.makedirs(looping_final_directory_path)

top_FD_combined_out_file_name_path = topFD_rawconverter_combined_out_path + '\\' + sample_name + '_combined_spectrum.csv'
prelim_AMM_out_file_name_path = prelim_AMM_out_path + '\\' + sample_name + '_AMM_results.csv'
AMM_v_SHS_out_results = AMM_v_SHS_out_path + '\\' + sample_name + '_unique_AMM.csv'
target_list_out_results = target_inclusion_list_path + '\\' + sample_name + '_inclusion_list.csv'
formatted_ion_list_prefix = formatted_ion_list_path + '\\Theoretical_b_y_ion_list_'
formatted_ion_list_report = formatted_ion_list_report_path + '\\Theoretical_b_y_ion_list_report.csv'
formatted_fragment_list_prefix = filtered_fragment_list_path + '\\Theoretical_b_y_fragment_list_'
filtered_fragment_list_report = filtered_fragment_list_report_path + '\\Theoretical_b_y_fragment_list_report.csv'
non0_precursor_matches_out = non0_precursor_fragment_matches_out + '\\' + sample_name + 'precursor_matches.csv'
non0_fragment_matches_out = non0_precursor_fragment_matches_out + '\\' + sample_name + 'fragment_matches.csv'
assign0_precursor_matches_out = assign0_working_directory_path + '\\' + sample_name + 'precursor_matches.csv'
assign0_1_fragment_matches_out = assign0_working_directory_path + '\\' + sample_name + '_1_zero_reassign_fragment_matches.csv'
all_fragment_matches_report_out = combined_fragments_out + '\\' + sample_name + '_all_fragments.csv'
sequence_coverage_out_path = sequence_final_directory_path + '\\' + sample_name + '_all_coverage_formatted.csv'

folder_generation_status = True