# pet-adoption


## Setup
1. Navigate to your project directory and install dependencies:
    * `cd pet-adoption`
    * `pip install  -r requirements.txt`
    * Generate a private key file for your service account. In the Firebase console, open Settings > [Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk).
    * Click Generate New Private Key, then confirm by clicking Generate Key.
    * Move the private key file to this project directory: `mv path/to/downloaded_key.json path/to/pet-adoption/servicekey.json`

2. Run the application
    * `python main.py`

3. In your web browser, enter the following address
    * `localhost:8080`

