import xml.etree.ElementTree as ET
import subprocess
import os


def main(args):
    res_path = '/opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml'
    pro_path = '/opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml'

    cn_name = args.get('computenode', 'localhost')
    out_file = args.get('outfile')
    python_path = args.get('pythonpath', '.')
    comps_app_path = args.get('compsapppath', '.')

    def set_compute_node(path):
        tree = ET.parse(path)
        cnode = tree.find('ComputeNode')
        cnode.set('Name', cn_name)
        tree.write(path)
        
    if cn_name == 'localhost':
        completed_proc2 = subprocess.run(["/usr/sbin/service", "ssh", "start"])   
        #print(completed_proc2)
    else:
        set_compute_node(res_path)
        set_compute_node(pro_path)
     
    app_args = args.get('app_args')
    completed_proc = subprocess.run(["/opt/COMPSs/Runtime/scripts/user/runcompss", "--tracing=true",
                                     "--lang=python", "--python_interpreter=python2", 
                                     "--pythonpath=%s" % python_path, "./%s" % comps_app_path, str(app_args)], env={"JAVA_HOME": "/usr/lib/jvm/java-1.8.0-openjdk-amd64"})
    #print(completed_proc)
    #completed_proc1 = subprocess.run(["ls", "-al"]) 
    #print(completed_proc1)

    with open(out_file) as f:
        first_line = f.readline()
   
    return {"result": (int)(first_line.strip())}
