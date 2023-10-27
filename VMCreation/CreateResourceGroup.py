from azure.mgmt.resource import ResourceManagementClient

# 1 - create a resource group
def CreateResourceGroup(credential, subscription_id, resource_group_name, location):

    # Create a Resource Management Client.
    resource_client = ResourceManagementClient(credential, subscription_id)

    # Create the resource group.
    try:
        rg_result = resource_client.resource_groups.create_or_update(resource_group_name,
            {
                "location": location
            }
        )

        print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

    except Exception as e:
        print(f"Error: {e}")
        quit()