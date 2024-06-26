from cyclonedds.domain import DomainParticipant
from cyclonedds.pub import DataWriter
from cyclonedds.sub import DataReader
from cyclonedds.topic import Topic

from _idl._dds_fmu import DDSInput, DDSOutput

import time



# DDS Topic Setup (START) --------------------------------------------------
# Create a DomainParticipant
# This way this python script is bounded to DDS
# We can set many parameters here to configure out relationship between Python script and DDS, like Domain ID, QoS, Listeners ect...
# For our usage we simply leave parameters as default, nothing to set up basically
dp = DomainParticipant()

# reader = DataReader(dp, Topic(dp, "DDSInput", DDSInput))
# writer = DataWriter(dp, Topic(dp, "DDSOutput", DDSOutput))
writer = DataWriter(dp, Topic(dp, "DDSInput", DDSInput))


def read_data():
    msg = reader.read()
    print(msg)

    if msg:
        data = msg[0].fmu_output_value
        
        return data
    else:
        print("ERROR: Failed to retrieve data from DDS-FMU :(")
        return None
    
# Function to publish data to DDS
def publish_data() -> None:
    # msg = DDSOutput( outputHullPosition= 6*[1.0],
    #     outputAntenna1Position= 3*[2.0],
    #     outputAntenna2Position= 3*[3.0],
    #     ouputVelocitySpeed= 4.0,
    #     outputVelocityAngle = 5.0,
    #     outputAccelerationLinear = 3*[6.0],
    #     outputVelocityAngular = 3*[7.0]
    #     )

    msg = DDSInput(
            TBinputForce = 2.0,
            TBinputAngle = 3.0,
            TPinputForce = 4.0,
            TPinputAngle = 5.0,
            TSinputForce = 6.0,
            TSinputAngle = 6.0,
            inputWindSpeed = 8.0,
            inputWindAngle = 9.0,
            inputWaterCurrentSpeed = 10.0,
            inputWaterCurrentAngle = 11.0,
            inputWaveHeight = 5*[3.0])
            

    writer.write(msg)


if __name__ == "__main__":
    while True:
        time.sleep(0.5)
        # data = read_data()
        publish_data()
        
