# create a folder structure using shell script
mkdir -p src
mkdir -p research
mkdir -p data

# create files
touch src/__init__.py
touch src/helper.py
touch src/prompt.py
touch .env
touch setup.py
touch app.py
touch research/trails.ipynb
touch requirements.txt

echo "Directory and files structure created successfully"

# Run command
# Open Gibash in vscode and run the below command
# sh template.sh