
# Testing module instance_type.m2
import pytest
import ec2_compare.internal.instance_type.m2

def test_get_internal_data_instance_type_m2_get_instances_list():
  assert len(ec2_compare.internal.instance_type.m2.get_instances_list()) > 0
def test_get_internal_data_instance_type_m2_get():
  assert len(ec2_compare.internal.instance_type.m2.get) > 0
