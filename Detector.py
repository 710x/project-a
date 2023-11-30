import platform
import threading
import win32con
import win32file

class Detector:
    def __init__(self, path):
        self.is_windows = platform.system()=='Windows'
        self.path = path
        self.msg=[]
        self.mutex=threading.Lock()
        self.rename = ''
        self.hDir = win32file.CreateFile(self.path,win32con.GENERIC_READ,win32con.FILE_SHARE_READ|win32con.FILE_SHARE_WRITE|win32con.FILE_SHARE_DELETE,None,win32con.OPEN_EXISTING,win32con.FILE_FLAG_BACKUP_SEMANTICS,None)
        def f():
            if(self.is_windows):
                while True:self.add(win32file.ReadDirectoryChangesW(self.hDir,0x1000,False,win32con.FILE_NOTIFY_CHANGE_FILE_NAME|win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,None,None))
        if (self.is_windows): threading.Thread(target=f,daemon=True,name=f'Detector({path})').start()
    
    def get_path(self):
        return self.path
    
    def add(self,x):
        if(not self.is_windows):
            return
        def onCreated(file):
            for i in(i for i in range(len(self.msg)-1,-1,-1)if self.msg[i][1]==file):
                if self.msg[i][0]==2:
                    self.msg[i][0]=3
                    return
                break
            self.msg.append([1,file])
        def onDeleted(file):
            for i in(i for i in range(len(self.msg)-1,-1,-1)if self.msg[i][1]==file):
                if self.msg[i][0]==1:
                    del self.msg[i]
                    return
                if self.msg[i][0]==3:
                    del self.msg[i]
                    break
                temp=self.msg[i-1][1]
                del self.msg[i-1:i+1]
                return onDeleted(temp)
            self.msg.append([2,file])
        def onUpdated(file):
            for i in(i for i in range(len(self.msg)-1,-1,-1)if self.msg[i][1]==file):
                if self.msg[i][0]==1 or self.msg[i][0]==3:return
                if self.msg[i][0]==5:
                    temp=self.msg[i-1][1]
                    del self.msg[i-1:i+1]
                    onDeleted(temp)
                    return onCreated(file)
                break
            self.msg.append([3,file])
        def onRenamedFrom(file):
            self.rename=file
        def onRenamedTo(file):
            for i in range(len(self.msg)-1,-1,-1):
                if self.msg[i][1]==file:break
                if self.msg[i][1]==self.rename:
                    if self.msg[i][0]==1:
                        del self.msg[i]
                        return onCreated(file)
                    if self.msg[i][0]==3:
                        self.msg[i][0]=2
                        return onCreated(file)
                    if self.msg[i][0]==5:
                        self.rename=self.msg[i-1][1]
                        del self.msg[i-1:i+1]
                        if self.rename==file:return
                    break
            self.msg+=[[4,self.rename],[5,file]]
        with self.mutex:[{1:onCreated,2:onDeleted,3:onUpdated,4:onRenamedFrom,5:onRenamedTo}.get(i[0],lambda _:print(f'Unknown Operate {i}'))(i[1])for i in x]
            # 1:FILE_ACTION_ADDED 2:FILE_ACTION_REMOVED 3:FILE_ACTION_MODIFIED 4:FILE_ACTION_RENAMED_OLD_NAME 5:FILE_ACTION_RENAMED_NEW_NAME
            
    def get(self):
        if(not self.is_windows):
            return
        with self.mutex:ans,self.msg=self.msg,[]
        return ans
    
        