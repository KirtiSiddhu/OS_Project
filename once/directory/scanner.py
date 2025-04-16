class DirectoryScanner:
    def __init__(self, root_directory):
        self.root_directory = root_directory

    def scan(self):
        directory_info = []
        for dirpath, dirnames, filenames in os.walk(self.root_directory):
            directory_info.append({
                'directory': dirpath,
                'subdirectories': dirnames,
                'files': filenames
            })
        return directory_info

    def list_files(self):
        files = []
        for dirpath, dirnames, filenames in os.walk(self.root_directory):
            for filename in filenames:
                files.append(os.path.join(dirpath, filename))
        return files

    def filter_files(self, extension):
        filtered_files = []
        for dirpath, dirnames, filenames in os.walk(self.root_directory):
            for filename in filenames:
                if filename.endswith(extension):
                    filtered_files.append(os.path.join(dirpath, filename))
        return filtered_files