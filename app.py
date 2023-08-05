from directory_structure import DirectoryStructureUpdater

def main():
    tree_updater = DirectoryStructureUpdater()
    directory_file = tree_updater.update_and_save_directory_tree()
    print(f"Updated directory structure saved to {directory_file}")

if __name__ == "__main__":
    main()
