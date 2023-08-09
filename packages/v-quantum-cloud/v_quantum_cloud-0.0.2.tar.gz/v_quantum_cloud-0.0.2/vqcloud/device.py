from enum import Enum


class Device(str, Enum):
    Local = "local"
    IonQDevice = "aws/ionq/ionQdevice"
    IonQAria1 = "aws/ionq/Aria-1"
    IonQHarmony = "aws/ionq/Harmony"
    OqcLucy = "aws/oqc/Lucy"
    AspenM3 = "aws/rigetti/Aspen-M-3"
    SimSv1 = "aws/amazon/sv1"
    SimTn1 = "aws/amazon/tn1"
    SimDm1 = "aws/amazon/dm1"
