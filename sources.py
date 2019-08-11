import os 

class Sources:
    def __init__(self, path):
        self.path = path
    
    def walk_folder(self):
        files = []
        ruta =  self.path #"C:\\Users\\devel\\Downloads\\SQM\\Financieros\\"
        #r= dirpath, d=dirnames, f=filenames    
        for (r,d,f) in os.walk(ruta):
            f = [file for file in f if not file[0] == '.']
            for file_visible in f:
                if '.xlsx' in file_visible:
                    files.append(os.path.join(r,file_visible)) 
        return files 