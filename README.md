# nslookup Tool for Multiple Websites

This Python script allows you to perform **nslookup** on multiple websites simultaneously to retrieve their IP addresses. The tool is simple to use and can be easily modified to suit your needs.

## Features

- **Batch Lookup**: Resolve IP addresses for multiple domains in one go.
- **Error Handling**: Handles invalid or unreachable domains gracefully.
- **Easy to Use**: Just list the domains and run the script.

## Prerequisites

- **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Download the Script**

   You can download the script directly from [this link](https://github.com/IrsyadSEC/GRANDAlookup/blob/main/GRANDAlookup.py) or clone the repository using:

   ```bash
   git clone https://github.com/IrsyadSEC/GRANDAlookup.git

   Prepare the Script

Open the downloaded script file GRANDAlookup.py in your text editor or IDE.

Edit the Script (Optional)

Modify the list of websites in the script if you want to perform lookups on different domains. The list is defined in the script as follows:

python
Copy code
websites = [
    'example.com',
    'google.com',
    'facebook.com'
]
Run the Script

Open a terminal or Command Prompt and navigate to the directory where you saved the script. Execute the script using:

bash
Copy code
python GRANDAlookup.py
The script will output the IP addresses for the websites listed.

Example Output
When you run the script, you might see output similar to this:

makefile
Copy code
example.com: 93.184.216.34
google.com: 142.250.190.78
facebook.com: 157.240.22.35
If a domain is unreachable or invalid, the script will display:

makefile
Copy code
invalidwebsite.com: Invalid domain or unreachable
Contributing
Feel free to fork the repository and submit pull requests with improvements or additional features. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or issues, please reach out to IrsyadSEC.
