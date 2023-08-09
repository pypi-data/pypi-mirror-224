# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        owner_id: int = None,
        port: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The network type of the endpoint. Valid values:
        # 
        # *   **primary**: primary endpoint
        # *   **cluster**: instance endpoint. This value is supported only for an instance that contains multiple coordinator nodes.
        # 
        # >  The default value is primary.
        self.address_type = address_type
        # The prefix of the endpoint.
        # 
        # Specify a prefix for the endpoint. Example: `gp-bp12ga6v69h86****`. In this example, the endpoint is `gp-bp12ga6v69h86****.gpdb.rds.aliyuncs.com`.
        self.connection_string_prefix = connection_string_prefix
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The port number. Example: 5432.
        self.port = port
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateInstancePublicConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AllocateInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The ID of the region. You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        has_service_linked_role: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # Indicates whether an SLR is created.
        self.has_service_linked_role = has_service_linked_role
        # The ID of the region.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_service_linked_role is not None:
            result['HasServiceLinkedRole'] = self.has_service_linked_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasServiceLinkedRole') is not None:
            self.has_service_linked_role = m.get('HasServiceLinkedRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        dbinstance_id: str = None,
        database_name: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
    ):
        # The description of the privileged account.
        self.account_description = account_description
        # The name of the privileged account.
        # 
        # *   The name can contain lowercase letters, digits, and underscores (\_).
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   The name cannot start with gp.
        # *   The name must be 2 to 16 characters in length.
        self.account_name = account_name
        # The password of the privileged account.
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # *   The password must be 8 to 32 characters in length.
        self.account_password = account_password
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database_name = database_name
        self.owner_id = owner_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCollectionRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        dimension: int = None,
        full_text_retrieval_fields: str = None,
        hnsw_m: int = None,
        manager_account: str = None,
        manager_account_password: str = None,
        metadata: str = None,
        metrics: str = None,
        namespace: str = None,
        owner_id: int = None,
        parser: str = None,
        pq_enable: int = None,
        region_id: str = None,
    ):
        self.collection = collection
        self.dbinstance_id = dbinstance_id
        self.dimension = dimension
        self.full_text_retrieval_fields = full_text_retrieval_fields
        self.hnsw_m = hnsw_m
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        self.metadata = metadata
        self.metrics = metrics
        self.namespace = namespace
        self.owner_id = owner_id
        self.parser = parser
        self.pq_enable = pq_enable
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields
        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.pq_enable is not None:
            result['PqEnable'] = self.pq_enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')
        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('PqEnable') is not None:
            self.pq_enable = m.get('PqEnable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCollectionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCollectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Take note of the following requirements:
        # 
        # - The tag key cannot be an empty string.
        # - The tag key can be up to 128 characters in length.
        # - The tag key cannot start with `aliyun` or `acs:`, and contain `http://` or `https://`.
        self.key = key
        # The value of tag N. Take note of the following requirements:
        # 
        # - The tag key cannot be an empty string.
        # - The tag key can be up to 128 characters in length.
        # - The tag key cannot start with `aliyun` or `acs:`, and contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        create_sample_data: bool = None,
        dbinstance_category: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_group_count: str = None,
        dbinstance_mode: str = None,
        encryption_key: str = None,
        encryption_type: str = None,
        engine: str = None,
        engine_version: str = None,
        idle_time: int = None,
        instance_network_type: str = None,
        instance_spec: str = None,
        master_node_num: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_iplist: str = None,
        seg_disk_performance_level: str = None,
        seg_node_num: str = None,
        seg_storage_type: str = None,
        serverless_mode: str = None,
        serverless_resource: int = None,
        storage_size: int = None,
        storage_type: str = None,
        tag: List[CreateDBInstanceRequestTag] = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vector_configuration_status: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. For more information, see [Ensure idempotence](~~327176~~).
        self.client_token = client_token
        # Specifies whether to load a sample dataset after the instance is created. Valid values:
        # 
        # - **true**\
        # - **false**\
        # 
        # If you do not specify this parameter, no sample dataset is loaded.
        self.create_sample_data = create_sample_data
        # The edition of the instance. Valid values:
        # 
        # - **HighAvailability**: High-availability Edition.
        # - **Basic**: Basic Edition.
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode.
        self.dbinstance_category = dbinstance_category
        # The instance type of the instance. For information, see [Instance types](~~86942~~).
        # 
        # > This parameter must be specified when you create an instance in reserved storage mode.
        self.dbinstance_class = dbinstance_class
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The number of compute groups. Valid values: 2, 4, 8, 12, 16, 24, 32, 64, 96, and 128.
        # 
        # > This parameter must be specified when you create an instance in reserved storage mode.
        self.dbinstance_group_count = dbinstance_group_count
        # The resource type of the instance. Valid values:
        # 
        # - **StorageElastic**: elastic storage mode.
        # - **Serverless**: Serverless mode.
        # - **Classic**: reserved storage mode.
        # 
        # > This parameter must be specified.
        self.dbinstance_mode = dbinstance_mode
        # The ID of the encryption key.
        # 
        # > If EncryptionType is set to CloudDisk, you must specify an encryption key that resides in the same region as the cloud disk that is specified by EncryptionType. Otherwise, leave this parameter empty.
        self.encryption_key = encryption_key
        # The encryption type. Valid values:
        # 
        # - **NULL** (default): Encryption is disabled.
        # - **CloudDisk**: Encryption is enabled on cloud disks, and EncryptionKey is used to specify an encryption key.
        # 
        # > Disk encryption cannot be disabled after it is enabled.
        self.encryption_type = encryption_type
        # The database engine of the instance. Set the value to gpdb.
        self.engine = engine
        # The version of the database engine. Valid values:
        # 
        # - 6.0
        # - 7.0
        self.engine_version = engine_version
        # The wait time for the instance that has no traffic to become idle. Minimum value: 60. Default value: 600. Unit: seconds.
        # 
        # > This parameter must be specified only when you create an instance in automatic Serverless mode.
        self.idle_time = idle_time
        # The network type of the instance. Set the value to VPC.
        # 
        # > 
        # - Only the Virtual Private Cloud (VPC) type is supported.
        # - If you do not specify this parameter, VPC is used.
        self.instance_network_type = instance_network_type
        # The specifications of compute nodes.
        # 
        # Valid values for High-availability Edition instances in elastic storage mode:
        # 
        # - **2C16G**\
        # - **4C32G**\
        # - **16C128G**\
        # 
        # Valid values for Basic Edition instances in elastic storage mode:
        # 
        # - **2C8G**\
        # - **4C16G**\
        # - **8C32G**\
        # - **16C64G**\
        # 
        # Valid values for instances in Serverless mode:
        # 
        # - **4C16G**\
        # - **8C32G**\
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode or Serverless mode.
        self.instance_spec = instance_spec
        # The number of coordinator nodes. Valid values: 1 and 2.
        # 
        # > If you do not specify this parameter, 1 is used.
        self.master_node_num = master_node_num
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        # > 
        # - If you do not specify this parameter, Postpaid is used.
        # - You can obtain more cost savings if you create a subscription instance for one year or longer. We recommend that you select the billing method that best suits your needs.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # 
        # - **Month**\
        # - **Year**\
        # > This parameter must be specified when PayType is set to Prepaid.
        self.period = period
        # The private IP address of the instance.
        self.private_ip_address = private_ip_address
        # The ID of the region. You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The IP address whitelist of the instance.
        # 
        # A value of 127.0.0.1 specifies that no IP address is allowed for external access. You can call the [ModifySecurityIps](~~86928~~) operation to modify the IP address whitelist after you create an instance.
        self.security_iplist = security_iplist
        # The performance level of ESSDs. Valid values:
        # 
        # - **pl0**\
        # - **pl1**\
        # - **pl2**\
        # > 
        # - This parameter takes effect only when SegStorageType is set to cloud_essd.
        # - If you do not specify this parameter, pl1 is used.
        self.seg_disk_performance_level = seg_disk_performance_level
        # The number of compute nodes.
        # 
        # - Valid values for High-availability Edition instances in elastic storage mode: multiples of 4 in the range of 4 to 512.
        # - Valid values for Basic Edition instances in elastic storage mode: multiples of 2 in the range of 2 to 512.
        # - Valid values for instances in Serverless mode: multiples of 2 in the range of 2 to 512.
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode or Serverless mode.
        self.seg_node_num = seg_node_num
        # The disk storage type of the instance. Only enhanced SSDs (ESSDs) are supported. Set the value to cloud_essd.
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode.
        self.seg_storage_type = seg_storage_type
        # The type of the Serverless mode. Valid values:
        # 
        # - **Manual** (default): manual scheduling.
        # - **Auto**: automatic scheduling.
        # 
        # > This parameter must be specified only when you create an instance in Serverless mode.
        self.serverless_mode = serverless_mode
        # The threshold of computing resources. Unit: AnalyticDB compute unit (ACU). Valid values: 8 to 32. The value must be in increments of 8 ACUs. Default value: 32.
        # 
        # > This parameter must be specified only when you create an instance in automatic Serverless mode.
        self.serverless_resource = serverless_resource
        # The storage capacity of the instance. Unit: GB. Valid values: 50 to 4000.
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode.
        self.storage_size = storage_size
        # This parameter is no longer used.
        self.storage_type = storage_type
        # The list of tags.
        self.tag = tag
        # The subscription duration.
        # 
        # - Valid values when Period is set to Month: 1 to 9.
        # - Valid values when Period is set to Year: 1 to 3.
        # > This parameter must be specified when PayType is set to Prepaid.
        self.used_time = used_time
        # The VPC ID of the instance.
        # 
        # > 
        # - This parameter must be specified.
        # - The region where the VPC resides must be the same as the region that is specified by RegionId.
        self.vpcid = vpcid
        # The vSwitch ID of the instance.
        # 
        # > 
        # - This parameter must be specified.
        # - The zone where the vSwitch resides must be the same as the zone that is specified by ZoneId.
        self.v_switch_id = v_switch_id
        # Specifies whether to enable vector engine optimization. Valid values:
        # 
        # - **enabled**\
        # - **disabled** (default)
        # 
        # > 
        # - We recommend that you do not enable vector engine optimization in mainstream analysis and real-time data warehousing scenarios.
        # - We recommend that you enable vector engine optimization in AI Generated Content (AIGC) and vector retrieval scenarios that require the vector analysis engine.
        self.vector_configuration_status = vector_configuration_status
        # The zone ID of the read-only instance. You can call the [DescribeRegions](~~86912~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.create_sample_data is not None:
            result['CreateSampleData'] = self.create_sample_data
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type
        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode
        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vector_configuration_status is not None:
            result['VectorConfigurationStatus'] = self.vector_configuration_status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CreateSampleData') is not None:
            self.create_sample_data = m.get('CreateSampleData')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')
        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')
        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VectorConfigurationStatus') is not None:
            self.vector_configuration_status = m.get('VectorConfigurationStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
        order_id: str = None,
        port: str = None,
        request_id: str = None,
    ):
        # An invalid parameter. It is no longer returned when you call this operation.
        # 
        # You can call the [DescribeDBInstanceAttribute](~~86910~~) operation to query the endpoint that is used to connect to the instance.
        self.connection_string = connection_string
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The order ID.
        self.order_id = order_id
        # An invalid parameter. It is no longer returned when you call this operation.
        # 
        # You can call the [DescribeDBInstanceAttribute](~~86910~~) operation to query the port number that is used to connect to the instance.
        self.port = port
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.port is not None:
            result['Port'] = self.port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstancePlanRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        plan_config: str = None,
        plan_desc: str = None,
        plan_end_date: str = None,
        plan_name: str = None,
        plan_schedule_type: str = None,
        plan_start_date: str = None,
        plan_type: str = None,
    ):
        # The ID of instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The execution information of the plan. Specify the parameter in the JSON format. The parameter value varies based on the values of the **PlanType** and **PlanScheduleType** parameters. The following section describes the PlanConfig parameter.
        self.plan_config = plan_config
        # The description of the plan.
        self.plan_desc = plan_desc
        # The end time of the plan. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        # 
        # > *   This parameter is required only if the **PlanScheduleType** parameter is set to **Regular**.
        # > *   If you do not specify this parameter, the plan does not end.
        self.plan_end_date = plan_end_date
        # The name of the plan.
        self.plan_name = plan_name
        # The execution mode of the plan. Valid values:
        # 
        # *   **Postpone**: The plan is executed later.
        # *   **Regular**: The plan is executed periodically.
        self.plan_schedule_type = plan_schedule_type
        # The start time of the plan. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # >  *   This parameter is required only if the **PlanScheduleType** parameter is set to **Regular**.
        # >  *   If you do not specify this parameter, the plan is executed immediately.
        self.plan_start_date = plan_start_date
        # The type of the plan. Valid values:
        # 
        # *   **PauseResume**: pauses and resumes an instance.
        # *   **Resize**: changes the number of compute nodes.
        # *   **ModifySpec**: changes compute node specifications.
        # 
        # > *   You can specify the value to Resize only for instances in Serverless mode.
        # > *   You can specify the value to ModifySpec only for instances in elastic storage mode.
        self.plan_type = plan_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_config is not None:
            result['PlanConfig'] = self.plan_config
        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc
        if self.plan_end_date is not None:
            result['PlanEndDate'] = self.plan_end_date
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_schedule_type is not None:
            result['PlanScheduleType'] = self.plan_schedule_type
        if self.plan_start_date is not None:
            result['PlanStartDate'] = self.plan_start_date
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanConfig') is not None:
            self.plan_config = m.get('PlanConfig')
        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')
        if m.get('PlanEndDate') is not None:
            self.plan_end_date = m.get('PlanEndDate')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanScheduleType') is not None:
            self.plan_schedule_type = m.get('PlanScheduleType')
        if m.get('PlanStartDate') is not None:
            self.plan_start_date = m.get('PlanStartDate')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        return self


class CreateDBInstancePlanResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        plan_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of instance.
        self.dbinstance_id = dbinstance_id
        # The error message.
        # 
        # This parameter is returned only if the operation fails.
        self.error_message = error_message
        # The ID of the plan.
        self.plan_id = plan_id
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateDBInstancePlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBInstancePlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDBInstancePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSampleDataRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateSampleDataResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned if an error occurs. This message does not affect the execution of the operation.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The execution state of the operation. Valid values:
        # 
        # *   **false**: The operation fails.
        # *   **true**: The operation is successful.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateSampleDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSampleDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSampleDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVectorIndexRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        dimension: int = None,
        hnsw_m: int = None,
        manager_account: str = None,
        manager_account_password: str = None,
        metrics: str = None,
        namespace: str = None,
        owner_id: int = None,
        pq_enable: int = None,
        region_id: str = None,
    ):
        self.collection = collection
        self.dbinstance_id = dbinstance_id
        self.dimension = dimension
        self.hnsw_m = hnsw_m
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        # Distance Metrics。
        self.metrics = metrics
        self.namespace = namespace
        self.owner_id = owner_id
        self.pq_enable = pq_enable
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pq_enable is not None:
            result['PqEnable'] = self.pq_enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PqEnable') is not None:
            self.pq_enable = m.get('PqEnable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateVectorIndexResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateVectorIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVectorIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVectorIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCollectionRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.collection = collection
        self.dbinstance_id = dbinstance_id
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCollectionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCollectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCollectionDataRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        collection_data: str = None,
        collection_data_filter: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.collection = collection
        self.collection_data = collection_data
        self.collection_data_filter = collection_data_filter
        self.dbinstance_id = dbinstance_id
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.collection_data is not None:
            result['CollectionData'] = self.collection_data
        if self.collection_data_filter is not None:
            result['CollectionDataFilter'] = self.collection_data_filter
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('CollectionData') is not None:
            self.collection_data = m.get('CollectionData')
        if m.get('CollectionDataFilter') is not None:
            self.collection_data_filter = m.get('CollectionDataFilter')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCollectionDataResponseBody(TeaModel):
    def __init__(
        self,
        applied_rows: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.applied_rows = applied_rows
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_rows is not None:
            result['AppliedRows'] = self.applied_rows
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedRows') is not None:
            self.applied_rows = m.get('AppliedRows')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteCollectionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCollectionDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCollectionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. For more information, see [How to ensure idempotence](~~327176~~).
        self.client_token = client_token
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstancePlanRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        plan_id: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](~~449398~~) operation to query the details of plans, including plan IDs.
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class DeleteDBInstancePlanResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        plan_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned.
        # 
        # This parameter is returned only when the operation fails.
        self.error_message = error_message
        # The ID of the plan.
        self.plan_id = plan_id
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteDBInstancePlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBInstancePlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDBInstancePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        namespace: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        self.namespace = namespace
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVectorIndexRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        namespace: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.collection = collection
        self.dbinstance_id = dbinstance_id
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        self.namespace = namespace
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteVectorIndexResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteVectorIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVectorIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVectorIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dbinstance_id: str = None,
    ):
        # The name of the account.
        self.account_name = account_name
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeAccountsResponseBodyAccountsDBInstanceAccount(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        dbinstance_id: str = None,
    ):
        # The description of the account.
        self.account_description = account_description
        # The name of the account.
        self.account_name = account_name
        # The state of the account.
        # 
        # *   **0**: The account is being created.
        # *   **1**: The account is in use.
        # *   **3**: The account is being deleted.
        self.account_status = account_status
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeAccountsResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        dbinstance_account: List[DescribeAccountsResponseBodyAccountsDBInstanceAccount] = None,
    ):
        self.dbinstance_account = dbinstance_account

    def validate(self):
        if self.dbinstance_account:
            for k in self.dbinstance_account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceAccount'] = []
        if self.dbinstance_account is not None:
            for k in self.dbinstance_account:
                result['DBInstanceAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_account = []
        if m.get('DBInstanceAccount') is not None:
            for k in m.get('DBInstanceAccount'):
                temp_model = DescribeAccountsResponseBodyAccountsDBInstanceAccount()
                self.dbinstance_account.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(
        self,
        accounts: DescribeAccountsResponseBodyAccounts = None,
        request_id: str = None,
    ):
        # Details of the account.
        self.accounts = accounts
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourcesRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        region: str = None,
        zone_id: str = None,
    ):
        # The billing method. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.charge_type = charge_type
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region = region
        # The ID of the zone.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.region is not None:
            result['Region'] = self.region
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount(TeaModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # The maximum number of compute nodes.
        self.max_count = max_count
        # The minimum number of compute nodes.
        self.min_count = min_count
        # The step size for adding compute nodes.
        # 
        # For example, if the value of this parameter is 4, compute nodes must be added by multiples of 4.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize(TeaModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # The maximum storage capacity of each compute node.
        self.max_count = max_count
        # The minimum storage capacity of each compute node.
        self.min_count = min_count
        # The step size for adding storage capacity for compute nodes.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses(TeaModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        display_class: str = None,
        instance_class: str = None,
        node_count: DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount = None,
        storage_size: DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize = None,
        storage_type: str = None,
    ):
        # The instance edition. Valid values:
        # 
        # *   **HighAvailability**: High-availability Edition
        # *   **Basic**: Basic Edition
        self.category = category
        # The description of compute node specifications.
        self.description = description
        # The specifications of each compute node.
        self.display_class = display_class
        # The specifications of each compute node.
        self.instance_class = instance_class
        # Details about the compute nodes.
        self.node_count = node_count
        # Details about the storage capacity of compute nodes.
        self.storage_size = storage_size
        # The storage type. Valid values:
        # 
        # *   **cloud_essd**: enhanced SSD (ESSD)
        # *   **cloud_efficiency**: ultra disk
        # *   **oss**: Object Storage Service (OSS)
        self.storage_type = storage_type

    def validate(self):
        if self.node_count:
            self.node_count.validate()
        if self.storage_size:
            self.storage_size.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.display_class is not None:
            result['DisplayClass'] = self.display_class
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayClass') is not None:
            self.display_class = m.get('DisplayClass')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        if m.get('StorageSize') is not None:
            temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize()
            self.storage_size = temp_model.from_map(m['StorageSize'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEngines(TeaModel):
    def __init__(
        self,
        mode: str = None,
        supported_engine_version: str = None,
        supported_instance_classes: List[DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses] = None,
    ):
        # The instance resource type. Valid values:
        # 
        # *   **ecs**: elastic storage mode
        # *   **serverless**: Serverless mode
        self.mode = mode
        # The available engine version.
        self.supported_engine_version = supported_engine_version
        # The available specifications.
        self.supported_instance_classes = supported_instance_classes

    def validate(self):
        if self.supported_instance_classes:
            for k in self.supported_instance_classes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.supported_engine_version is not None:
            result['SupportedEngineVersion'] = self.supported_engine_version
        result['SupportedInstanceClasses'] = []
        if self.supported_instance_classes is not None:
            for k in self.supported_instance_classes:
                result['SupportedInstanceClasses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('SupportedEngineVersion') is not None:
            self.supported_engine_version = m.get('SupportedEngineVersion')
        self.supported_instance_classes = []
        if m.get('SupportedInstanceClasses') is not None:
            for k in m.get('SupportedInstanceClasses'):
                temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses()
                self.supported_instance_classes.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        supported_engines: List[DescribeAvailableResourcesResponseBodyResourcesSupportedEngines] = None,
        zone_id: str = None,
    ):
        # The available engine version and specifications.
        self.supported_engines = supported_engines
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.supported_engines:
            for k in self.supported_engines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedEngines'] = []
        if self.supported_engines is not None:
            for k in self.supported_engines:
                result['SupportedEngines'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engines = []
        if m.get('SupportedEngines') is not None:
            for k in m.get('SupportedEngines'):
                temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEngines()
                self.supported_engines.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourcesResponseBody(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        request_id: str = None,
        resources: List[DescribeAvailableResourcesResponseBodyResources] = None,
    ):
        # The ID of the region.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # Details of the available resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = DescribeAvailableResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAvailableResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        enable_recovery_point: bool = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        recovery_point_period: str = None,
        request_id: str = None,
    ):
        # The number of days for which data backup files are retained.
        self.backup_retention_period = backup_retention_period
        # Indicates whether automatic point-in-time backup is enabled. Valid values:
        # 
        # *   **true**: Automatic point-in-time backup is enabled.
        # *   **false**: Automatic point-in-time backup is disabled.
        self.enable_recovery_point = enable_recovery_point
        # The cycle based on which backups are performed. If more than one day of the week is specified, the days of the week are separated by commas (,). Valid values:
        # 
        # *   **Monday**\
        # *   **Tuesday**\
        # *   **Wednesday**\
        # *   **Thursday**\
        # *   **Friday**\
        # *   **Saturday**\
        # *   **Sunday**\
        self.preferred_backup_period = preferred_backup_period
        # The backup time. The time is in the HH:mmZ-HH:mmZ format. The time is displayed in UTC.
        self.preferred_backup_time = preferred_backup_time
        # The frequency of the point-in-time backup. Valid values:
        # 
        # *   **1**: per hour
        # *   **2**: per 2 hours
        # *   **4**: per 4 hours
        # *   **8**: per 8 hours
        self.recovery_point_period = recovery_point_period
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.enable_recovery_point is not None:
            result['EnableRecoveryPoint'] = self.enable_recovery_point
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.recovery_point_period is not None:
            result['RecoveryPointPeriod'] = self.recovery_point_period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('EnableRecoveryPoint') is not None:
            self.enable_recovery_point = m.get('EnableRecoveryPoint')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RecoveryPointPeriod') is not None:
            self.recovery_point_period = m.get('RecoveryPointPeriod')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCollectionRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.collection = collection
        self.dbinstance_id = dbinstance_id
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCollectionResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dimension: int = None,
        full_text_retrieval_fields: str = None,
        message: str = None,
        metadata: Dict[str, str] = None,
        metrics: str = None,
        namespace: str = None,
        parser: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.dimension = dimension
        self.full_text_retrieval_fields = full_text_retrieval_fields
        self.message = message
        self.metadata = metadata
        # Distance Metrics。
        self.metrics = metrics
        self.namespace = namespace
        self.parser = parser
        self.region_id = region_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields
        if self.message is not None:
            result['Message'] = self.message
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCollectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterNodeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        node_type: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The node type. Valid values:
        # 
        # *   **master**: coordinator node
        # *   **segment**: compute node
        # 
        # >  If you do not specify this parameter, the information of all nodes is returned.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeDBClusterNodeResponseBodyNodes(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the node.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDBClusterNodeResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        nodes: List[DescribeDBClusterNodeResponseBodyNodes] = None,
        request_id: str = None,
    ):
        # The ID of the instance.
        self.dbcluster_id = dbcluster_id
        # The information of nodes.
        self.nodes = nodes
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeDBClusterNodeResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBClusterNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        key: str = None,
        node_type: str = None,
        nodes: str = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format.
        # 
        # >  The end time must be later than the start time. The interval cannot be more than seven days.
        self.end_time = end_time
        # The performance metric that you want to query. Separate multiple values with commas (,). For more information, see [Performance parameters](~~86943~~).
        self.key = key
        # The node type. Valid values:
        # 
        # *   **master**: coordinator node
        # *   **segment**: compute node
        # 
        # >  If you do not specify this parameter, the performance metrics of all nodes are returned.
        self.node_type = node_type
        # The nodes for which you want to query performance metrics. Separate multiple values with commas (,). Example: `master-10******1,master-10******2`. You can call the [DescribeDBClusterNode](~~390136~~) operation to query the names of nodes.
        # 
        # The nodes can also be filtered based on their metric values. Valid values:
        # 
        # *   **top10**: the 10 nodes that have the highest metric values
        # *   **top20**: the 20 nodes that have the highest metric values
        # *   **bottom10**: the 10 nodes that have the lowest metric values
        # *   **bottom20**: the 20 nodes that have the lowest metric values
        self.nodes = nodes
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format.
        # 
        # >  You can query monitoring information only within the last 30 days.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues(TeaModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
        # The value of the performance metric and the time when the metric value was collected.
        self.point = point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        role: str = None,
        values: List[DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues] = None,
    ):
        # The name of the compute node or compute group.
        self.name = name
        # The role of the node. Valid values:
        # 
        # *   **master**: primary coordinator node
        # *   **standby**: standby coordinator node
        # *   **segment**: compute node
        self.role = role
        # The value of the performance metric collected at a point in time.
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.role is not None:
            result['Role'] = self.role
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(
        self,
        name: str = None,
        series: List[DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries] = None,
        unit: str = None,
    ):
        # The name of the performance metric. For more information, see [Performance parameters](~~86943~~).
        self.name = name
        # Details of the performance metric of a node.
        self.series = series
        # The unit of the performance metric.
        self.unit = unit

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performance_keys: List[DescribeDBClusterPerformanceResponseBodyPerformanceKeys] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. The time follows the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format. The time is displayed in UTC.
        self.end_time = end_time
        # Details of the performance metrics of the instance.
        self.performance_keys = performance_keys
        # The ID of the request.
        self.request_id = request_id
        # The start time of the query. The time follows the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performance_keys:
            for k in self.performance_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['PerformanceKeys'] = []
        if self.performance_keys is not None:
            for k in self.performance_keys:
                result['PerformanceKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performance_keys = []
        if m.get('PerformanceKeys') is not None:
            for k in m.get('PerformanceKeys'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeys()
                self.performance_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterPerformanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
    ):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a region.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute(TeaModel):
    def __init__(
        self,
        availability_value: str = None,
        connection_mode: str = None,
        connection_string: str = None,
        core_version: str = None,
        cpu_cores: int = None,
        cpu_cores_per_node: int = None,
        creation_time: str = None,
        dbinstance_category: str = None,
        dbinstance_class: str = None,
        dbinstance_class_type: str = None,
        dbinstance_cpu_cores: int = None,
        dbinstance_description: str = None,
        dbinstance_disk_mbps: int = None,
        dbinstance_group_count: str = None,
        dbinstance_id: str = None,
        dbinstance_memory: int = None,
        dbinstance_mode: str = None,
        dbinstance_net_type: str = None,
        dbinstance_status: str = None,
        dbinstance_storage: int = None,
        encryption_key: str = None,
        encryption_type: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        host_type: str = None,
        idle_time: int = None,
        instance_network_type: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        master_node_num: int = None,
        max_connections: int = None,
        memory_per_node: int = None,
        memory_size: int = None,
        memory_unit: str = None,
        minor_version: str = None,
        pay_type: str = None,
        port: str = None,
        read_delay_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        running_time: str = None,
        security_iplist: str = None,
        seg_disk_performance_level: str = None,
        seg_node_num: int = None,
        segment_counts: int = None,
        serverless_mode: str = None,
        serverless_resource: int = None,
        start_time: str = None,
        storage_per_node: int = None,
        storage_size: int = None,
        storage_type: str = None,
        storage_unit: str = None,
        support_restore: bool = None,
        tags: DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags = None,
        v_switch_id: str = None,
        vector_configuration_status: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The service availability of the instance. Unit: %.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.availability_value = availability_value
        # The access mode of the instance. Valid values:
        # 
        # *   **Performance**: standard mode.
        # *   **Safety**: safe mode.
        # *   **LVS**: Linux Virtual Server (LVS) mode.
        self.connection_mode = connection_mode
        # The endpoint that is used to connect to the instance.
        self.connection_string = connection_string
        # The number of the minor version.
        self.core_version = core_version
        # The number of CPU cores per compute node.
        self.cpu_cores = cpu_cores
        # The number of CPU cores per node.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.cpu_cores_per_node = cpu_cores_per_node
        # The time when the instance was created.
        self.creation_time = creation_time
        # The edition of the instance. Valid values:
        # 
        # *   **Basic**: Basic Edition.
        # *   **HighAvailability**: High-availability Edition.
        self.dbinstance_category = dbinstance_category
        # The instance type of the instance.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.dbinstance_class = dbinstance_class
        # The instance family of the instance. Valid values:
        # 
        # *   **s**: shared.
        # *   **x**: general-purpose.
        # *   **d**: dedicated.
        # *   **h**: dedicated host.
        self.dbinstance_class_type = dbinstance_class_type
        # The number of CPU cores.
        self.dbinstance_cpu_cores = dbinstance_cpu_cores
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The maximum disk throughput of the compute group. Unit: Mbit/s.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.dbinstance_disk_mbps = dbinstance_disk_mbps
        # The number of compute groups.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.dbinstance_group_count = dbinstance_group_count
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The memory capacity per compute node.
        # 
        # >  For instances in reserved storage mode, the unit of this parameter is MB. For instances in elastic storage mode and Serverless mode, the unit of this parameter is GB.
        self.dbinstance_memory = dbinstance_memory
        # The resource type of the instance. Valid values:
        # 
        # *   **Serverless**: Serverless mode.
        # *   **StorageElastic**: elastic storage mode.
        # *   **Classic**: reserved storage mode.
        self.dbinstance_mode = dbinstance_mode
        # The type of the network interface card (NIC) that is used by the instance. Valid values:
        # 
        # *   **0**: Internet.
        # *   **1**: internal network.
        # *   **2**: VPC.
        self.dbinstance_net_type = dbinstance_net_type
        # The state of the instance. For more information, see [Instance statuses](~~86944~~).
        self.dbinstance_status = dbinstance_status
        # The maximum storage capacity per node. Unit: GB.
        self.dbinstance_storage = dbinstance_storage
        # The encryption key.
        # 
        # >  This parameter is returned only for instances for which disk encryption is enabled.
        self.encryption_key = encryption_key
        # The encryption type. Valid values:
        # 
        # *   **CloudDisk**: disk encryption.
        # 
        # >  This parameter is returned only for instances for which disk encryption is enabled.
        self.encryption_type = encryption_type
        # The database engine of the instance.
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        # The expiration time of the instance. The time is displayed in UTC.
        # 
        # >  For pay-as-you-go instances, `2999-09-08T16:00:00Z` is returned.
        self.expire_time = expire_time
        # The disk type of the compute group. Valid values:
        # 
        # *   **0**: SSD.
        # *   **1**: HDD.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.host_type = host_type
        # The wait period for the instance that has no traffic to become idle. Unit: seconds.
        # 
        # >  This parameter is returned only for instances in automatic Serverless mode.
        self.idle_time = idle_time
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network.
        # *   **VPC**: VPC.
        self.instance_network_type = instance_network_type
        # The lock mode of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked due to instance restoration.
        # *   **LockByDiskQuota**: The instance is automatically locked due to exhausted storage.
        self.lock_mode = lock_mode
        # An invalid parameter. It is no longer returned when you call this operation.
        self.lock_reason = lock_reason
        # The end time of the maintenance window.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window.
        self.maintain_start_time = maintain_start_time
        # The number of coordinator nodes.
        self.master_node_num = master_node_num
        # The maximum number of concurrent connections to the instance.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.max_connections = max_connections
        # The memory capacity per node. The unit can be one of the valid values of the **MemoryUnit** parameter.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.memory_per_node = memory_per_node
        # The memory capacity per compute node.
        # 
        # >  For instances in reserved storage mode, the unit of this parameter is MB. For instances in elastic storage mode and Serverless mode, the unit of this parameter is GB.
        self.memory_size = memory_size
        # The unit of the memory capacity.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.memory_unit = memory_unit
        # The minor version of the instance.
        self.minor_version = minor_version
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type
        # The port number that is used to connect to the instance.
        self.port = port
        # An invalid parameter. It is no longer returned when you call this operation.
        self.read_delay_time = read_delay_time
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The running duration of the instance.
        self.running_time = running_time
        # The IP address whitelist of the instance.
        self.security_iplist = security_iplist
        # The performance level of ESSDs. Only **PL1** is supported.
        self.seg_disk_performance_level = seg_disk_performance_level
        # The number of compute nodes.
        # 
        # >  This parameter is available only for instances in elastic storage mode or manual Serverless mode.
        self.seg_node_num = seg_node_num
        # The number of compute groups.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.segment_counts = segment_counts
        # The type of the Serverless mode. Valid values:
        # 
        # *   **Manual**: manual scheduling.
        # *   **Auto**: automatic scheduling.
        # 
        # >  This parameter is returned only for instances in Serverless mode.
        self.serverless_mode = serverless_mode
        # The threshold of computing resources. Unit: AnalyticDB compute unit (ACU).
        # 
        # >  This parameter is returned only for instances in automatic Serverless mode.
        self.serverless_resource = serverless_resource
        # The time when the instance started to run.
        self.start_time = start_time
        # The storage capacity per node. The unit can be one of the valid values of the **StorageUnit** parameter.
        # 
        # >  This parameter is available only for instances in reserved storage mode.
        self.storage_per_node = storage_per_node
        # The storage capacity. Unit: GB.
        self.storage_size = storage_size
        # The storage type of the instance. Valid values:
        # 
        # - **cloud_essd**: enhanced SSD (ESSD).
        # - **cloud_efficiency**: ultra disk.
        # 
        # >  This parameter is available only for instances in elastic storage mode.
        self.storage_type = storage_type
        # The unit of the storage capacity. Valid values:
        # 
        # *   **GB SSD**\
        # *   **TB SSD**\
        # *   **GB HDD**\
        # 
        # >  This parameter is available only for instances in reserved storage mode or Serverless mode.
        self.storage_unit = storage_unit
        # Indicates whether the instance supports backup and restoration.
        # 
        # *   **true**\
        # *   **false**\
        self.support_restore = support_restore
        # The tags of the instance. Each tag is a key-value pair.
        self.tags = tags
        # The vSwitch ID of the instance.
        self.v_switch_id = v_switch_id
        # Indicates whether vector engine optimization is enabled. Valid values:
        # 
        # *   **enabled**\
        # *   **disabled**\
        self.vector_configuration_status = vector_configuration_status
        # The virtual private cloud (VPC) ID of the instance.
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.core_version is not None:
            result['CoreVersion'] = self.core_version
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.cpu_cores_per_node is not None:
            result['CpuCoresPerNode'] = self.cpu_cores_per_node
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_class_type is not None:
            result['DBInstanceClassType'] = self.dbinstance_class_type
        if self.dbinstance_cpu_cores is not None:
            result['DBInstanceCpuCores'] = self.dbinstance_cpu_cores
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_disk_mbps is not None:
            result['DBInstanceDiskMBPS'] = self.dbinstance_disk_mbps
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_memory is not None:
            result['DBInstanceMemory'] = self.dbinstance_memory
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.memory_per_node is not None:
            result['MemoryPerNode'] = self.memory_per_node
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.memory_unit is not None:
            result['MemoryUnit'] = self.memory_unit
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.read_delay_time is not None:
            result['ReadDelayTime'] = self.read_delay_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.segment_counts is not None:
            result['SegmentCounts'] = self.segment_counts
        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode
        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage_per_node is not None:
            result['StoragePerNode'] = self.storage_per_node
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_unit is not None:
            result['StorageUnit'] = self.storage_unit
        if self.support_restore is not None:
            result['SupportRestore'] = self.support_restore
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vector_configuration_status is not None:
            result['VectorConfigurationStatus'] = self.vector_configuration_status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CoreVersion') is not None:
            self.core_version = m.get('CoreVersion')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('CpuCoresPerNode') is not None:
            self.cpu_cores_per_node = m.get('CpuCoresPerNode')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceClassType') is not None:
            self.dbinstance_class_type = m.get('DBInstanceClassType')
        if m.get('DBInstanceCpuCores') is not None:
            self.dbinstance_cpu_cores = m.get('DBInstanceCpuCores')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceDiskMBPS') is not None:
            self.dbinstance_disk_mbps = m.get('DBInstanceDiskMBPS')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceMemory') is not None:
            self.dbinstance_memory = m.get('DBInstanceMemory')
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MemoryPerNode') is not None:
            self.memory_per_node = m.get('MemoryPerNode')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('MemoryUnit') is not None:
            self.memory_unit = m.get('MemoryUnit')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ReadDelayTime') is not None:
            self.read_delay_time = m.get('ReadDelayTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegmentCounts') is not None:
            self.segment_counts = m.get('SegmentCounts')
        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')
        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StoragePerNode') is not None:
            self.storage_per_node = m.get('StoragePerNode')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUnit') is not None:
            self.storage_unit = m.get('StorageUnit')
        if m.get('SupportRestore') is not None:
            self.support_restore = m.get('SupportRestore')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VectorConfigurationStatus') is not None:
            self.vector_configuration_status = m.get('VectorConfigurationStatus')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbinstance_attribute: List[DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute] = None,
    ):
        self.dbinstance_attribute = dbinstance_attribute

    def validate(self):
        if self.dbinstance_attribute:
            for k in self.dbinstance_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_attribute = []
        if m.get('DBInstanceAttribute') is not None:
            for k in m.get('DBInstanceAttribute'):
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDBInstanceAttributeResponseBodyItems = None,
        request_id: str = None,
    ):
        # The queried instance.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceDataBloatRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDBInstanceDataBloatResponseBodyItems(TeaModel):
    def __init__(
        self,
        bloat_ceoff: str = None,
        bloat_size: str = None,
        database_name: str = None,
        expect_table_size: str = None,
        real_table_size: str = None,
        schema_name: str = None,
        sequence: int = None,
        storage_type: str = None,
        suggested_action: str = None,
        table_name: str = None,
        time_last_updated: str = None,
        time_last_vacuumed: str = None,
    ):
        # The coefficient of data bloat. It is calculated by using the following formula:
        # 
        # Bloat coefficient = Number of dead rows/Number of active rows.
        self.bloat_ceoff = bloat_ceoff
        # The bloat size of the table. It indicates the amount of space that can be released.
        self.bloat_size = bloat_size
        # The name of the database.
        self.database_name = database_name
        # The expected size of the table.
        # 
        # It indicates the size of the table that has no data bloat.
        self.expect_table_size = expect_table_size
        # The actual size of the table.
        self.real_table_size = real_table_size
        # The name of the schema.
        self.schema_name = schema_name
        # The sequence number.
        self.sequence = sequence
        # The storage type of the table. Valid values:
        # 
        # *   **Heap**: heap table
        # *   **AO**: append-optimized (AO) table
        self.storage_type = storage_type
        # This parameter is not returned.
        self.suggested_action = suggested_action
        # The name of the table.
        self.table_name = table_name
        # The time when the table was last deleted, inserted, or updated.
        self.time_last_updated = time_last_updated
        # The time when the table was last vacuumed. The time is displayed in UTC.
        self.time_last_vacuumed = time_last_vacuumed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bloat_ceoff is not None:
            result['BloatCeoff'] = self.bloat_ceoff
        if self.bloat_size is not None:
            result['BloatSize'] = self.bloat_size
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.expect_table_size is not None:
            result['ExpectTableSize'] = self.expect_table_size
        if self.real_table_size is not None:
            result['RealTableSize'] = self.real_table_size
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.suggested_action is not None:
            result['SuggestedAction'] = self.suggested_action
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated
        if self.time_last_vacuumed is not None:
            result['TimeLastVacuumed'] = self.time_last_vacuumed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BloatCeoff') is not None:
            self.bloat_ceoff = m.get('BloatCeoff')
        if m.get('BloatSize') is not None:
            self.bloat_size = m.get('BloatSize')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('ExpectTableSize') is not None:
            self.expect_table_size = m.get('ExpectTableSize')
        if m.get('RealTableSize') is not None:
            self.real_table_size = m.get('RealTableSize')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SuggestedAction') is not None:
            self.suggested_action = m.get('SuggestedAction')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')
        if m.get('TimeLastVacuumed') is not None:
            self.time_last_vacuumed = m.get('TimeLastVacuumed')
        return self


class DescribeDBInstanceDataBloatResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeDBInstanceDataBloatResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of data bloat.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceDataBloatResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceDataBloatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceDataBloatResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceDataBloatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceDataSkewRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **20**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **20**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDBInstanceDataSkewResponseBodyItems(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        distribute_key: str = None,
        owner: str = None,
        schema_name: str = None,
        sequence: int = None,
        table_name: str = None,
        table_size: str = None,
        table_skew: str = None,
        time_last_updated: str = None,
    ):
        # The name of the database.
        self.database_name = database_name
        # The distribution key of the table.
        self.distribute_key = distribute_key
        # The owner of the table.
        self.owner = owner
        # The name of the schema.
        self.schema_name = schema_name
        # The sequence number of the data skew case. All data skew cases are sorted by severity in descending order.
        self.sequence = sequence
        # The name of the table.
        self.table_name = table_name
        # The total number of rows in the table.
        self.table_size = table_size
        # The skew ratio of the table. Valid values: 0 to 100. Unit: %. A greater value indicates that the table is more severely skewed. A smaller value indicates less impact on query performance. A value of 0 indicates no data skew.
        self.table_skew = table_skew
        # The time when the table was last deleted, inserted, or updated.
        self.time_last_updated = time_last_updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.distribute_key is not None:
            result['DistributeKey'] = self.distribute_key
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_size is not None:
            result['TableSize'] = self.table_size
        if self.table_skew is not None:
            result['TableSkew'] = self.table_skew
        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DistributeKey') is not None:
            self.distribute_key = m.get('DistributeKey')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')
        if m.get('TableSkew') is not None:
            self.table_skew = m.get('TableSkew')
        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')
        return self


class DescribeDBInstanceDataSkewResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeDBInstanceDataSkewResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about data skew.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceDataSkewResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceDataSkewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceDataSkewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceDataSkewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceDiagnosisSummaryRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        role_preferd: str = None,
        start_status: str = None,
        sync_mode: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **20**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **20**.
        self.page_size = page_size
        # The role state of the node. It indicates whether a primary/secondary switchover occurs. Valid values:
        # 
        # *   **normal**: The node role is normal. No primary/secondary switchover occurs.
        # *   **reverse**: The node role is reversed. A primary/secondary switchover occurs.
        self.role_preferd = role_preferd
        # The running state of the node. Valid values:
        # 
        # *   **UP**: The node is running.
        # *   **DOWN**: The node is faulty.
        # 
        # If this parameter is not specified, information of nodes in all running states is returned.
        self.start_status = start_status
        # The data synchronization state of the node. Valid values:
        # 
        # *   **synced**: The node data is synchronized.
        # *   **notSyncing**: The node data is not synchronized.
        # 
        # If this parameter is not specified, information of nodes in all synchronization states is returned.
        self.sync_mode = sync_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_preferd is not None:
            result['RolePreferd'] = self.role_preferd
        if self.start_status is not None:
            result['StartStatus'] = self.start_status
        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RolePreferd') is not None:
            self.role_preferd = m.get('RolePreferd')
        if m.get('StartStatus') is not None:
            self.start_status = m.get('StartStatus')
        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')
        return self


