# merge_all_trimble_rover_files
Merge all rover shapefiles in a directory (and all sub-directories) into one single file....this script is intended to help GIS professionals find old Trimble GNSS data.


After changeing the user-defined parameters run this script in your ArcGIS Pro Python IDE or in Python interpretor in ArcGIS Pro.


This script will sort though the user-defined directory, and all sub-directories, and look for shapefiles exported out of Pathfinder Office.  The script builds a list of the file names and paths.  The script finally merges all the data into a single shapefile.  This script will not merge any PosnPnt files that you may have exported since these are just GNSS pings and not actual data collected.  
Any and all attributes from the rover files are added to the final merge file.
