
# Testing module instance_type.z
import pytest
import ec2_compare.internal.instance_type.z

def test_get_internal_data_instance_type_z_get_instances_list():
  assert len(ec2_compare.internal.instance_type.z.get_instances_list()) > 0
def test_get_internal_data_instance_type_z_get():
  assert len(ec2_compare.internal.instance_type.z.get) > 0
