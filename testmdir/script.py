import docker

client = docker.Client(base_url='unix://var/run/docker.sock')
containers = client.containers()

cname = '/testjs_web_1'
check = False

if(len(containers) == 0):
    print("Error: not running any containers")
else:
    for c in containers:
        names = c['Names']
        for n in names:
            if(n == cname):
                check = True
    if(check):        
        container = client.inspect_container('testjs_web_1')
        envs = container['Config']['Env']
        for env in envs:
            print(env)
    else:
        print("Error: There is no container " + cname)

