import argparse,os;
from core.basic import *;
from core.config import *;
import core.server as Web;
class Allocate:
    def __init__(self,args:argparse.Namespace) -> None:
        self.args = vars(args);
    
    def start(self):
        if self.args.get('init'):
            if self.args['work']:
                dirs = self.args['work'];
                if useableDir(dirs):
                    w2Config('config.yaml','work_space',dirs)
                else:
                    qcWarning('dir couldn\'t use!');
            else:
                qcWarning('plz input your work dir!');
                return 0;
        else:
            mode = self.args.get('mode');
            if mode == 'server':
                port = self.args.get('port')
                if port:
                    Web.run(port);
                else:
                    Web.run();
                pass;
            elif mode == 'console':
                pass;
            else:
                pass;
            pass;

    