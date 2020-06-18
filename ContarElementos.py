import arcpy
import os

# Coloque la ruta de la GDB dentro de las comillas:
arcpy.env.workspace = r"C:\EIA\GDB\CARTOGRAFIA_BASE.gdb"

# Aquí comienza el codigo.
tables = arcpy.ListTables()
datasets = arcpy.ListDatasets()

for table in tables:
    count3 = str(arcpy.GetCount_management(table))
    tabla = arcpy.Describe(table)
    print tabla.name + " " + count3

for ds in datasets:
    listFCs = arcpy.ListFeatureClasses(feature_dataset = ds)
    for fc in listFCs:
        count2 = str(arcpy.GetCount_management(fc))
        capa = arcpy.Describe(fc)
        print capa.name + " " + count2