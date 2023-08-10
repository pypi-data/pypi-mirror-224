import os
from pathlib import Path
from threading import Thread

class Git:
    
    def __init__(self, Wrap, querys):
        self.Wrap = Wrap
        self.querys = querys
    
    def start(self):
        print("start download:"+str(self.querys))
        p = Thread(target=self.down, args=(self.querys,))
        p.start()
    

    def down(self, querys):
        for query in querys:
            self.Wrap.msg = "downloading "+query+" ..."
            msg = self.download(query)
            self.Wrap.msg = query + " " + msg
    
    def download(self, name):
        try:
            assert name.startswith("https://huggingface")
            home = str((Path("~") / ".cache" ).expanduser())
            os.popen(f"cd {home} && git lfs clone  {name} ")
            return "ok"
        except AssertionError:
            return name+ " : error in repo must start with https://huggingface"
        except Exception as e:
            return str(e)
            