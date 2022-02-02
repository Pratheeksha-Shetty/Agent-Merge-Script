# This function deletes console users
##Command -> python3 delete_users.py agent.txt
import json
import argparse
import subprocess

def delete_accounts(agent_email):
    # command to extract user info
    cmd = "apid-cli ef user --filter \"email = '" + agent_email + "'\" -c metadata-dashboard" #replace with metadata-dashboard-cn for China
    print(cmd)
    returned_value = subprocess.check_output(cmd, shell=True)  # executes the command
    returned_string = returned_value.decode('utf-8')  # converts byte to string
    response_dict = json.loads(returned_string)  # converts to dictionary
    print("Count result: ", response_dict['result_count'])  # checks if user does not exist
    if response_dict['result_count'] == 0:
        print("No user with email " + agent_email + " found!")
        return
    id = str(response_dict['results'][0]['id'])
    cmd2 = 'apid-cli ed user -c metadata-dashboard --id ' + id  # Command to delete user
    print(cmd2)
    response = subprocess.check_output(cmd2, shell=True)
    response = response.decode('utf-8')
    print(response)
    return


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("filename", help="Enter file name")  # takes file as arg
        args = parser.parse_args()
        filename = args.filename
        with open(filename, "r") as f:
            for lines in f:
                agent_email = lines.rstrip('\n')
                print("agent_email", agent_email)
                delete_accounts(agent_email)
    except Exception as e:
        print("Something went wrong! Check your input file. This program is expecting a text file containing email", e)
