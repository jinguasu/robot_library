# -*- coding: utf-8 -*-
from subprocess import Popen,PIPE
import os
from logger import logger
import xlrd
from xml.etree import ElementTree


def get_was_node():
    p = Popen(['/opt/cpf/sbin/netact_status.sh','status','service','fmwas'],stdout=PIPE) # 命令行是一个list
    out = p.communicate()[0]
    was_nodes = []
    for line in out.split(os.linesep):    #os.linesep 行终止符
        if line.startswith("fmwas"):
            was_nodes.append(line.split(":")[1])
            # if re.match(r'fmwas.*:(.*):.*',i):       这里也可以用正则表达式来匹配
            # was_node.append(re.match(r'fmwas.*:(.*):.*',i).group(1))
    return was_nodes

def parse_excel(input_file):
    logger.info('begin to parse input file'+ input_file)
    workbook = xlrd.open_workbook(input_file)
    sheet = workbook.sheet_by_index(0)   #根据sheet索引获取sheet的内容，从0开始

    rows = []
    for row in range(sheet.nrows):
        rows.append(sheet.row_values(row))   #获取每一行的内容，为一个list
    logger.info('finish parsing input excel, will integrate %s MRBTSs'%len(rows))

    return rows



def write_conf(input_excel,output_dir):
    #was_nodes = get_was_node()      在netact上执行，获取common node
    was_nodes = ['sprintlab339vm20', 'sprintlab339vm21', 'sprintlab339vm22', 'sprintlab339vm23',
                 'sprintlab339vm24', 'sprintlab339vm25', 'sprintlab339vm26', 'sprintlab339vm27']
    was_count = len(was_nodes)
    rows = parse_excel(input_excel)

    if len(rows) < was_count:
        was_count = len(rows)
        was_nodes = was_nodes[:was_count]

    btsDict = {}
    for idx, row in enumerate(rows):
        """
        在这里，因为表中的数据比较多，每一个node需要存放一些数据，在这里，按照node数目，平均分配了MRBTS的数目
        结合取余数的方法，采用字典来存放，0 放入全部余数是0的
        站的数目，以此，共有8个node， 字典数值为0-7，数目就是一样的了

        """
        key = idx % was_count
        if key not in btsDict:
            btsDict[key] = []

        btsDict[key].append(row)
    logger.info('begin to generate configuration file')
    node_tpl_map = {}
    for i in range(was_count):
        root = ElementTree.Element("init-configuration")
        neType = ElementTree.SubElement(root,"NEType")
        neType.attrib["adaptation"] = "com.nokia.sbts"
        neType.attrib["version"] = "SBTS16.2"
        neType.attrib["class"] = "SBTS"

        for row in btsDict[i]:
            (mr, mrbts, fqdn) = row[0:3]
            (noneTlsPort, tlsPort, ipVer, isTls) = (int(row[3]), int(row[4]), int(row[5]), int(row[6]))


            neInsElem = ElementTree.SubElement(neType, "NEInstance")
            neInsElem.attrib["agentAddress"] = fqdn

            mrElem = ElementTree.SubElement(neInsElem, "MR")
            mrElem.attrib["distName"] = mr

            mrbtsMoElem = ElementTree.SubElement(mrElem, "MO")
            mrbtsMoElem.attrib["distName"] = mrbts

            verElem = ElementTree.SubElement(mrbtsMoElem, "version")
            verElem.text = "SBTS16.2"

            ne3sMoElem = ElementTree.SubElement(neInsElem, "MO")
            ne3sMoElem.attrib["distName"] = mrbts + "/NE3SWS-1"

            hostElem = ElementTree.SubElement(ne3sMoElem, "hostName")
            hostElem.text = fqdn
            bsElem = ElementTree.SubElement(ne3sMoElem, "baseServiceName")
            bsElem.text = "NE3S/1.0"
            ne3sBaOS = ElementTree.SubElement(ne3sMoElem, "ne3sBasicOperationsService")
            ne3sBaOS.text = "NE3SBasicOperationsService"
            ne3sBuOS = ElementTree.SubElement(ne3sMoElem, "ne3sBulkOperationsService")
            ne3sBuOS.text = "NE3SBulkOperationsService"
            ne3sOS = ElementTree.SubElement(ne3sMoElem, "ne3sOperationService")
            ne3sOS.text = "NE3SOperationService"
            ne3sRS = ElementTree.SubElement(ne3sMoElem, "ne3sRegistrationService")
            ne3sRS.text = "NE3SRegistrationService"
            ne3sSS = ElementTree.SubElement(ne3sMoElem, "ne3sSessionService")
            ne3sSS.text = "NE3SSessionService"
            httpPortElem = ElementTree.SubElement(ne3sMoElem, "httpPort")
            httpPortElem.text = str(noneTlsPort)
            httpsPortElem = ElementTree.SubElement(ne3sMoElem, "httpsPort")
            httpsPortElem.text = str(tlsPort)
            ipVerElem = ElementTree.SubElement(ne3sMoElem, "ipVersion")
            ipVerElem.text = str(ipVer)
            smElem = ElementTree.SubElement(ne3sMoElem, "securityMode")
            smElem.text = str(isTls)

            emMoElem = ElementTree.SubElement(neInsElem, "MO")
            emMoElem.attrib["distName"] = mrbts + "/EM-1"

            emDnElem = ElementTree.SubElement(emMoElem, "hostName")

        tree = ElementTree.ElementTree(root)
        tpl_file = output_dir + '/' + was_nodes[i] + "_template" + ".xml"
        tree.write(tpl_file)
        logger.info("finish generate confiuration file %s, will run on node %s"%(tpl_file,was_nodes[i]))

        node_tpl_map[was_nodes[i]]= tpl_file

    return node_tpl_map







if __name__ == '__main__':
    #print get_was_node()
    #print parse_excel('MRBTS_conf_1-500.xlsx')
    write_conf('MRBTS_conf_1-500.xlsx','templates')