#!/usr/bin/python3
from test_shared import *
from lib.sim900.smshandler import SimGsmSmsHandler, SimSmsPduCompiler
import random

MINE			= "+381643354778"
VOJA			= "+381648255218"

COMPORT_NAME            = "/dev/ttyUSB0"

#logging levels
CONSOLE_LOGGER_LEVEL    = logging.DEBUG
LOGGER_LEVEL            = logging.DEBUG

#WARN: scecify recipient number here!!!
TARGET_PHONE_NUMBER     = VOJA

#You can specify SMS center number, but it's not necessary. If you will not specify SMS center number, SIM900
#module will get SMS center number from memory
# SMS_CENTER_NUMBER       = "+1 050 123 45 67"
SMS_CENTER_NUMBER       = ""

def printScaPlusPdu(pdu, logger):
    #printing SCA+PDU just for debug
    d = pdu.compile()
    if d is None:
        return False

    for (sca, pdu, ) in d:
        logger.info("sendSms(): sca + pdu = \"{0}\"".format(sca + pdu))

def sendSms(sms, pdu, logger):
    #just for debug printing all SCA + PDU parts
    printScaPlusPdu(pdu, logger)

    if not sms.sendPduMessage(pdu, 1):
        logger.error("error sending SMS: {0}".format(sms.errorText))
        return False

    return True


def main():
    """
    Tests SMS sending.

    :return: true if everything was OK, otherwise returns false
    """

    #adding & initializing port object
    port = initializeUartPort(portName=COMPORT_NAME)

    #initializing logger
    (formatter, logger, consoleLogger,) = initializeLogs(LOGGER_LEVEL, CONSOLE_LOGGER_LEVEL)

    #making base operations
    d = baseOperations(port, logger)
    if d is None:
        return False

    (gsm, imei) = d

    #creating object for SMS sending
    sms = SimGsmSmsHandler(port, logger)

    #ASCII
    logger.info("sending ASCII (Latin-1) SMS")
    pduHelper = SimSmsPduCompiler(
        SMS_CENTER_NUMBER,
        TARGET_PHONE_NUMBER,
        "Ajmo na pivo?"
    )
    if not sendSms(sms, pduHelper, logger):
        return False
    """
    #UCS2
    logger.info("sending UCS2 message")
    pduHelper = SimSmsPduCompiler(
        SMS_CENTER_NUMBER,
        TARGET_PHONE_NUMBER,
        "Uraaa"
    )
    if not sendSms(sms, pduHelper, logger):
        return False

    #long UCS2 message
    logger.info("sending long UCS2 (Unicode) SMS")
    pduHelper = SimSmsPduCompiler(
        SMS_CENTER_NUMBER,
        TARGET_PHONE_NUMBER,
        "jos jednom uraaa"
    )
    """
    pduHelper.setValidationPeriodInDays(10)

    if not sendSms(sms, pduHelper, logger):
        return False

    gsm.closePort()
    return True

if __name__ == "__main__":
    main()
    print("DONE")
