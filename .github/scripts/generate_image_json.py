import os
import json
from pathlib import Path

def generate_json():
    image_folder = Path('icon')  # Using pathlib for better path handling
    json_data = {
        "name": "Mikephie图标订阅",
        "description": "收集一些自己脚本用到的图标",
        "icons": []
    }

    if not image_folder.exists():
        raise FileNotFoundError(f"The folder '{image_folder}' does not exist.")

    # Ensure GITHUB_REPOSITORY exists in environment variables
    github_repo = os.environ.get('GITHUB_REPOSITORY')
    if not github_repo:
        raise EnvironmentError("GITHUB_REPOSITORY environment variable is not set.")

    # Loop through icons folder and add PNG files to the JSON
    for filename in image_folder.iterdir():
        if filename.suffix == ".png":
            raw_url = f"https://raw.githubusercontent.com/{github_repo}/main/{filename}"
            icon_data = {"name": filename.name, "url": raw_url}
            json_data["icons"].append(icon_data)

    # Output JSON file
    output_path = Path.cwd() / 'mikephie.icons.json'

    # Write JSON to file
    with output_path.open('w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

    # Save output path to GITHUB_STATE
    github_state = os.environ.get('GITHUB_STATE')
    if github_state:
        with open(github_state, 'a') as state_file:
            state_file.write(f"ICONS_JSON_PATH={output_path}\n")
    else:
        print("GITHUB_STATE environment variable is not set.")

if __name__ == "__main__":
    generate_json()
