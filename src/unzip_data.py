import os
import zipfile


# Project directory,Data(zip )file path,output unzip file path
proj_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file_path=os.path.join(proj_dir,"data","archive.zip")
output_file_path=os.path.join(proj_dir,"data")

class UnZip_data:
    def __init__(self,zip_file_path:str,output_path):
        self.zip_path=zip_file_path
        self.output_path=output_path

    def unziping_data(self):
        if not os.path.exists(self.zip_path):
            print("provide the exact path")
            raise FileNotFoundError
        
        else:
            with zipfile.ZipFile(self.zip_path,"r") as file:
                file.extractall(self.output_path)
        

if __name__=="__main__":
    unzip_obj=UnZip_data(input_file_path,output_file_path)
    unzip_obj.unziping_data()