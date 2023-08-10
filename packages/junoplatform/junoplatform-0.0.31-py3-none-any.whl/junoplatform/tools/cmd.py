"""junoplatform.tools.cmd.py: junocli cmd implementation"""
__author__      = "Bruce.Lu"
__email__       = "lzbgt@icloud.com"
__time__ = "2023/07/20"


import click
import os
import yaml
import logging
import requests
import shutil
import traceback
import yaml
import uuid
import json
from io import StringIO
from pylint.lint import Run
from pylint.reporters.text import TextReporter
from typing import List
import zipfile
from junoplatform.io.utils import driver_cfg, get_package_path, api_url

import junoplatform
from junoplatform.meta.decorators import auth
from typing import Optional, Mapping
import collections
from decouple import config as dcfg

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s - %(message)s')
        
class CMDBase(object):
    def __init__(self):
        self.juno_dir = os.path.expanduser('~') + '/.juno'
        self.juno_file = self.juno_dir +  '/config.yaml'
        self.juno_cfg = {}
        try:
            self.juno_cfg = yaml.safe_load(open(self.juno_file, 'r'))
        except:
            pass

class OrderedGroup(click.Group):
    def __init__(self, name: Optional[str] = None, commands: Optional[Mapping[str, click.Command]] = None, **kwargs):
        super(OrderedGroup, self).__init__(name, commands, **kwargs)
        #: the registered subcommands by their exported names.
        self.commands = commands or collections.OrderedDict()

    def list_commands(self, ctx: click.Context) -> Mapping[str, click.Command]:
        return self.commands

@click.group(cls=OrderedGroup)
@click.pass_context
def main(ctx, ):
    ctx.obj = CMDBase()

pass_base = click.make_pass_decorator(CMDBase)


@main.command()
@click.option("-u", "--username", prompt=True)
@click.option("-p", "--password", prompt=True, hide_input=True,
)
@pass_base
def login(base:CMDBase, username, password):
    '''must login success before all other commands
    '''
    auth = {"username": username, "password": password}
    logging.info(f"login at {api_url}")
    r = requests.post(f'{api_url}/login', data=auth, headers = {'Content-Type': 'application/x-www-form-urlencoded'})
    if r.status_code != 200:
        if 'detail' in r.json():
            detail = r.json()['detail']
            logging.error(f"login error: {detail}")
            return
        else:
            logging.error(f"login error: {r.status_code}")
    token = r.json()['access_token']
    data = {"auth": auth, "token": token}

    with open(base.juno_file, 'w') as f:
        f.write(yaml.dump(data)) 
    logging.info("successfully logged in")

@main.command()
@click.argument('name')
@click.argument('plant')
@click.argument('module')
@pass_base
@auth
def init(base, name, plant, module):
    '''create an algo module with project NAME
    '''
    home = os.path.dirname(junoplatform.__file__)
    src = f"{home}/templates/main.py"
    try:
        os.makedirs(name, exist_ok=False)
        shutil.copy2(src, name)
        doc = {"name": name, "version": "0.0.0", "author": os.getlogin(), "description": "template algo project", "plant": plant, "module": module}
        yaml.dump(doc, open(f"{name}/project.yml", "w"), sort_keys=False)
        input = {
        "tags": [
            "AI-T20502_DIS",
            "AI-T20501_DIS"
        ],
        "items": 1440,
        "sched_interval": 5
        }
        
        if plant == 'yudai':
            input["tags"] = ['AI_AT-P10503-DISP', 'COD2']

        
        if plant == 'yulin':
            input['tags'] = ['通道 1.设备 1.opc.group.3004FV00306_AI.PV', '通道 1.设备 1.opc.group.3007LIT00202_AI.PV']

        config = {"key1": 1, "key2": [1,2]}

        json.dump(input, open(f"{name}/input.json", "w"), sort_keys=False)
        json.dump(config, open(f"{name}/config.json", "w"), sort_keys=False)
    except Exception as e:
        msg = traceback.format_exc()
        logging.error(f"failed to create project {name}: {e}")

@main.command()
@pass_base
@auth
def run(base):
    '''run a package locally for testing
    '''
    os.system("python main.py")

@main.group(cls=OrderedGroup)
@click.pass_context
def package(ctx):
    pass

@main.group(cls=OrderedGroup)
@click.pass_context
def deployment(ctx):
    pass

