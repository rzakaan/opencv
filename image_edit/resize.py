#!/usr/bin/python
import os, argparse, cv2

exportDir="scale"

def resize(directory, size):
    os.mkdir(exportDir)

    for name in os.listdir(directory):
        path = directory + '/' + name
        exportPath = exportDir + '/' + name
        
        img = cv2.imread(path)
        small = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
        cv2.imwrite(exportPath, small)
        
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize Images")
    parser.add_argument('-d', '--directory',     type=str, required=True, help='Directory')
    parser.add_argument('-s', '--size', nargs=2, type=int, required=True, help='Size')
    args = parser.parse_args()
    
    resize(args.directory, args.size)
