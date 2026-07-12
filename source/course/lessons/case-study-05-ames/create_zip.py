#!/usr/bin/env python3
"""
Script to create a zip file of the Ames Housing case study materials,
excluding hidden files, R notebooks, and untitled notebooks.

This script can be run from any directory - it will find the case study files
based on its own location.
"""

import os
import zipfile
import re
import sys
from datetime import datetime

def should_include(filename):
    """Determine if a file should be included in the zip"""
    # Skip hidden files/directories
    if filename.startswith('.'):
        return False
    
    # Skip R notebooks
    if filename.endswith('-r.ipynb'):
        return False
    
    # Skip untitled notebooks
    if re.match(r'Untitled.*\.ipynb', filename):
        return False
    
    return True

def create_zip():
    """Create a zip file with the selected files"""
    # Get the directory where this script is located
    script_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(script_path)
    
    print(f"Creating zip from directory: {current_dir}")
    
    # Create a timestamp for the zip filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_filename = os.path.join(current_dir, f'ames_housing_case_study_{timestamp}.zip')
    
    # Create a new zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the directory
        for root, dirs, files in os.walk(current_dir):
            # Filter out directories we don't want to traverse
            dirs[:] = [d for d in dirs if should_include(d)]
            
            # Process files
            for file in files:
                if should_include(file) and file != os.path.basename(__file__):
                    # Get the full path of the file
                    file_path = os.path.join(root, file)
                    
                    # Calculate the relative path for the archive
                    rel_path = os.path.relpath(file_path, current_dir)
                    
                    # Add the file to the zip
                    zipf.write(file_path, rel_path)
                    print(f"Added: {rel_path}")
    
    print(f"\nZip file created: {zip_filename}")
    return zip_filename

if __name__ == "__main__":
    try:
        zip_file = create_zip()
        print("\nTo extract the zip file, run:")
        print(f"unzip {os.path.basename(zip_file)}")
        print(f"\nFull path to zip file: {zip_file}")
    except Exception as e:
        print(f"Error creating zip file: {e}")
        sys.exit(1)
