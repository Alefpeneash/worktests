import docker
from kubernetes import client, config
import kubernetes
config.load_kube_config()
# config.load_incluster_config()


v1 = client.CoreV1Api()

print("Listing pods with their IPs:")

ret = v1.list_namespaced_pod(namespace="default")
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

v2 = client.ExtensionsV1beta1Api()
api_instance = client.CoreV1Api()

# DELETING
# v2 = client.ExtensionsV1beta1Api()
# api_instance.delete_namespaced_service(name="web", namespace="default",body=client.V1DeleteOptions())
# v1.delete_namespaced_pod(name="web", namespace="default", body=client.V1DeleteOptions())
# v2.delete_namespaced_deployment(name="web", namespace="default", body=client.V1DeleteOptions(
#             propagation_policy='Foreground',
#             grace_period_seconds=5))




# /////////////////////////////////////////////////////
# /////////////////////////////////////////////////////
# CREATING DEPLOYMENT V1
container = client.V1Container(
    name = "web",
    image = "maximbaryshnikov/web:v1",
    ports = [client.V1ContainerPort(container_port=8080)]
)
template = client.V1PodTemplateSpec(
    metadata=client.V1ObjectMeta(labels={"app": "web"}),
    spec=client.V1PodSpec(containers=[container])
)
spec = client.ExtensionsV1beta1DeploymentSpec(
    replicas = 0,
    template = template
)
# !! всё создаётся, но получается какая-то херня, сервис не связан с подом и вообще кал. Ниже попытка создавать под вместе с деплойментом (так нужно)
# container=client.V1Container(name="web", image="maximbaryshnikov/web:v1", args=["sleep", "3600"])
# container.image="maximbaryshnikov/web:v1"
# container.args=["sleep", "3600"]
# container.name="web"
pod=client.V1Pod()
# spec=client.V1PodSpec(containers=[container])
# pod.metadata=client.V1ObjectMeta(name="web")
pod.spec = spec


deployment =  client.ExtensionsV1beta1Deployment(
    api_version="extensions/v1beta1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="web"),
    spec=spec
)
v1.create_namespaced_pod(namespace="default",body=pod)

extension = client.ExtensionsV1beta1Api()

api_response = extension.create_namespaced_deployment(
    body=deployment,
    namespace="default"
)
print("Deployment created. status='%s'" % str(api_response.status))
# -----------------------------------------------------------------

# # CREATING POD 
# container=client.V1Container(name="web", image="maximbaryshnikov/web:v1", args=["sleep", "3600"])
# container.image="maximbaryshnikov/web:v1"
# container.args=["sleep", "3600"]
# container.name="web"
# pod=client.V1Pod()
# spec=client.V1PodSpec(containers=[container])
# pod.metadata=client.V1ObjectMeta(name="web")
# pod.spec = spec
# v1.create_namespaced_pod(namespace="default",body=pod)
# # -----------------------------------------------------

# # CREATING SERVICE
# service = client.V1Service()

# service.api_version = "v1"
# service.kind = "Service"
# service.metadata = client.V1ObjectMeta(name="web")

# spec = client.V1ServiceSpec()
# spec.selector = {"app": "web"}
# spec.ports = [client.V1ServicePort(protocol="TCP", port=8080)]
# service.spec = spec
# api_instance.create_namespaced_service(namespace="default", body=service)
# ------------------------------------
# /////////////////////////////////////////////////////
# /////////////////////////////////////////////////////




# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

# client = docker.from_env()
# containers = client.containers()
# images = client.images()

# buildResponse = [line for line in client.build(
#     path="./", forcerm=True, rm=True, nocache=True, stream=True, tag='maximbaryshnikov/web:v1'
# )]
# buildResponse

# pushResponse = [line for line in client.push('maximbaryshnikov/web:v1', stream=True)]
# pushResponse
