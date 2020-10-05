import argparse
import pathlib
import json
import util
import save

def convert_to_json(file):
    genFileList = util.genDirList(file)
    fileList = genFileList.listOut
    for fileObj in fileList:
        if str(fileObj).split('.')[-1] == 'sav':
            dataOut = save.parseSaveFile(fileObj, skip_bools=False)
            if dataOut != None:
                fileOpen = open(pathlib.Path(str(f'{fileObj}.json')), 'wt')
                fileOpen.write(json.dumps(dataOut, indent=2))
                fileOpen.close()
            else:
                continue
        else:
            continue
