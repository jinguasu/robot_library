# -*- coding: utf-8 -*-
import xlwt, os, re,sys

case_list = []
case_name_list = []

def get_the_case_name_in_one_suit(path):
    with open(path,'r',encoding= 'utf-8') as f:
        b = f.readlines()
        a = 0
        for i in b:
            m = re.match(r'<td class=.name.><a name=.test_(.*)\">.*',i)
            if m != None:
                a += 1
                case_name_list.append(m.group(1))
    return a

def write_to_excel():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Case Info')
    ws.write(0, 0, 'Test Suite')
    ws.write(0, 1, 'Case Name')
    ws.write(0, 2, 'Run')
    ws.write(0, 3, 'Timeout(min)')
    a = len(case_list)
    i = 1
    while i <= a:
        ws.write(i,0,case_list[i-1])
        ws.write(i,1,case_name_list[i-1])
        ws.write(i,2,'1')
        ws.write(i,3,'60')
        i += 1
    wb.save('test.csv')

def creat_case_list(path):
    og_path = os.listdir(path)
    for i in og_path:
        if i != '.svn':
            feature_path = os.path.join(path ,i)
            feature_name = os.listdir(feature_path)
            for x in feature_name:
                feature_name_path = os.path.join(feature_path,x)
                the_case = os.listdir(feature_name_path)
                for u in the_case:
                    if u.find('html') != -1:
                        the_case_all_path = os.path.join(feature_name_path,u)
                        num = get_the_case_name_in_one_suit(the_case_all_path)
                        x = 0
                        while x < num:
                            case_list.append(the_case_all_path)
                            x += 1

if __name__ == '__main__':
    path = 'D:\DEV-HZ2_case\TL17SP\CIT\ASMI'
    creat_case_list(path)
    write_to_excel()












