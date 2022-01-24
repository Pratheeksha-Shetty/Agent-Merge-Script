#The below code should serve as an example of how to use /entityType.addAttribute
##to load attribute definitions in automated fashion.
##It is NOT intended to be used as is as productional level architecture and implemntation.
##The patterns illustrated are for demonstration purposes only.
import sys
import time
import os
import json
import argparse
import requests
import types
import logging
def main():
    parser = argparse.ArgumentParser(description='Add attributes from a definition file in JSON format.  An attempt will be madee to add each definition regardless of previous individual api call failures.  Review logfile noted below in case of individual failures and update inputfile accordingly.')
    parser.add_argument("inputfile", help="name of input file in JSON format containing an array of attribute definitions")
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument("-u", "--url",  help="request url",required=True)
    requiredNamed .add_argument("-t", "--entitytypename",  help="target entity type name",required=True)
    requiredNamed .add_argument("-i", "--clientid",  help="client id",required=True)
    requiredNamed .add_argument("-s", "--clientsecret",  help="client secret",required=True)
    requiredNamed .add_argument("-c", "--targetkey",  help="target key from config file",required=True)
    args = parser.parse_args()
    clientsecret = args.clientsecret
    clientid = args.clientid
    url = args.url
    entitytype = args.entitytypename
    key = args.targetkey
    inputfile = args.inputfile
    logging.basicConfig(filename='schema_update.log',format='%(asctime)s %(message)s',level=logging.DEBUG)
    def addAttribute(uri,entitytype,clientid,clientsecret,definition):
        headers = {
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        endpoint = url+"/entityType.addAttribute"
        dataObject = {'type_name' : entitytype, 'attr_def' : definition}
        response  = requests.post(endpoint, headers=headers,  data = dataObject, auth = (clientid,clientsecret))
        return response
    def addLength(attribute_name,attribute_length):
        ## udpage this so the entity type is retrived from the arguments.  Look at APID-CLI help
        cmd = "apid-cli adsal "+entitytype +" "+attribute_name+" "+attribute_length+" -c "+key
        returned_value = os.system(cmd)
        returned_value_string = str(returned_value)
        response = attribute_name+": "+returned_value_string
        logging.debug(cmd)
        return response
    def doLogging(APIResponse):
        logging.debug(APIResponse)
    with open(inputfile) as json_file:
        attributes = json.load(json_file)
        for item in attributes:
            name = item['name']
            message = "Loading "+name
            print(message)
            logging.debug(message)
            jsondef = json.dumps(item)
            addAttributeResponse = addAttribute(url,entitytype,clientid,clientsecret,jsondef)
            jsonreponse = addAttributeResponse.json()
            stat = jsonreponse["stat"]
            text = addAttributeResponse.text
            httpstat = addAttributeResponse.ok
            if ((httpstat == True) and (stat == "ok")):
                print("stat : "+stat)
            else:
                print(text)
            logging.debug(text)
################ Length givenName ##################
    message = "Length givenName"
    print(message)
    logging.debug(message)
    attribute_name = "givenName"
    attribute_length = "80"
    addLengthResponse = addLength(attribute_name,attribute_length)
    doLogging(addLengthResponse)  
################ Length familyName ##################
    message = "Length familyName"
    print(message)
    logging.debug(message)
    attribute_name = "familyName"
    attribute_length = "80"
    addLengthResponse = addLength(attribute_name,attribute_length)
    doLogging(addLengthResponse)  
################ Length displayName ##################
    message = "Length displayName"
    print(message)
    logging.debug(message)
    attribute_name = "displayName"
    attribute_length = "255"
    addLengthResponse = addLength(attribute_name,attribute_length)
    doLogging(addLengthResponse)  
################ Length email ##################
    message = "Length email"
    print(message)
    logging.debug(message)
    attribute_name = "email"
    attribute_length = "76"
    addLengthResponse = addLength(attribute_name,attribute_length)
    doLogging(addLengthResponse)  
################ Length primaryAddress.address1 ##################
    message = "Length primaryAddress.address1"
    print(message)
    logging.debug(message)
    attribute_name = "primaryAddress.address1"
    attribute_length = "100"
    addLengthResponse = addLength(attribute_name,attribute_length)
    doLogging(addLengthResponse)  
################ Length primaryAddress.address2 ##################
    message = "Length primaryAddress.address2"
    print(message)
    logging.debug(message)
    attribute_name = "primaryAddress.address2"
    attribute_length = "100"
    addLengthResponse = addLength(attribute_name,attribute_length)
    doLogging(addLengthResponse)  
################ Length primaryAddress.city ##################
    message = "Length primaryAddress.city"
    print(message)
    logging.debug(message)
    attribute_name = "primaryAddress.city"
    attribute_length = "100"
    addLengthResponse = addLength(attribute_name,attribute_length)
    doLogging(addLengthResponse)  
################ Length primaryAddress.country ##################
    message = "Length primaryAddress.country"
    print(message)
    logging.debug(message)
    attribute_name = "primaryAddress.country"
    attribute_length = "100"
    addLengthResponse = addLength(attribute_name,attribute_length)
    doLogging(addLengthResponse)  
if __name__ == '__main__':
    main()