
# Testing module instance_type.x1
import pytest
import ec2_compare.internal.instance_type.x1

def test_get_internal_data_instance_type_x1_get_instances_list():
  assert len(ec2_compare.internal.instance_type.x1.get_instances_list()) > 0
def test_get_internal_data_instance_type_x1_get():
  assert len(ec2_compare.internal.instance_type.x1.get) > 0
