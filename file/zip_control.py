# -*- coding: utf-8 -*-

import zipfile
import os
import re

class ZFile(object):

    def __init__(self,filename,mode='r'):
        self.filename = filename
        self.mode = mode
        if self.mode in ('w','r'):
            self.zfile = zipfile.ZipFile(filename,self.mode,compression=zipfile.ZIP_DEFLATED)
        else:
            self.zfile = zipfile.ZipFile(filename,self.mode)

    def add_file(self,path):
        path = path.replace('//','/')
        self.zfile.write(path)

    def search_file(self,target):
        for zfile in self.zfile.namelist():
            #print zfile
            if re.search(target,str(zfile)):
                return zfile
        raise Exception('not find this file %s' %target)

    def close(self):
        self.zfile.close()

    def extract_to_path(self,path):  #path should be like 'D:\\TA_Project\\library\\file\\'
        for zfile in self.zfile.namelist():
            filename = os.path.join(path,zfile)
            file(filename,'w').write(self.zfile.read(zfile))

def _use_7z_unzip(zip_file_name,target_folder_name):  # D:\\TA_Project\\library\\file\\
    import platform
    if platform.system() != 'Windows':
        if zip_file_name.endswith('.xz'):
            os.system('unxz -k -f %s' %zip_file_name)
        else:
            print 'unsupport format'
    else:
        os.environ['path'] = ';C:\\Program Files (x86)\\7-Zip\\'
        ret = os.popen('7z.exe x %s -y -o%s' %(zip_file_name,target_folder_name)).read()
        print ret
        if 'Everything is Ok' in ret:
            print '%s unzip to this path %s success' %(zip_file_name,target_folder_name)
        else:
            print 'zip failed'


def zip_file(src_file_name,zip_file_name):
    import platform
    if platform.system() == 'Windows':
        os.environ['path'] = ';C:\\Program Files (x86)\\7-Zip\\'
        ret = os.popen("7z.exe a %s %s" % (zip_file_name,src_file_name)).read()
        print ret
        if 'Everything is Ok' in ret:
            print '%s zip to %s success' %(zip_file_name,src_file_name)
        else:
            print 'zip failed'
    else:
        ret = os.popen('zip -r %s %s' %(src_file_name,zip_file_name))
        print ret
        print '%s zip to %s success' %(src_file_name,zip_file_name)


def unzip_file(zip_file_name,target_folder_name):
    """

    :param zip_file_name:
    :param target_folder_name:  need be this format  D:\\TA_Project\\library\\file\\
    :return:
    """
    init_zip = None
    if zip_file_name.endswith('.tar'):
        _use_7z_unzip(zip_file_name,target_folder_name)
    else:
        try:
            init_zip = ZFile(zip_file_name)
            init_zip.extract_to_path(target_folder_name)
            print "unzip %s to %s success" %(zip_file_name,target_folder_name)
        except Exception as error:
            print 'unzip failed and try to user 7z method to unzip this file'
            _use_7z_unzip(zip_file_name,target_folder_name)
        finally:
            if init_zip:
                init_zip.close()


if __name__ == '__main__':
    #z = ZFile('file.zip',mode='r')
    #print z.search_file('4.txt')
    #z.close()
    #print os.path.dirname('D:\\TA_Project\\library\\file\\2.txt')
    #zip_file('D:\\TA_Project\\library\\file\\sun','D:\\TA_Project\\library\\file\\sunb.zip')
    #z.extract('D:\\TA_Project\\library\\file\\')
    unzip_file('sun.zip','D:\\TA_Project\\library\\file\\')
