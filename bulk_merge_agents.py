# This function will merge customers custom IDP with their traditional/other account.
# Also deletes password from their traditional account for security purpose.
#Command -> python3 bulk_merge_agents.py agents.txt "idp"
import json
import argparse
import subprocess


def merge_accounts(agent_email, new_idp):
    cmd = "apid-cli ef user --filter \"email = '" + agent_email + "'\" -c metadata-dashboard" #replace with metadata-dashboard-cn for China
    print(cmd)
    returned_value = subprocess.check_output(cmd, shell=True)  # executes the api cmd
    returned_string = returned_value.decode('utf-8')  # converts byte to string
    response_dict = json.loads(returned_string)  # loads the string into dict
    print("Count result: ", response_dict['result_count'])
    if response_dict['result_count'] == 0:  # checking if user doesn't exist
        print("No user with email " + agent_email + " found!")
        return
    uuid = response_dict['results'][0]['uuid']
    cmd2 = 'apid-cli eu user \'{"accounts":[{"identifier":"' + new_idp + '"}]}\' --uuid ' + uuid + ' -c metadata-dashboard'
    print(cmd2)
    response = subprocess.check_output(cmd2, shell=True)
    response = response.decode('utf-8')
    print(response)
    id = response_dict['results'][0]['id']
    disable_traditional_login(id)  # separating delete password fun, comment this line if you only want to merge
    return


# function to delete password/ disable traditional account
def disable_traditional_login(id):
    id = str(id)
    cmd = "apid-cli eu user '{\"password\": null}' --id " + id + " -c metadata-dashboard"
    print(cmd)
    returned_value = subprocess.check_output(cmd, shell=True)
    returned_string = returned_value.decode('utf-8')
    print(returned_string)
    return returned_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Enter file name")  # file as argument
    parser.add_argument("new_idp", help="Enter idp url")  # url as argument
    args = parser.parse_args()
    filename = args.filename
    new_idp = args.new_idp
    try:
        with open(filename, "r") as f:
            for lines in f:
                agent_email = lines.rstrip('\n')
                idp_email = agent_email.replace("@" ,"%40")
                idp = new_idp+"/"+idp_email
                print(idp)
                merge_accounts(agent_email, idp)
    except Exception as e:
        print(
            "Something went wrong! Check your input file. This program is expecting a text file with comma separated value of email, new idp ",
            e)
