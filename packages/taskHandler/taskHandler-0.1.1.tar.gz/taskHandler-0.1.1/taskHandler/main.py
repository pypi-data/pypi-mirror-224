import os,pwd

class ManageDownloads():
    def __init__(self):
        if os.name=='nt':
            self.user_name = os.getlogin()
            self._download_path = rf'C:\Users\{self.user_name}\Downloads'
        else:
            self.user_name = pwd.getpwuid(os.getuid())[0]
            self._download_path = f'home/{self.user_name}/Downloads'

        self._whitelist = {
            'Media': {'mp3', 'mp4'},
            'Images': {'jpg', 'jpeg', 'gif', 'png'},
            'Web': {'html', 'css'},
            'MS-Office': {'docx', 'xlsx', 'ppt'},
            'Scripts': {'py', 'pyc', 'c++', 'cpp', 'c', 'java', 'js'},
            "Pdf&csv": {'pdf', 'csv'},
            'Application': {'exe', 'bat'}
        }
    # @property
    def get_download_path(self):
        return self._download_path

    # @download_path.setter
    def set_download_path(self, new_path):
        if os.path.isdir(new_path):
            self._download_path = new_path
        else:
            raise ValueError("Invalid path. Please provide a valid directory path.")
        

    def get_whitelist(self):
        return self._whitelist

    def set_whitelist(self, new_whitelist):
        if isinstance(new_whitelist, dict):
            self._whitelist = new_whitelist
        else:
            raise ValueError("Whitelist must be a dictionary.")


    def get_key_by_value(self,my_dict, target_value):
        for key, value in my_dict.items():
            if target_value in value:
                return key
        return None

    def check_value_exist(self,my_dict, target_value):
        for value_set in my_dict.values():
            if target_value in value_set:
                return True
        return False

    def move_file(self,source_path, destination_path):
        if os.name=='nt':
            cmd=f'move "{source_path}" "{destination_path}"'
            os.system(cmd)
        else:
            cmd=f'mv "{source_path}" "{destination_path}"'
            os.system(cmd)

    def organize_downloads(self):
        dir_list = os.listdir(self._download_path)
        for filename in dir_list:
            full_path = os.path.join(self._download_path, filename)
            split_file_ext = filename.split(".")[-1]
            if self.check_value_exist(self._whitelist, split_file_ext):
                folder_path = os.path.join(self._download_path, self.get_key_by_value(self._whitelist, split_file_ext))
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                self.move_file(full_path, os.path.join(folder_path, filename))

if __name__ == "__main__":
    dm = ManageDownloads()
    # print(dm.get_download_path())
    # print(dm.get_whitelist())
    # download_path = r"C:\Users\vardhan.negi\Downloads\Images"
    # dm.set_download_path(download_path)
    dm.organize_downloads()
    print("Done")
