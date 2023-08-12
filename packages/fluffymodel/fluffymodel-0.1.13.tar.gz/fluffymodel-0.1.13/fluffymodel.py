import os
import subprocess
import requests
import json
import uuid
import re
import sys
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="A script that requires a git_name argument.")
    parser.add_argument("git_name", help="Name of the git repository in hugging face")
    args = parser.parse_args()
    return args.git_name


def create_hf_space(git_name):
    uuid_v1 = str(uuid.uuid1()).split('-')[0]
    print(uuid_v1)
    space_name_raw = f"{str(git_name)}_{str(uuid_v1)}"
    space_name = re.sub('[^A-Za-z0-9]', '_', space_name_raw)
    url = "https://huggingface.co/api/repos/create"
    print(f"Creating space...{space_name}")

    payload = json.dumps({
    "name": f"{space_name}",
    "type": "space",
    "license": "openrail",
    "private": False,
    "sdk": "gradio",
    "hardware": "cpu-basic",
    "sleepTimeSeconds": 172800,
    "secrets": [],
    "variables": [],
    "storageTier": None
    })
    headers = {
    'authority': 'huggingface.co',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '__stripe_mid=0ed6351c-47a5-4010-b24f-3675fe0505536500e4; token=VjFykIAVPyMOQOxvlyVxEQaMAlpiClUUSVhXYEHxTviNlSvaZcvdpxuDiyuBgrkNkhJlttDLmYEwSWadbsHQKBvrHxceIFDQfxwiLRCKKnQiTEIBimRpaBQfNmhdoeBi; intercom-id-hgve3glw=abff486b-e4e0-47b1-98b6-a9869238223b; intercom-device-id-hgve3glw=02685ee1-d891-49a9-a52f-e2db7f802a18; hf-chat=4d396fcc-1b6f-4352-bf17-ed42b73f9331; _gid=GA1.2.1049075653.1691430914; __stripe_sid=2ca33ac5-c037-4f87-b1ce-62efd6af86b7cca63a; intercom-session-hgve3glw=; _ga_8Q63TH4CSL=GS1.1.1691746267.70.1.1691746882.0.0.0; _ga=GA1.1.1047328574.1673851121',
    'origin': 'https://huggingface.co',
    'referer': 'https://huggingface.co/new-space',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()
    space_link = response_json['url']

    print(response.text)
    return space_name,space_link


def hf_to_gradio(git_name=None):
    if git_name is None:
        git_name = input("Please enter the git name: ")
    space_name, space_link = create_hf_space(git_name)

    git_name_clean = re.sub('[^A-Za-z0-9]', '_', git_name)
    
    HF_TOKEN = "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"
    

    commands = f"""
    git clone "https://Avinaash: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@https://huggingface.co/spaces/Avinaash/{space_name}"
    cd {space_name}
    python3 -m venv {space_name}
    source {space_name}/bin/activate
    cd {space_name}
    echo "env/" >> .gitignore
    cd {space_name}
    cat > README.md <<EOF
    ---
title: REST API for {git_name}
sdk: gradio
emoji: 🚀
colorFrom: green
colorTo: blue
license: openrail
sdk_version: 3.12.0
app_file: app.py
---
EOF
cd {space_name}
    cat > requirements.txt <<EOF 
aiohttp==3.8.3
aiosignal==1.2.0
appnope==0.1.3
asttokens==2.2.1
async-timeout==4.0.2
attrs==22.1.0
backcall==0.2.0
bitsandbytes==0.41.1
blis==0.7.9
catalogue==2.0.7
certifi==2023.7.22
cffi==1.15.1
charset-normalizer==2.0.4
click==8.0.4
confection==0.0.4
cryptography==41.0.2
cymem==2.0.6
datasets==2.12.0
debugpy==1.6.7
decorator==5.1.1
dill==0.3.6
executing==1.2.0
filelock==3.9.0
frozenlist==1.3.3
fsspec==2023.4.0
gmpy2==2.1.2
huggingface-hub==0.15.1
idna==3.4
importlib-metadata==6.8.0
ipykernel==6.25.1
ipython==8.14.0
jedi==0.19.0
Jinja2==3.1.2
joblib==1.2.0
jupyter_client==8.3.0
jupyter_core==5.3.0
langcodes==3.3.0
MarkupSafe==2.1.1
matplotlib-inline==0.1.6
multidict==6.0.2
multiprocess==0.70.14
murmurhash==1.0.7
nest-asyncio==1.5.6
networkx==3.1
numpy==1.25.2
packaging==23.0
pandas==1.5.3
parso==0.8.3
pathy==0.10.1
pexpect==4.8.0
pickleshare==0.7.5
Pillow==9.4.0
preshed==3.0.6
prompt-toolkit==3.0.39
psutil==5.9.0
ptyprocess==0.7.0
pure-eval==0.2.2
pyarrow==11.0.0
pycparser==2.21
pydantic==1.10.8
Pygments==2.16.1
pyOpenSSL==23.2.0
pytesseract==0.3.10
python-dateutil==2.8.2
pytz==2022.7
PyYAML==6.0
pyzmq==25.1.0
regex==2022.7.9
requests==2.31.0
responses==0.13.3
safetensors==0.3.2
six==1.16.0
smart-open==5.2.1
spacy-legacy==3.0.12
spacy-loggers==1.0.4
spacy==3.5.3
srsly==2.4.6
stack-data==0.6.2
thinc==8.1.10
timm==0.9.5
tokenizers==0.13.2
torch==2.0.1
torchvision==0.15.2
tornado==6.3.2
tqdm==4.65.0
traitlets==5.9.0
transformers==4.29.2
typer==0.4.1
typing_extensions==4.7.1
urllib3==1.26.16
wasabi==0.9.1
wcwidth==0.2.6
wheel==0.38.4
xxhash==2.0.2
yarl==1.8.1
zipp==3.16.2
scikit-learn==1.3.0
scipy==1.11.1
spacy-alignments==0.9.0
spacy-transformers==1.2.4
beautifulsoup4==4.11.1
fastapi==0.88.0
setuptools==68.0.0
soupsieve==2.3.2.post1
spacy-alignments==0.9.0
spacy-transformers==1.2.4
sympy==1.11.1
uvicorn==0.20.0
websocket-client==1.4.1    
EOF
cd {space_name}
    cat > app.py <<EOF 
import gradio
from transformers import pipeline

def model_pipeline(input):
    model = pipeline(model='{git_name}')
    try:
      result = model(input)
    except Exception as e:
      result = f"Model couldn't process input, refer to model card at https://huggingface.co/{git_name}.)"

    return result

gradio_interface = gradio.Interface(
    fn=model_pipeline,
    inputs="text",
    outputs="json",
    title=f"Your personal space for {git_name_clean}",
    description=f"Model card:+ https://huggingface.co/{git_name}",
  )
gradio_interface.launch()
EOF
cd {space_name}
    git add .
    git commit -m "Creating app.py"
    git push
    """
    
    process = subprocess.Popen(commands, shell=True)
    process.communicate()

    
    print(f"Visit {space_link} to start the build of the inference endpoint.")
    print("Use the below curl to hit the inference endpoint:")
    print(f"""
    curl --location 'https://avinaash-{space_name}.hf.space/run/predict' \\
    --header 'Content-Type: application/json' \\
    --data '{{"data": ["<input>"]}}'
    """)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please provide a git name")
        sys.exit()
    else:
        git_name = str(sys.argv[1])
        hf_to_gradio(git_name)