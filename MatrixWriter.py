"""Converts a list of planes to a list of 4X4 transforamtions and exports it as a .csv file.
    Inputs:
        FileName: The name of the exported file.If None it will be "Transformations.csv"
        FilePath: The location of the exported file. If None it will be the directory of the Grasshopper file that owns this component.
        ReferencePlane: The Plane to use as the Basis of the Transformations. By default it is WorldXY.
        Planes: The planes to convert to Transforms.
        Save: Set to True to write the file.

__author__ = "George Adamopoulos"
__version__ = "2018.11.18"

import Rhino.Geometry as rhg
import csv
import os.path as path

def GetMatrix(ref, p):
    return rhg.Transform.PlaneToPlane(ref, p)

if FileName is None:
    FileName = "TransformationMatrices.csv"

if not FileName.endswith(".csv"):
    FileName += ".csv"

if FilePath is None:
    dir = path.dirname(ghdoc.Path)
    FilePath = path.join(dir, FileName)

if ReferencePlane is None:
    ReferencePlane = rhg.Plane.WorldXY

if Save is True:
    transforms = [GetMatrix(ReferencePlane, p) for p in Planes]
    
    with open(FilePath, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["m00", "m01", "m02", "m03", "m10", "m11", "m12", "m13", "m20","m21", "m22", "m23", "m30","m31","m32","m33"])
        writer.writerows(row.ToFloatArray(True) for row in transforms)
    
    # Optionally open the exported file
    #subprocess.Popen('explorer ' + FilePath)
