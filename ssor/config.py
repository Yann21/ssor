import os
from dotenv import load_dotenv

load_dotenv()

org_roam_path = "/home/yann/Documents/Application/KnowledgeManager/pages"
persist_directory = "/home/yann/Documents/Application/KnowledgeManager/chroma"
banned_org_roam_files = {"screening"}
openai_api_key = os.environ["OPENAI_API_KEY"]
