import os
import shutil
target   = 'tfboard.sh' 
def register_service(target):
    filename = os.path.basename(target)
    name     = os.path.splitext(target)[0]
    current_dir = os.path.abspath('./')
    service_dir = '/etc/systemd/system/'
    service_name = name+'.service'
    service_path = os.path.join(current_dir,service_name)

    services = [file for file in os.listdir(service_dir) if file.endswith('.service')]
    if name+'.service' in services:
        print(f'{name}.service already exists in {service_dir}')
        if os.path.exists(service_path):
            os.remove()
    else:
        print(f'{name}.service doesn\'t exists in {service_dir} ')

    if os.path.exists(service_path):
        shutil.copy(service_path,os.path.join(service_dir,service_name) )

register_service(target)