@package.command()
@click.argument('conf_file', default="config.json")
@click.option('-t', '--tag', type=click.Choice(['algo', 'config', 'ac', 'other']), required = True)
@click.option('-m', '--message', required = True)
@click.option('-i','--input', help = "the path of input spec file", default="input.json")
@pass_base
@auth
def pack(base, conf_file,  tag, message, input):
    ''' make a package and get a package_id
    '''
    try:
        lint = StringIO()  # Custom open stream
        reporter = TextReporter(lint)
        Run(["main.py"], reporter=reporter, exit=False)
        errors = lint.getvalue().split("\n")
        for x in errors:
            if "failed"  in x or "fatal" in x:
                logging.error(x)
                logging.info("fix the error above and redo package")
                exit(1)

        package_id = uuid.uuid4().hex
        driver_cfg['package_id'] = package_id

        def parse_version(s:str) -> List[int]|None:
            v = s.split(".")
            if len(v) != 3:
                return None
            try:
                return [int(x) for x in v]
            except:
                return None
            
        def inc_version(v: str, t:type):
            v = parse_version(v)
            if tag == 'algo':
                v[0] +=1
                driver_cfg['tag'] = 'algo'
            elif tag == 'config':
                v[1] +=1
                driver_cfg['tag'] = 'config'
            elif tag == 'ac':
                v[0] +=1
                v[1] +=1
                driver_cfg['tag'] = 'ac'
            else:
                v[2] +=1
            driver_cfg["version"] = ".".join([str(x) for x in v])

        if "version" not in driver_cfg:
            driver_cfg["version"] = "0.0.0"
        try:
            inc_version(driver_cfg["version"], tag)
        except:
            logging.error(f"invalid version: {driver_cfg['version']}")
            exit(1)

        driver_cfg["message"] = message
            
        with open('project.yml', 'w') as f:
            yaml.safe_dump(driver_cfg, f, sort_keys=False)

        logging.info(f"pack success(new can be found in project.yml):\n\tplant: {driver_cfg['plant']}, \
                     module: {driver_cfg['module']}, conf: {conf_file}\n\t{tag}: {message}\
                     \n\tid: {package_id}\n\tversion: {driver_cfg['version']}")

        # dist
        os.makedirs("dist", exist_ok=True)
        module = driver_cfg['module']
        plant = driver_cfg['plant']
        arch = f'dist/{plant}-{module}-{driver_cfg["package_id"]}.zip'
        with zipfile.ZipFile(arch, 'w') as f:
            for root, dirs, files in os.walk('./'):
                if root[-4:] == 'dist':
                    continue
                for file in files:
                    p = os.path.join(root, file)
                    f.write(p)
                    logging.info(f"added: {p}")
        logging.info(f"package stored in: {arch}")

    except Exception as e:
        logging.error(e)

@package.command()
@click.argument('package_id', default="", required=False)
@pass_base
@auth
def build(base, package_id):
    '''build a package only (no deploy action)
    '''
    if not package_id:
        package_id = driver_cfg["package_id"]
    
    api = f"{api_url}/package"
    logging.info(f"build package {package_id} to {api}")
    papath = get_package_path(driver_cfg, package_id)

    logging.info(base.juno_cfg['token'])
    
    r = requests.post(api, files = {'file': (f'{package_id}.zip', open(papath, 'rb'), 'application/zip')}, headers={"Authorization": f"Bearer {base.juno_cfg['token']}"})
    if r.status_code != 200:
        msg = f"faild upload package {package_id} "
        if "detail" in r.json():
            msg += r.json()["detail"]
        logging.error(msg)
    else:
        logging.info(f"successfully upload package {package_id}")

@package.command()
@click.argument('package_id', required=False)
@pass_base
@auth
def rebuild(base, package_id):
    if not package_id:
        package_id=driver_cfg["package_id"]
    api = f"{api_url}/package"
    params = {"package_id": package_id}
    r = requests.patch(api, params=params, headers={"Authorization": f"Bearer {base.juno_cfg['token']}"})
    if r.status_code != 200:
        msg = f"faild rebuild package in cloud:  {package_id} "
        if "detail" in r.json():
            msg += r.json()["detail"]
        logging.error(msg)
    else:
        logging.info(f"successfully summit recompile package request: {package_id}")

statusmap = {
    0: "building",
    1: "ready",
    2: "failed"
}


def info_package(token:str, package_id:str):
    '''info packages
    '''
    api = f"{api_url}/package/info"
    params = {}
    params["package_id"] = package_id
    r = requests.get(api, params=params, headers={"Authorization": f"Bearer {token}"})
    if r.status_code != 200:
        msg = f"faild fetch packages "
        if "detail" in r.json():
            msg += r.json()["detail"]
        return msg
    else:
        data = r.json()
        data["config"] = json.loads(data["config"])
        data["status"] = statusmap.get(data["status"])
        return data

@package.command()
@click.argument('package_id', required=True)
@pass_base
@auth
def info(base, package_id):
    '''info packages
    '''
    if not package_id:
        package_id = driver_cfg["package_id"]

    res = info_package(base.juno_cfg['token'], package_id)
    if isinstance(res, str):
        logging.error(res)
    else:
        logging.info(json.dumps(res, indent=2))


