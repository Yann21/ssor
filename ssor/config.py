import os
from dotenv import dotenv

dotenv()

org_roam_path = "/home/yann/Documents/Application/KnowledgeManager/pages"
persist_directory = "/home/yann/persist"
banned_org_roam_files = {"screening"}
openai_api_key = os.environ["OPENAI_API_KEY"]
