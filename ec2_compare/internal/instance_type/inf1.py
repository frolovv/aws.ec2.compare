
# Automatically generated

# pylint: disable=all
get = [{'InstanceType': 'inf1.xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs'], 'BareMetal': False, 'Hypervisor': 'nitro', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 4, 'DefaultCores': 2, 'DefaultThreadsPerCore': 2, 'ValidCores': [2], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 8192}, 'InstanceStorageSupported': False, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'Up to 25 Gigabit', 'MaximumNetworkInterfaces': 4, 'Ipv4AddressesPerInterface': 10, 'Ipv6AddressesPerInterface': 10, 'Ipv6Supported': True, 'EnaSupport': 'required'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'InferenceAcceleratorInfo': {'Accelerators': [{'Count': 1, 'Name': 'Inferentia', 'Manufacturer': 'AWS'}]}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': False}, {'InstanceType': 'inf1.2xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs'], 'BareMetal': False, 'Hypervisor': 'nitro', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 8, 'DefaultCores': 4, 'DefaultThreadsPerCore': 2, 'ValidCores': [2, 4], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 16384}, 'InstanceStorageSupported': False, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': 'Up to 25 Gigabit', 'MaximumNetworkInterfaces': 4, 'Ipv4AddressesPerInterface': 10, 'Ipv6AddressesPerInterface': 10, 'Ipv6Supported': True, 'EnaSupport': 'required'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'InferenceAcceleratorInfo': {'Accelerators': [{'Count': 1, 'Name': 'Inferentia', 'Manufacturer': 'AWS'}]}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': False}, {'InstanceType': 'inf1.6xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs'], 'BareMetal': False, 'Hypervisor': 'nitro', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 24, 'DefaultCores': 12, 'DefaultThreadsPerCore': 2, 'ValidCores': [2, 4, 6, 8, 10, 12], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 49152}, 'InstanceStorageSupported': False, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': '25 Gigabit', 'MaximumNetworkInterfaces': 8, 'Ipv4AddressesPerInterface': 30, 'Ipv6AddressesPerInterface': 30, 'Ipv6Supported': True, 'EnaSupport': 'required'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'InferenceAcceleratorInfo': {'Accelerators': [{'Count': 4, 'Name': 'Inferentia', 'Manufacturer': 'AWS'}]}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': False, 'AutoRecoverySupported': False}, {'InstanceType': 'inf1.24xlarge', 'CurrentGeneration': True, 'FreeTierEligible': False, 'SupportedUsageClasses': ['on-demand', 'spot'], 'SupportedRootDeviceTypes': ['ebs'], 'BareMetal': False, 'Hypervisor': 'nitro', 'ProcessorInfo': {'SupportedArchitectures': ['x86_64'], 'SustainedClockSpeedInGhz': 2.5}, 'VCpuInfo': {'DefaultVCpus': 96, 'DefaultCores': 48, 'DefaultThreadsPerCore': 2, 'ValidCores': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48], 'ValidThreadsPerCore': [1, 2]}, 'MemoryInfo': {'SizeInMiB': 196608}, 'InstanceStorageSupported': False, 'EbsInfo': {'EbsOptimizedSupport': 'default', 'EncryptionSupport': 'supported'}, 'NetworkInfo': {'NetworkPerformance': '100 Gigabit', 'MaximumNetworkInterfaces': 11, 'Ipv4AddressesPerInterface': 30, 'Ipv6AddressesPerInterface': 30, 'Ipv6Supported': True, 'EnaSupport': 'required'}, 'PlacementGroupInfo': {'SupportedStrategies': ['cluster', 'partition', 'spread']}, 'InferenceAcceleratorInfo': {'Accelerators': [{'Count': 16, 'Name': 'Inferentia', 'Manufacturer': 'AWS'}]}, 'HibernationSupported': False, 'BurstablePerformanceSupported': False, 'DedicatedHostsSupported': True, 'AutoRecoverySupported': False}] # noqa: E501

def get_instances_list() -> list:
    '''Returns list EC2 instances with InstanceType = inf1 .'''
    # pylint: disable=all
    return get

