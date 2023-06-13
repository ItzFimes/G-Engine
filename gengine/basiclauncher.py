import os
import fnmatch
import random
import string
import logging
import fileinput
import base64
import xml.etree.ElementTree as ET
def find_files(top_dir, pattern, exclude_dir_prefix):
    try:
        for dir_path, dir_names, file_names in os.walk(top_dir):
                for file_name in file_names:
                    if not exclude_dir_prefix or not get_file_name(dir_path).startswith(exclude_dir_prefix):
                        if fnmatch.fnmatch(file_name, pattern):
                            yield os.path.join(dir_path, file_name)
    except (IOError, OSError) as ex:
        raise e.LoadFileException(str(ex)+'\nUnable to load ' + top_dir + ' with pattern ' + pattern + ' excluding ' + exclude_dir_prefix)
        