
# Automatically generated

# pylint: disable=all
get = [{'InstanceType': 'c1.medium', 'CurrentGeneration': False, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['i386', 'x86_64']}, 'VCpuInfo': {'DefaultVCpus': 2, 'DefaultCores': 2, 'DefaultThreadsPerCore': 1, 'ValidCores': [1, 2], 'ValidThreadsPerCore': [1]}, 'MemoryInfo': {'SizeInMiB': 1740}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 350, 'Disks': [{'SizeInGB': 350, 'Count': 1, 'Type': 'hdd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'unsupported', 'EncryptionSupport': 'unsupported'}, 'NetworkInfo': {'NetworkPerformance': 'Moderate', 'MaximumNetworkInterfaces': 2, 'Ipv4AddressesPerInterface': 6, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': False}, {'InstanceType': 'c1.xlarge', 'CurrentGeneration': False, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64']}, 'VCpuInfo': {'DefaultVCpus': 8, 'DefaultCores': 8, 'DefaultThreadsPerCore': 1, 'ValidCores': [1, 2, 3, 4, 5, 6, 7, 8], 'ValidThreadsPerCore': [1]}, 'MemoryInfo': {'SizeInMiB': 7168}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 1680, 'Disks': [{'SizeInGB': 420, 'Count': 4, 'Type': 'hdd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'supported', 'EncryptionSupport': 'unsupported'}, 'NetworkInfo': {'NetworkPerformance': 'High', 'MaximumNetworkInterfaces': 4, 'Ipv4AddressesPerInterface': 15, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': False}] # noqa: E501

def get_instances_list() -> list:
    '''Returns list EC2 instances with InstanceType = c1 .'''
    # pylint: disable=all
    return get

