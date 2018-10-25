import docker 
import compilers
import os
import static_testing
client = docker.from_env()     


def build_image():

    for i in range(1, len(compilers.compilers)+1):
        dockerFileText = compilers.compilers["1"]
        dockerFile = open('dfile/Dockerfile', 'w', encoding = 'utf-8') #Dockerfile for gcc
        dockerFile.write(dockerFileText)
        dockerFile.close()
        client.images.build(path="dfile", tag = "gcc14")


def main():

    build_image()

    print('''AVAILABLE LANGUAGE: 
                1: C++ ''')
    
    lang = input('SELECT LANGUAGE:')

    if lang == 'C++':

        print('''AVAILABLE STANDARD:
                1: std98
                2: std03
                3: std11
                4: std14
                5: std17''')
        
        std = input('SELECT STANDARD:')

        srcPath = os.getcwd() + '/output'
        if std == 'std98':
            containerObj = client.containers.run(image="gcc14", 
            command=["/bin/bash", "-c", "cd /tmp; g++ -std=c++98 in.cpp 2> out.txt"], 
            volumes={srcPath:{'bind': '/tmp', 'mode':'rw'}}, detach=True, remove=True)
        static_testing.staticTest(srcPath)



if __name__=="__main__" : main()
