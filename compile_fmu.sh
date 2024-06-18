#!/bin/bash

ROOT=$(pwd)
cd src
./resources/tools/linux64/repacker create -v -o dds-fmu.fmu . && cd $ROOT
mv src/dds-fmu.fmu .


cd src/resources/config/idl/
idlc -l py dds-fmu.idl && cd $ROOT

mv src/resources/config/idl/_idl/_dds-fmu.py dds-fmu-interface/_dds_fmu.py
