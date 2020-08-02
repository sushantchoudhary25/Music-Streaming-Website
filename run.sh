# Change permissions of current directory
chmod +rwx .

# export environment variables
export STORAGE_ACCOUNT_CONNECTION_STRING="your_storage_account_connection_string"

export PROJECT_ROOT_DIR="$PWD"

export STORAGE_CONTAINER_NAME="your_storage_account_container_name"

export BLOB_URL="your_storage_account_container_url"

# create virtual environment for dependencies
python3 -m venv develop

# activate virtual environment
source develop/bin/activate

# upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

python3 run.py
