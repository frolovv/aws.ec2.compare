
# Testing module instance_type.m5ad
import pytest
import ec2_compare.internal.instance_type.m5ad

def test_get_internal_data_instance_type_m5ad_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m5ad.get_instances_list()) > 0
def test_get_internal_data_instance_type_m5ad_get():
  assert len(ec2_compare.internal.instance_type.m5ad.get) > 0
