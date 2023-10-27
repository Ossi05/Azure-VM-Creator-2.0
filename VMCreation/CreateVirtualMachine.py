from azure.mgmt.compute import ComputeManagementClient

# 6 - Create the virtual machine
def CreateVirtualMachine(credential, subscription_id, vmData, nic_result):
    print("Creating VM")

    # Get the management object for virtual machines
    compute_client = ComputeManagementClient(credential, subscription_id)

    print(f"Provisioning virtual machine {vmData.vm_name}; this operation might take a few minutes.")

    vm_parameters = {
        "location": vmData.location,
        "os_profile": {
            "computer_name": vmData.vm_name,
            "admin_username": vmData.username,
            "admin_password": vmData.password,
        },
        "hardware_profile": {
            "vm_size": vmData.RAMAmount,
        },
        "storage_profile": {
            "image_reference": {
                "publisher": vmData.publisher,
                "offer": vmData.offer,
                "sku": vmData.sku,
                "version": vmData.version,
            },
        },
        "network_profile": {
            "network_interfaces": [
                {
                    "id": nic_result.id,
                },
            ],
        },
    }
    try:
        poller = compute_client.virtual_machines.begin_create_or_update(
            vmData.resource_group_name,
            vmData.vm_name,
            vm_parameters
        )

        vm_result = poller.result()
        print(f"Provisioned virtual machine {vm_result.name}")
    except Exception as e:
        print(f"Error creating VM: {e}")
        quit()

    vnet_result = poller.result()