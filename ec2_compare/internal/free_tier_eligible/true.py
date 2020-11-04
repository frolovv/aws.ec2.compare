
# Automatically generated

# pylint: disable=all
get = [{'InstanceType': 't1.micro', 'CurrentGeneration': False, 'FreeTierEligible': True, 'SupportedUsageClasses': ['on-demand'], 'SupportedRootDeviceTypes': ['ebs'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['i386', 'x86_64']}, 'VCpuInfo': {'DefaultVCpus': 1, 'DefaultCores': 1, 'DefaultThreadsPerCore': 1, 'ValidCores': [1], 'ValidThreadsPerCore': [1]}, 'MemoryInfo': {'SizeInMiB': 627}, 'InstanceStorageSupported': False, 'EbsInfo': {'EbsOptimizedSupport': 'unsupported', 'EncryptionSupport': 'unsupported'}, 'NetworkInfo': {'NetworkPerformance': 'Very Low', 'MaximumNetworkInterfaces': 2, 'Ipv4AddressesPerInterface': 2, 'Ipv6AddressesPerInterface': 0, 'Ipv6Supported': False, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': False}, {'InstanceType': 't2.micro', 'CurrentGeneration': True, 'FreeTierEligible': True, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs'], 'BareMetal': False, 'Hypervisor': 'xen', 'ProcessorInfo': {'SupportedArchitectures': ['i386', 'x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 1, 'DefaultCores': 1, 'DefaultThreadsPerCore': 1, 'ValidCores': [1], 'ValidThreadsPerCore': [1]}, 'MemoryInfo': {'SizeInMiB': 1024}, 'InstanceStorageSupported': False, 'EbsInfo': {'EbsOptimizedSupport': 'unsupported', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'Low to Moderate', 'MaximumNetworkInterfaces': 2, 'Ipv4AddressesPerInterface': 2, 'Ipv6AddressesPerInterface': 2, 'Ipv6Supported': True, 'EnaSupport': 'unsupported'}, 'PlacementGroupInfo': {'SupportedStrategies': ['partition', 'spread']}, 'HibernationSupported': True, 'BurstablePerformanceSupported': True, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': True}] # noqa: E501

def get_instances_list() -> list:
    '''Returns list EC2 instances with FreeTierEligible = True .'''
    # pylint: disable=all
    return get

