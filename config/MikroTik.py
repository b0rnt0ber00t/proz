# specific import library
from json import load
from tqdm import tqdm
from flask import Flask, request, jsonify
from netmiko import ConnectHandler, NetMikoTimeoutException

# Automation
def provision():
    with open('json/provision/script.json') as json_script:
        script_json = load(json_script)
        for script_jsons in script_json:
            print('-'*75)
            print('Connecting to ' + script_jsons['ip'] + ' ...')
            try:
                ssh = ConnectHandler(host=script_jsons['ip'], device_type="mikrotik_routeros", username=script_jsons['username'], password=script_jsons['password'], port=script_jsons['port'], timeout=10)
            except (NetMikoTimeoutException) as e:
                print("error : " + e)
            script_txt = open('script/provision/script.txt')
            for script_txts in tqdm(script_txt, ascii=True, desc=script_jsons['name'], unit=' config', dynamic_ncols=True):
                ssh.send_config_set(script_txts)
            print('Disconnecting from ' + script_jsons['ip'] + ' ...')
            ssh.disconnect()
            print('-'*75)

# ztp
def ztp():
    with open('json/ztp/script.json') as json_script:
        script_json = load(json_script)
        for script_jsons in script_json:
            print('-'*75)
            print('Connecting to ' + script_jsons['ip'] + ' ...')
            try:
                ssh = ConnectHandler(host=script_jsons['ip'], device_type="mikrotik_routeros", username=script_jsons['username'], password=script_jsons['password'], port=script_jsons['port'], timeout=10)
            except (NetMikoTimeoutException) as e:
                print("error : " + e)
            script_txt = open('script/ztp/listen.txt')
            for script_txts in tqdm(script_txt, ascii=True, desc=script_jsons['name'], unit=' config', dynamic_ncols=True):
                out = ssh.send_config_set(script_txts)
                print(out)
            print('Disconnecting from ' + script_jsons['ip'] + ' ...')
            ssh.disconnect()
            print('-'*75)
        
    # Flask api
    app = Flask(__name__)

    @app.route('/config', methods=['POST'])
    def config():
        dats = request.get_json()

        ip = dats['ip_router']
        username = 'admin'
        password = ''
        port = 22
        
        print('-'*75)
        print('Connecting to ' + ip + ' ...')
        try:
            ssh = ConnectHandler(host=ip, device_type="mikrotik_routeros", username=username, password=password, port=port, timeout=10)
        except (NetMikoTimeoutException) as e:
            e = str(e)
            return("error :" + e)
            print("error : " + e)
        script_txt = open('script/ztp/script.txt')
        for script_txts in script_txt:
            print('Sending : ' + script_txts.replace('\n', ''))
            ssh.send_config_set(script_txts)
        print('Disconnecting from ' + ip + ' ...')
        ssh.disconnect()
        print('-'*75)
        
        data = {'status':'ok'}

        return jsonify(data)
    
    # Run flask API
    app.run(host='0.0.0.0', debug=False)
    
