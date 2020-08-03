# Change permissions of current directory
chmod +rwx .

# export environment variables
export STORAGE_ACCOUNT_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=sushant25;AccountKey=3weU42tRnUMIGflMiSY780b8AkzrbXtxtd2bJeAN6e3ETpJ31/LOO96HhFR0q9i3P0Vif5mw/IdU2pUbAqpisA==;EndpointSuffix=core.windows.net"

export PROJECT_ROOT_DIR="$PWD"

export STORAGE_CONTAINER_NAME="data"

export BLOB_URL="https://sushant25.blob.core.windows.net/data/"

# create virtual environment for dependencies
python3 -m venv develop

# activate virtual environment
source develop/bin/activate

# upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

python3 run.py
