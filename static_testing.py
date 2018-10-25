import docker
def staticTest(srcPath):
	cli = docker.DockerClient(base_url='unix://var/run/docker.sock')
	# srcPath is the path of the source file
	# detach = True is necessary for object returning
	containerObj = cli.containers.run('dcppcheck:latest', volumes={srcPath:{'bind':'/src','mode':'rw'}},  detach = True)
	stripChar = ['b', '\'', '"', '\n', ' '] # List of to be stripped characters
	statOut = str(containerObj.logs(stdout=True,stderr=False)).strip('b\'\\n')
	statError = str(containerObj.logs(stdout=False,stderr=True)).strip('b"\\n')

	statOutFile = open('statResult/staticOutput.txt', 'w', encoding = 'utf-8') #StaticTesting Output File
	statOutFile.write(statOut)
	statOutFile.close()

	statErrorFile = open('statResult/staticError.txt', 'w', encoding = 'utf-8')
	statErrorFile.write(statError);
	statErrorFile.close()

