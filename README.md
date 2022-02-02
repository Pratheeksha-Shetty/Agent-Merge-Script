
# Agent Migration/Merge

The merge script is intended for assisting with the console agent merge process after creating a custom console login page like https://company.janrain.com. Existing agents who have traditional login in https://console.janrain.com, cannot access the Custom Console page as console does not support Merging Traditional and Social logins. We PS need to merge the traditional and IDP accounts internally first. If everything works fine, we have to delete the password from traditional login, so that the user is able to login via IDP only.

## Documentation

[Documentation](https://janrain.atlassian.net/wiki/spaces/GS/pages/459833359/Merging+Console+Login+Traditional+and+Custom+IDP+Logins)
This document explains how to merge accounts one at a time. But if we have a bigger account which already has 100s of agents, the process becomes tedious. The above script automates the process.

## Table of Contents:
------------------
* [Requirements](#requirements)
    * [Data Format](#data-format)
* [Merge Script](#merge-script)
* [Delete Users Script](#delete-users-script)
* [Remove Password Script](#remove-password-script)

## Requirements

* [Python](https://www.python.org/) >= 3.0
* Cluster or app owner credentials for the metadata app - both Global(US) and China in your [.janrain-capture file](https://janrain.atlassian.net/wiki/spaces/GS/pages/166337981/Installing+Your+Cluster+Credentials+.janrain-capture+Self-Study+moved). 
* Tool [apid-cli](https://janrain.atlassian.net/wiki/spaces/ENG/pages/5406785/apid-cli) for making API calls to manage clients and settings.
* TXT file with all agent emails to be merged following Data Format guidelines below.

### Data Format

The script consumes TXT files with email id's of Agents, one in each newline. Make sure there are no spaces before and after each email id.
See `agent.txt` for an example.

## Merge Script

* This script will merge customers custom IDP with their traditional/other account.
* Also deletes password from their traditional account for security purpose.

***Steps to execute***

* Download or copy the script from Github into a file and name it as merge.py and place it in the same folder as agents.txt.
* Make sure that you have saved "metadata-dashboard" credentials in your .janrain-capture. Change in the script or .janrain-capture if you have saved the credentials as dashboard-metadata.
* If you are working on CN console then in the script change "metadata-dashboard" to "metadata-dashboard-cn" or whatever that you have saved as in your .janrain-capture file.
* Comment the "disable_traditional_login(id)" function in line 26 if you are only looking to Merge the accounts and not to delete the traditional password. You can later use "remove_password.py" script to delete password. 
* agents.txt should include the agent emails as in the sample file.
* Determine employee login IDP identifier.
    In most cases, this is some form of the agent's email address.  The easiest way to do this is to have a new user login with the IDP, then look at the 'accounts.identifier' entry in the metadata schema using an apid-cli entity.find command:
    apid-cli ef user --filter "email = 'new.user@customer.com'" -c metadata-dashboard
* Idp value is usually something like "https://idp.com/agent.name%40customer.com" 
* Open the command prompt and cd to the above folder.
* Run the below command:

    python3 merge.py agents.txt "{{idp}}"

    Replace {{idp}} with proper value.

* Script will take sometime to complete and you can see the command being executed in the prompt.
* If the email address is present in metadata-dashboard then the Count result will be >0. If its 0 then you will see "No user with email "xyz" found" printed and the script continues with the next email.

## Delete Users Script

* Sometimes users ask us to clean up/ delete large number of agents from console then you can use this script to do the same.

***Steps to execute***

* Download or copy the script from Github into a file and name it as delete_users.py and place it in the same folder as agents.txt.
* Make sure that you have saved "metadata-dashboard" credentials in your .janrain-capture. Change in the script or .janrain-capture if you have saved the credentials as dashboard-metadata.
* If you are working on CN console then in the script change "metadata-dashboard" to "metadata-dashboard-cn" or whatever that you have saved as in your .janrain-capture file.
* agents.txt should include the agent emails as in the sample file.
* Open the command prompt and cd to the folder containing agents.txt and delete_users.py.
* Run the below command:

    python3 delete_users.py agent.txt

* Script will take sometime to complete and you can see the command being executed in the prompt.
* If the email address is present in metadata-dashboard then the Count result will be >0. If its 0 then you will see "No user with email "xyz" found" printed and the script continues with the next email.

## Remove Password Script

* If you have only merged the agent accounts for the first time(to confirm if its working fine) then you have to delete agent passwords/disable traditional login, remove_password.py helps with the same.

***Steps to execute***

* Download or copy the script from Github into a file and name it as remove_password.py and place it in the same folder as agents.txt.
* Make sure that you have saved "metadata-dashboard" credentials in your .janrain-capture. Change in the script or .janrain-capture if you have saved the credentials as dashboard-metadata.
* If you are working on CN console then in the script change "metadata-dashboard" to "metadata-dashboard-cn" or whatever that you have saved as in your .janrain-capture file.
* agents.txt should include the agent emails as in the sample file.
* Open the command prompt and cd to the folder containing agents.txt and remove_password.py.
* Run the below command:

    python3 remove_password.py agent.txt

* Script will take sometime to complete and you can see the command being executed in the prompt.
* If the email address is present in metadata-dashboard then the Count result will be >0. If its 0 then you will see "No user with email "xyz" found" printed and the script continues with the next email.

## Authors

- [Pratheeksha Shetty](https://contacts.akamai.com/prashett)

