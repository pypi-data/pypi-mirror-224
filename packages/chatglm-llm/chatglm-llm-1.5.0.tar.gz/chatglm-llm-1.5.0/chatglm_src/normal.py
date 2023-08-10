from typing import Any
import tqdm
from termcolor import colored
import json
import time
from websocket import create_connection
from hashlib import md5
from typing import List
import datetime
from typing import Iterable

class SmallModel:

    def __init__(self,name, remote):
        self.remote_host  = remote
        self.name = name
        self._ok = False
    
    
    def status(self):
        try:
            ws = create_connection(f"ws://{self.remote_host}:15000")
            user_id = md5(time.asctime().encode()).hexdigest()
            TODAY = datetime.datetime.now()
            PASSWORD = "ADSFADSGADSHDAFHDSG@#%!@#T%DSAGADSHDFAGSY@#%@!#^%@#$Y^#$TYDGVDFSGDS!@$!@$" + f"{TODAY.year}-{TODAY.month}"
            ws.send(json.dumps({"user_id":user_id, "password":PASSWORD}))
            res = ws.recv()
            if res != "ok":
                print(colored("[info]:","yellow") ,res)
                raise Exception("password error")
            res = self.send_and_recv(json.dumps({"embed_documents":[self.name], "method":"status"}),ws)
            return res
        except Exception as e:
            raise e
        finally:
            ws.close()
    
    @classmethod
    def from_remote(cls, name,remote):
        model = cls(name, remote)
        model.try_load_in_remote()
        return model
    
    @classmethod
    def show_all_models(cls, remote):
        ws = create_connection(f"ws://{remote}:15000")
        user_id = md5(time.asctime().encode()).hexdigest()
        TODAY = datetime.datetime.now()
        PASSWORD = "ADSFADSGADSHDAFHDSG@#%!@#T%DSAGADSHDFAGSY@#%@!#^%@#$Y^#$TYDGVDFSGDS!@$!@$" + f"{TODAY.year}-{TODAY.month}"
        ws.send(json.dumps({"user_id":user_id, "password":PASSWORD}))
        res = ws.recv()
        if res != "ok":
            print(colored("[info]:","yellow") ,res)
            raise Exception("password error")
        res = cls.send_and_recv(json.dumps({"embed_documents":["all"], "method":"ls-all"}),ws)
        return res
        

    
    def down_remote(self):
        try:
            ws = create_connection(f"ws://{self.remote_host}:15000")
            user_id = md5(time.asctime().encode()).hexdigest()
            TODAY = datetime.datetime.now()
            PASSWORD = "ADSFADSGADSHDAFHDSG@#%!@#T%DSAGADSHDFAGSY@#%@!#^%@#$Y^#$TYDGVDFSGDS!@$!@$" + f"{TODAY.year}-{TODAY.month}"
            ws.send(json.dumps({"user_id":user_id, "password":PASSWORD}))
            res = ws.recv()
            if res != "ok":
                print(colored("[info]:","yellow") ,res)
                raise Exception("password error")
            res = self.send_and_recv(json.dumps({"embed_documents":[self.name], "method":"clone"}),ws)
            return res
            
        except Exception as e:
            raise e
        finally:
            ws.close()

    @classmethod
    def send_and_recv(cls, data, ws):
        try:
            T = len(data)// 1024*102
            bart = tqdm.tqdm(total=T,desc=colored(" + sending data","cyan"))
            bart.leave = False
            for i in range(0, len(data), 1024*102):
                bart.update(1)
                ws.send(data[i:i+1024*102])
            bart.clear()
            bart.close()

            ws.send("[STOP]")
            message = ""
            total = int(ws.recv())
            bar = tqdm.tqdm(desc=colored(" + receiving data","cyan", attrs=["bold"]), total=total)
            bar.leave = False
            while 1:
                res = ws.recv()
                message += res
                bar.update(len(res))
                if message.endswith("[STOP]"):
                    message = message[:-6]
                    break
            bar.clear()
            bar.close()
            msg = json.loads(message)
            return msg
        except Exception as e:
            raise e
    
    def check(self):
        self._ok = False
        name = self.name
        if "/" in name:
            name = name.rsplit("/",1)[-1]

        ws = create_connection(f"ws://{self.remote_host}:15000")
        user_id = md5(time.asctime().encode()).hexdigest()
        TODAY = datetime.datetime.now()
        PASSWORD = "ADSFADSGADSHDAFHDSG@#%!@#T%DSAGADSHDFAGSY@#%@!#^%@#$Y^#$TYDGVDFSGDS!@$!@$" + f"{TODAY.year}-{TODAY.month}"
        ws.send(json.dumps({"user_id":user_id, "password":PASSWORD}))
        res = ws.recv()
        if res != "ok":
            print(colored("[info]:","yellow") ,res)
            raise Exception("password error")
        if self.send_and_recv(json.dumps({"embed_documents":[name], "method":"check"}), ws)["embed"] == "ok":
            self._ok = True
        return self._ok
    
    def try_load_in_remote(self):
        try:
            self._ok = False
            name = self.name
            if "/" in name:
                name = name.rsplit("/",1)[-1]
                
            ws = create_connection(f"ws://{self.remote_host}:15000")
            user_id = md5(time.asctime().encode()).hexdigest()
            TODAY = datetime.datetime.now()
            PASSWORD = "ADSFADSGADSHDAFHDSG@#%!@#T%DSAGADSHDFAGSY@#%@!#^%@#$Y^#$TYDGVDFSGDS!@$!@$" + f"{TODAY.year}-{TODAY.month}"
            ws.send(json.dumps({"user_id":user_id, "password":PASSWORD}))
            res = ws.recv()
            if res != "ok":
                print(colored("[info]:","yellow") ,res)
                raise Exception("password error")
            if self.send_and_recv(json.dumps({"embed_documents":[name], "method":"load"}), ws)["embed"] == "ok":
                self._ok = True
                return True
            return False
        except Exception as e:
            raise e
        finally:
            ws.close()

    def show_remote_models(self):
        try:
            name = self.name
            if "/" in name:
                name = name.rsplit("/",1)[-1]
                
            ws = create_connection(f"ws://{self.remote_host}:15000")
            user_id = md5(time.asctime().encode()).hexdigest()
            TODAY = datetime.datetime.now()
            PASSWORD = "ADSFADSGADSHDAFHDSG@#%!@#T%DSAGADSHDFAGSY@#%@!#^%@#$Y^#$TYDGVDFSGDS!@$!@$" + f"{TODAY.year}-{TODAY.month}"
            ws.send(json.dumps({"user_id":user_id, "password":PASSWORD}))
            res = ws.recv()
            if res != "ok":
                print(colored("[info]:","yellow") ,res)
                raise Exception("password error")
            return self.send_and_recv(json.dumps({"embed_documents":[name], "method":"show"}), ws)["embed"]
        except Exception as e:
            raise e
        finally:
            ws.close()

    def __call__(self, args: List[str]) -> Any:
        if isinstance(args, str):
            args = [args]
        assert isinstance(args, (list, tuple,Iterable,))
        if not self._ok:
            self.check()

        if not self._ok :
            raise Exception("remote's service no such model deployed"+self.name)
        ws = create_connection(f"ws://{self.remote_host}:15000")
        user_id = md5(time.asctime().encode()).hexdigest()
        TODAY = datetime.datetime.now()
        PASSWORD = "ADSFADSGADSHDAFHDSG@#%!@#T%DSAGADSHDFAGSY@#%@!#^%@#$Y^#$TYDGVDFSGDS!@$!@$" + f"{TODAY.year}-{TODAY.month}"
        ws.send(json.dumps({"user_id":user_id, "password":PASSWORD}))
        # time.sleep(0.5)
        res = ws.recv()
        if res != "ok":
            print(colored("[info]:","yellow") ,res)
            raise Exception("password error")
        name = self.name
        if "/" in name:
            name = name.rsplit("/",1)[-1]
            
        data = json.dumps({"embed_documents":args, "method": name})
        try:
            msg = self.send_and_recv(data, ws)
            return msg["embed"]
        except Exception as e:
            print(e)
            import ipdb;ipdb.set_trace()