class DescribeDBInstanceDiagnosisSummaryResponseBodyItems(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        node_address: str = None,
        node_cid: str = None,
        node_id: str = None,
        node_name: str = None,
        node_port: str = None,
        node_preferred_role: str = None,
        node_replication_mode: str = None,
        node_role: str = None,
        node_status: str = None,
        node_type: str = None,
    ):
        # The name of the node.
        self.hostname = hostname
        # The IP address of the node.
        self.node_address = node_address
        # The ID of the node group.
        self.node_cid = node_cid
        # The ID of the node.
        self.node_id = node_id
        # The name of the host where the node resides.
        self.node_name = node_name
        # The port number of the node.
        self.node_port = node_port
        # The initial role of the node. Valid values:
        # 
        # *   **primary**: primary node
        # *   **mirror**: secondary node
        # 
        # If the value of this parameter is the same as that of **NodeRole**, no primary/secondary switchover occurs. If the value of this parameter is not the same as that of **NodeRole**, a primary/secondary switchover occurs.
        self.node_preferred_role = node_preferred_role
        # The data synchronization state of the node. Valid values:
        # 
        # *   **Synced**: The node data is synchronized.
        # *   **Not Syncing**: The node data is not synchronized.
        # *   **No sync required**: Data synchronization is not required. This value may be returned only for the coordinator node.
        self.node_replication_mode = node_replication_mode
        # The current role of the node. Valid values:
        # 
        # *   **primary**: primary node
        # *   **mirror**: secondary node
        self.node_role = node_role
        # The running state of the node. Valid values:
        # 
        # *   **UP**: The node is running.
        # *   **DOWN**: The node is faulty.
        self.node_status = node_status
        # The type of the node. Valid values:
        # 
        # *   **master**: primary coordinator node
        # *   **slave**: standby coordinator node
        # *   **segment**: compute node
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.node_address is not None:
            result['NodeAddress'] = self.node_address
        if self.node_cid is not None:
            result['NodeCID'] = self.node_cid
        if self.node_id is not None:
            result['NodeID'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_port is not None:
            result['NodePort'] = self.node_port
        if self.node_preferred_role is not None:
            result['NodePreferredRole'] = self.node_preferred_role
        if self.node_replication_mode is not None:
            result['NodeReplicationMode'] = self.node_replication_mode
        if self.node_role is not None:
            result['NodeRole'] = self.node_role
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('NodeAddress') is not None:
            self.node_address = m.get('NodeAddress')
        if m.get('NodeCID') is not None:
            self.node_cid = m.get('NodeCID')
        if m.get('NodeID') is not None:
            self.node_id = m.get('NodeID')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')
        if m.get('NodePreferredRole') is not None:
            self.node_preferred_role = m.get('NodePreferredRole')
        if m.get('NodeReplicationMode') is not None:
            self.node_replication_mode = m.get('NodeReplicationMode')
        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo(TeaModel):
    def __init__(
        self,
        exception_node_num: int = None,
        normal_node_num: int = None,
        not_preferred_node_num: int = None,
        not_syncing_node_num: int = None,
        preferred_node_num: int = None,
        synced_node_num: int = None,
    ):
        # The number of abnormal nodes.
        self.exception_node_num = exception_node_num
        # The number of normal nodes.
        self.normal_node_num = normal_node_num
        # The number of nodes whose roles are reversed.
        self.not_preferred_node_num = not_preferred_node_num
        # The number of unsynchronized nodes.
        self.not_syncing_node_num = not_syncing_node_num
        # The number of nodes whose roles are normal.
        self.preferred_node_num = preferred_node_num
        # The number of synchronized nodes.
        self.synced_node_num = synced_node_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_node_num is not None:
            result['ExceptionNodeNum'] = self.exception_node_num
        if self.normal_node_num is not None:
            result['NormalNodeNum'] = self.normal_node_num
        if self.not_preferred_node_num is not None:
            result['NotPreferredNodeNum'] = self.not_preferred_node_num
        if self.not_syncing_node_num is not None:
            result['NotSyncingNodeNum'] = self.not_syncing_node_num
        if self.preferred_node_num is not None:
            result['PreferredNodeNum'] = self.preferred_node_num
        if self.synced_node_num is not None:
            result['SyncedNodeNum'] = self.synced_node_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionNodeNum') is not None:
            self.exception_node_num = m.get('ExceptionNodeNum')
        if m.get('NormalNodeNum') is not None:
            self.normal_node_num = m.get('NormalNodeNum')
        if m.get('NotPreferredNodeNum') is not None:
            self.not_preferred_node_num = m.get('NotPreferredNodeNum')
        if m.get('NotSyncingNodeNum') is not None:
            self.not_syncing_node_num = m.get('NotSyncingNodeNum')
        if m.get('PreferredNodeNum') is not None:
            self.preferred_node_num = m.get('PreferredNodeNum')
        if m.get('SyncedNodeNum') is not None:
            self.synced_node_num = m.get('SyncedNodeNum')
        return self


class DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo(TeaModel):
    def __init__(
        self,
        exception_node_num: int = None,
        normal_node_num: int = None,
        not_preferred_node_num: int = None,
        not_syncing_node_num: int = None,
        preferred_node_num: int = None,
        synced_node_num: int = None,
    ):
        # The number of abnormal nodes.
        self.exception_node_num = exception_node_num
        # The number of normal nodes.
        self.normal_node_num = normal_node_num
        # The number of nodes whose roles are reversed.
        self.not_preferred_node_num = not_preferred_node_num
        # The number of unsynchronized nodes.
        self.not_syncing_node_num = not_syncing_node_num
        # The number of nodes whose roles are normal.
        self.preferred_node_num = preferred_node_num
        # The number of synchronized nodes.
        self.synced_node_num = synced_node_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_node_num is not None:
            result['ExceptionNodeNum'] = self.exception_node_num
        if self.normal_node_num is not None:
            result['NormalNodeNum'] = self.normal_node_num
        if self.not_preferred_node_num is not None:
            result['NotPreferredNodeNum'] = self.not_preferred_node_num
        if self.not_syncing_node_num is not None:
            result['NotSyncingNodeNum'] = self.not_syncing_node_num
        if self.preferred_node_num is not None:
            result['PreferredNodeNum'] = self.preferred_node_num
        if self.synced_node_num is not None:
            result['SyncedNodeNum'] = self.synced_node_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionNodeNum') is not None:
            self.exception_node_num = m.get('ExceptionNodeNum')
        if m.get('NormalNodeNum') is not None:
            self.normal_node_num = m.get('NormalNodeNum')
        if m.get('NotPreferredNodeNum') is not None:
            self.not_preferred_node_num = m.get('NotPreferredNodeNum')
        if m.get('NotSyncingNodeNum') is not None:
            self.not_syncing_node_num = m.get('NotSyncingNodeNum')
        if m.get('PreferredNodeNum') is not None:
            self.preferred_node_num = m.get('PreferredNodeNum')
        if m.get('SyncedNodeNum') is not None:
            self.synced_node_num = m.get('SyncedNodeNum')
        return self


class DescribeDBInstanceDiagnosisSummaryResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeDBInstanceDiagnosisSummaryResponseBodyItems] = None,
        master_status_info: DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo = None,
        page_number: str = None,
        request_id: str = None,
        segment_status_info: DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo = None,
        total_count: str = None,
    ):
        # Details of instance nodes.
        self.items = items
        # State statistics of the coordinator node.
        self.master_status_info = master_status_info
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # State statistics of compute nodes.
        self.segment_status_info = segment_status_info
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.master_status_info:
            self.master_status_info.validate()
        if self.segment_status_info:
            self.segment_status_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.master_status_info is not None:
            result['MasterStatusInfo'] = self.master_status_info.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.segment_status_info is not None:
            result['SegmentStatusInfo'] = self.segment_status_info.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceDiagnosisSummaryResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('MasterStatusInfo') is not None:
            temp_model = DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo()
            self.master_status_info = temp_model.from_map(m['MasterStatusInfo'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SegmentStatusInfo') is not None:
            temp_model = DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo()
            self.segment_status_info = temp_model.from_map(m['SegmentStatusInfo'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceDiagnosisSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceDiagnosisSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceDiagnosisSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceErrorLogRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        host: str = None,
        keywords: str = None,
        log_level: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        user: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # This parameter is not supported in Alibaba Cloud public cloud.
        self.host = host
        # One or more keywords that can be used to query error logs.
        self.keywords = keywords
        # The level of the logs to query. Valid values:
        # 
        # *   **ALL**: queries all error logs.
        # *   **PANIC**: queries only abnormal-level logs.
        # *   **FATAL**: queries only critical-level logs.
        # *   **ERROR**: queries only error-level logs.
        self.log_level = log_level
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **20**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **20**.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.host is not None:
            result['Host'] = self.host
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDBInstanceErrorLogResponseBodyItems(TeaModel):
    def __init__(
        self,
        database: str = None,
        host: str = None,
        log_context: str = None,
        log_level: str = None,
        time: int = None,
        user: str = None,
    ):
        # The name of the database.
        self.database = database
        # This parameter is not supported.
        self.host = host
        # The content of the error log.
        self.log_context = log_context
        # The level of the queried log.
        self.log_level = log_level
        # The time when the log was generated. The time is displayed in UTC.
        self.time = time
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.host is not None:
            result['Host'] = self.host
        if self.log_context is not None:
            result['LogContext'] = self.log_context
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.time is not None:
            result['Time'] = self.time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('LogContext') is not None:
            self.log_context = m.get('LogContext')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDBInstanceErrorLogResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeDBInstanceErrorLogResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the error logs.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceErrorLogResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceErrorLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceErrorLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceErrorLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceIPArrayListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray(TeaModel):
    def __init__(
        self,
        dbinstance_iparray_attribute: str = None,
        dbinstance_iparray_name: str = None,
        security_iplist: str = None,
    ):
        # The attribute of the IP address whitelist. By default, this parameter is empty. A whitelist with the `hidden` attribute does not appear in the console.
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute
        # The name of the IP address whitelist.
        self.dbinstance_iparray_name = dbinstance_iparray_name
        # The IP addresses listed in the whitelist. You can add up to 1,000 IP addresses to the whitelist. Separate multiple IP addresses with commas (,). The IP addresses must use one of the following formats:
        # 
        # *   0.0.0.0/0
        # *   10.23.12.24. This is a standard IP address.
        # *   10.23.12.24/24. This is a CIDR block. The value `/24` indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value in the range of `1 to 32`.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeDBInstanceIPArrayListResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbinstance_iparray: List[DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray] = None,
    ):
        self.dbinstance_iparray = dbinstance_iparray

    def validate(self):
        if self.dbinstance_iparray:
            for k in self.dbinstance_iparray:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceIPArray'] = []
        if self.dbinstance_iparray is not None:
            for k in self.dbinstance_iparray:
                result['DBInstanceIPArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_iparray = []
        if m.get('DBInstanceIPArray') is not None:
            for k in m.get('DBInstanceIPArray'):
                temp_model = DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray()
                self.dbinstance_iparray.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceIPArrayListResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDBInstanceIPArrayListResponseBodyItems = None,
        request_id: str = None,
    ):
        # Details of the IP address whitelists.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBInstanceIPArrayListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceIPArrayListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceIPArrayListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceIPArrayListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceIndexUsageRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **20**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **20**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDBInstanceIndexUsageResponseBodyItems(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        index_def: str = None,
        index_name: str = None,
        index_scan_times: int = None,
        index_size: str = None,
        is_partition_table: bool = None,
        parent_table_name: str = None,
        schema_name: str = None,
        table_name: str = None,
        time_last_updated: str = None,
    ):
        # The name of the database.
        self.database_name = database_name
        # The definition of the index.
        self.index_def = index_def
        # The name of the index.
        self.index_name = index_name
        # The number of index scans.
        self.index_scan_times = index_scan_times
        # The size of the index. Unit: bytes.
        self.index_size = index_size
        # Indicates whether the table is a partitioned table. Valid values:
        # 
        # *   **true**: The table is a partitioned table.
        # *   **false**: The table is not a partitioned table.
        self.is_partition_table = is_partition_table
        # The name of the parent table.
        self.parent_table_name = parent_table_name
        # The name of the schema.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name
        # The time when the table was last deleted, inserted, or updated.
        self.time_last_updated = time_last_updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.index_def is not None:
            result['IndexDef'] = self.index_def
        if self.index_name is not None:
            result['IndexName'] = self.index_name
        if self.index_scan_times is not None:
            result['IndexScanTimes'] = self.index_scan_times
        if self.index_size is not None:
            result['IndexSize'] = self.index_size
        if self.is_partition_table is not None:
            result['IsPartitionTable'] = self.is_partition_table
        if self.parent_table_name is not None:
            result['ParentTableName'] = self.parent_table_name
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IndexDef') is not None:
            self.index_def = m.get('IndexDef')
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')
        if m.get('IndexScanTimes') is not None:
            self.index_scan_times = m.get('IndexScanTimes')
        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')
        if m.get('IsPartitionTable') is not None:
            self.is_partition_table = m.get('IsPartitionTable')
        if m.get('ParentTableName') is not None:
            self.parent_table_name = m.get('ParentTableName')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')
        return self


class DescribeDBInstanceIndexUsageResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeDBInstanceIndexUsageResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of index usage.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceIndexUsageResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceIndexUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceIndexUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceIndexUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceNetInfoRequest(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
    ):
        self.connection_string = connection_string
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query details about all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        connection_string: str = None,
        ipaddress: str = None,
        iptype: str = None,
        port: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        # The IP address type of the instance.
        self.address_type = address_type
        # The endpoint used to connect to the instance.
        self.connection_string = connection_string
        # The IP address of the instance.
        self.ipaddress = ipaddress
        # The type of IP address.
        # 
        # *   Valid values for instances in the classic network: Inner and Public
        # *   Valid values for instances in a virtual private cloud (VPC): Private and Public
        self.iptype = iptype
        # The port number used to connect to the instance.
        self.port = port
        # The ID of the VPC.
        self.vpcid = vpcid
        # The ID of the vSwitch. Multiple IDs are separated by commas (,).
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.iptype is not None:
            result['IPType'] = self.iptype
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos(TeaModel):
    def __init__(
        self,
        dbinstance_net_info: List[DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo] = None,
    ):
        self.dbinstance_net_info = dbinstance_net_info

    def validate(self):
        if self.dbinstance_net_info:
            for k in self.dbinstance_net_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceNetInfo'] = []
        if self.dbinstance_net_info is not None:
            for k in self.dbinstance_net_info:
                result['DBInstanceNetInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_net_info = []
        if m.get('DBInstanceNetInfo') is not None:
            for k in m.get('DBInstanceNetInfo'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo()
                self.dbinstance_net_info.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceNetInfoResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_net_infos: DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos = None,
        instance_network_type: str = None,
        request_id: str = None,
    ):
        # The connection information of the instance.
        self.dbinstance_net_infos = dbinstance_net_infos
        # The network type of the instance. 
        # 
        # *   **VPC**: a virtual private cloud (VPC)
        # *   **Classic**: classic network
        self.instance_network_type = instance_network_type
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dbinstance_net_infos:
            self.dbinstance_net_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_net_infos is not None:
            result['DBInstanceNetInfos'] = self.dbinstance_net_infos.to_map()
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceNetInfos') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos()
            self.dbinstance_net_infos = temp_model.from_map(m['DBInstanceNetInfos'])
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceNetInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceNetInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancePerformanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        key: str = None,
        resource_group_id: str = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # The performance metric. Separate multiple values with commas (,). For more information, see [Performance parameters](~~86943~~).
        self.key = key
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstancePerformanceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        engine: str = None,
        performance_keys: List[str] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The end time of the query.
        self.end_time = end_time
        # The database engine of the instance.
        self.engine = engine
        # Details of the performance metrics. Format: {perf1, perf2, perf3, …}.
        self.performance_keys = performance_keys
        # The ID of the request.
        self.request_id = request_id
        # The start time of the query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('PerformanceKeys') is not None:
            self.performance_keys = m.get('PerformanceKeys')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstancePerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstancePerformanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstancePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancePlansRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        plan_create_date: str = None,
        plan_desc: str = None,
        plan_id: str = None,
        plan_schedule_type: str = None,
        plan_type: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The time used to filter plans. If you specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format, the plans created before this time are returned. The time must be in UTC. If you do not specify this parameter, all plans are returned.
        self.plan_create_date = plan_create_date
        # The description of the plan.
        self.plan_desc = plan_desc
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](~~449398~~) operation to query the details of plans, including plan IDs.
        self.plan_id = plan_id
        # The execution mode of the plan. Valid values:
        # 
        # *   **Postpone**: The plan is executed later.
        # *   **Regular**: The plan is executed periodically.
        self.plan_schedule_type = plan_schedule_type
        # The type of the plan. Valid values:
        # 
        # *   **PauseResume**: pauses and resumes an instance.
        # *   **Resize**: scales an instance.
        self.plan_type = plan_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_create_date is not None:
            result['PlanCreateDate'] = self.plan_create_date
        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_schedule_type is not None:
            result['PlanScheduleType'] = self.plan_schedule_type
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanCreateDate') is not None:
            self.plan_create_date = m.get('PlanCreateDate')
        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanScheduleType') is not None:
            self.plan_schedule_type = m.get('PlanScheduleType')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        return self


class DescribeDBInstancePlansResponseBodyItemsPlanList(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        plan_config: str = None,
        plan_desc: str = None,
        plan_end_date: str = None,
        plan_id: str = None,
        plan_name: str = None,
        plan_schedule_type: str = None,
        plan_start_date: str = None,
        plan_status: str = None,
        plan_type: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The execution information of the plan.
        self.plan_config = plan_config
        # The description of the plan.
        self.plan_desc = plan_desc
        # The end time of the plan. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is returned only for periodically executed plans.
        self.plan_end_date = plan_end_date
        # The ID of the plan.
        self.plan_id = plan_id
        # The name of the plan.
        self.plan_name = plan_name
        # The execution mode of the plan. Valid values:
        # 
        # *   **Postpone**: The plan is executed later.
        # *   **Regular**: The plan is executed periodically.
        self.plan_schedule_type = plan_schedule_type
        # The start time of the plan. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is returned only for periodically executed plans.
        self.plan_start_date = plan_start_date
        # The state of the plan. Valid values:
        # 
        # *   **active**: The plan is running.
        # *   **cancel**: The plan is canceled.
        # *   **deleted**: The plan is deleted.
        # *   **finished**: The plan execution is complete.
        self.plan_status = plan_status
        # The type of the plan. Valid values:
        # 
        # *   **PauseResume**: pauses and resumes an instance.
        # *   **Resize**: scales an instance.
        self.plan_type = plan_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.plan_config is not None:
            result['PlanConfig'] = self.plan_config
        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc
        if self.plan_end_date is not None:
            result['PlanEndDate'] = self.plan_end_date
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_schedule_type is not None:
            result['PlanScheduleType'] = self.plan_schedule_type
        if self.plan_start_date is not None:
            result['PlanStartDate'] = self.plan_start_date
        if self.plan_status is not None:
            result['PlanStatus'] = self.plan_status
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PlanConfig') is not None:
            self.plan_config = m.get('PlanConfig')
        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')
        if m.get('PlanEndDate') is not None:
            self.plan_end_date = m.get('PlanEndDate')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanScheduleType') is not None:
            self.plan_schedule_type = m.get('PlanScheduleType')
        if m.get('PlanStartDate') is not None:
            self.plan_start_date = m.get('PlanStartDate')
        if m.get('PlanStatus') is not None:
            self.plan_status = m.get('PlanStatus')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        return self


class DescribeDBInstancePlansResponseBodyItems(TeaModel):
    def __init__(
        self,
        plan_list: List[DescribeDBInstancePlansResponseBodyItemsPlanList] = None,
    ):
        self.plan_list = plan_list

    def validate(self):
        if self.plan_list:
            for k in self.plan_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PlanList'] = []
        if self.plan_list is not None:
            for k in self.plan_list:
                result['PlanList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plan_list = []
        if m.get('PlanList') is not None:
            for k in m.get('PlanList'):
                temp_model = DescribeDBInstancePlansResponseBodyItemsPlanList()
                self.plan_list.append(temp_model.from_map(k))
        return self


class DescribeDBInstancePlansResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        items: DescribeDBInstancePlansResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        status: str = None,
        total_record_count: int = None,
    ):
        # The error message returned.
        # 
        # This parameter is returned only when the operation fails.
        self.error_message = error_message
        # Details of the plans.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
        self.status = status
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Items') is not None:
            temp_model = DescribeDBInstancePlansResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeDBInstancePlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstancePlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstancePlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceSSLResponseBody(TeaModel):
    def __init__(
        self,
        cert_common_name: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        request_id: str = None,
        sslenabled: bool = None,
        sslexpired_time: str = None,
    ):
        # The name of the SSL certificate.
        self.cert_common_name = cert_common_name
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The name of the instance.
        self.dbinstance_name = dbinstance_name
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether SSL encryption is enabled.
        self.sslenabled = sslenabled
        # The expiration time of the SSL certificate.
        self.sslexpired_time = sslexpired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        return self


class DescribeDBInstanceSSLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceSSLResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstancesRequest(TeaModel):
    def __init__(
        self,
        dbinstance_categories: List[str] = None,
        dbinstance_description: str = None,
        dbinstance_ids: str = None,
        dbinstance_modes: List[str] = None,
        dbinstance_statuses: List[str] = None,
        instance_deploy_types: List[str] = None,
        instance_network_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[DescribeDBInstancesRequestTag] = None,
    ):
        # The edition of the instance. Separate multiple values with commas (,). Valid values:
        # 
        # *   **basic**: Basic Edition
        # *   **highavailability**: High-availability Edition
        # *   **finance**: Enterprise Edition
        self.dbinstance_categories = dbinstance_categories
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance. Separate multiple IDs with commas (,).
        self.dbinstance_ids = dbinstance_ids
        # The resource type of the instance. Separate multiple values with commas (,). Valid values:
        # 
        # *   **serverless**: Serverless mode
        # *   **storageelastic**: elastic storage mode
        # *   **classic**: reserved storage mode
        self.dbinstance_modes = dbinstance_modes
        # The state of the instance. Separate multiple values with commas (,). For more information, see [Instance statuses](~~86944~~).
        # 
        # >  The value of this parameter must be in lowercase.
        self.dbinstance_statuses = dbinstance_statuses
        # This parameter is no longer used.
        self.instance_deploy_types = instance_deploy_types
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**\
        # *   **Classic**\
        # 
        # >  If you do not specify this parameter, instances of both network types are returned.
        self.instance_network_type = instance_network_type
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_categories is not None:
            result['DBInstanceCategories'] = self.dbinstance_categories
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_modes is not None:
            result['DBInstanceModes'] = self.dbinstance_modes
        if self.dbinstance_statuses is not None:
            result['DBInstanceStatuses'] = self.dbinstance_statuses
        if self.instance_deploy_types is not None:
            result['InstanceDeployTypes'] = self.instance_deploy_types
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceCategories') is not None:
            self.dbinstance_categories = m.get('DBInstanceCategories')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceModes') is not None:
            self.dbinstance_modes = m.get('DBInstanceModes')
        if m.get('DBInstanceStatuses') is not None:
            self.dbinstance_statuses = m.get('DBInstanceStatuses')
        if m.get('InstanceDeployTypes') is not None:
            self.instance_deploy_types = m.get('InstanceDeployTypes')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        dbinstance_categories_shrink: str = None,
        dbinstance_description: str = None,
        dbinstance_ids: str = None,
        dbinstance_modes_shrink: str = None,
        dbinstance_statuses_shrink: str = None,
        instance_deploy_types_shrink: str = None,
        instance_network_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[DescribeDBInstancesShrinkRequestTag] = None,
    ):
        # The edition of the instance. Separate multiple values with commas (,). Valid values:
        # 
        # *   **basic**: Basic Edition
        # *   **highavailability**: High-availability Edition
        # *   **finance**: Enterprise Edition
        self.dbinstance_categories_shrink = dbinstance_categories_shrink
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance. Separate multiple IDs with commas (,).
        self.dbinstance_ids = dbinstance_ids
        # The resource type of the instance. Separate multiple values with commas (,). Valid values:
        # 
        # *   **serverless**: Serverless mode
        # *   **storageelastic**: elastic storage mode
        # *   **classic**: reserved storage mode
        self.dbinstance_modes_shrink = dbinstance_modes_shrink
        # The state of the instance. Separate multiple values with commas (,). For more information, see [Instance statuses](~~86944~~).
        # 
        # >  The value of this parameter must be in lowercase.
        self.dbinstance_statuses_shrink = dbinstance_statuses_shrink
        # This parameter is no longer used.
        self.instance_deploy_types_shrink = instance_deploy_types_shrink
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**\
        # *   **Classic**\
        # 
        # >  If you do not specify this parameter, instances of both network types are returned.
        self.instance_network_type = instance_network_type
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_categories_shrink is not None:
            result['DBInstanceCategories'] = self.dbinstance_categories_shrink
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_modes_shrink is not None:
            result['DBInstanceModes'] = self.dbinstance_modes_shrink
        if self.dbinstance_statuses_shrink is not None:
            result['DBInstanceStatuses'] = self.dbinstance_statuses_shrink
        if self.instance_deploy_types_shrink is not None:
            result['InstanceDeployTypes'] = self.instance_deploy_types_shrink
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceCategories') is not None:
            self.dbinstance_categories_shrink = m.get('DBInstanceCategories')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceModes') is not None:
            self.dbinstance_modes_shrink = m.get('DBInstanceModes')
        if m.get('DBInstanceStatuses') is not None:
            self.dbinstance_statuses_shrink = m.get('DBInstanceStatuses')
        if m.get('InstanceDeployTypes') is not None:
            self.instance_deploy_types_shrink = m.get('InstanceDeployTypes')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstancesResponseBodyItemsDBInstanceTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyItemsDBInstance(TeaModel):
    def __init__(
        self,
        connection_mode: str = None,
        create_time: str = None,
        dbinstance_category: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_mode: str = None,
        dbinstance_net_type: str = None,
        dbinstance_status: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        instance_deploy_type: str = None,
        instance_network_type: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        master_node_num: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        seg_node_num: str = None,
        serverless_mode: str = None,
        storage_size: str = None,
        storage_type: str = None,
        tags: DescribeDBInstancesResponseBodyItemsDBInstanceTags = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # An invalid parameter. It is no longer returned when you call this operation.
        # 
        # You can call the [DescribeDBInstanceAttribute](~~86910~~) operation to query the access mode of an instance.
        self.connection_mode = connection_mode
        # The time when the instance was created. The time is displayed in UTC.
        self.create_time = create_time
        # The edition of the instance. Valid values:
        # 
        # *   **Basic**: Basic Edition
        # *   **HighAvailability**: High-availability Edition
        # *   **Finance**: Enterprise Edition
        self.dbinstance_category = dbinstance_category
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The resource type of the instance. Valid values:
        # 
        # *   **Serverless**: Serverless mode
        # *   **StorageElastic**: elastic storage mode
        # *   **Classic**: reserved storage mode
        self.dbinstance_mode = dbinstance_mode
        # The type of the network interface card (NIC) that is used by the instance. Valid values:
        # 
        # *   **0**: Internet
        # *   **1**: internal network
        # *   **2**: VPC
        self.dbinstance_net_type = dbinstance_net_type
        # The state of the instance. For more information, see [Instance statuses](~~86944~~).
        self.dbinstance_status = dbinstance_status
        # The database engine that the instance runs.
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        # The expiration time of the instance. The time is displayed in UTC.
        # 
        # >  For pay-as-you-go instances, `2999-09-08T16:00:00Z` is returned.
        self.expire_time = expire_time
        # The resource type of the instance. Valid values:
        # 
        # *   **cluster**: elastic storage mode or Serverless mode
        # *   **replicaSet**: reserved storage mode
        self.instance_deploy_type = instance_deploy_type
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**\
        # *   **VPC**\
        self.instance_network_type = instance_network_type
        # The lock mode of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked due to instance restoration.
        # *   **LockByDiskQuota**: The instance is automatically locked due to exhausted storage.
        # *   **LockReadInstanceByDiskQuota**: The instance is a read-only instance and is automatically locked due to exhausted storage.
        self.lock_mode = lock_mode
        # The reason why the cluster is locked.
        # 
        # >  This parameter is returned only when the cluster is locked. The value is **instance_expire**.
        self.lock_reason = lock_reason
        # The number of coordinator nodes.
        self.master_node_num = master_node_num
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The number of compute nodes.
        self.seg_node_num = seg_node_num
        # The type of the Serverless mode. Valid values:
        # 
        # *   **Manual**: manual scheduling
        # *   **Auto**: automatic scheduling
        # 
        # >  This parameter is returned only for instances in Serverless mode.
        self.serverless_mode = serverless_mode
        # The storage capacity. Unit: GB.
        self.storage_size = storage_size
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd**: enhanced SSD (ESSD)
        # *   **cloud_efficiency**: ultra disk
        self.storage_type = storage_type
        # The tags of the instance. Each tag is a key-value pair.
        self.tags = tags
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_deploy_type is not None:
            result['InstanceDeployType'] = self.instance_deploy_type
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceDeployType') is not None:
            self.instance_deploy_type = m.get('InstanceDeployType')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstancesResponseBodyItemsDBInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbinstance: List[DescribeDBInstancesResponseBodyItemsDBInstance] = None,
    ):
        self.dbinstance = dbinstance

    def validate(self):
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k in self.dbinstance:
                result['DBInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k in m.get('DBInstance'):
                temp_model = DescribeDBInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDBInstancesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # Details of the instance.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBInstancesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataBackupsRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_mode: str = None,
        backup_status: str = None,
        dbinstance_id: str = None,
        data_type: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The ID of the backup set. If you specify the BackupId parameter, the details of the backup set are returned.
        self.backup_id = backup_id
        # The backup mode. Valid values:
        # 
        # *   Automated: automatic backup
        # *   Manual: manual backup
        # 
        # If you do not specify this parameter, the records of the backup sets in all modes are returned.
        self.backup_mode = backup_mode
        # The status of the backup set. Valid values:
        # 
        # *   Success: The backup is complete.
        # *   Failed: The backup task fails.
        # 
        # If you do not specify this parameter, the records of the backup sets in all states are returned.
        self.backup_status = backup_status
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The type of the backup. Valid values:
        # 
        # *   DATA: full backup
        # *   RESTOREPOI: point-in-time backup
        # 
        # If you do not specify this parameter, the records of the full backup set are returned.
        self.data_type = data_type
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.end_time = end_time
        # The number of the page to return. The value must be an integer that is larger than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        # 
        # Default value: 30.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataBackupsResponseBodyItems(TeaModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_end_time_local: str = None,
        backup_mode: str = None,
        backup_set_id: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_start_time_local: str = None,
        backup_status: str = None,
        bakset_name: str = None,
        consistent_time: int = None,
        dbinstance_id: str = None,
        data_type: str = None,
    ):
        # The UTC time when the backup ended. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.backup_end_time = backup_end_time
        # The local time when the backup ended. The time is in the yyyy-MM-dd HH:mm:ss format. The time is your local time.
        self.backup_end_time_local = backup_end_time_local
        # The backup mode.
        # 
        # Valid values for full backup:
        # 
        # *   Automated: automatic backup
        # *   Manual: manual backup
        # 
        # Valid values for point-in-time backup:
        # 
        # *   Automated: point-in-time backup after full backup
        # *   Manual: manual point-in-time backup
        # *   Period: point-in-time backup that is triggered by a backup policy
        self.backup_mode = backup_mode
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        # The size of the backup file. Unit: bytes.
        self.backup_size = backup_size
        # The UTC time when the backup started. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.backup_start_time = backup_start_time
        # The local time when the backup started. The time is in the yyyy-MM-dd HH:mm:ss format. The time is your local time.
        self.backup_start_time_local = backup_start_time_local
        # The status of the backup set. Valid values:
        # 
        # *   Success
        # *   Failure
        self.backup_status = backup_status
        # The name of a point-in-time backup set or the full backup set.
        self.bakset_name = bakset_name
        # *   For full backup, this parameter indicates the point in time at which the data in the data backup file is consistent.
        # *   For point-in-time backup, this parameter indicates that the returned point in time is a timestamp.
        self.consistent_time = consistent_time
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The type of the backup. Valid values:
        # 
        # *   DATA: full backup
        # *   RESTOREPOI: point-in-time backup
        self.data_type = data_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_end_time_local is not None:
            result['BackupEndTimeLocal'] = self.backup_end_time_local
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_start_time_local is not None:
            result['BackupStartTimeLocal'] = self.backup_start_time_local
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.bakset_name is not None:
            result['BaksetName'] = self.bakset_name
        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupEndTimeLocal') is not None:
            self.backup_end_time_local = m.get('BackupEndTimeLocal')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStartTimeLocal') is not None:
            self.backup_start_time_local = m.get('BackupStartTimeLocal')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BaksetName') is not None:
            self.bakset_name = m.get('BaksetName')
        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        return self


class DescribeDataBackupsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeDataBackupsResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the backup sets.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of backup sets on the page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataBackupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataReDistributeInfoRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo(TeaModel):
    def __init__(
        self,
        message: str = None,
        progress: int = None,
        remain_time: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        self.message = message
        self.progress = progress
        self.remain_time = remain_time
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDataReDistributeInfoResponseBody(TeaModel):
    def __init__(
        self,
        data_re_distribute_info: DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo = None,
        request_id: str = None,
    ):
        self.data_re_distribute_info = data_re_distribute_info
        self.request_id = request_id

    def validate(self):
        if self.data_re_distribute_info:
            self.data_re_distribute_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_re_distribute_info is not None:
            result['DataReDistributeInfo'] = self.data_re_distribute_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataReDistributeInfo') is not None:
            temp_model = DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo()
            self.data_re_distribute_info = temp_model.from_map(m['DataReDistributeInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataReDistributeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataReDistributeInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataReDistributeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataShareInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        search_value: str = None,
    ):
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: 30.
        self.page_size = page_size
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The keyword used to filter instances, which can be an instance ID or instance description.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs and instance descriptions.
        self.search_value = search_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        return self


class DescribeDataShareInstancesResponseBodyItemsDBInstance(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbinstance_mode: str = None,
        data_share_status: str = None,
        description: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The resource type of the instance. Valid values:
        # 
        # *   **Serverless**: Serverless mode
        # *   **StorageElasic**: elastic storage mode
        # *   **Classic**: reserved storage mode
        self.dbinstance_mode = dbinstance_mode
        # The state of data sharing. Valid values:
        # 
        # *   **opening**: Data sharing is being enabled.
        # *   **opened**: Data sharing is enabled.
        # *   **closing**: Data sharing is being disabled.
        # *   **closed**: Data sharing is disabled.
        self.data_share_status = data_share_status
        # The description of the instance.
        self.description = description
        # The region ID of the instance.
        self.region_id = region_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.data_share_status is not None:
            result['DataShareStatus'] = self.data_share_status
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('DataShareStatus') is not None:
            self.data_share_status = m.get('DataShareStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDataShareInstancesResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbinstance: List[DescribeDataShareInstancesResponseBodyItemsDBInstance] = None,
    ):
        self.dbinstance = dbinstance

    def validate(self):
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k in self.dbinstance:
                result['DBInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k in m.get('DBInstance'):
                temp_model = DescribeDataShareInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        return self


class DescribeDataShareInstancesResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDataShareInstancesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # Details of the instances.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDataShareInstancesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeDataShareInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataShareInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataShareInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSharePerformanceRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        key: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time
        # The name of the performance metric. Separate multiple values with commas (,). Valid values:
        # 
        # *   **adbpg_datashare_topic_count**: the number of shared topics.
        # *   **adbpg_datashare_data_size_mb**: the amount of data shared.
        self.key = key
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataSharePerformanceResponseBodyPerformanceKeysSeriesValues(TeaModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
        # The value of the performance metric at a point in time.
        self.point = point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeDataSharePerformanceResponseBodyPerformanceKeysSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: List[DescribeDataSharePerformanceResponseBodyPerformanceKeysSeriesValues] = None,
    ):
        # The name of the performance metric.
        self.name = name
        # One or more values of the performance metric.
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeDataSharePerformanceResponseBodyPerformanceKeysSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeDataSharePerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(
        self,
        name: str = None,
        series: List[DescribeDataSharePerformanceResponseBodyPerformanceKeysSeries] = None,
        unit: str = None,
    ):
        # The name of the performance metric.
        self.name = name
        # Details of the performance metric.
        self.series = series
        # The unit of the performance metric.
        self.unit = unit

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDataSharePerformanceResponseBodyPerformanceKeysSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDataSharePerformanceResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performance_keys: List[DescribeDataSharePerformanceResponseBodyPerformanceKeys] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        self.dbcluster_id = dbcluster_id
        # The end time of the query.
        self.end_time = end_time
        # Details of data sharing performance metrics.
        self.performance_keys = performance_keys
        # The ID of the request.
        self.request_id = request_id
        # The start time of the query.
        self.start_time = start_time

    def validate(self):
        if self.performance_keys:
            for k in self.performance_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['PerformanceKeys'] = []
        if self.performance_keys is not None:
            for k in self.performance_keys:
                result['PerformanceKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performance_keys = []
        if m.get('PerformanceKeys') is not None:
            for k in m.get('PerformanceKeys'):
                temp_model = DescribeDataSharePerformanceResponseBodyPerformanceKeys()
                self.performance_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataSharePerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataSharePerformanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataSharePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisDimensionsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDiagnosisDimensionsResponseBody(TeaModel):
    def __init__(
        self,
        databases: List[str] = None,
        request_id: str = None,
        user_names: List[str] = None,
    ):
        # The name of the database.
        self.databases = databases
        # The ID of the request.
        self.request_id = request_id
        # The name of the database account.
        self.user_names = user_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.databases is not None:
            result['Databases'] = self.databases
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_names is not None:
            result['UserNames'] = self.user_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Databases') is not None:
            self.databases = m.get('Databases')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')
        return self


class DescribeDiagnosisDimensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisDimensionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiagnosisDimensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisMonitorPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        query_condition: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # The filter condition on queries. Specify the value in the JSON format. Valid values:
        # 
        # *   `{"Type":"maxCost", "Value":"100"}`: filters the top 100 queries that are the most time-consuming.
        # 
        # *   `{"Type":"status","Value":"finished"}`: filters completed queries.
        # 
        # *   `{"Type":"status","Value":"running"}`: filters running queries.
        # 
        # *   `{"Type":"cost","Min":"30","Max":"50"}`: filters the queries that consume 30 milliseconds or more and less than 50 milliseconds. You can customize a filter condition by setting **Min** and **Max**.
        # 
        #     *   If only **Min** is specified, the queries that consume a period of time that is greater than or equal to the Min value are filtered.
        #     *   If only **Max** is specified, the queries that consume a period of time that is less than the Max value are filtered.
        #     *   If both **Min** and **Max** are specified, the queries that consume a period of time that is greater than or equal to the **Min** value and less than the **Max** value are filtered.
        self.query_condition = query_condition
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisMonitorPerformanceResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        cost: int = None,
        database: str = None,
        query_id: str = None,
        start_time: int = None,
        status: str = None,
        user: str = None,
    ):
        # The execution duration of the query. Unit: milliseconds.
        self.cost = cost
        # The name of the database.
        self.database = database
        # The ID of the query. It is a unique identifier of the query.
        self.query_id = query_id
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The execution state of the query. Valid values:
        # 
        # *   **running**: The query is being executed.
        # *   **finished**: The query is complete.
        self.status = status
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.database is not None:
            result['Database'] = self.database
        if self.query_id is not None:
            result['QueryID'] = self.query_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisMonitorPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        performances: List[DescribeDiagnosisMonitorPerformanceResponseBodyPerformances] = None,
        performances_threshold: int = None,
        performances_truncated: bool = None,
        request_id: str = None,
    ):
        # Details of query execution.
        self.performances = performances
        # The threshold for the number of queries.
        self.performances_threshold = performances_threshold
        # Indicates whether the queries are truncated when the number of queries exceeds the threshold. Valid values:
        # 
        # *   **true**: The queries are truncated.
        # *   **false**: The queries are not truncated.
        self.performances_truncated = performances_truncated
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.performances_threshold is not None:
            result['PerformancesThreshold'] = self.performances_threshold
        if self.performances_truncated is not None:
            result['PerformancesTruncated'] = self.performances_truncated
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDiagnosisMonitorPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('PerformancesThreshold') is not None:
            self.performances_threshold = m.get('PerformancesThreshold')
        if m.get('PerformancesTruncated') is not None:
            self.performances_truncated = m.get('PerformancesTruncated')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDiagnosisMonitorPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisMonitorPerformanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiagnosisMonitorPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisRecordsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        keyword: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        query_condition: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # The keyword of the SQL statement.
        self.keyword = keyword
        # The order of fields in the console. You do not need to specify this parameter.
        self.order = order
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The filter condition on queries. Specify the value in the JSON format. Valid values:
        # 
        # *   `{"Type":"maxCost", "Value":"100"}`: filters the top 100 queries that are the most time-consuming.
        # 
        # *   `{"Type":"status","Value":"finished"}`: filters completed queries.
        # 
        # *   `{"Type":"status","Value":"running"}`: filters running queries.
        # 
        # *   `{"Type":"cost","Min":"30","Max":"50"}`: filters the queries that consume 30 milliseconds or more and less than 50 milliseconds. You can customize a filter condition by setting **Min** and **Max**.
        # 
        #     *   If only **Min** is specified, the queries that consume a period of time that is greater than or equal to the Min value are filtered.
        #     *   If only **Max** is specified, the queries that consume a period of time that is less than the Max value are filtered.
        #     *   If both **Min** and **Max** are specified, the queries that consume a period of time that is greater than or equal to the **Min** value and less than the **Max** value are filtered.
        self.query_condition = query_condition
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisRecordsResponseBodyItems(TeaModel):
    def __init__(
        self,
        database: str = None,
        duration: int = None,
        query_id: str = None,
        sqlstmt: str = None,
        sqltruncated: bool = None,
        sqltruncated_threshold: int = None,
        session_id: str = None,
        start_time: int = None,
        status: str = None,
        user: str = None,
    ):
        # The name of the database.
        self.database = database
        # The execution duration of the query. Unit: seconds.
        self.duration = duration
        # The ID of the query. It is a unique identifier of the query.
        self.query_id = query_id
        # The SQL statement.
        self.sqlstmt = sqlstmt
        # Indicates whether the SQL statement needs to be truncated. Valid values:
        # 
        # *   **true**: The SQL statement needs to be truncated.
        # *   **false**: The SQL statement does not need to be truncated.
        self.sqltruncated = sqltruncated
        # The threshold used to determine whether an SQL statement must be truncated. The value is the number of characters.
        self.sqltruncated_threshold = sqltruncated_threshold
        # The ID of the session that contains the query.
        self.session_id = session_id
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The execution state of the query. Valid values:
        # 
        # *   **running**: The query is being executed.
        # *   **finished**: The query is complete.
        self.status = status
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.query_id is not None:
            result['QueryID'] = self.query_id
        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt
        if self.sqltruncated is not None:
            result['SQLTruncated'] = self.sqltruncated
        if self.sqltruncated_threshold is not None:
            result['SQLTruncatedThreshold'] = self.sqltruncated_threshold
        if self.session_id is not None:
            result['SessionID'] = self.session_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')
        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')
        if m.get('SQLTruncated') is not None:
            self.sqltruncated = m.get('SQLTruncated')
        if m.get('SQLTruncatedThreshold') is not None:
            self.sqltruncated_threshold = m.get('SQLTruncatedThreshold')
        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisRecordsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeDiagnosisRecordsResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of SQL queries.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDiagnosisRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiagnosisRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiagnosisRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisSQLInfoRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        query_id: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The ID of the query. It is a unique identifier of the query.
        # 
        # >  You can call the [DescribeDiagnosisRecords](~~450511~~) operation to query the query ID.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.query_id is not None:
            result['QueryID'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')
        return self


class DescribeDiagnosisSQLInfoResponseBody(TeaModel):
    def __init__(
        self,
        database: str = None,
        duration: int = None,
        max_output_rows: str = None,
        query_id: str = None,
        query_plan: str = None,
        request_id: str = None,
        sqlstmt: str = None,
        session_id: str = None,
        sorted_metrics: str = None,
        start_time: int = None,
        status: str = None,
        text_plan: str = None,
        user: str = None,
    ):
        # The name of the database.
        self.database = database
        # The execution duration of the query. Unit: seconds.
        self.duration = duration
        # The maximum number of output rows.
        self.max_output_rows = max_output_rows
        # The ID of the query.
        self.query_id = query_id
        # The information of the operator.
        self.query_plan = query_plan
        # The ID of the request.
        self.request_id = request_id
        # The SQL statement.
        self.sqlstmt = sqlstmt
        # The ID of the session that contains the query.
        self.session_id = session_id
        # The sequence of metrics.
        self.sorted_metrics = sorted_metrics
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The execution state of the query. Valid values:
        # 
        # *   **running**: The query is being executed.
        # *   **finished**: The query execution is complete.
        self.status = status
        # The information of the execution plan.
        self.text_plan = text_plan
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.max_output_rows is not None:
            result['MaxOutputRows'] = self.max_output_rows
        if self.query_id is not None:
            result['QueryID'] = self.query_id
        if self.query_plan is not None:
            result['QueryPlan'] = self.query_plan
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt
        if self.session_id is not None:
            result['SessionID'] = self.session_id
        if self.sorted_metrics is not None:
            result['SortedMetrics'] = self.sorted_metrics
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.text_plan is not None:
            result['TextPlan'] = self.text_plan
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MaxOutputRows') is not None:
            self.max_output_rows = m.get('MaxOutputRows')
        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')
        if m.get('QueryPlan') is not None:
            self.query_plan = m.get('QueryPlan')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')
        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')
        if m.get('SortedMetrics') is not None:
            self.sorted_metrics = m.get('SortedMetrics')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TextPlan') is not None:
            self.text_plan = m.get('TextPlan')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisSQLInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisSQLInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiagnosisSQLInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadRecordsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDownloadRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        download_id: int = None,
        download_url: str = None,
        exception_msg: str = None,
        file_name: str = None,
        status: str = None,
    ):
        # The ID of the download record.
        self.download_id = download_id
        # The URL that can be used to download the file.
        self.download_url = download_url
        # The error message returned.
        self.exception_msg = exception_msg
        # The name of the file.
        self.file_name = file_name
        # The state of the upload task. After you call the DownloadDiagnosisRecords operation, query diagnostic information is first uploaded to Object Storage Service (OSS). After the upload task is complete, the query diagnostic information can be downloaded. Valid values:
        # 
        # *   **running**: uploading
        # *   **finished**: uploaded
        # *   **failed**: failed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDownloadRecordsResponseBody(TeaModel):
    def __init__(
        self,
        records: List[DescribeDownloadRecordsResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # Details of the download records.
        self.records = records
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDownloadRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDownloadRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDownloadRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadSQLLogsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDownloadSQLLogsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        download_id: int = None,
        download_url: str = None,
        exception_msg: str = None,
        file_name: str = None,
        status: str = None,
    ):
        self.download_id = download_id
        self.download_url = download_url
        self.exception_msg = exception_msg
        self.file_name = file_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDownloadSQLLogsResponseBody(TeaModel):
    def __init__(
        self,
        records: List[DescribeDownloadSQLLogsResponseBodyRecords] = None,
        request_id: str = None,
    ):
        self.records = records
        self.request_id = request_id

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDownloadSQLLogsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDownloadSQLLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadSQLLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDownloadSQLLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthStatusRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        key: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The performance metric that you want to query. Separate multiple values with commas (,). For more information, see [Performance parameters](~~86943~~).
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The status corresponding to the maximum storage usage among all compute nodes. Valid values:
        # 
        # *   **critical**: The compute node storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The compute node storage usage is greater than or equal to 80% and less than 90%.
        # *   **healthy**: The compute node storage usage is less than 80%.
        self.status = status
        # The metric value of maximum compute node storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The connection health status of the instance. Valid values:
        # 
        # *   **critical**: The instance connection usage is greater than 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The instance connection usage is greater than 90% and less than or equal to 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The instance connection usage is less than or equal to 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The instance connection usage is the maximum connection usage among all the coordinator and compute nodes.
        self.status = status
        # The metric value of instance connection usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The storage status of the instance. Valid values:
        # 
        # *   **critical**: The instance storage usage is greater than or equal to 90%. In this case, this metric is marked in red in the console and the instance is locked.
        # *   **warning**: The instance storage usage is greater than or equal to 70% and less than 90%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The instance storage usage is less than 70%. In this case, this metric is marked in green in the console.
        # 
        # >  The instance storage usage is the average storage usage of all compute nodes.
        self.status = status
        # The metric value of instance storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The status corresponding to the storage usage of the instance. Valid values:
        # 
        # *   **critical**: The instance storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The instance storage usage is greater than or equal to 70% and less than 90%.
        # *   **healthy**: The instance storage usage is less than 70%.
        # 
        # >  The instance storage usage is the average storage usage of all compute nodes.
        self.status = status
        # The metric value of instance storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The status corresponding to the maximum storage usage of the coordinator node. Valid values:
        # 
        # *   **critical**: The coordinator node storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The coordinator node storage usage is greater than or equal to 70% and less than 90%.
        # *   **healthy**: The coordinator node storage usage is less than 70%.
        self.status = status
        # The metric value of maximum coordinator node storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The availability status of the coordinator node. Valid values:
        # 
        # *   **critical**: Both the primary and standby coordinator nodes are unavailable. In this case, this metric is marked in red in the console.
        # *   **warning**: The primary or standby coordinator node is unavailable. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: Both the primary and standby coordinator nodes are available. In this case, this metric is marked in green in the console.
        self.status = status
        # The metric value of coordinator node availability status. Valid values:
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The availability status of compute nodes. Valid values:
        # 
        # *   **critical**: All the primary and secondary compute nodes are unavailable. In this case, this metric is marked in red in the console.
        # *   **warning**: Fifty percent or more than fifty percent of compute nodes are unavailable. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: All compute nodes are available. In this case, this metric is marked in green in the console.
        self.status = status
        # The metric value of compute node availability status.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The health status of the instance. Valid values:
        # 
        # *   **critical**: The coordinator node or a compute node is unavailable. In this case, this metric is marked in red in the console.
        # *   **healthy**: All nodes are available. In this case, this metric is marked in green in the console.
        self.status = status
        # The metric value of instance health status. Valid values:
        # 
        # *   **1**: healthy
        # *   **0**: critical
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The connection health status of the coordinator node. Valid values:
        # 
        # *   **critical**: The coordinator node connection usage is greater than 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The coordinator node connection usage is greater than or equal to 90% and less than 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The coordinator node connection usage is less than 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The coordinator node connection usage is the maximum connection usage of the coordinator node.
        self.status = status
        # The metric value of coordinator node connection usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusNodeMasterStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The health status of the coordinator node. Valid values:
        # 
        # *   **critical**: The primary or standby coordinator node is unavailable. In this case, this metric is marked in red in the console.
        # *   **healthy**: Both the primary and standby coordinator nodes are available. In this case, this metric is marked in green in the console.
        self.status = status
        # The metric value of coordinator node health status. Valid values:
        # 
        # *   **1**: healthy
        # *   **0**: critical
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The connection health status of compute nodes. Valid values:
        # 
        # *   **critical**: The compute node connection usage is greater than or equal to 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The compute node connection usage is greater than or equal to 90% and less than 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The compute node connection usage is less than 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The compute node connection usage is the maximum connection usage among all compute nodes.
        self.status = status
        # The metric value of maximum compute node connection usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The storage status of compute nodes. Valid values:
        # 
        # *   **critical**: The compute node storage usage is greater than or equal to 90%. In this case, this metric is marked in red in the console and the instance is locked.
        # *   **warning**: The compute node storage usage is greater than or equal to 80% and less than 90%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The compute node storage usage is less than 80%. In this case, this metric is marked in green in the console.
        # 
        # >  The compute node storage usage is the maximum storage usage among all compute nodes.
        self.status = status
        # The metric value of maximum compute node storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatus(TeaModel):
    def __init__(
        self,
        adbgp_segment_disk_usage_percent_max: DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax = None,
        adbpg_connection_status: DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus = None,
        adbpg_disk_status: DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus = None,
        adbpg_disk_usage_percent: DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent = None,
        adbpg_instance_cold_data_gb: DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb = None,
        adbpg_instance_hot_data_gb: DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb = None,
        adbpg_instance_total_data_gb: DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb = None,
        adbpg_master_disk_usage_percent_max: DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax = None,
        adbpg_master_status: DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus = None,
        adbpg_segment_status: DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus = None,
        adbpg_status: DescribeHealthStatusResponseBodyStatusAdbpgStatus = None,
        node_master_connection_status: DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus = None,
        node_master_status: DescribeHealthStatusResponseBodyStatusNodeMasterStatus = None,
        node_segment_connection_status: DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus = None,
        node_segment_disk_status: DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus = None,
    ):
        # The information of maximum compute node storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbgp_segment_disk_usage_percent_max = adbgp_segment_disk_usage_percent_max
        # The information of instance connection health status.
        self.adbpg_connection_status = adbpg_connection_status
        # The information of instance storage status.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_disk_status = adbpg_disk_status
        # The information of instance storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_disk_usage_percent = adbpg_disk_usage_percent
        self.adbpg_instance_cold_data_gb = adbpg_instance_cold_data_gb
        self.adbpg_instance_hot_data_gb = adbpg_instance_hot_data_gb
        self.adbpg_instance_total_data_gb = adbpg_instance_total_data_gb
        # The information of maximum coordinator node storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_master_disk_usage_percent_max = adbpg_master_disk_usage_percent_max
        # The information of coordinator node availability status.
        self.adbpg_master_status = adbpg_master_status
        # The information of compute node availability status.
        self.adbpg_segment_status = adbpg_segment_status
        # The information of instance health status.
        self.adbpg_status = adbpg_status
        # The information of coordinator node connection health status.
        self.node_master_connection_status = node_master_connection_status
        # The information of coordinator node health status.
        self.node_master_status = node_master_status
        # The information of compute node connection health status.
        self.node_segment_connection_status = node_segment_connection_status
        # The information of compute node storage status.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.node_segment_disk_status = node_segment_disk_status

    def validate(self):
        if self.adbgp_segment_disk_usage_percent_max:
            self.adbgp_segment_disk_usage_percent_max.validate()
        if self.adbpg_connection_status:
            self.adbpg_connection_status.validate()
        if self.adbpg_disk_status:
            self.adbpg_disk_status.validate()
        if self.adbpg_disk_usage_percent:
            self.adbpg_disk_usage_percent.validate()
        if self.adbpg_instance_cold_data_gb:
            self.adbpg_instance_cold_data_gb.validate()
        if self.adbpg_instance_hot_data_gb:
            self.adbpg_instance_hot_data_gb.validate()
        if self.adbpg_instance_total_data_gb:
            self.adbpg_instance_total_data_gb.validate()
        if self.adbpg_master_disk_usage_percent_max:
            self.adbpg_master_disk_usage_percent_max.validate()
        if self.adbpg_master_status:
            self.adbpg_master_status.validate()
        if self.adbpg_segment_status:
            self.adbpg_segment_status.validate()
        if self.adbpg_status:
            self.adbpg_status.validate()
        if self.node_master_connection_status:
            self.node_master_connection_status.validate()
        if self.node_master_status:
            self.node_master_status.validate()
        if self.node_segment_connection_status:
            self.node_segment_connection_status.validate()
        if self.node_segment_disk_status:
            self.node_segment_disk_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adbgp_segment_disk_usage_percent_max is not None:
            result['adbgp_segment_disk_usage_percent_max'] = self.adbgp_segment_disk_usage_percent_max.to_map()
        if self.adbpg_connection_status is not None:
            result['adbpg_connection_status'] = self.adbpg_connection_status.to_map()
        if self.adbpg_disk_status is not None:
            result['adbpg_disk_status'] = self.adbpg_disk_status.to_map()
        if self.adbpg_disk_usage_percent is not None:
            result['adbpg_disk_usage_percent'] = self.adbpg_disk_usage_percent.to_map()
        if self.adbpg_instance_cold_data_gb is not None:
            result['adbpg_instance_cold_data_gb'] = self.adbpg_instance_cold_data_gb.to_map()
        if self.adbpg_instance_hot_data_gb is not None:
            result['adbpg_instance_hot_data_gb'] = self.adbpg_instance_hot_data_gb.to_map()
        if self.adbpg_instance_total_data_gb is not None:
            result['adbpg_instance_total_data_gb'] = self.adbpg_instance_total_data_gb.to_map()
        if self.adbpg_master_disk_usage_percent_max is not None:
            result['adbpg_master_disk_usage_percent_max'] = self.adbpg_master_disk_usage_percent_max.to_map()
        if self.adbpg_master_status is not None:
            result['adbpg_master_status'] = self.adbpg_master_status.to_map()
        if self.adbpg_segment_status is not None:
            result['adbpg_segment_status'] = self.adbpg_segment_status.to_map()
        if self.adbpg_status is not None:
            result['adbpg_status'] = self.adbpg_status.to_map()
        if self.node_master_connection_status is not None:
            result['node_master_connection_status'] = self.node_master_connection_status.to_map()
        if self.node_master_status is not None:
            result['node_master_status'] = self.node_master_status.to_map()
        if self.node_segment_connection_status is not None:
            result['node_segment_connection_status'] = self.node_segment_connection_status.to_map()
        if self.node_segment_disk_status is not None:
            result['node_segment_disk_status'] = self.node_segment_disk_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adbgp_segment_disk_usage_percent_max') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax()
            self.adbgp_segment_disk_usage_percent_max = temp_model.from_map(m['adbgp_segment_disk_usage_percent_max'])
        if m.get('adbpg_connection_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus()
            self.adbpg_connection_status = temp_model.from_map(m['adbpg_connection_status'])
        if m.get('adbpg_disk_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus()
            self.adbpg_disk_status = temp_model.from_map(m['adbpg_disk_status'])
        if m.get('adbpg_disk_usage_percent') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent()
            self.adbpg_disk_usage_percent = temp_model.from_map(m['adbpg_disk_usage_percent'])
        if m.get('adbpg_instance_cold_data_gb') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb()
            self.adbpg_instance_cold_data_gb = temp_model.from_map(m['adbpg_instance_cold_data_gb'])
        if m.get('adbpg_instance_hot_data_gb') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb()
            self.adbpg_instance_hot_data_gb = temp_model.from_map(m['adbpg_instance_hot_data_gb'])
        if m.get('adbpg_instance_total_data_gb') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb()
            self.adbpg_instance_total_data_gb = temp_model.from_map(m['adbpg_instance_total_data_gb'])
        if m.get('adbpg_master_disk_usage_percent_max') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax()
            self.adbpg_master_disk_usage_percent_max = temp_model.from_map(m['adbpg_master_disk_usage_percent_max'])
        if m.get('adbpg_master_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus()
            self.adbpg_master_status = temp_model.from_map(m['adbpg_master_status'])
        if m.get('adbpg_segment_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus()
            self.adbpg_segment_status = temp_model.from_map(m['adbpg_segment_status'])
        if m.get('adbpg_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgStatus()
            self.adbpg_status = temp_model.from_map(m['adbpg_status'])
        if m.get('node_master_connection_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus()
            self.node_master_connection_status = temp_model.from_map(m['node_master_connection_status'])
        if m.get('node_master_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusNodeMasterStatus()
            self.node_master_status = temp_model.from_map(m['node_master_status'])
        if m.get('node_segment_connection_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus()
            self.node_segment_connection_status = temp_model.from_map(m['node_segment_connection_status'])
        if m.get('node_segment_disk_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus()
            self.node_segment_disk_status = temp_model.from_map(m['node_segment_disk_status'])
        return self


class DescribeHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        status: DescribeHealthStatusResponseBodyStatus = None,
    ):
        # The ID of instance.
        self.dbcluster_id = dbcluster_id
        # The ID of the request.
        self.request_id = request_id
        # The information of performance metrics. Each performance metric consists of the parameter name, status, and metric value. The metric information is returned only for the performance parameters specified by **Key**. For example, if you set **Key** to **adbpg_status**, only the metric information of **adbpg_status** is returned.
        # 
        # For more information about performance parameters, see [Performance parameters](~~86943~~).
        self.status = status

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class DescribeHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHealthStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogBackupsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.end_time = end_time
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeLogBackupsResponseBodyItems(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        dbinstance_id: str = None,
        log_file_name: str = None,
        log_file_size: int = None,
        log_time: str = None,
        segment_name: str = None,
    ):
        # The ID of the backup set.
        self.backup_id = backup_id
        # The ID of the coordinator node.
        self.dbinstance_id = dbinstance_id
        # The name of the log backup set that is stored in Object Storage Service (OSS).
        self.log_file_name = log_file_name
        # The size of the log backup set. Unit: bytes.
        self.log_file_size = log_file_size
        # The timestamp of the log.
        self.log_time = log_time
        # The name of the compute node.
        self.segment_name = segment_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.log_file_name is not None:
            result['LogFileName'] = self.log_file_name
        if self.log_file_size is not None:
            result['LogFileSize'] = self.log_file_size
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.segment_name is not None:
            result['SegmentName'] = self.segment_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('LogFileName') is not None:
            self.log_file_name = m.get('LogFileName')
        if m.get('LogFileSize') is not None:
            self.log_file_size = m.get('LogFileSize')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('SegmentName') is not None:
            self.segment_name = m.get('SegmentName')
        return self


class DescribeLogBackupsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeLogBackupsResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_log_size: int = None,
    ):
        # Details of the backup sets.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of backup sets on the current page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The total size of logs in the time range. Unit: bytes.
        self.total_log_size = total_log_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_log_size is not None:
            result['TotalLogSize'] = self.total_log_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeLogBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalLogSize') is not None:
            self.total_log_size = m.get('TotalLogSize')
        return self


class DescribeLogBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogBackupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLogBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModifyParameterLogRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query.
        self.end_time = end_time
        # The beginning of the time range to query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeModifyParameterLogResponseBodyChangelogs(TeaModel):
    def __init__(
        self,
        effect_time: str = None,
        parameter_name: str = None,
        parameter_valid: str = None,
        parameter_value_after: str = None,
        parameter_value_before: str = None,
    ):
        # The time when the configuration change takes effect.
        self.effect_time = effect_time
        # The name of the parameter.
        self.parameter_name = parameter_name
        # Indicates whether the configuration change takes effect.
        self.parameter_valid = parameter_valid
        # The original value of the parameter.
        self.parameter_value_after = parameter_value_after
        # The new value of the parameter.
        self.parameter_value_before = parameter_value_before

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_valid is not None:
            result['ParameterValid'] = self.parameter_valid
        if self.parameter_value_after is not None:
            result['ParameterValueAfter'] = self.parameter_value_after
        if self.parameter_value_before is not None:
            result['ParameterValueBefore'] = self.parameter_value_before
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValid') is not None:
            self.parameter_valid = m.get('ParameterValid')
        if m.get('ParameterValueAfter') is not None:
            self.parameter_value_after = m.get('ParameterValueAfter')
        if m.get('ParameterValueBefore') is not None:
            self.parameter_value_before = m.get('ParameterValueBefore')
        return self


class DescribeModifyParameterLogResponseBody(TeaModel):
    def __init__(
        self,
        changelogs: List[DescribeModifyParameterLogResponseBodyChangelogs] = None,
        request_id: str = None,
    ):
        # Details about the parameter reconfiguration logs.
        self.changelogs = changelogs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.changelogs:
            for k in self.changelogs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Changelogs'] = []
        if self.changelogs is not None:
            for k in self.changelogs:
                result['Changelogs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.changelogs = []
        if m.get('Changelogs') is not None:
            for k in m.get('Changelogs'):
                temp_model = DescribeModifyParameterLogResponseBodyChangelogs()
                self.changelogs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeModifyParameterLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeModifyParameterLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeModifyParameterLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        namespace: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        self.namespace = namespace
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        message: str = None,
        namespace: str = None,
        namespace_info: Dict[str, str] = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.message = message
        self.namespace = namespace
        self.namespace_info = namespace_info
        self.region_id = region_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_info is not None:
            result['NamespaceInfo'] = self.namespace_info
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceInfo') is not None:
            self.namespace_info = m.get('NamespaceInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        current_value: str = None,
        force_restart_instance: str = None,
        is_changeable_config: str = None,
        optional_range: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The current value of the parameter.
        self.current_value = current_value
        # Indicates whether a restart is required for parameter modifications to take effect. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.force_restart_instance = force_restart_instance
        # Indicates whether the parameter can be modified. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_changeable_config = is_changeable_config
        # The valid values of the parameter.
        self.optional_range = optional_range
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The default value of the parameter.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.force_restart_instance is not None:
            result['ForceRestartInstance'] = self.force_restart_instance
        if self.is_changeable_config is not None:
            result['IsChangeableConfig'] = self.is_changeable_config
        if self.optional_range is not None:
            result['OptionalRange'] = self.optional_range
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('ForceRestartInstance') is not None:
            self.force_restart_instance = m.get('ForceRestartInstance')
        if m.get('IsChangeableConfig') is not None:
            self.is_changeable_config = m.get('IsChangeableConfig')
        if m.get('OptionalRange') is not None:
            self.optional_range = m.get('OptionalRange')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(
        self,
        parameters: List[DescribeParametersResponseBodyParameters] = None,
        request_id: str = None,
    ):
        # Details of the parameters.
        self.parameters = parameters
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeParametersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdsVSwitchsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list and zone list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The ID of virtual private cloud (VPC).
        # 
        # > *   You can call the [DescribeRdsVpcs](~~208327~~) operation to query the available VPCs.
        # > *   This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the zone.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list and zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        bid: str = None,
        cidr_block: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_default: bool = None,
        iz_no: str = None,
        region_no: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        # An invalid parameter. It is no longer returned when you call this operation.
        self.ali_uid = ali_uid
        # An invalid parameter. It is no longer returned when you call this operation.
        self.bid = bid
        # The CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_create = gmt_create
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_modified = gmt_modified
        # Indicates whether the vSwitch is the default vSwitch. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_default = is_default
        # The ID of the zone.
        self.iz_no = iz_no
        # An invalid parameter. It is no longer returned when you call this operation.
        self.region_no = region_no
        # The state of the vSwitch. If **Available** is returned, the vSwitch is available.
        self.status = status
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The name of the vSwitch.
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.iz_no is not None:
            result['IzNo'] = self.iz_no
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeRdsVSwitchsResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        v_switch: List[DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch] = None,
    ):
        # Details of the vSwitch.
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeRdsVSwitchsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        v_switches: DescribeRdsVSwitchsResponseBodyVSwitches = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Details of the vSwitches.
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitches') is not None:
            temp_model = DescribeRdsVSwitchsResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeRdsVSwitchsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRdsVSwitchsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRdsVSwitchsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdsVpcsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        zone_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_default: bool = None,
        iz_no: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        # The CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_create = gmt_create
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_modified = gmt_modified
        # Indicates whether the vSwitch is the default vSwitch. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_default = is_default
        # The ID of the zone to which the vSwitch belongs.
        self.iz_no = iz_no
        # The state of the vSwitch. If **Available** is returned, the vSwitch is available.
        self.status = status
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The name of the vSwitch.
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.iz_no is not None:
            result['IzNo'] = self.iz_no
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeRdsVpcsResponseBodyVpcsVpc(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        bid: str = None,
        cidr_block: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_default: bool = None,
        region_no: str = None,
        status: str = None,
        v_switchs: List[DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # An invalid parameter. It is no longer returned when you call this operation.
        self.ali_uid = ali_uid
        # An invalid parameter. It is no longer returned when you call this operation.
        self.bid = bid
        # The CIDR block of the VPC.
        self.cidr_block = cidr_block
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_create = gmt_create
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_modified = gmt_modified
        # Indicates whether the VPC is the default VPC. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_default = is_default
        # The ID of the region.
        self.region_no = region_no
        # The state of the VPC. If **Available** is returned, the VPC is available.
        self.status = status
        # Details of the vSwitches.
        self.v_switchs = v_switchs
        # The ID of VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.v_switchs:
            for k in self.v_switchs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.status is not None:
            result['Status'] = self.status
        result['VSwitchs'] = []
        if self.v_switchs is not None:
            for k in self.v_switchs:
                result['VSwitchs'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.v_switchs = []
        if m.get('VSwitchs') is not None:
            for k in m.get('VSwitchs'):
                temp_model = DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs()
                self.v_switchs.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeRdsVpcsResponseBodyVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[DescribeRdsVpcsResponseBodyVpcsVpc] = None,
    ):
        # Details of the VPC.
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeRdsVpcsResponseBodyVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeRdsVpcsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vpcs: DescribeRdsVpcsResponseBodyVpcs = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Details of the VPCs.
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vpcs') is not None:
            temp_model = DescribeRdsVpcsResponseBodyVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        return self


class DescribeRdsVpcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRdsVpcsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRdsVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(
        self,
        vpc_enabled: bool = None,
        zone_id: str = None,
    ):
        # Indicates whether Virtual Private Cloud (VPC) is available.
        # 
        # *   **true**: VPC is available.
        # *   **false**: VPC is unavailable.
        self.vpc_enabled = vpc_enabled
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeRegionsResponseBodyRegionsRegionZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zones: DescribeRegionsResponseBodyRegionsRegionZones = None,
    ):
        # The ID of the region.
        self.region_id = region_id
        # Details of the zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # Details of the regions.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogCountRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        execute_cost: str = None,
        execute_state: str = None,
        max_execute_cost: str = None,
        min_execute_cost: str = None,
        operation_class: str = None,
        operation_type: str = None,
        query_keywords: str = None,
        source_ip: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mmZ` format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time. Their interval cannot be more than seven days.
        self.end_time = end_time
        # The execution duration of the query. Unit: seconds.
        self.execute_cost = execute_cost
        # The execution state of the query. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state
        # The maximum amount of time consumed by a slow query. Minimum value: 0. Unit: seconds.
        self.max_execute_cost = max_execute_cost
        # The minimum amount of time consumed by a slow query. Minimum value: 0. Unit: seconds.
        self.min_execute_cost = min_execute_cost
        # The type of the query language. Valid values:
        # 
        # *   **DQL**\
        # *   **DML**\
        # *   **DDL**\
        # *   **DCL**\
        # *   **TCL**\
        self.operation_class = operation_class
        # The type of the SQL statement.
        # 
        # > *   If the **OperationClass** parameter is specified, the **OperationType** value must belong to the corresponding query language. For example, if the **OperationClass** value is **DQL**, the **OperationType** value must be a **DQL** SQL statement such as **SELECT**.
        # >*   If the **OperationClass** parameter is not specified, the **OperationType** value can be an SQL statement of all query languages.
        # >*   If neither of the **OperationClass** and **OperationType** parameters is specified, all types of SQL statements are returned.
        self.operation_type = operation_type
        # The keywords used to query.
        self.query_keywords = query_keywords
        # The source IP address.
        self.source_ip = source_ip
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mmZ` format. The time must be in UTC.
        self.start_time = start_time
        # The username that is used to log on to the database.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLLogCountResponseBodyItemsSeriesValues(TeaModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
        # The time when the audit logs were generated and the number of the audit logs.
        self.point = point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeSQLLogCountResponseBodyItemsSeries(TeaModel):
    def __init__(
        self,
        values: List[DescribeSQLLogCountResponseBodyItemsSeriesValues] = None,
    ):
        # Details of the audit logs.
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeSQLLogCountResponseBodyItemsSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeSQLLogCountResponseBodyItems(TeaModel):
    def __init__(
        self,
        name: str = None,
        series: List[DescribeSQLLogCountResponseBodyItemsSeries] = None,
    ):
        # The name of the table.
        self.name = name
        # Details of the audit logs.
        self.series = series

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeSQLLogCountResponseBodyItemsSeries()
                self.series.append(temp_model.from_map(k))
        return self


class DescribeSQLLogCountResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        items: List[DescribeSQLLogCountResponseBodyItems] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        self.dbcluster_id = dbcluster_id
        # The end time of the query.
        self.end_time = end_time
        # Details of the audit logs of the instance.
        self.items = items
        # The ID of the request.
        self.request_id = request_id
        # The start time of the query.
        self.start_time = start_time

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSQLLogCountResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSQLLogCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLLogCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSQLLogCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogsV2Request(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        execute_cost: str = None,
        execute_state: str = None,
        max_execute_cost: str = None,
        min_execute_cost: str = None,
        operation_class: str = None,
        operation_type: str = None,
        page_number: str = None,
        page_size: str = None,
        query_keywords: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The ID of instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time. The interval cannot be more than 24 hours.
        self.end_time = end_time
        # The execution duration of the query. Unit: seconds.
        self.execute_cost = execute_cost
        # The execution state of the query. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state
        # The maximum amount of time consumed by a slow query. Minimum value: 0. Unit: seconds.
        self.max_execute_cost = max_execute_cost
        # The minimum amount of time consumed by a slow query. Minimum value: 0. Unit: seconds.
        self.min_execute_cost = min_execute_cost
        # The type of the query language. Valid values:
        # 
        # *   **DQL**\
        # *   **DML**\
        # *   **DDL**\
        # *   **DCL**\
        # *   **TCL**\
        self.operation_class = operation_class
        # The type of the SQL statement.
        # 
        # > *   If the **OperationClass** parameter is specified, the **OperationType** value must belong to the corresponding query language. For example, if the **OperationClass** value is **DQL**, the **OperationType** value must be a **DQL** SQL statement such as **SELECT**.
        # >*   If the **OperationClass** parameter is not specified, the **OperationType** value can be an SQL statement of all query languages.
        # >*   If neither of the **OperationClass** and **OperationType** parameters is specified, all types of SQL statements are returned.
        self.operation_type = operation_type
        # The number of entries to return on each page.
        self.page_number = page_number
        # The number of the page to return. The maximum value is 200.
        self.page_size = page_size
        # The keywords of the SQL statement.
        self.query_keywords = query_keywords
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The source IP address.
        self.source_ip = source_ip
        # The beginning of the time range. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        self.start_time = start_time
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLLogsV2ResponseBodyItems(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dbname: str = None,
        dbrole: str = None,
        execute_cost: float = None,
        execute_state: str = None,
        operation_class: str = None,
        operation_execute_time: str = None,
        operation_type: str = None,
        return_row_counts: int = None,
        sqltext: str = None,
        scan_row_counts: int = None,
        source_ip: str = None,
        source_port: int = None,
    ):
        # The database account that executes the SQL statement.
        self.account_name = account_name
        # The name of the database.
        self.dbname = dbname
        # The role of the database.
        self.dbrole = dbrole
        # The execution duration of the query.
        self.execute_cost = execute_cost
        # The execution state of the query. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state
        # The type of the query language.
        self.operation_class = operation_class
        # The time when the SQL statement was executed.
        self.operation_execute_time = operation_execute_time
        # The type of the SQL statement.
        self.operation_type = operation_type
        # The number of entries returned.
        self.return_row_counts = return_row_counts
        # The SQL statement.
        self.sqltext = sqltext
        # The number of entries scanned.
        self.scan_row_counts = scan_row_counts
        # The source IP address.
        self.source_ip = source_ip
        # The number of the source port.
        self.source_port = source_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.dbrole is not None:
            result['DBRole'] = self.dbrole
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DBRole') is not None:
            self.dbrole = m.get('DBRole')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        return self


class DescribeSQLLogsV2ResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeSQLLogsV2ResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
    ):
        # Details of the SQL logs.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSQLLogsV2ResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSQLLogsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLLogsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSQLLogsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSampleDataRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeSampleDataResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        has_sample_data: bool = None,
        request_id: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned if an error occurs. This message does not affect the execution of the operation.
        self.error_message = error_message
        # Indicates whether a sample dataset is loaded to the instance. Valid values:
        # 
        # *   **true**: A sample dataset is loaded.
        # *   **false**: No sample dataset is loaded.
        self.has_sample_data = has_sample_data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.has_sample_data is not None:
            result['HasSampleData'] = self.has_sample_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HasSampleData') is not None:
            self.has_sample_data = m.get('HasSampleData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSampleDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSampleDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSampleDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSupportFeaturesRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeSupportFeaturesResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        request_id: str = None,
        support_feature_list: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The ID of the request.
        self.request_id = request_id
        # The features supported by the instance. Valid values:
        # 
        # *   sample_data: sample dataset. For more information, see [Sample dataset](~~452278~~).
        # *   diagnose_and_optimize: diagnostics and optimization. For more information, see [Diagnostics and optimization](~~323453~~).
        self.support_feature_list = support_feature_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_feature_list is not None:
            result['SupportFeatureList'] = self.support_feature_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportFeatureList') is not None:
            self.support_feature_list = m.get('SupportFeatureList')
        return self


class DescribeSupportFeaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSupportFeaturesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSupportFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Set the value to **instance**.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[DescribeTagsResponseBodyTags] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Details of the tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserEncryptionKeyListRequest(TeaModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of KMS keys to return on each page. Default value: 10.
        self.page_size = page_size
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUserEncryptionKeyListResponseBodyKmsKeys(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        # The ID of the KMS key.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DescribeUserEncryptionKeyListResponseBody(TeaModel):
    def __init__(
        self,
        kms_keys: List[DescribeUserEncryptionKeyListResponseBodyKmsKeys] = None,
        request_id: str = None,
    ):
        # Details about the KMS keys.
        self.kms_keys = kms_keys
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.kms_keys:
            for k in self.kms_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KmsKeys'] = []
        if self.kms_keys is not None:
            for k in self.kms_keys:
                result['KmsKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kms_keys = []
        if m.get('KmsKeys') is not None:
            for k in m.get('KmsKeys'):
                temp_model = DescribeUserEncryptionKeyListResponseBodyKmsKeys()
                self.kms_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserEncryptionKeyListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserEncryptionKeyListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserEncryptionKeyListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWaitingSQLInfoRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        pid: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The ID of the process that uniquely identifies the query.
        # 
        # >  You can call the [DescribeWaitingSQLRecords](~~461735~~) operation to obtain the process IDs of lock-waiting queries.
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.pid is not None:
            result['PID'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('PID') is not None:
            self.pid = m.get('PID')
        return self


class DescribeWaitingSQLInfoResponseBodyItems(TeaModel):
    def __init__(
        self,
        application: str = None,
        blocked_by_application: str = None,
        blocked_by_pid: str = None,
        blocked_by_sqlstmt: str = None,
        blocked_by_user: str = None,
        grant_locks: str = None,
        not_grant_locks: str = None,
        pid: str = None,
        sqlstmt: str = None,
        user: str = None,
    ):
        # The application that sent the query.
        self.application = application
        # The application that sent the blocking query.
        self.blocked_by_application = blocked_by_application
        # The process ID of the blocking query.
        self.blocked_by_pid = blocked_by_pid
        # The SQL statement of the blocking query.
        self.blocked_by_sqlstmt = blocked_by_sqlstmt
        # The database account that is used to perform the blocking query.
        self.blocked_by_user = blocked_by_user
        # The authorized locks.
        self.grant_locks = grant_locks
        # The unauthorized locks.
        self.not_grant_locks = not_grant_locks
        # The ID of the process that uniquely identifies the query.
        self.pid = pid
        # The SQL statement of the query.
        self.sqlstmt = sqlstmt
        # The database account that is used to perform the query.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application
        if self.blocked_by_application is not None:
            result['BlockedByApplication'] = self.blocked_by_application
        if self.blocked_by_pid is not None:
            result['BlockedByPID'] = self.blocked_by_pid
        if self.blocked_by_sqlstmt is not None:
            result['BlockedBySQLStmt'] = self.blocked_by_sqlstmt
        if self.blocked_by_user is not None:
            result['BlockedByUser'] = self.blocked_by_user
        if self.grant_locks is not None:
            result['GrantLocks'] = self.grant_locks
        if self.not_grant_locks is not None:
            result['NotGrantLocks'] = self.not_grant_locks
        if self.pid is not None:
            result['PID'] = self.pid
        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('BlockedByApplication') is not None:
            self.blocked_by_application = m.get('BlockedByApplication')
        if m.get('BlockedByPID') is not None:
            self.blocked_by_pid = m.get('BlockedByPID')
        if m.get('BlockedBySQLStmt') is not None:
            self.blocked_by_sqlstmt = m.get('BlockedBySQLStmt')
        if m.get('BlockedByUser') is not None:
            self.blocked_by_user = m.get('BlockedByUser')
        if m.get('GrantLocks') is not None:
            self.grant_locks = m.get('GrantLocks')
        if m.get('NotGrantLocks') is not None:
            self.not_grant_locks = m.get('NotGrantLocks')
        if m.get('PID') is not None:
            self.pid = m.get('PID')
        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeWaitingSQLInfoResponseBody(TeaModel):
    def __init__(
        self,
        database: str = None,
        items: List[DescribeWaitingSQLInfoResponseBodyItems] = None,
        request_id: str = None,
    ):
        # The name of the database.
        self.database = database
        # Details of the lock-waiting query.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeWaitingSQLInfoResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWaitingSQLInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWaitingSQLInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWaitingSQLInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWaitingSQLRecordsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        keyword: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        query_condition: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        # 
        # If this parameter is not specified, all lock diagnostics records that are generated after the query start time are returned. If the query start time is not specified either, all lock diagnostics records are returned.
        self.end_time = end_time
        # The keyword used to filter queries.
        self.keyword = keyword
        # The field used to sort lock diagnostics records and the sorting order.
        # 
        # Default value: `{"Field":"StartTime","Type":"Desc"}`, which indicates that lock diagnostics records are sorted by the start time in descending order. No other values are supported.
        self.order = order
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The filter condition on queries. Valid values:
        # 
        # *   `{"Type":"maxCost","Value":"10"}`: filters the top 10 longest-waiting queries.
        # *   `{"Type":"status","Value":"LockWaiting"}`: filters lock-waiting queries.
        # *   `{"Type":"status","Value":"ResourceWaiting"}`: filters resource-waiting queries.
        self.query_condition = query_condition
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # If this parameter is not specified, all lock diagnostics records that are generated before the query end time are returned. If the query end time is not specified either, all lock diagnostics records are returned.
        self.start_time = start_time
        # The name of the database account. If this parameter is not specified, the lock diagnostics records of all database accounts are queried.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeWaitingSQLRecordsResponseBodyItems(TeaModel):
    def __init__(
        self,
        database: str = None,
        pid: str = None,
        sqlstmt: str = None,
        session_id: str = None,
        start_time: int = None,
        status: str = None,
        user: str = None,
        waiting_time: int = None,
    ):
        # The name of the database.
        self.database = database
        # The ID of the process that uniquely identifies the query.
        self.pid = pid
        # The SQL statement of the query.
        self.sqlstmt = sqlstmt
        # The ID of the session that contains the query.
        self.session_id = session_id
        # The start time of the query. This value is in the timestamp format. Unit: milliseconds.
        self.start_time = start_time
        # The waiting state of the query. Valid values:
        # 
        # *   **LockWaiting**\
        # *   **ResourceWaiting**\
        self.status = status
        # The database account that is used to perform the query.
        self.user = user
        # The waiting period of the query. Unit: milliseconds.
        self.waiting_time = waiting_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.pid is not None:
            result['PID'] = self.pid
        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt
        if self.session_id is not None:
            result['SessionID'] = self.session_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user is not None:
            result['User'] = self.user
        if self.waiting_time is not None:
            result['WaitingTime'] = self.waiting_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('PID') is not None:
            self.pid = m.get('PID')
        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')
        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('WaitingTime') is not None:
            self.waiting_time = m.get('WaitingTime')
        return self


class DescribeWaitingSQLRecordsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeWaitingSQLRecordsResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of lock diagnostics records.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeWaitingSQLRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWaitingSQLRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWaitingSQLRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWaitingSQLRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadDiagnosisRecordsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        lang: str = None,
        query_condition: str = None,
        resource_group_id: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time
        # The language of the file that contains the query diagnostic information. Valid values:
        # 
        # *   **zh**: simplified Chinese
        # *   **en**: English
        # *   **ja**: Japanese
        # *   **zh-tw**: traditional Chinese
        self.lang = lang
        # The filter condition on queries. The value is in the JSON format. Valid values:
        # 
        # *   `{"Type":"maxCost", "Value":"100"}`: filters the top 100 queries that are the most time-consuming.
        # *   `{"Type":"status","Value":"finished"}`: filters completed queries.
        # *   `{"Type":"status","Value":"running"}`: filters running queries.
        # *   `{"Type":"cost","Max":"200"}`: filters the queries that consume less than 200 milliseconds.
        # *   `{"Type":"cost","Min":"200","Max":"60000"}`: filters the queries that consume 200 milliseconds or more and less than 1 minute.
        # *   `{"Type":"cost","Min":"60000"}`: filters the queries that consume 1 minute or more.
        # *   `{"Type":"cost","Min":"30","Max":"50"}`: filters the queries that consume 30 milliseconds or more and less than 50 milliseconds. You can customize a filter condition by setting **Min** and **Max**.
        self.query_condition = query_condition
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DownloadDiagnosisRecordsResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        download_id: str = None,
        request_id: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The ID of the download task.
        self.download_id = download_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadDiagnosisRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadDiagnosisRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DownloadDiagnosisRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadSQLLogsRecordsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        execute_cost: str = None,
        execute_state: str = None,
        lang: str = None,
        max_execute_cost: str = None,
        min_execute_cost: str = None,
        operation_class: str = None,
        operation_type: str = None,
        page_number: int = None,
        page_size: int = None,
        query_keywords: str = None,
        source_ip: str = None,
        start_time: str = None,
        user: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.database = database
        self.end_time = end_time
        self.execute_cost = execute_cost
        self.execute_state = execute_state
        self.lang = lang
        self.max_execute_cost = max_execute_cost
        self.min_execute_cost = min_execute_cost
        self.operation_class = operation_class
        self.operation_type = operation_type
        self.page_number = page_number
        self.page_size = page_size
        self.query_keywords = query_keywords
        self.source_ip = source_ip
        self.start_time = start_time
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DownloadSQLLogsRecordsResponseBody(TeaModel):
    def __init__(
        self,
        download_id: int = None,
        request_id: str = None,
    ):
        self.download_id = download_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadSQLLogsRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadSQLLogsRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DownloadSQLLogsRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantCollectionRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        grant_to_namespace: str = None,
        grant_type: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        namespace: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.collection = collection
        self.dbinstance_id = dbinstance_id
        self.grant_to_namespace = grant_to_namespace
        self.grant_type = grant_type
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        self.namespace = namespace
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.grant_to_namespace is not None:
            result['GrantToNamespace'] = self.grant_to_namespace
        if self.grant_type is not None:
            result['GrantType'] = self.grant_type
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('GrantToNamespace') is not None:
            self.grant_to_namespace = m.get('GrantToNamespace')
        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GrantCollectionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GrantCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantCollectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GrantCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitVectorDatabaseRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InitVectorDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class InitVectorDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitVectorDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitVectorDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCollectionsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCollectionsResponseBodyCollections(TeaModel):
    def __init__(
        self,
        collection: List[str] = None,
    ):
        self.collection = collection

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        return self


class ListCollectionsResponseBody(TeaModel):
    def __init__(
        self,
        collections: ListCollectionsResponseBodyCollections = None,
        count: int = None,
        dbinstance_id: str = None,
        message: str = None,
        namespace: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.collections = collections
        self.count = count
        self.dbinstance_id = dbinstance_id
        self.message = message
        self.namespace = namespace
        self.region_id = region_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.collections:
            self.collections.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collections is not None:
            result['Collections'] = self.collections.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            temp_model = ListCollectionsResponseBodyCollections()
            self.collections = temp_model.from_map(m['Collections'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCollectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCollectionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacesRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.manager_account = manager_account
        self.manager_account_password = manager_account_password
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListNamespacesResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        namespace: List[str] = None,
    ):
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class ListNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        dbinstance_id: str = None,
        message: str = None,
        namespaces: ListNamespacesResponseBodyNamespaces = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.count = count
        self.dbinstance_id = dbinstance_id
        self.message = message
        self.namespaces = namespaces
        self.region_id = region_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.namespaces:
            self.namespaces.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespaces') is not None:
            temp_model = ListNamespacesResponseBodyNamespaces()
            self.namespaces = temp_model.from_map(m['Namespaces'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. The key must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        # 
        # You can use `Tag.N.Key and Tag.N.Value` to query AnalyticDB for PostgreSQL instances to which specific tags are bound.
        # 
        # *   If you specify only `Tag.N.Key`, the instances whose tags contain the specified tag keys are returned.
        # *   If you specify only `Tag.N.Value`, `InvalidParameter.TagValue` is returned.
        # *   If you specify multiple tag key-value pairs at a time, the instances to which all the specified tags are bound are returned.
        self.key = key
        # The value of tag N. The value must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The token used to perform the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of instance N. Valid values of N: 1 to 50.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The storage mode of the instance. Valid values:
        # 
        # *   `instance`: reserved storage mode
        # *   `ALIYUN::GPDB::INSTANCE`: elastic storage mode
        self.resource_type = resource_type
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the instance.
        self.resource_id = resource_id
        # The storage mode of the instance.
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # The token used to perform the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # Details about the instances and tags, including the instance IDs, instance modes, and tag key-value pairs.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        dbinstance_id: str = None,
    ):
        # The new description of the database account.
        # 
        # *   The description must start with a letter.
        # *   The description cannot start with `http://` or `https://`.
        # *   The description can contain letters, underscores (\_), hyphens (-), and digits.
        # *   The description must be 2 to 256 characters in length.
        self.account_description = account_description
        # The name of the database account.
        self.account_name = account_name
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccountDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        dbinstance_id: str = None,
        enable_recovery_point: bool = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        recovery_point_period: str = None,
    ):
        # The number of days for which data backup files are retained. Default value: 7. Maximum value: 7. Valid values: 1 to 7.
        self.backup_retention_period = backup_retention_period
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to enable automatic point-in-time backup.
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.enable_recovery_point = enable_recovery_point
        # The cycle based on which you want to perform a backup. Separate multiple values with commas (,). Valid values:
        # 
        # *   Monday
        # *   Tuesday
        # *   Wednesday
        # *   Thursday
        # *   Friday
        # *   Saturday
        # *   Sunday
        self.preferred_backup_period = preferred_backup_period
        # The backup window. Specify the backup window in the HH:mmZ-HH:mmZ format. The backup window must be in UTC. Default value: 00:00-01:00.
        self.preferred_backup_time = preferred_backup_time
        # The frequency of point-in-time backup.
        # 
        # *   1: per hour
        # *   2: per 2 hours
        # *   4: per 4 hours
        # *   8: per 8 hours
        # 
        # Default value: 8.
        self.recovery_point_period = recovery_point_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.enable_recovery_point is not None:
            result['EnableRecoveryPoint'] = self.enable_recovery_point
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.recovery_point_period is not None:
            result['RecoveryPointPeriod'] = self.recovery_point_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EnableRecoveryPoint') is not None:
            self.enable_recovery_point = m.get('EnableRecoveryPoint')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RecoveryPointPeriod') is not None:
            self.recovery_point_period = m.get('RecoveryPointPeriod')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBackupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        idle_time: int = None,
        resource_group_id: str = None,
        serverless_resource: int = None,
    ):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The wait period for the instance that has no traffic to become idle. Minimum value: 60. Default value: 600. Unit: seconds.
        self.idle_time = idle_time
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The threshold of computing resources. Valid values: 8 to 32. Unit: AnalyticDB Compute Units (ACUs).
        self.serverless_resource = serverless_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')
        return self


class ModifyDBInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        db_instance_id: str = None,
        error_message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The ID of the instance.
        self.db_instance_id = db_instance_id
        # The error message returned if the operation fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation. Valid values:
        # 
        # *   **0**: The operation failed.
        # *   **1**: The operation is successful.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyDBInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        current_connection_string: str = None,
        dbinstance_id: str = None,
        port: str = None,
    ):
        # The new endpoint of the instance.
        self.connection_string_prefix = connection_string_prefix
        # The original endpoint of the instance.
        self.current_connection_string = current_connection_string
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The new port number of the instance.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyDBInstanceConnectionStringResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceConnectionStringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceConnectionStringResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        resource_group_id: str = None,
    ):
        # The description of the instance.
        # 
        # The description must be 2 to 256 characters in length. It cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyDBInstanceDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceMaintainTimeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        resource_group_id: str = None,
        start_time: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The end time of the maintenance window. The end time must be later than the start time. Specify the time in the HH:mmZ format. The time must be in UTC.
        self.end_time = end_time
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The start time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ModifyDBInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceMaintainTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceMaintainTimeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        new_resource_group_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The ID of the resource group to which you want to move the instance. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.new_resource_group_id = new_resource_group_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBInstanceResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceSSLRequest(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
        sslenabled: int = None,
    ):
        # The encrypted endpoint. By default, the wildcards are used for instances that are hosted on ECS instances. This way, the endpoints that can be resolved to the same IP address are encrypted.
        self.connection_string = connection_string
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The status of SSL encryption. Valid values:
        # 
        # *   0: disables SSL encryption.
        # *   1: enables SSL encryption.
        # *   2: updates SSL encryption.
        self.sslenabled = sslenabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        return self


class ModifyDBInstanceSSLResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceSSLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceSSLResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParametersRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        force_restart_instance: bool = None,
        parameters: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to forcibly restart the instance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.force_restart_instance = force_restart_instance
        # The name and value of the parameter to be modified. Specify the parameter in the `<Parameter name>:<Parameter value>` format.
        # 
        # You can call the [DescribeParameters](~~208310~~) operation to query the parameters that can be modified.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.force_restart_instance is not None:
            result['ForceRestartInstance'] = self.force_restart_instance
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ForceRestartInstance') is not None:
            self.force_restart_instance = m.get('ForceRestartInstance')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class ModifyParametersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyParametersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySQLCollectorPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        sqlcollector_status: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to enable or disable SQL collection.
        # 
        # *   Enable: enables SQL collection.
        # *   Disabled: disables SQL collection.
        self.sqlcollector_status = sqlcollector_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.sqlcollector_status is not None:
            result['SQLCollectorStatus'] = self.sqlcollector_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SQLCollectorStatus') is not None:
            self.sqlcollector_status = m.get('SQLCollectorStatus')
        return self


class ModifySQLCollectorPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySQLCollectorPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySQLCollectorPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySQLCollectorPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_iparray_attribute: str = None,
        dbinstance_iparray_name: str = None,
        dbinstance_id: str = None,
        modify_mode: str = None,
        resource_group_id: str = None,
        security_iplist: str = None,
    ):
        # The attribute of the IP address whitelist. By default, this parameter is empty. A whitelist with the `hidden` attribute does not appear in the console.
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute
        # The name of the whitelist. If you do not enter a name, IP addresses are added to the default whitelist.
        # 
        # >  You can create up to 50 whitelists for an instance.
        self.dbinstance_iparray_name = dbinstance_iparray_name
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The method of modification. Valid values:
        # 
        # *   **Cover**: overwrites the whitelist.
        # *   **Append**: appends data to the whitelist.
        # *   **Delete**: deletes the whitelist.
        self.modify_mode = modify_mode
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The IP addresses listed in the whitelist. You can add up to 1,000 IP addresses to the whitelist. Separate multiple IP addresses with commas (,). The IP addresses must use one of the following formats:
        # 
        # *   0.0.0.0/0
        # *   10.23.12.24. This is a standard IP address.
        # *   10.23.12.24/24. This is a CIDR block. The value `/24` indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value in the range of `1 to 32`.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySecurityIpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVectorConfigurationRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        vector_configuration_status: str = None,
    ):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a region.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # Specifies whether to enable vector engine optimization. Valid values:
        # 
        # *   **enabled**\
        # *   **disabled**\
        # 
        # > *   We recommend that you **do not enable** vector engine optimization in mainstream analysis and real-time data warehousing scenarios.
        # > *   We recommend that you **enable** vector engine optimization in AI Generated Content (AIGC) and vector retrieval scenarios that require the vector analysis engine.
        self.vector_configuration_status = vector_configuration_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.vector_configuration_status is not None:
            result['VectorConfigurationStatus'] = self.vector_configuration_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('VectorConfigurationStatus') is not None:
            self.vector_configuration_status = m.get('VectorConfigurationStatus')
        return self


class ModifyVectorConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The error message that is returned.
        # 
        # This parameter is returned only if the request fails.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyVectorConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVectorConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVectorConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class PauseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned.
        # 
        # This parameter is returned only if **false** is returned for the **Status** parameter.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **false**: The request failed.
        # *   **true**: The request was successful.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PauseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PauseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PauseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCollectionDataRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        content: str = None,
        dbinstance_id: str = None,
        filter: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        top_k: int = None,
        vector: List[float] = None,
    ):
        self.collection = collection
        self.content = content
        self.dbinstance_id = dbinstance_id
        self.filter = filter
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id
        self.top_k = top_k
        self.vector = vector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.content is not None:
            result['Content'] = self.content
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.vector is not None:
            result['Vector'] = self.vector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('Vector') is not None:
            self.vector = m.get('Vector')
        return self


class QueryCollectionDataShrinkRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        content: str = None,
        dbinstance_id: str = None,
        filter: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        top_k: int = None,
        vector_shrink: str = None,
    ):
        self.collection = collection
        self.content = content
        self.dbinstance_id = dbinstance_id
        self.filter = filter
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id
        self.top_k = top_k
        self.vector_shrink = vector_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.content is not None:
            result['Content'] = self.content
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.vector_shrink is not None:
            result['Vector'] = self.vector_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('Vector') is not None:
            self.vector_shrink = m.get('Vector')
        return self


class QueryCollectionDataResponseBodyMatchesMatchValues(TeaModel):
    def __init__(
        self,
        value: List[float] = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryCollectionDataResponseBodyMatchesMatch(TeaModel):
    def __init__(
        self,
        id: str = None,
        metadata: Dict[str, str] = None,
        score: float = None,
        values: QueryCollectionDataResponseBodyMatchesMatchValues = None,
    ):
        self.id = id
        self.metadata = metadata
        self.score = score
        self.values = values

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.score is not None:
            result['Score'] = self.score
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Values') is not None:
            temp_model = QueryCollectionDataResponseBodyMatchesMatchValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class QueryCollectionDataResponseBodyMatches(TeaModel):
    def __init__(
        self,
        match: List[QueryCollectionDataResponseBodyMatchesMatch] = None,
    ):
        self.match = match

    def validate(self):
        if self.match:
            for k in self.match:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['match'] = []
        if self.match is not None:
            for k in self.match:
                result['match'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match = []
        if m.get('match') is not None:
            for k in m.get('match'):
                temp_model = QueryCollectionDataResponseBodyMatchesMatch()
                self.match.append(temp_model.from_map(k))
        return self


class QueryCollectionDataResponseBody(TeaModel):
    def __init__(
        self,
        matches: QueryCollectionDataResponseBodyMatches = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.matches = matches
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.matches:
            self.matches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matches is not None:
            result['Matches'] = self.matches.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Matches') is not None:
            temp_model = QueryCollectionDataResponseBodyMatches()
            self.matches = temp_model.from_map(m['Matches'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryCollectionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCollectionDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCollectionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebalanceDBInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests.
        # 
        # The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The instance ID.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class RebalanceDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebalanceDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebalanceDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RebalanceDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        current_connection_string: str = None,
        dbinstance_id: str = None,
    ):
        # The type of the endpoint. Default value: primary. Valid values:
        # 
        # *   **primary**: primary endpoint.
        # *   **cluster**: cluster endpoint. This type of endpoints can be created only for instances that have multiple coordinator nodes.
        self.address_type = address_type
        # The public endpoint of the instance.
        # 
        # You can log on to the AnalyticDB for PostgreSQL console and go to the **Basic Information** page of the instance to view the **public endpoint** in the **Database Connection** section.
        self.current_connection_string = current_connection_string
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ReleaseInstancePublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstancePublicConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dbinstance_id: str = None,
    ):
        # The ID of the instance.
        self.account_name = account_name
        # The name of the account.
        self.account_password = account_password
        # Before you call this operation, make sure that the following requirements are met:
        # 
        # *   The instance is in the running state.
        # *   The instance is not locked.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The new password for the account. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAccountPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. For more information, see [How to ensure idempotence](~~327176~~).
        self.client_token = client_token
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class RestartDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ResumeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned.
        # 
        # This parameter is returned only if **false** is returned for the **Status** parameter.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **false**: The request failed.
        # *   **true**: The request was successful.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ResumeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDBInstancePlanStatusRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        plan_id: str = None,
        plan_status: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](~~449398~~) operation to query the details of plans, including plan IDs.
        self.plan_id = plan_id
        # Specifies whether to enable or disable the plan. Valid values:
        # 
        # *   **disable**: disables the plan.
        # *   **enable**: enables the plan.
        self.plan_status = plan_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_status is not None:
            result['PlanStatus'] = self.plan_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanStatus') is not None:
            self.plan_status = m.get('PlanStatus')
        return self


class SetDBInstancePlanStatusResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        plan_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error message returned.
        # 
        # This parameter is returned only when the operation fails.
        self.error_message = error_message
        # The ID of the plan.
        self.plan_id = plan_id
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDBInstancePlanStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDBInstancePlanStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDBInstancePlanStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataShareInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_list: List[str] = None,
        operation_type: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ID of the AnalyticDB for PostgreSQL instance in Serverless mode.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.instance_list = instance_list
        # Specifies whether to enable or disable data sharing. Valid values:
        # 
        # *   **add**: enables data sharing.
        # *   **remove**: disables data sharing.
        self.operation_type = operation_type
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetDataShareInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_list_shrink: str = None,
        operation_type: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ID of the AnalyticDB for PostgreSQL instance in Serverless mode.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.instance_list_shrink = instance_list_shrink
        # Specifies whether to enable or disable data sharing. Valid values:
        # 
        # *   **add**: enables data sharing.
        # *   **remove**: disables data sharing.
        self.operation_type = operation_type
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_list_shrink is not None:
            result['InstanceList'] = self.instance_list_shrink
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            self.instance_list_shrink = m.get('InstanceList')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetDataShareInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error message returned if the operation fails.
        self.err_message = err_message
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation. Valid values:
        # 
        # *   **success**: The operation is successful.
        # *   **failed**: The operation fails.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDataShareInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDataShareInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDataShareInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchDBInstanceNetTypeRequest(TeaModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        port: str = None,
    ):
        # The prefix of the custom endpoint. The prefix must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter. A valid endpoint is in the following format: Prefix.Database engine.rds.aliyuncs.com. Example: test1234.mysql.rds.aliyuncs.com.
        self.connection_string_prefix = connection_string_prefix
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The port number. Valid values: 3000 to 5999.
        # 
        # > 
        # *   Only ApsaraDB PolarDB MySQL-compatible edition clusters support this parameter. If you leave this parameter empty, the default port 3306 is used.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class SwitchDBInstanceNetTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchDBInstanceNetTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchDBInstanceNetTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SwitchDBInstanceNetTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of a tag. Valid values of N: 1 to 20. This parameter value cannot be an empty string. A tag key can contain a maximum of 128 characters. It cannot start with `aliyun` or`  acs: ` and cannot contain `http://` or`  https:// `.
        self.key = key
        # The value of a tag. Valid values of N: 1 to 20. This parameter value can be an empty string. A tag value can contain a maximum of 128 characters. It cannot start with `acs:` and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region. You can call the [DescribeRegions](~~86912~~) operation to query region IDs.
        self.region_id = region_id
        # The ID of an instance. Valid values of N: 1 to 50.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The mode of the instance. Valid values:
        # 
        # *   `instance`: reserved storage mode
        # *   `ALIYUN::GPDB::INSTANCE`: elastic storage mode
        self.resource_type = resource_type
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnloadSampleDataRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UnloadSampleDataResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned if an error occurs. This message does not affect the execution of the operation.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The execution state of the operation. Valid values:
        # 
        # *   **false**: The operation fails.
        # *   **true**: The operation is successful.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UnloadSampleDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnloadSampleDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnloadSampleDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to unbind all tags from an instance. This parameter is valid only when the TagKey.N parameter is not specified. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.all = all
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The storage mode of the instance. Valid values:
        # 
        # *   `instance`: reserved storage mode
        # *   `ALIYUN::GPDB::INSTANCE`: elastic storage mode
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDBInstancePlanRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        plan_config: str = None,
        plan_desc: str = None,
        plan_end_date: str = None,
        plan_id: str = None,
        plan_name: str = None,
        plan_start_date: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The execution information of the plan. Specify the parameter in the JSON format. The parameter value varies based on the values of **PlanType** and **PlanScheduleType**. The following section describes the PlanConfig parameter.
        self.plan_config = plan_config
        # The description of the plan.
        self.plan_desc = plan_desc
        # The end time of the plan. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        # 
        # >  This parameter is required only for **periodically executed** plans.
        self.plan_end_date = plan_end_date
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](~~449398~~) operation to query the details of plans, including plan IDs.
        self.plan_id = plan_id
        # The name of the plan.
        self.plan_name = plan_name
        # The start time of the plan. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is required only for **periodically executed** plans.
        self.plan_start_date = plan_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_config is not None:
            result['PlanConfig'] = self.plan_config
        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc
        if self.plan_end_date is not None:
            result['PlanEndDate'] = self.plan_end_date
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_start_date is not None:
            result['PlanStartDate'] = self.plan_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanConfig') is not None:
            self.plan_config = m.get('PlanConfig')
        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')
        if m.get('PlanEndDate') is not None:
            self.plan_end_date = m.get('PlanEndDate')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanStartDate') is not None:
            self.plan_start_date = m.get('PlanStartDate')
        return self


class UpdateDBInstancePlanResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        plan_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned.
        # 
        # This parameter is returned only when the operation fails.
        self.error_message = error_message
        # The ID of the plan.
        self.plan_id = plan_id
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateDBInstancePlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDBInstancePlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDBInstancePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_class: str = None,
        dbinstance_group_count: str = None,
        dbinstance_id: str = None,
        instance_spec: str = None,
        master_node_num: str = None,
        owner_id: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        seg_disk_performance_level: str = None,
        seg_node_num: str = None,
        seg_storage_type: str = None,
        storage_size: str = None,
        upgrade_type: int = None,
    ):
        # This parameter is no longer used.
        self.dbinstance_class = dbinstance_class
        # This parameter is no longer used.
        self.dbinstance_group_count = dbinstance_group_count
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a region.
        self.dbinstance_id = dbinstance_id
        # The specifications of each compute node. For information about the supported specifications, see [Instance specifications](~~35406~~).
        # 
        # >  This parameter is available only for instances in elastic storage mode.
        self.instance_spec = instance_spec
        # The number of coordinator nodes. Valid values: 1 and 2.
        # 
        # >  This parameter is available only on the China site (aliyun.com).
        self.master_node_num = master_node_num
        self.owner_id = owner_id
        # This parameter is no longer used.
        self.pay_type = pay_type
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The performance level of enhanced SSDs (ESSDs). Valid values:
        # 
        # *   **pl0**\
        # *   **pl1**\
        # *   **pl2**\
        self.seg_disk_performance_level = seg_disk_performance_level
        # The number of compute nodes. The number of compute nodes varies based on the instance resource type and edition.
        # 
        # *   Valid values for High-availability Edition instances in elastic storage mode: 4 to 512, in 4 increments
        # *   Valid values for High-performance Edition instances in elastic storage mode: 2 to 512, in 2 increments
        # *   Valid values for instances in manual Serverless mode: 2 to 512, in 2 increments
        self.seg_node_num = seg_node_num
        # The disk storage type of the instance after the change. The disk storage type can be changed only to ESSD. Set the value to **cloud_essd**.
        self.seg_storage_type = seg_storage_type
        # The storage capacity of each compute node. Unit: GB. Valid values: 50 to 6000, in 50 increments.
        # 
        # >  This parameter is available only for instances in elastic storage mode.
        self.storage_size = storage_size
        # The type of the instance configuration change. Valid values:
        # 
        # *   **0** (default): changes the number of compute nodes.
        # *   **1**: changes the specifications and storage capacity of each compute node.
        # *   **2**: changes the number of coordinator nodes.
        # *   **3**: changes the disk storage type and ESSD performance level of the instance.
        # 
        # > *   The supported changes to compute node configurations vary based on the instance resource type. For more information, see the "[Precautions](~~50956~~)" section of the Change compute node configurations topic.
        # > *   After you specify a change type, only the corresponding parameters take effect. For example, if you set **UpgradeType** to 0, the parameter that is used to change the number of compute nodes takes effect, but the parameter that is used to change the number of coordinator nodes does not.
        # > *   The number of coordinator nodes can be changed only on the China site (aliyun.com).
        # > *   The disk storage type can be changed only from ultra disks to ESSDs.
        self.upgrade_type = upgrade_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        return self


class UpgradeDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBVersionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        major_version: str = None,
        minor_version: str = None,
        owner_id: int = None,
        region_id: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The major version of the instance.
        self.major_version = major_version
        # The minor version of the instance.
        self.minor_version = minor_version
        self.owner_id = owner_id
        # The region ID of the instance.
        self.region_id = region_id
        # The upgrade time.
        self.switch_time = switch_time
        # The upgrade method.
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class UpgradeDBVersionResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The name of the instance.
        self.dbinstance_name = dbinstance_name
        # The ID of the request.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeDBVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeDBVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeDBVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpsertCollectionDataRequestRows(TeaModel):
    def __init__(
        self,
        id: str = None,
        metadata: Dict[str, str] = None,
        vector: List[float] = None,
    ):
        self.id = id
        self.metadata = metadata
        self.vector = vector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.vector is not None:
            result['Vector'] = self.vector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Vector') is not None:
            self.vector = m.get('Vector')
        return self


class UpsertCollectionDataRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        rows: List[UpsertCollectionDataRequestRows] = None,
    ):
        self.collection = collection
        self.dbinstance_id = dbinstance_id
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id
        self.rows = rows

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['Rows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.rows = []
        if m.get('Rows') is not None:
            for k in m.get('Rows'):
                temp_model = UpsertCollectionDataRequestRows()
                self.rows.append(temp_model.from_map(k))
        return self


class UpsertCollectionDataShrinkRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        rows_shrink: str = None,
    ):
        self.collection = collection
        self.dbinstance_id = dbinstance_id
        self.namespace = namespace
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        self.region_id = region_id
        self.rows_shrink = rows_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rows_shrink is not None:
            result['Rows'] = self.rows_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Rows') is not None:
            self.rows_shrink = m.get('Rows')
        return self


class UpsertCollectionDataResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpsertCollectionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpsertCollectionDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpsertCollectionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


