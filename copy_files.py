import paramiko
from paramiko import SSHClient
from scp import SCPClient
import os
import click

@click.argument('ssh_key_path')
@click.argument('remote_nodes')
@click.argument('app_module')
@click.argument('remote_path')
def copy_file(ssh_key_path, remote_nodes, app_module, remote_path):

    def copy_node(remote_node):
        ssh = SSHClient() 
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_node, username='root', key_filename=ssh_key_path)
    
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(app_module, remote_path)
    
    for node in remote_nodes.split(","):
        print(node)
        copy_node(node.strip())


if __name__ == "__main__":
    copy_file()
