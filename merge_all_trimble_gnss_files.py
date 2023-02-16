#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch (geraldg@lummi-nsn.gov)'
__date__ = 'February 2023'

import sys
import traceback
import arcpy
import os

try:
    #########       USER DEFINED PARAMETERS     ####################
    workspace = r"E:\GISPublicGerry20210211\GerryG\GPS\Export"
    out_fc = r"C:\gTemp\all_gnss_pre2020.shp"
    ################################################################
    print('Running...')
    #a list of files and their paths to merge together...
    feature_classes = []
    #walk the directory and all subdirectories and get any file that is not a PosnPnt.shp
    for dirpath, dirnames, datatypes in arcpy.da.Walk(workspace,datatype="FeatureClass",type="Point"):
        for filename in datatypes:
            if filename == 'PosnPnt.shp':
                pass
            else:
                feature_classes.append(os.path.join(dirpath, filename))
    arcpy.management.Merge(feature_classes, out_fc, "", "ADD_SOURCE_INFO")
    print('Finished without error')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
