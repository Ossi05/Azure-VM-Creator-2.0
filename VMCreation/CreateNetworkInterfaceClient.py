# 5 - Create the network interface client
def CreateNetworkInterfaceClient(network_client, vmData, subnet_result, ip_address_result):

    poller = network_client.network_interfaces.begin_create_or_update(vmData.resource_group_name,
        vmData.nic_name, 
        {
            "location": vmData.location,


            "ip_configurations": [ {
                "name": vmData.ip_config_name,

                "subnet": { "id": subnet_result.id },

                "public_ip_address": {"id": ip_address_result.id },
            }],
            'NetworkSecurityGroup': {
            'id': f'/subscriptions/{vmData.azure_id}/resourceGroups/{vmData.resource_group_name}/providers/Microsoft.Network/networkSecurityGroups/{vmData.nsg_name}'
            }
        }
    )

    nic_result = poller.result()

    print(f"Provisioned network interface client {nic_result.name}")

    return nic_result