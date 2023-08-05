import os
import yaml

class DirectoryStructureUpdater:
    def __init__(self, config_file="config/config.yaml"):
        self.config_file = config_file

    def generate_tree_structure(self, path, prefix=""):
        entries = os.listdir(path)
        files = [f for f in entries if os.path.isfile(os.path.join(path, f))]
        dirs = [d for d in entries if os.path.isdir(os.path.join(path, d))]

        tree_structure = prefix + "├── " + os.path.basename(path) + "\n"

        for file in files:
            tree_structure += prefix + "│   ├── " + file + "\n"

        for i, dir in enumerate(dirs):
            if i == len(dirs) - 1:
                new_prefix = prefix + "    "
            else:
                new_prefix = prefix + "│   "
            dir_path = os.path.join(path, dir)
            tree_structure += self.generate_tree_structure(dir_path, new_prefix)

        return tree_structure

    def update_and_save_directory_tree(self):
        with open(self.config_file, "r") as config_yaml:
            config_data = yaml.safe_load(config_yaml)

        root_directory = config_data["root_directory"]
        project_description = config_data["project_description"]

        script_directory = os.path.dirname(os.path.abspath(__file__))
        root_path = os.path.join(script_directory, root_directory)

        tree_structure = self.generate_tree_structure(root_path)

        project_directory = os.path.join(script_directory, project_description)
        project_directory = os.path.normpath(project_directory)
        project_directory = os.path.join(project_directory, "Project Description")
        os.makedirs(project_directory, exist_ok=True)

        dest_file = os.path.join(project_directory, "Project_dir.txt")
        with open(dest_file, "w", encoding="utf-8") as file:
            file.write(tree_structure)

        return dest_file
