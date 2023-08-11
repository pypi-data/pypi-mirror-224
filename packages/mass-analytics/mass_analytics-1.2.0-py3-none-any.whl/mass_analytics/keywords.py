import requests
import json


class color:
   BOLD = '\033[1m'
   END = '\033[0m'

gist_id = "c36a2a2a5f11f72ae40a7425f36bd3f7"
file_name = "Keywords.json" 

def see_all():
    """
    Fetches JSON content from a specific file within a GitHub Gist.

    Args:
        gist_id (str): The unique identifier of the GitHub Gist.
        file_name (str): The name of the JSON file within the Gist.

    Returns:
        dict: A dictionary containing the parsed JSON content from the specified file.

    Raises:
        Exception: If the Gist or file retrieval fails, or if there is an error parsing JSON content.

    Note:
        This function utilizes the GitHub Gist API to fetch the content of a specified file within a Gist.
        The content is assumed to be in JSON format, and this function attempts to parse it as such.
    """

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(f"https://api.github.com/gists/{gist_id}", headers=headers)

    if response.status_code == 200:
        gist_data = response.json()
        if file_name in gist_data["files"]:
            content = gist_data["files"][file_name]["content"]
            try:
                json_content = json.loads(content)
                return json_content
            except json.JSONDecodeError:
                raise Exception("Error parsing JSON content")
        else:
            raise Exception("File not found in Gist")
    else:
        raise Exception("Failed to fetch Gist")
    
def add_value(category, key, value):
    """
    Add a value to a JSON file in a GitHub Gist.

    Args:
        category (str): The category under which the key-value pair should be added.
        key (str): The key within the specified category.
        value: The value to be added to the JSON file.

    This function retrieves the current content of a JSON file within a GitHub Gist,
    adds a new value to the specified category and key, and updates the Gist with
    the modified content.

    Note:
        - The function will prompt you to input your GitHub Personal Access Token.
        - Make sure the specified category/key exist.
        - The function handles possible errors related to JSON decoding, category, and key.

    Raises:
        Exception: If the Gist or file is not found, access token is incorrect,
                   JSON content cannot be parsed, or the category/key is invalid.
    """

    access_token = input("Write the access token please : ")
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Fetch the current Gist data
    response = requests.get(f"https://api.github.com/gists/{gist_id}", headers=headers)

    if response.status_code == 200:
        gist_data = response.json()
        
        if file_name in gist_data["files"]:
            file_data = gist_data["files"][file_name]
            content = file_data["content"]
            try:
                json_content = json.loads(content)
            except json.JSONDecodeError:
                raise Exception("Error parsing JSON content")
            try:
                json_content[category][key].append(value)
            except:
                for cat in json_content.keys():    
                    print(print(color.BOLD+"Category "+color.END+str(cat)+color.BOLD+"\n    keys "+color.END+str(list(json_content[cat].keys()))))
                raise Exception("Error: Wrong Category or Key")
            file_data["content"] = json.dumps(json_content, indent=4)

            # Update the Gist content
            data = {
                "files": {
                    file_name: file_data
                }
            }
            update_response = requests.patch(f"https://api.github.com/gists/{gist_id}", headers=headers, json=data)

            if update_response.status_code == 200:
                print("Gist content updated successfully.")
            else:
                raise Exception("Failed to update Gist content")
        else:
            raise Exception("File not found in Gist")
    else:
        raise Exception("Failed to fetch Gist maybe wrong access token")

