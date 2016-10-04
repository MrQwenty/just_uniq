# MrQwenty
# just_uniq

import md5
import glob
import os

def get_md5_hash(file):
    md5_hash = md5.new(open(file,'rb').read())
    return md5_hash.digest()

# Main
file_type = raw_input("Type your file extension, like 'jpg, png': ")
files_lst = glob.glob('./*.'+file_type)
md5_hash_lst = []

for file_ in files_lst:
    try:
        md5_hash_lst.index(get_md5_hash(os.path.abspath(file_)))
        os.remove(os.path.abspath(file_))
        print "Already exist: " + file_
    except ValueError:
        md5_hash_lst.append(get_md5_hash(os.path.abspath(file_)))
