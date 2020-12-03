
# Automatically generated

# pylint: disable=all
get = [{'InstanceType': 'g2.2xlarge', 'CurrentGeneration': False, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.6}, 'VCpuInfo': {'DefaultVCpus': 8, 'DefaultCores': 4, 'DefaultThreadsPerCore': 2, 'ValidCores': [1, 2, 3, 4], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 15360}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 60, 'Disks': [{'SizeInGB': 60, 'Count': 1, 'Type': 'ssd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'supported', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'Moderate', 'MaximumNetworkInterfaces': 4, 'Ipv4AddressesPerInterface': 15, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'GpuInfo': {'Gpus': [{'Name': 'K520', 'Manufacturer': 'NVIDIA', 'Count': 1, 'MemoryInfo': {'SizeInMiB': 4096}}], 'TotalGpuMemoryInMiB': 4096}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': False}, {'InstanceType': 'g2.8xlarge', 'CurrentGeneration': False, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.6}, 'VCpuInfo': {'DefaultVCpus': 32, 'DefaultCores': 16, 'DefaultThreadsPerCore': 2, 'ValidCores': [2, 4, 6, 8, 10, 12, 14, 16], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 61440}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 240, 'Disks': [{'SizeInGB': 120, 'Count': 2, 'Type': 'ssd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'unsupported', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'High', 'MaximumNetworkInterfaces': 8, 'Ipv4AddressesPerInterface': 30, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'GpuInfo': {'Gpus': [{'Name': 'K520', 'Manufacturer': 'NVIDIA', 'Count': 4, 'MemoryInfo': {'SizeInMiB': 4096}}], 'TotalGpuMemoryInMiB': 16384}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': False}]  # noqa: E501


def get_instances_list() -> list:
    '''Returns list EC2 instances with InstanceType = g2 .'''
    # pylint: disable=all
    return get