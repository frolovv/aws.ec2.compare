
# Automatically generated

# pylint: disable=all
get = [{'InstanceType': 'm3.medium', 'CurrentGeneration': False, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 1, 'DefaultCores': 1, 'DefaultThreadsPerCore': 1, 'ValidCores': [1], 'ValidThreadsPerCore': [1]}, 'MemoryInfo': {'SizeInMiB': 3840}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 4, 'Disks': [{'SizeInGB': 4, 'Count': 1, 'Type': 'ssd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'unsupported', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'Moderate', 'MaximumNetworkInterfaces': 2, 'Ipv4AddressesPerInterface': 6, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': True, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': True}, {'InstanceType': 'm3.large', 'CurrentGeneration': False, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 2, 'DefaultCores': 2, 'DefaultThreadsPerCore': 1, 'ValidCores': [1, 2], 'ValidThreadsPerCore': [1]}, 'MemoryInfo': {'SizeInMiB': 7680}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 32, 'Disks': [{'SizeInGB': 32, 'Count': 1, 'Type': 'ssd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'unsupported', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'Moderate', 'MaximumNetworkInterfaces': 3, 'Ipv4AddressesPerInterface': 10, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': True, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': True}, {'InstanceType': 'm3.xlarge', 'CurrentGeneration': False, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 4, 'DefaultCores': 4, 'DefaultThreadsPerCore': 1, 'ValidCores': [1, 2, 3, 4], 'ValidThreadsPerCore': [1]}, 'MemoryInfo': {'SizeInMiB': 15360}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 80, 'Disks': [{'SizeInGB': 40, 'Count': 2, 'Type': 'ssd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'supported', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'High', 'MaximumNetworkInterfaces': 4, 'Ipv4AddressesPerInterface': 15, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': True, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': True}, {'InstanceType': 'm3.2xlarge', 'CurrentGeneration': False, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs', 'instance-store'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 8, 'DefaultCores': 4, 'DefaultThreadsPerCore': 2, 'ValidCores': [1, 2, 3, 4], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 30720}, 'InstanceStorageSupported': True, 'InstanceStorageInfo': {'TotalSizeInGB': 160, 'Disks': [{'SizeInGB': 80, 'Count': 2, 'Type': 'ssd'}]}, 'EbsInfo': {'EbsOptimizedSupport': 'supported', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'High', 'MaximumNetworkInterfaces': 4, 'Ipv4AddressesPerInterface': 30, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': True, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': True}]  # noqa: E501


def get_instances_list() -> list:
    '''Returns list EC2 instances with InstanceType = m3 .'''
    # pylint: disable=all
    return get
