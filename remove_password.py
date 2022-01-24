# This function deletes password from their traditional account for security purpose.
#Command -> python3 remove_password.py agents.txt
import json
import argparse
import subprocess

# function to delete password/ disable traditional account
def disable_traditional_login(agent_email):
    cmd = "apid-cli ef user --filter \"email = '" + agent_email + "'\" -c metadata-dashboard" #replace with metadata-dashboard-cn for China
    print(cmd)
    returned_value = subprocess.check_output(cmd, shell=True)  # executes the api cmd
    returned_string = returned_value.decode('utf-8')  # converts byte to string
    response_dict = json.loads(returned_string)  # loads the string into dict
    print("Count result: ", response_dict['result_count'])
    if response_dict['result_count'] == 0:  # checking if user doesn't exist
        print("No user with email " + agent_email + " found!")
        return
    id = response_dict['results'][0]['id']
    id = str(id)
    cmd = "apid-cli eu user '{\"password\": null}' --id " + id + " -c metadata-dashboard" #replace with metadata-dashboard-cn for China
    print(cmd,"\n")
    returned_value = subprocess.check_output(cmd, shell=True)
    returned_string = returned_value.decode('utf-8')
    print(returned_string)
    return returned_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Enter file name")  # file as argument
    args = parser.parse_args()
    filename = args.filename
    try:
        with open(filename, "r") as f:
            for lines in f:
                agent_email = lines.rstrip('\n')
                disable_traditional_login(agent_email)
    except Exception as e:
        print(
            "Something went wrong! Check your input file. This program is expecting a text file with comma separated value of email, new idp ",
            e)
