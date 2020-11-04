
# Automatically generated

# pylint: disable=all
get = [{'InstanceType': 'p4d.24xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs'], 'BareMetal': False, 'Hypervisor': 'nitro', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 3.0}, 'VCpuInfo': {'DefaultVCpus': 96, 'DefaultCores': 48, 'DefaultThreadsPerCore': 2, 'ValidCores': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 1179648}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 8000, 'Disks': [{'SizeInGB': 1000, 'Count': 8, 'Type': 'ssd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': '4x 100 Gigabit', 'MaximumNetworkInterfaces': 60, 'Ipv4AddressesPerInterface': 50, 'Ipv6AddressesPerInterface': 50, 'Ipv6Supported': True, 'EnaSupport': 'required'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': False}] # noqa: E501

def get_instances_list() -> list:
    '''Returns list EC2 instances with InstanceType = p4d .'''
    # pylint: disable=all
    return get

