import asyncio
import os
from infrahub_sdk import InfrahubClient


async def get_device_configs():
    clab_directory_path = "./generated-configs/clab"
    config_directory_path = "./generated-configs/clab/configs/startup"
    if not os.path.exists(clab_directory_path):
        os.makedirs(clab_directory_path)
    if not os.path.exists(config_directory_path):
        os.makedirs(config_directory_path)


    client = InfrahubClient()
    devices = await client.all(kind="DcimDevice")

    for device in devices:
        await device.artifacts.fetch()
        for artifact in device.artifacts.peers:
            if artifact.display_label == "startup-config":
                artifact = await device.artifact_fetch(artifact.display_label)
                with open(f"{config_directory_path}/{device.name.value}.cfg", "w") as file:
                    file.write(artifact)
            if str(artifact.display_label).startswith("Containerlab Topology"):
                artifact = device.artifact_fetch(artifact.display_label)
                with open(f"{clab_directory_path}/topology.yml", "w") as file:
                    file.write(artifact)


asyncio.run(get_device_configs())