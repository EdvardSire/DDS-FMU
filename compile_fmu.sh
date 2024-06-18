#!/bin/bash

ROOT=$(pwd)

# Compile fmu
cd src
./resources/tools/linux64/repacker create -v -o dds-fmu.fmu . && cd $ROOT
mv src/dds-fmu.fmu .


# Create python glue
cd src/resources/config/idl/
idlc -l py dds-fmu.idl && cd $ROOT
cp -r src/resources/config/idl/_idl dds-fmu-interface/
cd dds-fmu-interface/_idl && mv _dds-fmu.py _dds_fmu.py
sed -i "s/import _idl//" __init__.py
sed -i "s/_dds-fmu/_dds_fmu/" __init__.py