@package.command()
@click.argument('package_id', required=True)
@pass_base
@auth
def clone(base, package_id):
    '''clone package
    '''
    if not dcfg("ENABLE_DL", 0, cast=int):
        logging.error("package download is not enabled")

    api = f"{api_url}/package"
    params = {}
    params["package_id"] = package_id
    r = requests.get(api, params=params, headers={"Authorization": f"Bearer {base.juno_cfg['token']}"})
    if r.status_code != 200:
        msg = f"faild fetch packages "
        if "detail" in r.json():
            msg += r.json()["detail"]
        logging.error(msg)
    else:
        with open(f"{package_id}.zip", "wb") as f:
            for c in r.iter_content(chunk_size=2048):
                if c:
                    f.write(c)

def list_packages(token, plant, module):
    '''list packages
    '''
    api = f"{api_url}/packages"
    params = {}
    if plant:
        params["plant"] = plant
    if module:
        params["module"] = module

    r = requests.get(api, params=params, headers={"Authorization": f"Bearer {token}"})
    if r.status_code != 200:
        msg = f"faild fetch packages "
        if "detail" in r.json():
            msg += r.json()["detail"]
        return msg
    else:
        res = []
        for x in r.json():
            x["config"] = json.loads(x["config"])
            x["status"] = statusmap.get(x["status"])
            res.append(x)
        res.reverse()
        return res

@package.command()
@click.argument('plant', required=False)
@click.argument('module', required=False)
@pass_base
@auth
def list(base, plant, module):
    '''list packages
    '''
    res = list_packages(base.juno_cfg['token'], plant, module)
    if isinstance(res, str):
        logging.error(res)
    else:
        logging.info(json.dumps(res, indent=2))

def deploy_package(token, package_id:str, kind:int):
    api = f"{api_url}/deploy"
    params = {}
    params["package_id"] = package_id
    params["kind"]= kind
    r = requests.post(api, params=params, headers={"Authorization": f"Bearer {token}"})
    if r.status_code != 200:
        msg = f"faild fetch packages "
        if "detail" in r.json():
            msg += r.json()["detail"]
        return msg
    else:
        return None

@package.command()
@click.argument('package_id', required=False)
@pass_base
@auth
def deploy(base, package_id):
    '''deploy package
    '''
    if not package_id:
        package_id = driver_cfg["package_id"]
    s = deploy_package(base.juno_cfg['token'], package_id, kind=0)
    if s:
        logging.error(s)
    else:
        logging.info(f"deploy of package: {package_id} submitted.\nstatus can be viewed by run:\n\tjunocli deployment status {package_id}")
 
@package.command()
@click.argument('package_id', required=False)
@pass_base
@auth
def rollback(base, package_id):
    '''rollback a package to previous version or specific id[optional]
    '''
    token = base.juno_cfg['token']
    if not package_id:
        package_id = driver_cfg["package_id"]
    res = info_package(token, package_id=package_id)
    if isinstance(res, str):
        logging.error(res)
    else:
        res = list_packages(token, plant=res["plant"], module=res["module"])
        if isinstance(res, str):
            logging.error(str)
        else:
            res.reverse()
            target_idx = -1
            for idx, x in enumerate(res):
                if x["package_id"] == package_id:
                    target_idx = idx +1

            if target_idx < len(res):
                new_id = res[target_idx]["package_id"]
                res = deploy_package(token, new_id , 1)
                if not res:
                    logging.info(f"rollback from {package_id} to {new_id} submitted")
                else:
                    logging.error(res)
            else:
                logging.error(f"no available package to rollback for {package_id}")


def list_deployments(base, plant, module, user, package_id):
    ''' list deoployments
    '''
    api = f"{api_url}/deploys"
    params = {}
    params["package_id"] = package_id
    params["plant"] = plant
    params["module"] = module

    if user == "me":
        params["username"] = params["username"] = os.getlogin()
    else:
        params["username"] = user

    logging.info(params)

    r = requests.get(api, params=params, headers={"Authorization": f"Bearer {base.juno_cfg['token']}"})
    if r.status_code != 200:
        msg = f"faild fetch packages "
        if "detail" in r.json():
            msg += r.json()["detail"]
        return msg
    else:
        data = r.json()
        data.reverse()
        return data

@deployment.command()
@click.option("-p", "--plant", default="")
@click.option("-m", "--module", default="")
@click.option("-i", "--package_id", default="")
@click.option("-u", "--user", default="")
@pass_base
@auth
def list(base, plant, module, user, package_id):
    ''' list deoployments
    '''
    res = list_deployments(base, plant, module, user, package_id)
    if isinstance(res, str):
        logging.error(res)
    else:
        logging.info(json.dumps(res, indent=2))


@deployment.command()
@click.argument('deployment_id')
@pass_base
@auth
def status(base, plant, module):
    ''' check package status
    '''
    logging.info(f"TODO: status {id}")