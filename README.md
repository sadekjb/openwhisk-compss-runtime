## COMPSs based runtime OpenWhisk action
We embedded COMPSs installation within OW specific action. The COMPSs based OW action can be used as master and worker or as master only by specifying remote worker, and the action code will adapt accordingly.  
### Build COMPSs image:
	docker build -f <path-to-docker-file>/Dockerfile -t comps /opt/COMPSs
	docker tag comps <repo-name>/<name>:version
	docker push <repo-name>/<name>
#### Prebuilt image with comps 2.2: 
	sadek/compss:3.7
### Create COMPSs OpenWhisk action:
	zip -r action_files.zip __main__.py <comps_app.py>
	wsk action update -i compss_3.7 --docker <repo-name>/<name>:version -m 512 -t 300000 action_files.zip
### Invoke COMPSs OW action local worker node example:
	wsk action invoke compss_3.7 --param app_args 2 --param outfile 'counter' --param compsapppath simple.py -br
### Invoke COMPSs OW action remote worker example:
	wsk action invoke compss_3.7 --param app_args 2 --param outfile 'counter' --param compsapppath simple.py -br
## Copy COMPSs tasks files to workers
copy_files.py is a tool built to ease the distribution of compss app files to workers
### Usage example:
	python copy_files.py ./comps-runtime/.ssh/id_rsa 'x.x.x.x, y.y.y.y' ./simple1.py /usr/local   
