from cyclonedds.domain import DomainParticipant
from cyclonedds.pub import DataWriter
from cyclonedds.sub import DataReader
from cyclonedds.topic import Topic

from _idl._dds_fmu import MyCustomSignalStructureInput, MyCustomSignalStructureOutput, thrusterBowStruct, thrusterPortStruct, thrusterStarboardStruct, hullStruct



# DDS Topic Setup (START) --------------------------------------------------
# Create a DomainParticipant
# This way this python script is bounded to DDS
# We can set many parameters here to configure out relationship between Python script and DDS, like Domain ID, QoS, Listeners ect...
# For our usage we simply leave parameters as default, nothing to set up basically
dp = DomainParticipant()

# This is Where we define topics and what type of data structure they have
topicInput =  Topic(dp, "MyCustomDDSFMUTopicInput", MyCustomSignalStructureInput)
topicOutput = Topic(dp, "MyCustomDDSFMUTopicOutput", MyCustomSignalStructureOutput)

# We now finally bind these topics to DDS with correct data structure
# This is the objects we will use to read or write to our DDS-FMU on STC
dr = DataReader(dp, topicInput)
dw = DataWriter(dp, topicOutput)
# DDS Topic Setup (STOP) --------------------------------------------------



# DDS Functions (START) --------------------------------------------------
# Function to read data from DDS
def read_data():
    # Read value from DDS-FMU
    msg = dr.read()
    print(msg)

    # Check that the message is not empty and that DDS-FMU actually published something
    if msg:
        # Message is a array, and inside the array we find our data structure with aropriate data
        data = msg[0].fmu_output_value
        
        return data
    else:
        print("ERROR: Failed to retrieve data from DDS-FMU :(")
        return None
    
# Function to publish data to DDS
def publish_data() -> None:
    # Construct the message with the correct data type and values inside to publish to DDS, so that DDS FMU can receive it and output it 
    # msg = MyCustomSignalStructureOutput( outputHullPosition= 6*[1.0],
    #     outputAntenna1Position= 3*[2.0],
    #     outputAntenna2Position= 3*[3.0],
    #     ouputVelocitySpeed= 4.0,
    #     outputVelocityAngle = 5.0,
    #     outputAccelerationLinear = 3*[6.0],
    #     outputVelocityAngular = 3*[7.0]
    #     )
    msg = MyCustomSignalStructureInput(
            thrusterBowStruct(2.0, 2.0),
            thrusterPortStruct(2.0, 2.0),
            thrusterStarboardStruct(2.0, 2.0),
            hullStruct(1.0, 2.0, 3.0, 4.0, 5.0)
        )
            

    # Send message to DDS for DDS-FMU to receive as an output

    dw.write(msg)
# DDS Functions (STOP) --------------------------------------------------




# Variables for DDS Reading
data = 0

# Variable for DDS communication
waitPeriod = 0.5

# Variables that change over time
variableChanging = 0.0

if __name__ == "__main__":
    while True:
        data = read_data()
        publish_data()
        
