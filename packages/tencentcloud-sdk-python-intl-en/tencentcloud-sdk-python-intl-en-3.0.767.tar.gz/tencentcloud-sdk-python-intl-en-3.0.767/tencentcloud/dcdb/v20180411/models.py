# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Account(AbstractModel):
    """TencentDB account information

    """

    def __init__(self):
        r"""
        :param _User: Account name
        :type User: str
        :param _Host: Host address
        :type Host: str
        """
        self._User = None
        self._Host = None

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActiveHourDCDBInstanceRequest(AbstractModel):
    """ActiveHourDCDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instance IDs in the format of dcdbt-ow728lmc, which can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActiveHourDCDBInstanceResponse(AbstractModel):
    """ActiveHourDCDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: IDs of instances removed from isolation
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: IDs of instances failed to be removed from isolation
        :type FailedInstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class AddShardConfig(AbstractModel):
    """Instance upgrade -- Adding shard

    """

    def __init__(self):
        r"""
        :param _ShardCount: The number of shards to be added
        :type ShardCount: int
        :param _ShardMemory: Shard memory capacity in GB
        :type ShardMemory: int
        :param _ShardStorage: Shard storage capacity in GB
        :type ShardStorage: int
        """
        self._ShardCount = None
        self._ShardMemory = None
        self._ShardStorage = None

    @property
    def ShardCount(self):
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def ShardMemory(self):
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage


    def _deserialize(self, params):
        self._ShardCount = params.get("ShardCount")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param _SecurityGroupId: ID of the security group to be associated in the format of sg-efil73jd.
        :type SecurityGroupId: str
        :param _InstanceIds: ID(s) of the instance(s) to be associated in the format of tdsqlshard-lesecurk. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BriefNodeInfo(AbstractModel):
    """Node information of a sharded database

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID
        :type NodeId: str
        :param _Role: Node role. Valid values: `master`, `slave`
        :type Role: str
        :param _ShardId: The ID of the shard where the node resides
        :type ShardId: str
        """
        self._NodeId = None
        self._Role = None
        self._ShardId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Role = params.get("Role")
        self._ShardId = params.get("ShardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDcnJobRequest(AbstractModel):
    """CancelDcnJob request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Disaster recovery instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDcnJobResponse(AbstractModel):
    """CancelDcnJob response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloneAccountRequest(AbstractModel):
    """CloneAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SrcUser: Source user account name
        :type SrcUser: str
        :param _SrcHost: Source user host
        :type SrcHost: str
        :param _DstUser: Target user account name
        :type DstUser: str
        :param _DstHost: Target user host
        :type DstHost: str
        :param _DstDesc: Target account description
        :type DstDesc: str
        """
        self._InstanceId = None
        self._SrcUser = None
        self._SrcHost = None
        self._DstUser = None
        self._DstHost = None
        self._DstDesc = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SrcUser(self):
        return self._SrcUser

    @SrcUser.setter
    def SrcUser(self, SrcUser):
        self._SrcUser = SrcUser

    @property
    def SrcHost(self):
        return self._SrcHost

    @SrcHost.setter
    def SrcHost(self, SrcHost):
        self._SrcHost = SrcHost

    @property
    def DstUser(self):
        return self._DstUser

    @DstUser.setter
    def DstUser(self, DstUser):
        self._DstUser = DstUser

    @property
    def DstHost(self):
        return self._DstHost

    @DstHost.setter
    def DstHost(self, DstHost):
        self._DstHost = DstHost

    @property
    def DstDesc(self):
        return self._DstDesc

    @DstDesc.setter
    def DstDesc(self, DstDesc):
        self._DstDesc = DstDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SrcUser = params.get("SrcUser")
        self._SrcHost = params.get("SrcHost")
        self._DstUser = params.get("DstUser")
        self._DstHost = params.get("DstHost")
        self._DstDesc = params.get("DstDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneAccountResponse(AbstractModel):
    """CloneAccount response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of an instance for which to disable public network access. The ID is in the format of dcdbt-ow728lmc and can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceId: str
        :param _Ipv6Flag: Whether IPv6 is used. Default value: 0
        :type Ipv6Flag: int
        """
        self._InstanceId = None
        self._Ipv6Flag = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ipv6Flag(self):
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """Column permission information

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _Column: Column name
        :type Column: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Column = None
        self._Privileges = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Column(self):
        return self._Column

    @Column.setter
    def Column(self, Column):
        self._Column = Column

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Column = params.get("Column")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigValue(AbstractModel):
    """Configuration information,  which contains `Config` and `Value`.

    """

    def __init__(self):
        r"""
        :param _Config: Configuration name, which supports `max_user_connections`.
        :type Config: str
        :param _Value: Configuration value
        :type Value: str
        """
        self._Config = None
        self._Value = None

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Config = params.get("Config")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConstraintRange(AbstractModel):
    """Range of constraint type values

    """

    def __init__(self):
        r"""
        :param _Min: Minimum value when the constraint type is `section`
        :type Min: str
        :param _Max: Maximum value when the constraint type is `section`
        :type Max: str
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _SrcUserName: Source username
        :type SrcUserName: str
        :param _SrcHost: Access host allowed for a source user
        :type SrcHost: str
        :param _DstUserName: Target username
        :type DstUserName: str
        :param _DstHost: Access host allowed for a target user
        :type DstHost: str
        :param _SrcReadOnly: `ReadOnly` attribute of a source account
        :type SrcReadOnly: str
        :param _DstReadOnly: `ReadOnly` attribute of a target account
        :type DstReadOnly: str
        """
        self._InstanceId = None
        self._SrcUserName = None
        self._SrcHost = None
        self._DstUserName = None
        self._DstHost = None
        self._SrcReadOnly = None
        self._DstReadOnly = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SrcUserName(self):
        return self._SrcUserName

    @SrcUserName.setter
    def SrcUserName(self, SrcUserName):
        self._SrcUserName = SrcUserName

    @property
    def SrcHost(self):
        return self._SrcHost

    @SrcHost.setter
    def SrcHost(self, SrcHost):
        self._SrcHost = SrcHost

    @property
    def DstUserName(self):
        return self._DstUserName

    @DstUserName.setter
    def DstUserName(self, DstUserName):
        self._DstUserName = DstUserName

    @property
    def DstHost(self):
        return self._DstHost

    @DstHost.setter
    def DstHost(self, DstHost):
        self._DstHost = DstHost

    @property
    def SrcReadOnly(self):
        return self._SrcReadOnly

    @SrcReadOnly.setter
    def SrcReadOnly(self, SrcReadOnly):
        self._SrcReadOnly = SrcReadOnly

    @property
    def DstReadOnly(self):
        return self._DstReadOnly

    @DstReadOnly.setter
    def DstReadOnly(self, DstReadOnly):
        self._DstReadOnly = DstReadOnly


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SrcUserName = params.get("SrcUserName")
        self._SrcHost = params.get("SrcHost")
        self._DstUserName = params.get("DstUserName")
        self._DstHost = params.get("DstHost")
        self._SrcReadOnly = params.get("SrcReadOnly")
        self._DstReadOnly = params.get("DstReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc, which can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceId: str
        :param _UserName: AccountName
        :type UserName: str
        :param _Host: Host that can be logged in to, which is in the same format as the host of the MySQL account and supports wildcards, such as %, 10.%, and 10.20.%.
        :type Host: str
        :param _Password: Account password. It must contain 8-32 characters in all of the following four types: lowercase letters, uppercase letters, digits, and symbols (()~!@#$%^&*-+=_|{}[]:<>,.?/), and cannot start with a slash (/).
        :type Password: str
        :param _ReadOnly: Whether to create a read-only account. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail; 3: only the secondary will be read from.
        :type ReadOnly: int
        :param _Description: Account remarks, which can contain 0-256 letters, digits, and common symbols.
        :type Description: str
        :param _DelayThresh: If the secondary delay exceeds the set value of this parameter, the secondary will be deemed to have failed.
It is recommended that this parameter be set to a value greater than 10. This parameter takes effect when `ReadOnly` is 1 or 2.
        :type DelayThresh: int
        :param _SlaveConst: Whether to specify a replica server for read-only account. Valid values: `0` (No replica server is specified, which means that the proxy will select another available replica server to keep connection with the client if the current replica server doesn’t meet the requirement). `1` (The replica server is specified, which means that the connection will be disconnected if the specified replica server doesn’t meet the requirement.)
        :type SlaveConst: int
        :param _MaxUserConnections: Maximum number of connections. If left empty or `0` is passed in, the connections will be unlimited. This parameter configuration is not supported for kernel version 10.1.
        :type MaxUserConnections: int
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Password = None
        self._ReadOnly = None
        self._Description = None
        self._DelayThresh = None
        self._SlaveConst = None
        self._MaxUserConnections = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DelayThresh(self):
        return self._DelayThresh

    @DelayThresh.setter
    def DelayThresh(self, DelayThresh):
        self._DelayThresh = DelayThresh

    @property
    def SlaveConst(self):
        return self._SlaveConst

    @SlaveConst.setter
    def SlaveConst(self, SlaveConst):
        self._SlaveConst = SlaveConst

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Password = params.get("Password")
        self._ReadOnly = params.get("ReadOnly")
        self._Description = params.get("Description")
        self._DelayThresh = params.get("DelayThresh")
        self._SlaveConst = params.get("SlaveConst")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is passed through from the input parameters.
        :type InstanceId: str
        :param _UserName: Username, which is passed through from the input parameters.
        :type UserName: str
        :param _Host: Host allowed for access, which is passed through from the input parameters.
        :type Host: str
        :param _ReadOnly: Passed through from the input parameters.
        :type ReadOnly: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._ReadOnly = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._ReadOnly = params.get("ReadOnly")
        self._RequestId = params.get("RequestId")


class CreateDCDBInstanceRequest(AbstractModel):
    """CreateDCDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Zones: AZs to deploy shard nodes. You can specify up to two AZs. When the shard specification is 1-source-2-replica, two of the nodes are deployed in the first AZ.
The current purchasable AZ needs be pulled through `DescribeDCDBSaleInfo` API.
        :type Zones: list of str
        :param _Period: Validity period in months
        :type Period: int
        :param _ShardMemory: Shard memory size in GB, which can be obtained 
 by querying the instance specification through `DescribeShardSpec` API.
        :type ShardMemory: int
        :param _ShardStorage: Shard storage size in GB, which can be obtained
 by querying the instance specification through `DescribeShardSpec` API.
        :type ShardStorage: int
        :param _ShardNodeCount: Number of nodes in a single shard, which can be obtained
 by querying the instance specification through `DescribeShardSpec` API.
        :type ShardNodeCount: int
        :param _ShardCount: The number of shards in the instance. Value range: 2-8. You can increase up to 64 shards by upgrading your instance.
        :type ShardCount: int
        :param _Count: The number of instances to be purchased
        :type Count: int
        :param _ProjectId: Project ID, which can be obtained through the `DescribeProjects` API. If this parameter is not passed in, the instance will be associated with the default project.
        :type ProjectId: int
        :param _VpcId: VPC ID. If this parameter is left empty or not passed in, the instance will be created on the classic network.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID, which is required when `VpcId` is specified.
        :type SubnetId: str
        :param _DbVersionId: Database engine version. Valid values: `5.7`, `8.0`, `10.0`, `10.1`.
        :type DbVersionId: str
        :param _AutoVoucher: Whether to automatically use vouchers. This option is disabled by default.
        :type AutoVoucher: bool
        :param _VoucherIds: Voucher ID list. Currently, you can specify only one voucher.
        :type VoucherIds: list of str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _InstanceName: Custom name of the instance
        :type InstanceName: str
        :param _Ipv6Flag: Whether IPv6 is supported. Valid values: `0` (unsupported), `1` (supported).
        :type Ipv6Flag: int
        :param _ResourceTags: Array of tag key-value pairs
        :type ResourceTags: list of ResourceTag
        :param _InitParams: List of parameters. Valid values: `character_set_server` (character set; required); `lower_case_table_names` (table name case sensitivity; required; `0`: case-sensitive; `1`: case-insensitive); `innodb_page_size` (InnoDB data page size; default size: 16 KB); `sync_mode` (sync mode; `0`: async; `1`: strong sync; `2`: downgradable strong sync; default value: `2`).
        :type InitParams: list of DBParamValue
        :param _DcnRegion: DCN source region
        :type DcnRegion: str
        :param _DcnInstanceId: DCN source instance ID
        :type DcnInstanceId: str
        :param _AutoRenewFlag: Renewal mode. Valid values: `0` (manual renewal, which is the default mode), `1` (auto-renewal), `2` (manual renewal, which is specified by users).  If no renewal is required, set it to `0`.
        :type AutoRenewFlag: int
        :param _SecurityGroupIds: Security group IDs in array. This parameter is compatible with the old parameter `SecurityGroupId`.
        :type SecurityGroupIds: list of str
        """
        self._Zones = None
        self._Period = None
        self._ShardMemory = None
        self._ShardStorage = None
        self._ShardNodeCount = None
        self._ShardCount = None
        self._Count = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._DbVersionId = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._SecurityGroupId = None
        self._InstanceName = None
        self._Ipv6Flag = None
        self._ResourceTags = None
        self._InitParams = None
        self._DcnRegion = None
        self._DcnInstanceId = None
        self._AutoRenewFlag = None
        self._SecurityGroupIds = None

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ShardMemory(self):
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ShardNodeCount(self):
        return self._ShardNodeCount

    @ShardNodeCount.setter
    def ShardNodeCount(self, ShardNodeCount):
        self._ShardNodeCount = ShardNodeCount

    @property
    def ShardCount(self):
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DbVersionId(self):
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Ipv6Flag(self):
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def InitParams(self):
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def DcnRegion(self):
        return self._DcnRegion

    @DcnRegion.setter
    def DcnRegion(self, DcnRegion):
        self._DcnRegion = DcnRegion

    @property
    def DcnInstanceId(self):
        return self._DcnInstanceId

    @DcnInstanceId.setter
    def DcnInstanceId(self, DcnInstanceId):
        self._DcnInstanceId = DcnInstanceId

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._Zones = params.get("Zones")
        self._Period = params.get("Period")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ShardNodeCount = params.get("ShardNodeCount")
        self._ShardCount = params.get("ShardCount")
        self._Count = params.get("Count")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DbVersionId = params.get("DbVersionId")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceName = params.get("InstanceName")
        self._Ipv6Flag = params.get("Ipv6Flag")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._DcnRegion = params.get("DcnRegion")
        self._DcnInstanceId = params.get("DcnInstanceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDCDBInstanceResponse(AbstractModel):
    """CreateDCDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Long order ID, which is used to call the `DescribeOrders` API.
 The parameter can be used to either query order details or call the user account APIs to make another payment when this payment fails.
        :type DealName: str
        :param _InstanceIds: IDs of the instances you have purchased in this order. If no instance IDs are returned, you can query them with the `DescribeOrders` API. You can also use the `DescribeDBInstances` API to check whether an instance has been created successfully.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateHourDCDBInstanceRequest(AbstractModel):
    """CreateHourDCDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ShardMemory: Shard memory in GB, which can be obtained through the `DescribeShardSpec` API.
  
        :type ShardMemory: int
        :param _ShardStorage: Shard capacity in GB, which can be obtained through the `DescribeShardSpec` API.
  
        :type ShardStorage: int
        :param _ShardNodeCount: The number of nodes per shard, which can be obtained through the `DescribeShardSpec` API.
  
        :type ShardNodeCount: int
        :param _ShardCount: The number of shards in the instance. Value range: 2-8. Upgrade your instance to have up to 64 shards if you require more.
        :type ShardCount: int
        :param _Count: The number of instances to be purchased
        :type Count: int
        :param _ProjectId: Project ID, which can be obtained through the `DescribeProjects` API. If this parameter is not passed in, the instance will be associated with the default project.
        :type ProjectId: int
        :param _VpcId: VPC ID. If this parameter is left empty or not passed in, the instance will be created on the classic network.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID, which is required when `VpcId` is specified
        :type SubnetId: str
        :param _ShardCpu: The number of CPU cores per shard, which can be obtained through the `DescribeShardSpec` API.
  
        :type ShardCpu: int
        :param _DbVersionId: Database engine version. Valid values: `5.7`, `8.0`, `10.0`, `10.1`.
        :type DbVersionId: str
        :param _Zones: AZs to deploy shard nodes. You can specify up to two AZs.
        :type Zones: list of str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _InstanceName: Custom name of the instance
        :type InstanceName: str
        :param _Ipv6Flag: Whether IPv6 is supported. Valid values: `0` (unsupported), `1` (supported).
        :type Ipv6Flag: int
        :param _ResourceTags: Array of tag key-value pairs
        :type ResourceTags: list of ResourceTag
        :param _DcnRegion: If you create a disaster recovery instance, you need to use this parameter to specify the region of the associated source instance so that the disaster recovery instance can sync data with the source instance over the Data Communication Network (DCN).
        :type DcnRegion: str
        :param _DcnInstanceId: If you create a disaster recovery instance, you need to use this parameter to specify the ID of the associated source instance so that the disaster recovery instance can sync data with the source instance over the Data Communication Network (DCN).
        :type DcnInstanceId: str
        :param _InitParams: List of parameters. Valid values: `character_set_server` (character set; required); `lower_case_table_names` (table name case sensitivity; required; 0: case-sensitive; 1: case-insensitive); `innodb_page_size` (InnoDB data page size; default size: 16 KB); `sync_mode` (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: 2).
        :type InitParams: list of DBParamValue
        :param _RollbackInstanceId: ID of the instance to be rolled back
        :type RollbackInstanceId: str
        :param _RollbackTime: Rollback time, such as "2021-11-22 00:00:00".
        :type RollbackTime: str
        :param _SecurityGroupIds: Array of security group IDs (this parameter is compatible with the old parameter `SecurityGroupId`)
        :type SecurityGroupIds: list of str
        """
        self._ShardMemory = None
        self._ShardStorage = None
        self._ShardNodeCount = None
        self._ShardCount = None
        self._Count = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._ShardCpu = None
        self._DbVersionId = None
        self._Zones = None
        self._SecurityGroupId = None
        self._InstanceName = None
        self._Ipv6Flag = None
        self._ResourceTags = None
        self._DcnRegion = None
        self._DcnInstanceId = None
        self._InitParams = None
        self._RollbackInstanceId = None
        self._RollbackTime = None
        self._SecurityGroupIds = None

    @property
    def ShardMemory(self):
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ShardNodeCount(self):
        return self._ShardNodeCount

    @ShardNodeCount.setter
    def ShardNodeCount(self, ShardNodeCount):
        self._ShardNodeCount = ShardNodeCount

    @property
    def ShardCount(self):
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ShardCpu(self):
        return self._ShardCpu

    @ShardCpu.setter
    def ShardCpu(self, ShardCpu):
        self._ShardCpu = ShardCpu

    @property
    def DbVersionId(self):
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Ipv6Flag(self):
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DcnRegion(self):
        return self._DcnRegion

    @DcnRegion.setter
    def DcnRegion(self, DcnRegion):
        self._DcnRegion = DcnRegion

    @property
    def DcnInstanceId(self):
        return self._DcnInstanceId

    @DcnInstanceId.setter
    def DcnInstanceId(self, DcnInstanceId):
        self._DcnInstanceId = DcnInstanceId

    @property
    def InitParams(self):
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def RollbackInstanceId(self):
        return self._RollbackInstanceId

    @RollbackInstanceId.setter
    def RollbackInstanceId(self, RollbackInstanceId):
        self._RollbackInstanceId = RollbackInstanceId

    @property
    def RollbackTime(self):
        return self._RollbackTime

    @RollbackTime.setter
    def RollbackTime(self, RollbackTime):
        self._RollbackTime = RollbackTime

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ShardNodeCount = params.get("ShardNodeCount")
        self._ShardCount = params.get("ShardCount")
        self._Count = params.get("Count")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ShardCpu = params.get("ShardCpu")
        self._DbVersionId = params.get("DbVersionId")
        self._Zones = params.get("Zones")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceName = params.get("InstanceName")
        self._Ipv6Flag = params.get("Ipv6Flag")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DcnRegion = params.get("DcnRegion")
        self._DcnInstanceId = params.get("DcnInstanceId")
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._RollbackInstanceId = params.get("RollbackInstanceId")
        self._RollbackTime = params.get("RollbackTime")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHourDCDBInstanceResponse(AbstractModel):
    """CreateHourDCDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: IDs of the instances you have purchased in this order. If no instance IDs are returned, you can query them with the `DescribeOrders` API. You can also use the `DescribeDBInstances` API to check whether an instance has been created successfully.
        :type InstanceIds: list of str
        :param _FlowId: Task ID, which can be used to query the creation progress
        :type FlowId: int
        :param _DealName: Order ID, which is used for calling the `DescribeOrders` API.
 The parameter can be used to either query order details or call the user account APIs to make another payment when this payment fails.
        :type DealName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceIds = None
        self._FlowId = None
        self._DealName = None
        self._RequestId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._FlowId = params.get("FlowId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class DBAccount(AbstractModel):
    """TencentDB account information

    """

    def __init__(self):
        r"""
        :param _UserName: Username
        :type UserName: str
        :param _Host: Host from which a user can log in (corresponding to the `host` field for a MySQL user; a user is uniquely identified by username and host; this parameter is in IP format and ends with % for IP range; % can be entered; if this parameter is left empty, % will be used by default).
        :type Host: str
        :param _Description: User remarks
        :type Description: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Last updated time
        :type UpdateTime: str
        :param _ReadOnly: Read-only flag. 0: no; 1: for the account's SQL requests, the replica will be used first, and if it is unavailable, the source will be used; 2: the replica will be used first, and if it is unavailable, the operation will fail.
        :type ReadOnly: int
        :param _DelayThresh: If the replica delay exceeds the set value of this parameter, the replica will be considered to have failed.
Set this parameter to a value above 10. This parameter takes effect when `ReadOnly` is 1 or 2.
        :type DelayThresh: int
        :param _SlaveConst: Whether to specify a replica server for read-only account. Valid values: `0` (No replica server is specified, which means that the proxy will select another available replica server to keep connection with the client if the current replica server doesn’t meet the requirement). `1` (The replica server is specified, which means that the connection will be disconnected if the specified replica server doesn’t meet the requirement.)
        :type SlaveConst: int
        :param _MaxUserConnections: Maximum number of connections. `0` indicates no limit.	
        :type MaxUserConnections: int
        """
        self._UserName = None
        self._Host = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ReadOnly = None
        self._DelayThresh = None
        self._SlaveConst = None
        self._MaxUserConnections = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def DelayThresh(self):
        return self._DelayThresh

    @DelayThresh.setter
    def DelayThresh(self, DelayThresh):
        self._DelayThresh = DelayThresh

    @property
    def SlaveConst(self):
        return self._SlaveConst

    @SlaveConst.setter
    def SlaveConst(self, SlaveConst):
        self._SlaveConst = SlaveConst

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ReadOnly = params.get("ReadOnly")
        self._DelayThresh = params.get("DelayThresh")
        self._SlaveConst = params.get("SlaveConst")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBParamValue(AbstractModel):
    """TencentDB parameter information.

    """

    def __init__(self):
        r"""
        :param _Param: Parameter name
        :type Param: str
        :param _Value: Parameter value
        :type Value: str
        """
        self._Param = None
        self._Value = None

    @property
    def Param(self):
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCDBInstanceInfo(AbstractModel):
    """TDSQL instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _AppId: Application ID
        :type AppId: int
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Region: Region
        :type Region: str
        :param _Zone: AZ
        :type Zone: str
        :param _VpcId: Numeric ID of a VPC
        :type VpcId: int
        :param _SubnetId: Subnet Digital ID
        :type SubnetId: int
        :param _StatusDesc: Status description
        :type StatusDesc: str
        :param _Status: Instance status. Valid values: `0` (creating), `1` (running task), `2` (running), `3` (uninitialized), `-1` (isolated), `4` (initializing), `5` (eliminating), `6` (restarting), `7` (migrating data)
        :type Status: int
        :param _Vip: Private IP
        :type Vip: str
        :param _Vport: Private network port
        :type Vport: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _AutoRenewFlag: Auto-renewal flag
        :type AutoRenewFlag: int
        :param _Memory: Memory size in GB
        :type Memory: int
        :param _Storage: Storage capacity in GB
        :type Storage: int
        :param _ShardCount: Number of shards
        :type ShardCount: int
        :param _PeriodEndTime: Expiration time
        :type PeriodEndTime: str
        :param _IsolatedTimestamp: Isolation time
        :type IsolatedTimestamp: str
        :param _Uin: Account ID
        :type Uin: str
        :param _ShardDetail: Shard details
        :type ShardDetail: list of ShardInfo
        :param _NodeCount: Number of nodes. 2: one master and one slave; 3: one master and two slaves
        :type NodeCount: int
        :param _IsTmp: Temporary instance flag. 0: non-temporary instance
        :type IsTmp: int
        :param _ExclusterId: Dedicated cluster ID. If this parameter is empty, the instance is a non-dedicated cluster instance
        :type ExclusterId: str
        :param _UniqueVpcId: VPC ID in string type
        :type UniqueVpcId: str
        :param _UniqueSubnetId: VPC subnet ID in string type
        :type UniqueSubnetId: str
        :param _Id: Numeric ID of instance (this field is obsolete and should not be depended on)
        :type Id: int
        :param _WanDomain: Domain name for public network access, which can be resolved by the public network
        :type WanDomain: str
        :param _WanVip: Public IP address, which can be accessed over the public network
        :type WanVip: str
        :param _WanPort: Public network port
        :type WanPort: int
        :param _Pid: Product type ID (this field is obsolete and should not be depended on)
        :type Pid: int
        :param _UpdateTime: Last updated time of an instance in the format of 2006-01-02 15:04:05
        :type UpdateTime: str
        :param _DbEngine: Database engine
        :type DbEngine: str
        :param _DbVersion: Database engine version
        :type DbVersion: str
        :param _Paymode: Billing mode
        :type Paymode: str
        :param _Locker: Async task flow ID when an async task is in progress on an instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type Locker: int
        :param _WanStatus: Public network access status. 0: not enabled; 1: enabled; 2: disabled; 3: enabling
        :type WanStatus: int
        :param _IsAuditSupported: Whether the instance supports audit. 1: yes; 0: no
        :type IsAuditSupported: int
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Ipv6Flag: Indicates whether the instance uses IPv6
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6Flag: int
        :param _Vipv6: Private network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vipv6: str
        :param _WanVipv6: Public network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanVipv6: str
        :param _WanPortIpv6: Public network IPv6 port
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanPortIpv6: int
        :param _WanStatusIpv6: Public network IPv6 status
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanStatusIpv6: int
        :param _DcnFlag: DCN type. Valid values: 0 (null), 1 (primary instance), 2 (disaster recovery instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnFlag: int
        :param _DcnStatus: DCN status. Valid values: 0 (null), 1 (creating), 2 (syncing), 3 (disconnected)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnStatus: int
        :param _DcnDstNum: The number of DCN disaster recovery instances
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnDstNum: int
        :param _InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (standard primary instance), `3` (standard disaster recovery instance), `4` (dedicated disaster recovery instance)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceType: int
        :param _ResourceTags: Instance tag information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceTags: list of ResourceTag
        :param _DbVersionId: Database engine version
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbVersionId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._StatusDesc = None
        self._Status = None
        self._Vip = None
        self._Vport = None
        self._CreateTime = None
        self._AutoRenewFlag = None
        self._Memory = None
        self._Storage = None
        self._ShardCount = None
        self._PeriodEndTime = None
        self._IsolatedTimestamp = None
        self._Uin = None
        self._ShardDetail = None
        self._NodeCount = None
        self._IsTmp = None
        self._ExclusterId = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._Id = None
        self._WanDomain = None
        self._WanVip = None
        self._WanPort = None
        self._Pid = None
        self._UpdateTime = None
        self._DbEngine = None
        self._DbVersion = None
        self._Paymode = None
        self._Locker = None
        self._WanStatus = None
        self._IsAuditSupported = None
        self._Cpu = None
        self._Ipv6Flag = None
        self._Vipv6 = None
        self._WanVipv6 = None
        self._WanPortIpv6 = None
        self._WanStatusIpv6 = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._DcnDstNum = None
        self._InstanceType = None
        self._ResourceTags = None
        self._DbVersionId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ShardCount(self):
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def IsolatedTimestamp(self):
        return self._IsolatedTimestamp

    @IsolatedTimestamp.setter
    def IsolatedTimestamp(self, IsolatedTimestamp):
        self._IsolatedTimestamp = IsolatedTimestamp

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ShardDetail(self):
        return self._ShardDetail

    @ShardDetail.setter
    def ShardDetail(self, ShardDetail):
        self._ShardDetail = ShardDetail

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def IsTmp(self):
        return self._IsTmp

    @IsTmp.setter
    def IsTmp(self, IsTmp):
        self._IsTmp = IsTmp

    @property
    def ExclusterId(self):
        return self._ExclusterId

    @ExclusterId.setter
    def ExclusterId(self, ExclusterId):
        self._ExclusterId = ExclusterId

    @property
    def UniqueVpcId(self):
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanVip(self):
        return self._WanVip

    @WanVip.setter
    def WanVip(self, WanVip):
        self._WanVip = WanVip

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DbEngine(self):
        return self._DbEngine

    @DbEngine.setter
    def DbEngine(self, DbEngine):
        self._DbEngine = DbEngine

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Paymode(self):
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def Locker(self):
        return self._Locker

    @Locker.setter
    def Locker(self, Locker):
        self._Locker = Locker

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def IsAuditSupported(self):
        return self._IsAuditSupported

    @IsAuditSupported.setter
    def IsAuditSupported(self, IsAuditSupported):
        self._IsAuditSupported = IsAuditSupported

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Ipv6Flag(self):
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def Vipv6(self):
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def WanVipv6(self):
        return self._WanVipv6

    @WanVipv6.setter
    def WanVipv6(self, WanVipv6):
        self._WanVipv6 = WanVipv6

    @property
    def WanPortIpv6(self):
        return self._WanPortIpv6

    @WanPortIpv6.setter
    def WanPortIpv6(self, WanPortIpv6):
        self._WanPortIpv6 = WanPortIpv6

    @property
    def WanStatusIpv6(self):
        return self._WanStatusIpv6

    @WanStatusIpv6.setter
    def WanStatusIpv6(self, WanStatusIpv6):
        self._WanStatusIpv6 = WanStatusIpv6

    @property
    def DcnFlag(self):
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def DcnDstNum(self):
        return self._DcnDstNum

    @DcnDstNum.setter
    def DcnDstNum(self, DcnDstNum):
        self._DcnDstNum = DcnDstNum

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbVersionId(self):
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._StatusDesc = params.get("StatusDesc")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CreateTime = params.get("CreateTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._ShardCount = params.get("ShardCount")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._IsolatedTimestamp = params.get("IsolatedTimestamp")
        self._Uin = params.get("Uin")
        if params.get("ShardDetail") is not None:
            self._ShardDetail = []
            for item in params.get("ShardDetail"):
                obj = ShardInfo()
                obj._deserialize(item)
                self._ShardDetail.append(obj)
        self._NodeCount = params.get("NodeCount")
        self._IsTmp = params.get("IsTmp")
        self._ExclusterId = params.get("ExclusterId")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._Id = params.get("Id")
        self._WanDomain = params.get("WanDomain")
        self._WanVip = params.get("WanVip")
        self._WanPort = params.get("WanPort")
        self._Pid = params.get("Pid")
        self._UpdateTime = params.get("UpdateTime")
        self._DbEngine = params.get("DbEngine")
        self._DbVersion = params.get("DbVersion")
        self._Paymode = params.get("Paymode")
        self._Locker = params.get("Locker")
        self._WanStatus = params.get("WanStatus")
        self._IsAuditSupported = params.get("IsAuditSupported")
        self._Cpu = params.get("Cpu")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._Vipv6 = params.get("Vipv6")
        self._WanVipv6 = params.get("WanVipv6")
        self._WanPortIpv6 = params.get("WanPortIpv6")
        self._WanStatusIpv6 = params.get("WanStatusIpv6")
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._DcnDstNum = params.get("DcnDstNum")
        self._InstanceType = params.get("InstanceType")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DbVersionId = params.get("DbVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCDBShardInfo(AbstractModel):
    """TDSQL shard information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ShardSerialId: Shard SQL passthrough ID, which is used to pass through SQL statements to the specified shard for execution.
        :type ShardSerialId: str
        :param _ShardInstanceId: Globally unique shard ID
        :type ShardInstanceId: str
        :param _Status: Status. 0: creating; 1: processing; 2: running; 3: shard not initialized.
        :type Status: int
        :param _StatusDesc: Status description
        :type StatusDesc: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _VpcId: VPC ID in string format
        :type VpcId: str
        :param _SubnetId: VPC subnet ID in string format
        :type SubnetId: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Region: Region
        :type Region: str
        :param _Zone: AZ
        :type Zone: str
        :param _Memory: Memory size in GB
        :type Memory: int
        :param _Storage: Storage capacity in GB
        :type Storage: int
        :param _PeriodEndTime: Expiration time
        :type PeriodEndTime: str
        :param _NodeCount: Number of nodes. 2: one source and one replica; 3: one source and two replicas
        :type NodeCount: int
        :param _StorageUsage: Storage utilization in %
        :type StorageUsage: float
        :param _MemoryUsage: Memory utilization in %
        :type MemoryUsage: float
        :param _ShardId: Numeric shard ID (this field is obsolete and should not be depended on)
        :type ShardId: int
        :param _Pid: Product ID
        :type Pid: int
        :param _ProxyVersion: Proxy version
        :type ProxyVersion: str
        :param _Paymode: Billing mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type Paymode: str
        :param _ShardMasterZone: Source AZ of the shard
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShardMasterZone: str
        :param _ShardSlaveZones: List of replica AZs of the shard
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShardSlaveZones: list of str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Range: The value range of shardkey, which includes 64 hash values, such as 0-31 or 32-63.
        :type Range: str
        """
        self._InstanceId = None
        self._ShardSerialId = None
        self._ShardInstanceId = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._VpcId = None
        self._SubnetId = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._PeriodEndTime = None
        self._NodeCount = None
        self._StorageUsage = None
        self._MemoryUsage = None
        self._ShardId = None
        self._Pid = None
        self._ProxyVersion = None
        self._Paymode = None
        self._ShardMasterZone = None
        self._ShardSlaveZones = None
        self._Cpu = None
        self._Range = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardSerialId(self):
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId

    @property
    def ShardInstanceId(self):
        return self._ShardInstanceId

    @ShardInstanceId.setter
    def ShardInstanceId(self, ShardInstanceId):
        self._ShardInstanceId = ShardInstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def StorageUsage(self):
        return self._StorageUsage

    @StorageUsage.setter
    def StorageUsage(self, StorageUsage):
        self._StorageUsage = StorageUsage

    @property
    def MemoryUsage(self):
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def ProxyVersion(self):
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def Paymode(self):
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def ShardMasterZone(self):
        return self._ShardMasterZone

    @ShardMasterZone.setter
    def ShardMasterZone(self, ShardMasterZone):
        self._ShardMasterZone = ShardMasterZone

    @property
    def ShardSlaveZones(self):
        return self._ShardSlaveZones

    @ShardSlaveZones.setter
    def ShardSlaveZones(self, ShardSlaveZones):
        self._ShardSlaveZones = ShardSlaveZones

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Range(self):
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardSerialId = params.get("ShardSerialId")
        self._ShardInstanceId = params.get("ShardInstanceId")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._NodeCount = params.get("NodeCount")
        self._StorageUsage = params.get("StorageUsage")
        self._MemoryUsage = params.get("MemoryUsage")
        self._ShardId = params.get("ShardId")
        self._Pid = params.get("Pid")
        self._ProxyVersion = params.get("ProxyVersion")
        self._Paymode = params.get("Paymode")
        self._ShardMasterZone = params.get("ShardMasterZone")
        self._ShardSlaveZones = params.get("ShardSlaveZones")
        self._Cpu = params.get("Cpu")
        self._Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """Database information

    """

    def __init__(self):
        r"""
        :param _DbName: Database name
        :type DbName: str
        """
        self._DbName = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseFunction(AbstractModel):
    """Database function information

    """

    def __init__(self):
        r"""
        :param _Func: Function name
        :type Func: str
        """
        self._Func = None

    @property
    def Func(self):
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func


    def _deserialize(self, params):
        self._Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    """Database permission

    """

    def __init__(self):
        r"""
        :param _Privileges: Permission information
        :type Privileges: list of str
        :param _Database: Database name
        :type Database: str
        """
        self._Privileges = None
        self._Database = None

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database


    def _deserialize(self, params):
        self._Privileges = params.get("Privileges")
        self._Database = params.get("Database")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseProcedure(AbstractModel):
    """Database stored procedure information

    """

    def __init__(self):
        r"""
        :param _Proc: Stored procedure name
        :type Proc: str
        """
        self._Proc = None

    @property
    def Proc(self):
        return self._Proc

    @Proc.setter
    def Proc(self, Proc):
        self._Proc = Proc


    def _deserialize(self, params):
        self._Proc = params.get("Proc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTable(AbstractModel):
    """Database table information

    """

    def __init__(self):
        r"""
        :param _Table: Table name
        :type Table: str
        """
        self._Table = None

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseView(AbstractModel):
    """Database view information

    """

    def __init__(self):
        r"""
        :param _View: View name
        :type View: str
        """
        self._View = None

    @property
    def View(self):
        return self._View

    @View.setter
    def View(self, View):
        self._View = View


    def _deserialize(self, params):
        self._View = params.get("View")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DcnDetailItem(AbstractModel):
    """DCN details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Region: Region where the instance resides
        :type Region: str
        :param _Zone: Availability zone where the instance resides
        :type Zone: str
        :param _Vip: Instance IP address
        :type Vip: str
        :param _Vipv6: Instance IPv6 address
        :type Vipv6: str
        :param _Vport: Instance port
        :type Vport: int
        :param _Status: Instance status
        :type Status: int
        :param _StatusDesc: Instance status description
        :type StatusDesc: str
        :param _DcnFlag: DCN flag. Valid values: `1` (primary), `2` (disaster recovery)
        :type DcnFlag: int
        :param _DcnStatus: DCN status. Valid values: `0` (none), `1` (creating), `2` (syncing), `3` (disconnected)
        :type DcnStatus: int
        :param _Cpu: Number of CPU cores of the instance
        :type Cpu: int
        :param _Memory: Instance memory capacity in GB
        :type Memory: int
        :param _Storage: Instance storage capacity in GB
        :type Storage: int
        :param _PayMode: Billing mode
        :type PayMode: int
        :param _CreateTime: Creation time of the instance in the format of 2006-01-02 15:04:05
        :type CreateTime: str
        :param _PeriodEndTime: Expiration time of the instance in the format of 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param _InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (non-dedicated primary instance), `3` (non-dedicated disaster recovery instance), and `4` (dedicated disaster recovery instance).
        :type InstanceType: int
        :param _EncryptStatus: Whether KMS is enabled.
        :type EncryptStatus: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._Zone = None
        self._Vip = None
        self._Vipv6 = None
        self._Vport = None
        self._Status = None
        self._StatusDesc = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._PayMode = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._InstanceType = None
        self._EncryptStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vipv6(self):
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DcnFlag(self):
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def EncryptStatus(self):
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Vip = params.get("Vip")
        self._Vipv6 = params.get("Vipv6")
        self._Vport = params.get("Vport")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._InstanceType = params.get("InstanceType")
        self._EncryptStatus = params.get("EncryptStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Deal(AbstractModel):
    """Order information

    """

    def __init__(self):
        r"""
        :param _DealName: Order ID.
        :type DealName: str
        :param _OwnerUin: Account
        :type OwnerUin: str
        :param _Count: Number of items
        :type Count: int
        :param _FlowId: The associated process ID, which can be used to query the process execution status.
        :type FlowId: int
        :param _InstanceIds: The ID of the created instance, which is required only for the order that creates an instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIds: list of str
        :param _PayMode: Billing mode. Valid values: `0` (postpaid), `1` (prepaid).
        :type PayMode: int
        """
        self._DealName = None
        self._OwnerUin = None
        self._Count = None
        self._FlowId = None
        self._InstanceIds = None
        self._PayMode = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._OwnerUin = params.get("OwnerUin")
        self._Count = params.get("Count")
        self._FlowId = params.get("FlowId")
        self._InstanceIds = params.get("InstanceIds")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc, which can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceId: str
        :param _UserName: Username
        :type UserName: str
        :param _Host: Access host allowed for a user
        :type Host: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param _UserName: Login username.
        :type UserName: str
        :param _Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param _DbName: Database name. `\*` indicates that global permissions will be queried (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored.
        :type DbName: str
        :param _Type: Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be queried (i.e., `db.\*`), in which case the `Object` parameter will be ignored.
        :type Type: str
        :param _Object: Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty.
        :type Object: str
        :param _ColName: If `Type` is `table` and `ColName` is `\*`, the permissions of the table will be queried; if `ColName` is a specific field name, the permissions of the corresponding field will be queried.
        :type ColName: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._DbName = None
        self._Type = None
        self._Object = None
        self._ColName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def ColName(self):
        return self._ColName

    @ColName.setter
    def ColName(self, ColName):
        self._ColName = ColName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._DbName = params.get("DbName")
        self._Type = params.get("Type")
        self._Object = params.get("Object")
        self._ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Privileges: Permission list
        :type Privileges: list of str
        :param _UserName: Database account username
        :type UserName: str
        :param _Host: Database account host
        :type Host: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Privileges = None
        self._UserName = None
        self._Host = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Privileges = params.get("Privileges")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is passed through from the input parameters.
        :type InstanceId: str
        :param _Users: Instance user list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Users: list of DBAccount
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Users = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = DBAccount()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupFilesRequest(AbstractModel):
    """DescribeBackupFiles request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Query by instance ID
        :type InstanceId: str
        :param _ShardId: Query by shard ID
        :type ShardId: str
        :param _BackupType: Backup type. Valid values: `Data` (data backup), `Binlog` (Binlog backup), `Errlog` (error log), `Slowlog` (slow log).
        :type BackupType: str
        :param _StartTime: Query by start time
        :type StartTime: str
        :param _EndTime: Query by end time
        :type EndTime: str
        :param _Limit: Pagination parameter
        :type Limit: int
        :param _Offset: Pagination parameter
        :type Offset: int
        :param _OrderBy: Sorting dimension. Valid values: `Time`, `Size`.
        :type OrderBy: str
        :param _OrderType: Sorting order. Valid values: `DESC`, `ASC`.
        :type OrderType: str
        """
        self._InstanceId = None
        self._ShardId = None
        self._BackupType = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardId = params.get("ShardId")
        self._BackupType = params.get("BackupType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupFilesResponse(AbstractModel):
    """DescribeBackupFiles response structure.

    """

    def __init__(self):
        r"""
        :param _Files: List of backup files
        :type Files: list of InstanceBackupFileItem
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Files = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Files(self):
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = InstanceBackupFileItem()
                obj._deserialize(item)
                self._Files.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBEncryptAttributesRequest(AbstractModel):
    """DescribeDBEncryptAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of  `tdsqlshard-ow728lmc`
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBEncryptAttributesResponse(AbstractModel):
    """DescribeDBEncryptAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _EncryptStatus: Whether encryption is enabled. Valid values: `1` (enabled), `2` (disabled).
        :type EncryptStatus: int
        :param _CipherText: DEK
        :type CipherText: str
        :param _ExpireDate: DEK expiration date
        :type ExpireDate: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EncryptStatus = None
        self._CipherText = None
        self._ExpireDate = None
        self._RequestId = None

    @property
    def EncryptStatus(self):
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus

    @property
    def CipherText(self):
        return self._CipherText

    @CipherText.setter
    def CipherText(self, CipherText):
        self._CipherText = CipherText

    @property
    def ExpireDate(self):
        return self._ExpireDate

    @ExpireDate.setter
    def ExpireDate(self, ExpireDate):
        self._ExpireDate = ExpireDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EncryptStatus = params.get("EncryptStatus")
        self._CipherText = params.get("CipherText")
        self._ExpireDate = params.get("ExpireDate")
        self._RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param _ShardId: Shard ID in the format of shard-7noic7tv
        :type ShardId: str
        :param _Type: Requested log type. Valid values: 1 (binlog); 2 (cold backup); 3 (errlog); 4 (slowlog).
        :type Type: int
        """
        self._InstanceId = None
        self._ShardId = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardId = params.get("ShardId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _Type: Requested log type. Valid values: 1 (binlog); 2 (cold backup); 3 (errlog); 4 (slowlog).
        :type Type: int
        :param _Total: Total number of requested logs
        :type Total: int
        :param _Files: List of log files
        :type Files: list of LogFileInfo
        :param _VpcPrefix: For an instance in a VPC, this prefix plus URI can be used as the download address
        :type VpcPrefix: str
        :param _NormalPrefix: For an instance in a common network, this prefix plus URI can be used as the download address
        :type NormalPrefix: str
        :param _ShardId: Shard ID in the format of shard-7noic7tv
        :type ShardId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Type = None
        self._Total = None
        self._Files = None
        self._VpcPrefix = None
        self._NormalPrefix = None
        self._ShardId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Files(self):
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def VpcPrefix(self):
        return self._VpcPrefix

    @VpcPrefix.setter
    def VpcPrefix(self, VpcPrefix):
        self._VpcPrefix = VpcPrefix

    @property
    def NormalPrefix(self):
        return self._NormalPrefix

    @NormalPrefix.setter
    def NormalPrefix(self, NormalPrefix):
        self._NormalPrefix = NormalPrefix

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._Total = params.get("Total")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = LogFileInfo()
                obj._deserialize(item)
                self._Files.append(obj)
        self._VpcPrefix = params.get("VpcPrefix")
        self._NormalPrefix = params.get("NormalPrefix")
        self._ShardId = params.get("ShardId")
        self._RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param _Params: Requests the current parameter values of the database
        :type Params: list of ParamDesc
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Params = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self._Params.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._Product = None
        self._InstanceId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group details
        :type Groups: list of SecurityGroup
        :param _VIP: Instance VIP
Note: This field may return null, indicating that no valid values can be obtained.
        :type VIP: str
        :param _VPort: Instance Port
Note: This field may return null, indicating that no valid value can be obtained.
        :type VPort: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._VIP = params.get("VIP")
        self._VPort = params.get("VPort")
        self._RequestId = params.get("RequestId")


class DescribeDBSlowLogsRequest(AbstractModel):
    """DescribeDBSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-hw0qj6m1
        :type InstanceId: str
        :param _Offset: Data entry number starting from which to return results
        :type Offset: int
        :param _Limit: Number of results to be returned
        :type Limit: int
        :param _StartTime: Query start time in the format of 2016-07-23 14:55:20
        :type StartTime: str
        :param _ShardId: Shard ID of the instance in the format of shard-53ima8ln
        :type ShardId: str
        :param _EndTime: Query end time in the format of 2016-08-22 14:55:20. If this parameter is left empty, the current time will be used as the query end time.
        :type EndTime: str
        :param _Db: Specific name of the database to be queried
        :type Db: str
        :param _OrderBy: Sorting metric. Valid values: `query_time_sum`, `query_count`. Default value: `query_time_sum`
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: `desc` (descending), `asc` (ascending). Default value: `desc`
        :type OrderByType: str
        :param _Slave: Query slow queries from either the source or the replica. Valid values: `0` (source), `1` (replica). Default value: `0`
        :type Slave: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._ShardId = None
        self._EndTime = None
        self._Db = None
        self._OrderBy = None
        self._OrderByType = None
        self._Slave = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Slave(self):
        return self._Slave

    @Slave.setter
    def Slave(self, Slave):
        self._Slave = Slave


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._ShardId = params.get("ShardId")
        self._EndTime = params.get("EndTime")
        self._Db = params.get("Db")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Slave = params.get("Slave")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSlowLogsResponse(AbstractModel):
    """DescribeDBSlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _LockTimeSum: Sum of all statement lock durations
        :type LockTimeSum: float
        :param _QueryCount: Total number of statement queries
        :type QueryCount: int
        :param _Total: Total number of results
        :type Total: int
        :param _QueryTimeSum: Sum of all statement query durations
        :type QueryTimeSum: float
        :param _Data: Slow query log data
        :type Data: list of SlowLogData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LockTimeSum = None
        self._QueryCount = None
        self._Total = None
        self._QueryTimeSum = None
        self._Data = None
        self._RequestId = None

    @property
    def LockTimeSum(self):
        return self._LockTimeSum

    @LockTimeSum.setter
    def LockTimeSum(self, LockTimeSum):
        self._LockTimeSum = LockTimeSum

    @property
    def QueryCount(self):
        return self._QueryCount

    @QueryCount.setter
    def QueryCount(self, QueryCount):
        self._QueryCount = QueryCount

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def QueryTimeSum(self):
        return self._QueryTimeSum

    @QueryTimeSum.setter
    def QueryTimeSum(self, QueryTimeSum):
        self._QueryTimeSum = QueryTimeSum

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LockTimeSum = params.get("LockTimeSum")
        self._QueryCount = params.get("QueryCount")
        self._Total = params.get("Total")
        self._QueryTimeSum = params.get("QueryTimeSum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SlowLogData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSyncModeRequest(AbstractModel):
    """DescribeDBSyncMode request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of an instance for which to modify the sync mode. The ID is in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSyncModeResponse(AbstractModel):
    """DescribeDBSyncMode response structure.

    """

    def __init__(self):
        r"""
        :param _SyncMode: Sync mode. 0: async; 1: strong sync; 2: downgradable strong sync
        :type SyncMode: int
        :param _IsModifying: Whether a modification is in progress. 1: yes; 0: no.
        :type IsModifying: int
        :param _CurrentSyncMode: Current sync mode. Valid values: `0` (async), `1` (sync).
        :type CurrentSyncMode: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SyncMode = None
        self._IsModifying = None
        self._CurrentSyncMode = None
        self._RequestId = None

    @property
    def SyncMode(self):
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def IsModifying(self):
        return self._IsModifying

    @IsModifying.setter
    def IsModifying(self, IsModifying):
        self._IsModifying = IsModifying

    @property
    def CurrentSyncMode(self):
        return self._CurrentSyncMode

    @CurrentSyncMode.setter
    def CurrentSyncMode(self, CurrentSyncMode):
        self._CurrentSyncMode = CurrentSyncMode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SyncMode = params.get("SyncMode")
        self._IsModifying = params.get("IsModifying")
        self._CurrentSyncMode = params.get("CurrentSyncMode")
        self._RequestId = params.get("RequestId")


class DescribeDCDBInstanceDetailRequest(AbstractModel):
    """DescribeDCDBInstanceDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, such as dcdbt-7oaxtcb7.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBInstanceDetailResponse(AbstractModel):
    """DescribeDCDBInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, such as dcdbt-7oaxtcb7.
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Status: Instance status. Valid values: `0` (creating), `1` (running task), `2` (running), `3` (uninitialized), `-1` (isolated).
        :type Status: int
        :param _StatusDesc: Current status of the instance
        :type StatusDesc: str
        :param _Vip: Instance private IP address
        :type Vip: str
        :param _Vport: Private port of instance
        :type Vport: int
        :param _NodeCount: Number of instance nodes. Valid values: `2` (1-source-1-replica), `3` (1-source-2-replica).
        :type NodeCount: int
        :param _Region: Instance region, such as ap-guangzhou.
        :type Region: str
        :param _VpcId: Instance VPC ID, such as vpc-r9jr0de3.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID of an instance, such as subnet-6rqs61o2.
        :type SubnetId: str
        :param _WanStatus: Public network status. Valid values: `0` (not enabled), `1` (enabled), `2` (disabled), `3`: (enabling), `4` (disabling).
        :type WanStatus: int
        :param _WanDomain: Domain name for public network access, which can be resolved by the public network.
        :type WanDomain: str
        :param _WanVip: Public IP address, which can be accessed over the public network.
        :type WanVip: str
        :param _WanPort: Public network access port
        :type WanPort: int
        :param _ProjectId: Project ID of the instance
        :type ProjectId: int
        :param _AutoRenewFlag: Automatic renewal flag for an instance. Valid values: `0` (normal renewal), `1` (auto-renewal), `3` (no renewal upon expiration).
        :type AutoRenewFlag: int
        :param _ExclusterId: Dedicated cluster ID
        :type ExclusterId: str
        :param _PayMode: Billing mode. Valid values: `prepaid` (monthly subscription), `postpaid` (pay-as-you-go).
        :type PayMode: str
        :param _CreateTime: Creation time of the instance in the format of 2006-01-02 15:04:05
        :type CreateTime: str
        :param _PeriodEndTime: Expiration time of the instance in the format of 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param _DbVersion: Database version information
        :type DbVersion: str
        :param _IsAuditSupported: Whether the instance supports audit. Valid values: `1` (yes), `0` (no).
        :type IsAuditSupported: int
        :param _IsEncryptSupported: Whether data encryption is supported for an instance. Valid values: `1` (yes), `0` (no).
        :type IsEncryptSupported: int
        :param _Machine: Instance machine model
        :type Machine: str
        :param _Memory: Instance memory size in GB, which is the sum of the memory of all shards.
        :type Memory: int
        :param _Storage: Instance disk storage size in GB, which is the sum of the disk size of all shards.
        :type Storage: int
        :param _StorageUsage: Instance storage space utilization. It is calculated by dividing the sum of the used disk size of all shards by the total disk size of all shards.
        :type StorageUsage: float
        :param _LogStorage: Size of log storage space in GB
        :type LogStorage: int
        :param _Pid: Product type ID
        :type Pid: int
        :param _MasterZone: Source AZ
        :type MasterZone: str
        :param _SlaveZones: Replica AZ
        :type SlaveZones: list of str
        :param _Shards: Shard information
        :type Shards: list of ShardBriefInfo
        :param _Vip6: Private network IPv6 address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vip6: str
        :param _Cpu: Number of CPU cores of an instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param _Qps: Instance QPS
Note: This field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param _DbEngine: Database engine
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbEngine: str
        :param _Ipv6Flag: Whether IPv6 is supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv6Flag: int
        :param _WanVipv6: Public IPv6 address, which can be accessed over the public network
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanVipv6: str
        :param _WanStatusIpv6: Public network status. Valid values: `0` (not enabled), `1` (enabled), `2` (disabled), `3`: (enabling), `4` (disabling).
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanStatusIpv6: int
        :param _WanPortIpv6: Public network IPv6 port
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanPortIpv6: int
        :param _ResourceTags: Tag information
        :type ResourceTags: list of ResourceTag
        :param _DcnFlag: DCN type. Valid values: `0` (N/A), `1` (source instance), `2` (disaster recovery read-only instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DcnFlag: int
        :param _DcnStatus: DCN status. Valid values: `0` (N/A), `1` (creating), `2` (syncing), `3` (disconnected).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DcnStatus: int
        :param _DcnDstNum: The number of DCN disaster recovery instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type DcnDstNum: int
        :param _InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (non-dedicated primary instance), `3` (non-dedicated disaster recovery read-only instance), `4` (dedicated disaster recovery read-only instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: int
        :param _IsMaxUserConnectionsSupported: Whether the instance supports setting the connection limit, which is not supported for kernel version 10.1.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsMaxUserConnectionsSupported: bool
        :param _DbVersionId: The displayed database version
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbVersionId: str
        :param _EncryptStatus: Encryption status. Valid values: `0` (disabled), `1` (enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptStatus: int
        :param _ExclusterType: Type of dedicated cluster. Valid values: `0` (public cloud), `1` (finance cage), `2` (CDC cluster).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExclusterType: int
        :param _RsAccessStrategy: Nearby VPC access
Note: This field may return null, indicating that no valid values can be obtained.
        :type RsAccessStrategy: int
        :param _ReservedNetResources: Unclaimed network resource
        :type ReservedNetResources: list of ReservedNetResource
        :param _IsPhysicalReplicationSupported: 
        :type IsPhysicalReplicationSupported: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._StatusDesc = None
        self._Vip = None
        self._Vport = None
        self._NodeCount = None
        self._Region = None
        self._VpcId = None
        self._SubnetId = None
        self._WanStatus = None
        self._WanDomain = None
        self._WanVip = None
        self._WanPort = None
        self._ProjectId = None
        self._AutoRenewFlag = None
        self._ExclusterId = None
        self._PayMode = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._DbVersion = None
        self._IsAuditSupported = None
        self._IsEncryptSupported = None
        self._Machine = None
        self._Memory = None
        self._Storage = None
        self._StorageUsage = None
        self._LogStorage = None
        self._Pid = None
        self._MasterZone = None
        self._SlaveZones = None
        self._Shards = None
        self._Vip6 = None
        self._Cpu = None
        self._Qps = None
        self._DbEngine = None
        self._Ipv6Flag = None
        self._WanVipv6 = None
        self._WanStatusIpv6 = None
        self._WanPortIpv6 = None
        self._ResourceTags = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._DcnDstNum = None
        self._InstanceType = None
        self._IsMaxUserConnectionsSupported = None
        self._DbVersionId = None
        self._EncryptStatus = None
        self._ExclusterType = None
        self._RsAccessStrategy = None
        self._ReservedNetResources = None
        self._IsPhysicalReplicationSupported = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanVip(self):
        return self._WanVip

    @WanVip.setter
    def WanVip(self, WanVip):
        self._WanVip = WanVip

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ExclusterId(self):
        return self._ExclusterId

    @ExclusterId.setter
    def ExclusterId(self, ExclusterId):
        self._ExclusterId = ExclusterId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def IsAuditSupported(self):
        return self._IsAuditSupported

    @IsAuditSupported.setter
    def IsAuditSupported(self, IsAuditSupported):
        self._IsAuditSupported = IsAuditSupported

    @property
    def IsEncryptSupported(self):
        return self._IsEncryptSupported

    @IsEncryptSupported.setter
    def IsEncryptSupported(self, IsEncryptSupported):
        self._IsEncryptSupported = IsEncryptSupported

    @property
    def Machine(self):
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageUsage(self):
        return self._StorageUsage

    @StorageUsage.setter
    def StorageUsage(self, StorageUsage):
        self._StorageUsage = StorageUsage

    @property
    def LogStorage(self):
        return self._LogStorage

    @LogStorage.setter
    def LogStorage(self, LogStorage):
        self._LogStorage = LogStorage

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def Shards(self):
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def Vip6(self):
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def DbEngine(self):
        return self._DbEngine

    @DbEngine.setter
    def DbEngine(self, DbEngine):
        self._DbEngine = DbEngine

    @property
    def Ipv6Flag(self):
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def WanVipv6(self):
        return self._WanVipv6

    @WanVipv6.setter
    def WanVipv6(self, WanVipv6):
        self._WanVipv6 = WanVipv6

    @property
    def WanStatusIpv6(self):
        return self._WanStatusIpv6

    @WanStatusIpv6.setter
    def WanStatusIpv6(self, WanStatusIpv6):
        self._WanStatusIpv6 = WanStatusIpv6

    @property
    def WanPortIpv6(self):
        return self._WanPortIpv6

    @WanPortIpv6.setter
    def WanPortIpv6(self, WanPortIpv6):
        self._WanPortIpv6 = WanPortIpv6

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DcnFlag(self):
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def DcnDstNum(self):
        return self._DcnDstNum

    @DcnDstNum.setter
    def DcnDstNum(self, DcnDstNum):
        self._DcnDstNum = DcnDstNum

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def IsMaxUserConnectionsSupported(self):
        return self._IsMaxUserConnectionsSupported

    @IsMaxUserConnectionsSupported.setter
    def IsMaxUserConnectionsSupported(self, IsMaxUserConnectionsSupported):
        self._IsMaxUserConnectionsSupported = IsMaxUserConnectionsSupported

    @property
    def DbVersionId(self):
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def EncryptStatus(self):
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus

    @property
    def ExclusterType(self):
        return self._ExclusterType

    @ExclusterType.setter
    def ExclusterType(self, ExclusterType):
        self._ExclusterType = ExclusterType

    @property
    def RsAccessStrategy(self):
        return self._RsAccessStrategy

    @RsAccessStrategy.setter
    def RsAccessStrategy(self, RsAccessStrategy):
        self._RsAccessStrategy = RsAccessStrategy

    @property
    def ReservedNetResources(self):
        return self._ReservedNetResources

    @ReservedNetResources.setter
    def ReservedNetResources(self, ReservedNetResources):
        self._ReservedNetResources = ReservedNetResources

    @property
    def IsPhysicalReplicationSupported(self):
        return self._IsPhysicalReplicationSupported

    @IsPhysicalReplicationSupported.setter
    def IsPhysicalReplicationSupported(self, IsPhysicalReplicationSupported):
        self._IsPhysicalReplicationSupported = IsPhysicalReplicationSupported

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._NodeCount = params.get("NodeCount")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._WanStatus = params.get("WanStatus")
        self._WanDomain = params.get("WanDomain")
        self._WanVip = params.get("WanVip")
        self._WanPort = params.get("WanPort")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ExclusterId = params.get("ExclusterId")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._DbVersion = params.get("DbVersion")
        self._IsAuditSupported = params.get("IsAuditSupported")
        self._IsEncryptSupported = params.get("IsEncryptSupported")
        self._Machine = params.get("Machine")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._StorageUsage = params.get("StorageUsage")
        self._LogStorage = params.get("LogStorage")
        self._Pid = params.get("Pid")
        self._MasterZone = params.get("MasterZone")
        self._SlaveZones = params.get("SlaveZones")
        if params.get("Shards") is not None:
            self._Shards = []
            for item in params.get("Shards"):
                obj = ShardBriefInfo()
                obj._deserialize(item)
                self._Shards.append(obj)
        self._Vip6 = params.get("Vip6")
        self._Cpu = params.get("Cpu")
        self._Qps = params.get("Qps")
        self._DbEngine = params.get("DbEngine")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._WanVipv6 = params.get("WanVipv6")
        self._WanStatusIpv6 = params.get("WanStatusIpv6")
        self._WanPortIpv6 = params.get("WanPortIpv6")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._DcnDstNum = params.get("DcnDstNum")
        self._InstanceType = params.get("InstanceType")
        self._IsMaxUserConnectionsSupported = params.get("IsMaxUserConnectionsSupported")
        self._DbVersionId = params.get("DbVersionId")
        self._EncryptStatus = params.get("EncryptStatus")
        self._ExclusterType = params.get("ExclusterType")
        self._RsAccessStrategy = params.get("RsAccessStrategy")
        if params.get("ReservedNetResources") is not None:
            self._ReservedNetResources = []
            for item in params.get("ReservedNetResources"):
                obj = ReservedNetResource()
                obj._deserialize(item)
                self._ReservedNetResources.append(obj)
        self._IsPhysicalReplicationSupported = params.get("IsPhysicalReplicationSupported")
        self._RequestId = params.get("RequestId")


class DescribeDCDBInstanceNodeInfoRequest(AbstractModel):
    """DescribeDCDBInstanceNodeInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Limit: The maximum number of results returned at a time. Value range: (0-100]. Default value: `100`.
        :type Limit: int
        :param _Offset: Offset of the returned results. Default value: `0`.
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBInstanceNodeInfoResponse(AbstractModel):
    """DescribeDCDBInstanceNodeInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of nodes
        :type TotalCount: int
        :param _NodesInfo: Node information
        :type NodesInfo: list of BriefNodeInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodesInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodesInfo(self):
        return self._NodesInfo

    @NodesInfo.setter
    def NodesInfo(self, NodesInfo):
        self._NodesInfo = NodesInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodesInfo") is not None:
            self._NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = BriefNodeInfo()
                obj._deserialize(item)
                self._NodesInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDCDBInstancesRequest(AbstractModel):
    """DescribeDCDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Query by instance ID or IDs. Instance ID is in the format of dcdbt-2t4cf98d
        :type InstanceIds: list of str
        :param _SearchName: Search field name. Valid values: instancename (search by instance name); vip (search by private IP); all (search by instance ID, instance name, and private IP).
        :type SearchName: str
        :param _SearchKey: Search keyword. Fuzzy search is supported. Multiple keywords should be separated by line breaks (`\n`).
        :type SearchKey: str
        :param _ProjectIds: Query by project ID
        :type ProjectIds: list of int
        :param _IsFilterVpc: Whether to search by VPC
        :type IsFilterVpc: bool
        :param _VpcId: VPC ID, which is valid when `IsFilterVpc` is 1
        :type VpcId: str
        :param _SubnetId: VPC subnet ID, which is valid when `IsFilterVpc` is 1
        :type SubnetId: str
        :param _OrderBy: Sort by field. Valid values: projectId; createtime; instancename
        :type OrderBy: str
        :param _OrderByType: Sort by type. Valid values: desc; asc
        :type OrderByType: str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _ExclusterType: 1: non-dedicated cluster; 2: dedicated cluster; 0: all
        :type ExclusterType: int
        :param _IsFilterExcluster: Identifies whether to use the `ExclusterType` field. false: no; true: yes
        :type IsFilterExcluster: bool
        :param _ExclusterIds: Dedicated cluster ID
        :type ExclusterIds: list of str
        :param _TagKeys: Tag key used in queries
        :type TagKeys: list of str
        :param _FilterInstanceType: Instance types used in filtering. Valid values: 1 (dedicated instance), 2 (primary instance), 3 (disaster recovery instance). Multiple values should be separated by commas.
        :type FilterInstanceType: str
        :param _Status: Use this filter to include instances in specific statuses
        :type Status: list of int
        :param _ExcludeStatus: Use this filter to exclude instances in specific statuses
        :type ExcludeStatus: list of int
        """
        self._InstanceIds = None
        self._SearchName = None
        self._SearchKey = None
        self._ProjectIds = None
        self._IsFilterVpc = None
        self._VpcId = None
        self._SubnetId = None
        self._OrderBy = None
        self._OrderByType = None
        self._Offset = None
        self._Limit = None
        self._ExclusterType = None
        self._IsFilterExcluster = None
        self._ExclusterIds = None
        self._TagKeys = None
        self._FilterInstanceType = None
        self._Status = None
        self._ExcludeStatus = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def SearchName(self):
        return self._SearchName

    @SearchName.setter
    def SearchName(self, SearchName):
        self._SearchName = SearchName

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def IsFilterVpc(self):
        return self._IsFilterVpc

    @IsFilterVpc.setter
    def IsFilterVpc(self, IsFilterVpc):
        self._IsFilterVpc = IsFilterVpc

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ExclusterType(self):
        return self._ExclusterType

    @ExclusterType.setter
    def ExclusterType(self, ExclusterType):
        self._ExclusterType = ExclusterType

    @property
    def IsFilterExcluster(self):
        return self._IsFilterExcluster

    @IsFilterExcluster.setter
    def IsFilterExcluster(self, IsFilterExcluster):
        self._IsFilterExcluster = IsFilterExcluster

    @property
    def ExclusterIds(self):
        return self._ExclusterIds

    @ExclusterIds.setter
    def ExclusterIds(self, ExclusterIds):
        self._ExclusterIds = ExclusterIds

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def FilterInstanceType(self):
        return self._FilterInstanceType

    @FilterInstanceType.setter
    def FilterInstanceType(self, FilterInstanceType):
        self._FilterInstanceType = FilterInstanceType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExcludeStatus(self):
        return self._ExcludeStatus

    @ExcludeStatus.setter
    def ExcludeStatus(self, ExcludeStatus):
        self._ExcludeStatus = ExcludeStatus


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._SearchName = params.get("SearchName")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._IsFilterVpc = params.get("IsFilterVpc")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ExclusterType = params.get("ExclusterType")
        self._IsFilterExcluster = params.get("IsFilterExcluster")
        self._ExclusterIds = params.get("ExclusterIds")
        self._TagKeys = params.get("TagKeys")
        self._FilterInstanceType = params.get("FilterInstanceType")
        self._Status = params.get("Status")
        self._ExcludeStatus = params.get("ExcludeStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBInstancesResponse(AbstractModel):
    """DescribeDCDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances
        :type TotalCount: int
        :param _Instances: List of instance details
        :type Instances: list of DCDBInstanceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = DCDBInstanceInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDCDBPriceRequest(AbstractModel):
    """DescribeDCDBPrice request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ ID of the purchased instance.
        :type Zone: str
        :param _Count: The number of instances to be purchased. You can purchase 1-10 instances.
        :type Count: int
        :param _Period: Validity period in months
        :type Period: int
        :param _ShardNodeCount: Number of nodes in a single shard, which can be obtained
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :type ShardNodeCount: int
        :param _ShardMemory: Shard memory size in GB, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :type ShardMemory: int
        :param _ShardStorage: Shard storage size in GB, which can be obtained
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :type ShardStorage: int
        :param _ShardCount: The number of shards in the instance. Value range: 2-8. Upgrade your instance to have up to 64 shards if you require more.
        :type ShardCount: int
        :param _Paymode: Billing type. Valid values: `postpaid` (pay-as-you-go), `prepaid` (monthly subscription).
        :type Paymode: str
        :param _AmountUnit: Price unit. Valid values:   
`* pent` (cent), 
`* microPent` (microcent).
        :type AmountUnit: str
        """
        self._Zone = None
        self._Count = None
        self._Period = None
        self._ShardNodeCount = None
        self._ShardMemory = None
        self._ShardStorage = None
        self._ShardCount = None
        self._Paymode = None
        self._AmountUnit = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ShardNodeCount(self):
        return self._ShardNodeCount

    @ShardNodeCount.setter
    def ShardNodeCount(self, ShardNodeCount):
        self._ShardNodeCount = ShardNodeCount

    @property
    def ShardMemory(self):
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ShardCount(self):
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def Paymode(self):
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def AmountUnit(self):
        return self._AmountUnit

    @AmountUnit.setter
    def AmountUnit(self, AmountUnit):
        self._AmountUnit = AmountUnit


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Count = params.get("Count")
        self._Period = params.get("Period")
        self._ShardNodeCount = params.get("ShardNodeCount")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ShardCount = params.get("ShardCount")
        self._Paymode = params.get("Paymode")
        self._AmountUnit = params.get("AmountUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBPriceResponse(AbstractModel):
    """DescribeDCDBPrice response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Original price  
* Unit: Cent (default). If the request parameter contains `AmountUnit`, see `AmountUnit` description.
* Currency: CNY (Chinese site), USD (international site)
        :type OriginalPrice: int
        :param _Price: The actual price may be different from the original price due to discounts. 
* Unit: Cent (default). If the request parameter contains `AmountUnit`, see `AmountUnit` description.
* Currency: CNY (Chinese site), USD (international site)
        :type Price: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class DescribeDCDBShardsRequest(AbstractModel):
    """DescribeDCDBShards request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _ShardInstanceIds: Shard ID list.
        :type ShardInstanceIds: list of str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _OrderBy: Sort by field. Only `createtime` is supported currently.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: desc, asc
        :type OrderByType: str
        """
        self._InstanceId = None
        self._ShardInstanceIds = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardInstanceIds(self):
        return self._ShardInstanceIds

    @ShardInstanceIds.setter
    def ShardInstanceIds(self, ShardInstanceIds):
        self._ShardInstanceIds = ShardInstanceIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardInstanceIds = params.get("ShardInstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBShardsResponse(AbstractModel):
    """DescribeDCDBShards response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible shards
        :type TotalCount: int
        :param _Shards: Shard information list
        :type Shards: list of DCDBShardInfo
        :param _DcnFlag: Disaster recovery flag. Valid values: 0 (none), 1 (source instance), 2 (disaster recovery instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DcnFlag: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Shards = None
        self._DcnFlag = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Shards(self):
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def DcnFlag(self):
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Shards") is not None:
            self._Shards = []
            for item in params.get("Shards"):
                obj = DCDBShardInfo()
                obj._deserialize(item)
                self._Shards.append(obj)
        self._DcnFlag = params.get("DcnFlag")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    """DescribeDatabaseObjects request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param _DbName: Database name, which can be obtained through the `DescribeDatabases` API.
        :type DbName: str
        """
        self._InstanceId = None
        self._DbName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    """DescribeDatabaseObjects response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Passed through from input parameters.
        :type InstanceId: str
        :param _DbName: Database name.
        :type DbName: str
        :param _Tables: Table list.
        :type Tables: list of DatabaseTable
        :param _Views: View list.
        :type Views: list of DatabaseView
        :param _Procs: Stored procedure list.
        :type Procs: list of DatabaseProcedure
        :param _Funcs: Function list.
        :type Funcs: list of DatabaseFunction
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Tables = None
        self._Views = None
        self._Procs = None
        self._Funcs = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Views(self):
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def Procs(self):
        return self._Procs

    @Procs.setter
    def Procs(self, Procs):
        self._Procs = Procs

    @property
    def Funcs(self):
        return self._Funcs

    @Funcs.setter
    def Funcs(self, Funcs):
        self._Funcs = Funcs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTable()
                obj._deserialize(item)
                self._Tables.append(obj)
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = DatabaseView()
                obj._deserialize(item)
                self._Views.append(obj)
        if params.get("Procs") is not None:
            self._Procs = []
            for item in params.get("Procs"):
                obj = DatabaseProcedure()
                obj._deserialize(item)
                self._Procs.append(obj)
        if params.get("Funcs") is not None:
            self._Funcs = []
            for item in params.get("Funcs"):
                obj = DatabaseFunction()
                obj._deserialize(item)
                self._Funcs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseTableRequest(AbstractModel):
    """DescribeDatabaseTable request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param _DbName: Database name, which can be obtained through the `DescribeDatabases` API.
        :type DbName: str
        :param _Table: Table name, which can be obtained through the `DescribeDatabaseObjects` API.
        :type Table: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Table = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseTableResponse(AbstractModel):
    """DescribeDatabaseTable response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name.
        :type InstanceId: str
        :param _DbName: Database name.
        :type DbName: str
        :param _Table: Table name.
        :type Table: str
        :param _Cols: Column information.
        :type Cols: list of TableColumn
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Table = None
        self._Cols = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Cols(self):
        return self._Cols

    @Cols.setter
    def Cols(self, Cols):
        self._Cols = Cols

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        if params.get("Cols") is not None:
            self._Cols = []
            for item in params.get("Cols"):
                obj = TableColumn()
                obj._deserialize(item)
                self._Cols.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases response structure.

    """

    def __init__(self):
        r"""
        :param _Databases: The database list of this instance.
        :type Databases: list of Database
        :param _InstanceId: Passed through from input parameters.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Databases = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DescribeDcnDetailRequest(AbstractModel):
    """DescribeDcnDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDcnDetailResponse(AbstractModel):
    """DescribeDcnDetail response structure.

    """

    def __init__(self):
        r"""
        :param _DcnDetails: DCN synchronization details
        :type DcnDetails: list of DcnDetailItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DcnDetails = None
        self._RequestId = None

    @property
    def DcnDetails(self):
        return self._DcnDetails

    @DcnDetails.setter
    def DcnDetails(self, DcnDetails):
        self._DcnDetails = DcnDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DcnDetails") is not None:
            self._DcnDetails = []
            for item in params.get("DcnDetails"):
                obj = DcnDetailItem()
                obj._deserialize(item)
                self._DcnDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileDownloadUrlRequest(AbstractModel):
    """DescribeFileDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ShardId: Shard ID
        :type ShardId: str
        :param _FilePath: Unsigned file path
        :type FilePath: str
        """
        self._InstanceId = None
        self._ShardId = None
        self._FilePath = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardId = params.get("ShardId")
        self._FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileDownloadUrlResponse(AbstractModel):
    """DescribeFileDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _PreSignedUrl: Signed download URL
        :type PreSignedUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PreSignedUrl = None
        self._RequestId = None

    @property
    def PreSignedUrl(self):
        return self._PreSignedUrl

    @PreSignedUrl.setter
    def PreSignedUrl(self, PreSignedUrl):
        self._PreSignedUrl = PreSignedUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PreSignedUrl = params.get("PreSignedUrl")
        self._RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID returned by an async request API.
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status. Valid values: `0` (succeeded), `1` (failed), `2` (running)
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders request structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: List of long order IDs to be queried, which are returned by the APIs for creating, renewing, or scaling instances.
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Returned number of orders
        :type TotalCount: int
        :param _Deals: Order information list
        :type Deals: list of Deal
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Deals = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Deals(self):
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._Product = None
        self._ProjectId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group details
        :type Groups: list of SecurityGroup
        :param _Total: Number of security groups.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DestroyDCDBInstanceRequest(AbstractModel):
    """DestroyDCDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of tdsqlshard-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDCDBInstanceResponse(AbstractModel):
    """DestroyDCDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is the same as the request parameter `InstanceId`.
        :type InstanceId: str
        :param _FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/557/56485?from_cn_redirect=1) API to query the async task result.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DestroyHourDCDBInstanceRequest(AbstractModel):
    """DestroyHourDCDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of tdsqlshard-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyHourDCDBInstanceResponse(AbstractModel):
    """DestroyHourDCDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/557/56485?from_cn_redirect=1) API to query the async task result.
        :type FlowId: int
        :param _InstanceId: Instance ID, which is the same as the request parameter `InstanceId`.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _InstanceIds: Instance ID list, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ExpandShardConfig(AbstractModel):
    """Instance upgrade -- Expanding shard

    """

    def __init__(self):
        r"""
        :param _ShardInstanceIds: Shard IDs in array
        :type ShardInstanceIds: list of str
        :param _ShardMemory: Shard memory capacity in GB
        :type ShardMemory: int
        :param _ShardStorage: Shard storage capacity in GB
        :type ShardStorage: int
        :param _ShardNodeCount: Number of shard nodes
        :type ShardNodeCount: int
        """
        self._ShardInstanceIds = None
        self._ShardMemory = None
        self._ShardStorage = None
        self._ShardNodeCount = None

    @property
    def ShardInstanceIds(self):
        return self._ShardInstanceIds

    @ShardInstanceIds.setter
    def ShardInstanceIds(self, ShardInstanceIds):
        self._ShardInstanceIds = ShardInstanceIds

    @property
    def ShardMemory(self):
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ShardNodeCount(self):
        return self._ShardNodeCount

    @ShardNodeCount.setter
    def ShardNodeCount(self, ShardNodeCount):
        self._ShardNodeCount = ShardNodeCount


    def _deserialize(self, params):
        self._ShardInstanceIds = params.get("ShardInstanceIds")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ShardNodeCount = params.get("ShardNodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _UserName: Login username.
        :type UserName: str
        :param _Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param _DbName: Database name. `\*` indicates that global permissions will be queried (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored
        :type DbName: str
        :param _Privileges: Global permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER ROUTINE`, `EVENT`, `TRIGGER`, `SHOW DATABASES`, `REPLICATION CLIENT`, `REPLICATION SLAVE`.
Database permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER ROUTINE`, `EVENT`, `TRIGGER`. 
Table permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`.  
Field permission. Valid values: `INSERT`, `REFERENCES`, `SELECT`, `UPDATE`.
        :type Privileges: list of str
        :param _Type: Type. Valid values: `table`, `\*`. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be set (i.e., `db.\*`), in which case the `Object` parameter will be ignored
        :type Type: str
        :param _Object: Type name. For example, if `Type` is table, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty
        :type Object: str
        :param _ColName: If `Type` = table and `ColName` is `\*`, the permissions will be granted to the table; if `ColName` is a specific field name, the permissions will be granted to the field
        :type ColName: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._DbName = None
        self._Privileges = None
        self._Type = None
        self._Object = None
        self._ColName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def ColName(self):
        return self._ColName

    @ColName.setter
    def ColName(self, ColName):
        self._ColName = ColName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._DbName = params.get("DbName")
        self._Privileges = params.get("Privileges")
        self._Type = params.get("Type")
        self._Object = params.get("Object")
        self._ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class InitDCDBInstancesRequest(AbstractModel):
    """InitDCDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of IDs of instances to be initialized. The ID is in the format of `dcdbt-ow728lmc` and can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceIds: list of str
        :param _Params: Parameter list. Valid values: character_set_server (character set; required); lower_case_table_names (table name case sensitivity; required; 0: case-sensitive, 1: case-insensitive); innodb_page_size (InnoDB data page; default size: 16 KB); sync_mode (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: strong sync).
        :type Params: list of DBParamValue
        """
        self._InstanceIds = None
        self._Params = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDCDBInstancesResponse(AbstractModel):
    """InitDCDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _FlowIds: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowIds: list of int non-negative
        :param _InstanceIds: Passed through from input parameters.
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowIds = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowIds = params.get("FlowIds")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class InstanceBackupFileItem(AbstractModel):
    """Backup file details of an instance

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceStatus: Instance status
        :type InstanceStatus: int
        :param _ShardId: Shard ID
        :type ShardId: str
        :param _FilePath: File path
        :type FilePath: str
        :param _FileName: File name
        :type FileName: str
        :param _FileSize: File size
        :type FileSize: int
        :param _BackupType: Backup type. Valid values: `Data` (data backup), `Binlog` (Binlog backup), `Errlog` (error log), `Slowlog` (slow log).
        :type BackupType: str
        :param _ManualBackup: Manual backup. Valid values: `0` (no), `1` (yes).
        :type ManualBackup: int
        :param _StartTime: Backup start time
        :type StartTime: str
        :param _EndTime: Backup end time
        :type EndTime: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceStatus = None
        self._ShardId = None
        self._FilePath = None
        self._FileName = None
        self._FileSize = None
        self._BackupType = None
        self._ManualBackup = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def ManualBackup(self):
        return self._ManualBackup

    @ManualBackup.setter
    def ManualBackup(self, ManualBackup):
        self._ManualBackup = ManualBackup

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceStatus = params.get("InstanceStatus")
        self._ShardId = params.get("ShardId")
        self._FilePath = params.get("FilePath")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._BackupType = params.get("BackupType")
        self._ManualBackup = params.get("ManualBackup")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDCDBInstanceRequest(AbstractModel):
    """IsolateDCDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID in the format of `tdsqlshard-avw0207d`,  which is the same as the instance ID displayed on the TencentDB console and can be queried through the `DescribeDBInstances` API.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDCDBInstanceResponse(AbstractModel):
    """IsolateDCDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: IDs of isolated instances
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: IDs of instances failed to be isolated
        :type FailedInstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class IsolateDedicatedDBInstanceRequest(AbstractModel):
    """IsolateDedicatedDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `dcdbt-ow728lmc`
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDedicatedDBInstanceResponse(AbstractModel):
    """IsolateDedicatedDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class IsolateHourDCDBInstanceRequest(AbstractModel):
    """IsolateHourDCDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: ID list of the instances to be upgraded  in the format of  `dcdbt-ow728lmc`, which can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateHourDCDBInstanceResponse(AbstractModel):
    """IsolateHourDCDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: IDs of isolated instances
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: IDs of instances failed to be isolated
        :type FailedInstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class KillSessionRequest(AbstractModel):
    """KillSession request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SessionId: List of session IDs
        :type SessionId: list of int
        :param _ShardId: Shard ID. Either `ShardId` or `ShardSerialId` is required.
        :type ShardId: str
        :param _ShardSerialId: Shard sequence ID. Either `ShardId` or `ShardSerialId` is required.
        :type ShardSerialId: str
        """
        self._InstanceId = None
        self._SessionId = None
        self._ShardId = None
        self._ShardSerialId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def ShardSerialId(self):
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SessionId = params.get("SessionId")
        self._ShardId = params.get("ShardId")
        self._ShardSerialId = params.get("ShardSerialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillSessionResponse(AbstractModel):
    """KillSession response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class LogFileInfo(AbstractModel):
    """Information of a pulled log

    """

    def __init__(self):
        r"""
        :param _Mtime: Last modified time of a log
        :type Mtime: int
        :param _Length: File length
        :type Length: int
        :param _Uri: Uniform resource identifier (URI) used during log download
        :type Uri: str
        :param _FileName: Filename
        :type FileName: str
        """
        self._Mtime = None
        self._Length = None
        self._Uri = None
        self._FileName = None

    @property
    def Mtime(self):
        return self._Mtime

    @Mtime.setter
    def Mtime(self, Mtime):
        self._Mtime = Mtime

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._Mtime = params.get("Mtime")
        self._Length = params.get("Length")
        self._Uri = params.get("Uri")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountConfigRequest(AbstractModel):
    """ModifyAccountConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of  `tdsqlshard-kpkvq5oj`, which is the same as the one displayed in the TencentDB console.
        :type InstanceId: str
        :param _UserName: Account name
        :type UserName: str
        :param _Host: Account domain name
        :type Host: str
        :param _Configs: Configuration list. Each element in the list is a pair of `Config` and `Value`.
        :type Configs: list of ConfigValue
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Configs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigValue()
                obj._deserialize(item)
                self._Configs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountConfigResponse(AbstractModel):
    """ModifyAccountConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _UserName: Login username.
        :type UserName: str
        :param _Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param _Description: New account remarks, which can contain 0-256 characters.
        :type Description: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Description = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of tdsql-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _Accounts: Database account, including username and host address.
        :type Accounts: list of Account
        :param _GlobalPrivileges: Global permission. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "PROCESS", "DROP", "REFERENCES", "INDEX", "ALTER", "SHOW DATABASES", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "SHOW VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER".
Note: If the parameter is left empty, no change will be made to the granted global permissions. To clear the granted global permissions, set the parameter to an empty array.
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: Database permission. Value range: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "REFERENCES", "INDEX", "ALTER", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "SHOW VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER".	
Note: If the parameter is not passed in, no change will be made to the granted stored procedure permissions. To clear the granted database permissions, set `Privileges` to an empty array.
        :type DatabasePrivileges: list of DatabasePrivilege
        :param _TablePrivileges: Database table permission. Valid values of `Privileges`: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`.
Note: If the parameter is not passed in, no change will be made to the granted view permissions. To clear the granted table permissions, set `Privileges` to an empty array.
        :type TablePrivileges: list of TablePrivilege
        :param _ColumnPrivileges: Column permission in the table. Valid values: "SELECT", "INSERT", "UPDATE", "REFERENCES".
Note: If the parameter is not passed in, no change will be made to the granted column permissions. To clear the granted column permissions, set `Privileges` to an empty array.
        :type ColumnPrivileges: list of ColumnPrivilege
        :param _ViewPrivileges: Database view permission. Valid values of `Privileges`: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`.
Note: If the parameter is not passed in, no change will be made to the granted table permissions. To clear the granted view permissions, set `Privileges` to an empty array.
        :type ViewPrivileges: list of ViewPrivileges
        """
        self._InstanceId = None
        self._Accounts = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None
        self._ColumnPrivileges = None
        self._ViewPrivileges = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def GlobalPrivileges(self):
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges

    @property
    def ColumnPrivileges(self):
        return self._ColumnPrivileges

    @ColumnPrivileges.setter
    def ColumnPrivileges(self, ColumnPrivileges):
        self._ColumnPrivileges = ColumnPrivileges

    @property
    def ViewPrivileges(self):
        return self._ViewPrivileges

    @ViewPrivileges.setter
    def ViewPrivileges(self, ViewPrivileges):
        self._ViewPrivileges = ViewPrivileges


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self._ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self._ColumnPrivileges.append(obj)
        if params.get("ViewPrivileges") is not None:
            self._ViewPrivileges = []
            for item in params.get("ViewPrivileges"):
                obj = ViewPrivileges()
                obj._deserialize(item)
                self._ViewPrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID, which can be used in the [DescribeFlow](https://www.tencentcloud.com/document/product/237/16177) API to query the async task result.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBEncryptAttributesRequest(AbstractModel):
    """ModifyDBEncryptAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsqlshard-ow728lmc`
        :type InstanceId: str
        :param _EncryptEnabled: Whether to enable the data encryption (Once enabled, it can’t be disabled). Valid values: `1` (Yes), `0` (No. Default).
        :type EncryptEnabled: int
        """
        self._InstanceId = None
        self._EncryptEnabled = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EncryptEnabled(self):
        return self._EncryptEnabled

    @EncryptEnabled.setter
    def EncryptEnabled(self, EncryptEnabled):
        self._EncryptEnabled = EncryptEnabled


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EncryptEnabled = params.get("EncryptEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBEncryptAttributesResponse(AbstractModel):
    """ModifyDBEncryptAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of tdsql-hdaprz0v
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIds: list of str
        """
        self._Product = None
        self._InstanceId = None
        self._SecurityGroupIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of IDs of instances to be modified. Instance ID is in the format of dcdbt-ow728lmc.
        :type InstanceIds: list of str
        :param _ProjectId: ID of the project to be assigned, which can be obtained through the `DescribeProjects` API.
        :type ProjectId: int
        """
        self._InstanceIds = None
        self._ProjectId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _Params: Parameter list. Each element is a combination of `Param` and `Value`.
        :type Params: list of DBParamValue
        """
        self._InstanceId = None
        self._Params = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _Result: Parameter modification result
        :type Result: list of ParamModifyResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Result = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ParamModifyResult()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyDBSyncModeRequest(AbstractModel):
    """ModifyDBSyncMode request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance for which to modify the sync mode. The ID is in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _SyncMode: Sync mode. Valid values: `0` (async), `1` (strong sync), `2` (downgradable strong sync).
        :type SyncMode: int
        """
        self._InstanceId = None
        self._SyncMode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SyncMode(self):
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSyncModeResponse(AbstractModel):
    """ModifyDBSyncMode response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceNetworkRequest(AbstractModel):
    """ModifyInstanceNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VpcId: The ID of the desired VPC network
        :type VpcId: str
        :param _SubnetId: The subnet ID of the desired VPC network
        :type SubnetId: str
        :param _Vip: The field is required to specify VIP.
        :type Vip: str
        :param _Vipv6: The field is required to specify VIPv6.
        :type Vipv6: str
        :param _VipReleaseDelay: VIP retention period in hours. Value range: 0-168. Default value: `24`. `0` indicates that the VIP will be released immediately, but there will be 1-minute delay.
        :type VipReleaseDelay: int
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vipv6 = None
        self._VipReleaseDelay = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vipv6(self):
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def VipReleaseDelay(self):
        return self._VipReleaseDelay

    @VipReleaseDelay.setter
    def VipReleaseDelay(self, VipReleaseDelay):
        self._VipReleaseDelay = VipReleaseDelay


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vipv6 = params.get("Vipv6")
        self._VipReleaseDelay = params.get("VipReleaseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNetworkResponse(AbstractModel):
    """ModifyInstanceNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID, which can be used to query the task status through `DescribeFlow` API.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceVipRequest(AbstractModel):
    """ModifyInstanceVip request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Vip: Instance VIP
        :type Vip: str
        :param _Ipv6Flag: IPv6 flag
        :type Ipv6Flag: int
        :param _VipReleaseDelay: VIP retention period in hours. Value range: 0-168. Default value: `24`. `0` indicates that the VIP will be released immediately, but there will be 1-minute delay.
        :type VipReleaseDelay: int
        """
        self._InstanceId = None
        self._Vip = None
        self._Ipv6Flag = None
        self._VipReleaseDelay = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Ipv6Flag(self):
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def VipReleaseDelay(self):
        return self._VipReleaseDelay

    @VipReleaseDelay.setter
    def VipReleaseDelay(self, VipReleaseDelay):
        self._VipReleaseDelay = VipReleaseDelay


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Vip = params.get("Vip")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._VipReleaseDelay = params.get("VipReleaseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceVipResponse(AbstractModel):
    """ModifyInstanceVip response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceVportRequest(AbstractModel):
    """ModifyInstanceVport request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Vport: Instance Vport
        :type Vport: int
        """
        self._InstanceId = None
        self._Vport = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceVportResponse(AbstractModel):
    """ModifyInstanceVport response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NodeInfo(AbstractModel):
    """Node information description

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID
        :type NodeId: str
        :param _Role: Node role. Valid values: `master`, `slave`.
        :type Role: str
        """
        self._NodeId = None
        self._Role = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamConstraint(AbstractModel):
    """Parameter constraint

    """

    def __init__(self):
        r"""
        :param _Type: Constraint type, such as `enum` and `section`
        :type Type: str
        :param _Enum: List of valid values when constraint type is `enum`
        :type Enum: str
        :param _Range: Range when constraint type is `section`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Range: :class:`tencentcloud.dcdb.v20180411.models.ConstraintRange`
        :param _String: List of valid values when constraint type is `string`
        :type String: str
        """
        self._Type = None
        self._Enum = None
        self._Range = None
        self._String = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Enum(self):
        return self._Enum

    @Enum.setter
    def Enum(self, Enum):
        self._Enum = Enum

    @property
    def Range(self):
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def String(self):
        return self._String

    @String.setter
    def String(self, String):
        self._String = String


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Enum = params.get("Enum")
        if params.get("Range") is not None:
            self._Range = ConstraintRange()
            self._Range._deserialize(params.get("Range"))
        self._String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDesc(AbstractModel):
    """Database parameter description

    """

    def __init__(self):
        r"""
        :param _Param: Parameter name
        :type Param: str
        :param _Value: Current parameter value
        :type Value: str
        :param _SetValue: Previously set value, which is the same as `value` after the parameter takes effect. If no value has been set, this field will not be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SetValue: str
        :param _Default: Default value
        :type Default: str
        :param _Constraint: Parameter constraint
        :type Constraint: :class:`tencentcloud.dcdb.v20180411.models.ParamConstraint`
        :param _HaveSetValue: Whether a value has been set. false: no, true: yes.
        :type HaveSetValue: bool
        :param _NeedRestart: Whether restart is required. false: no;
true: yes.
        :type NeedRestart: bool
        """
        self._Param = None
        self._Value = None
        self._SetValue = None
        self._Default = None
        self._Constraint = None
        self._HaveSetValue = None
        self._NeedRestart = None

    @property
    def Param(self):
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SetValue(self):
        return self._SetValue

    @SetValue.setter
    def SetValue(self, SetValue):
        self._SetValue = SetValue

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Constraint(self):
        return self._Constraint

    @Constraint.setter
    def Constraint(self, Constraint):
        self._Constraint = Constraint

    @property
    def HaveSetValue(self):
        return self._HaveSetValue

    @HaveSetValue.setter
    def HaveSetValue(self, HaveSetValue):
        self._HaveSetValue = HaveSetValue

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        self._SetValue = params.get("SetValue")
        self._Default = params.get("Default")
        if params.get("Constraint") is not None:
            self._Constraint = ParamConstraint()
            self._Constraint._deserialize(params.get("Constraint"))
        self._HaveSetValue = params.get("HaveSetValue")
        self._NeedRestart = params.get("NeedRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamModifyResult(AbstractModel):
    """Parameter modification result

    """

    def __init__(self):
        r"""
        :param _Param: Renames parameter
        :type Param: str
        :param _Code: Result of parameter modification. 0: success; -1: failure; -2: invalid parameter value
        :type Code: int
        """
        self._Param = None
        self._Code = None

    @property
    def Param(self):
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedNetResource(AbstractModel):
    """Information of the reserved network resource

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC
        :type VpcId: str
        :param _SubnetId: Subnet
        :type SubnetId: str
        :param _Vip: Reserved private network IP under `VpcId` and `SubnetId`
        :type Vip: str
        :param _Vports: Port under `Vip`
        :type Vports: list of int
        :param _RecycleTime: Valid hours of VIP	
        :type RecycleTime: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vports = None
        self._RecycleTime = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vports(self):
        return self._Vports

    @Vports.setter
    def Vports(self, Vports):
        self._Vports = Vports

    @property
    def RecycleTime(self):
        return self._RecycleTime

    @RecycleTime.setter
    def RecycleTime(self, RecycleTime):
        self._RecycleTime = RecycleTime


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vports = params.get("Vports")
        self._RecycleTime = params.get("RecycleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param _UserName: Login username.
        :type UserName: str
        :param _Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param _Password: New password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """Tag object, including tag key and tag value

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        :param _Inbound: Inbound rule
        :type Inbound: list of SecurityGroupBound
        :param _Outbound: Outbound rule
        :type Outbound: list of SecurityGroupBound
        """
        self._ProjectId = None
        self._CreateTime = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Inbound = None
        self._Outbound = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Inbound(self):
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    """Security group inbound/outbound rule

    """

    def __init__(self):
        r"""
        :param _Action: Policy, which can be `ACCEPT` or `DROP`
        :type Action: str
        :param _CidrIp: Source IP or source IP range, such as 192.168.0.0/16
        :type CidrIp: str
        :param _PortRange: Port
        :type PortRange: str
        :param _IpProtocol: Network protocol. UDP and TCP are supported.
        :type IpProtocol: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardBriefInfo(AbstractModel):
    """TDSQL shard information

    """

    def __init__(self):
        r"""
        :param _ShardSerialId: Shard serial ID
        :type ShardSerialId: str
        :param _ShardInstanceId: Shard ID, such as shard-7vg1o339.
        :type ShardInstanceId: str
        :param _Status: Shard running status
        :type Status: int
        :param _StatusDesc: Description of shard running status
        :type StatusDesc: str
        :param _CreateTime: Shard creation time
        :type CreateTime: str
        :param _Memory: Shard memory size in GB
        :type Memory: int
        :param _Storage: Shard disk size in GB
        :type Storage: int
        :param _LogDisk: Log disk space size of a shard in GB
        :type LogDisk: int
        :param _NodeCount: Number of shard nodes
        :type NodeCount: int
        :param _StorageUsage: Disk space utilization of a shard
        :type StorageUsage: float
        :param _ProxyVersion: Version information of the shard proxy
        :type ProxyVersion: str
        :param _ShardMasterZone: Source AZ of a shard
        :type ShardMasterZone: str
        :param _ShardSlaveZones: Replica AZ of a shard
        :type ShardSlaveZones: list of str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _NodesInfo: Node information
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodesInfo: list of NodeInfo
        """
        self._ShardSerialId = None
        self._ShardInstanceId = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._Memory = None
        self._Storage = None
        self._LogDisk = None
        self._NodeCount = None
        self._StorageUsage = None
        self._ProxyVersion = None
        self._ShardMasterZone = None
        self._ShardSlaveZones = None
        self._Cpu = None
        self._NodesInfo = None

    @property
    def ShardSerialId(self):
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId

    @property
    def ShardInstanceId(self):
        return self._ShardInstanceId

    @ShardInstanceId.setter
    def ShardInstanceId(self, ShardInstanceId):
        self._ShardInstanceId = ShardInstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def LogDisk(self):
        return self._LogDisk

    @LogDisk.setter
    def LogDisk(self, LogDisk):
        self._LogDisk = LogDisk

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def StorageUsage(self):
        return self._StorageUsage

    @StorageUsage.setter
    def StorageUsage(self, StorageUsage):
        self._StorageUsage = StorageUsage

    @property
    def ProxyVersion(self):
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def ShardMasterZone(self):
        return self._ShardMasterZone

    @ShardMasterZone.setter
    def ShardMasterZone(self, ShardMasterZone):
        self._ShardMasterZone = ShardMasterZone

    @property
    def ShardSlaveZones(self):
        return self._ShardSlaveZones

    @ShardSlaveZones.setter
    def ShardSlaveZones(self, ShardSlaveZones):
        self._ShardSlaveZones = ShardSlaveZones

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def NodesInfo(self):
        return self._NodesInfo

    @NodesInfo.setter
    def NodesInfo(self, NodesInfo):
        self._NodesInfo = NodesInfo


    def _deserialize(self, params):
        self._ShardSerialId = params.get("ShardSerialId")
        self._ShardInstanceId = params.get("ShardInstanceId")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._LogDisk = params.get("LogDisk")
        self._NodeCount = params.get("NodeCount")
        self._StorageUsage = params.get("StorageUsage")
        self._ProxyVersion = params.get("ProxyVersion")
        self._ShardMasterZone = params.get("ShardMasterZone")
        self._ShardSlaveZones = params.get("ShardSlaveZones")
        self._Cpu = params.get("Cpu")
        if params.get("NodesInfo") is not None:
            self._NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodesInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardInfo(AbstractModel):
    """Shard information

    """

    def __init__(self):
        r"""
        :param _ShardInstanceId: Shard ID
        :type ShardInstanceId: str
        :param _ShardSerialId: Shard set ID
        :type ShardSerialId: str
        :param _Status: Status. 0: creating; 1: processing; 2: running; 3: shard not initialized; -2: shard deleted
        :type Status: int
        :param _Createtime: Creation time
        :type Createtime: str
        :param _Memory: Memory size in GB
        :type Memory: int
        :param _Storage: Storage capacity in GB
        :type Storage: int
        :param _ShardId: Numeric ID of a shard
        :type ShardId: int
        :param _NodeCount: Number of nodes. 2: one primary and one secondary; 3: one primary and two secondaries
        :type NodeCount: int
        :param _Pid: Product type ID (this field is obsolete and should not be depended on)
        :type Pid: int
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        """
        self._ShardInstanceId = None
        self._ShardSerialId = None
        self._Status = None
        self._Createtime = None
        self._Memory = None
        self._Storage = None
        self._ShardId = None
        self._NodeCount = None
        self._Pid = None
        self._Cpu = None

    @property
    def ShardInstanceId(self):
        return self._ShardInstanceId

    @ShardInstanceId.setter
    def ShardInstanceId(self, ShardInstanceId):
        self._ShardInstanceId = ShardInstanceId

    @property
    def ShardSerialId(self):
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Createtime(self):
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._ShardInstanceId = params.get("ShardInstanceId")
        self._ShardSerialId = params.get("ShardSerialId")
        self._Status = params.get("Status")
        self._Createtime = params.get("Createtime")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._ShardId = params.get("ShardId")
        self._NodeCount = params.get("NodeCount")
        self._Pid = params.get("Pid")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogData(AbstractModel):
    """Information of a slow query that has been logged

    """

    def __init__(self):
        r"""
        :param _CheckSum: Statement checksum for querying details
        :type CheckSum: str
        :param _Db: Database name
        :type Db: str
        :param _FingerPrint: Abstracted SQL statement
        :type FingerPrint: str
        :param _LockTimeAvg: Average lock duration
        :type LockTimeAvg: str
        :param _LockTimeMax: Maximum lock duration
        :type LockTimeMax: str
        :param _LockTimeMin: Minimum lock duration
        :type LockTimeMin: str
        :param _LockTimeSum: Sum of lock durations
        :type LockTimeSum: str
        :param _QueryCount: Number of queries
        :type QueryCount: str
        :param _QueryTimeAvg: Average query duration
        :type QueryTimeAvg: str
        :param _QueryTimeMax: Maximum query duration
        :type QueryTimeMax: str
        :param _QueryTimeMin: Minimum query duration
        :type QueryTimeMin: str
        :param _QueryTimeSum: Sum of query durations
        :type QueryTimeSum: str
        :param _RowsExaminedSum: Number of scanned rows
        :type RowsExaminedSum: str
        :param _RowsSentSum: Number of sent rows
        :type RowsSentSum: str
        :param _TsMax: Last execution time
        :type TsMax: str
        :param _TsMin: First execution time
        :type TsMin: str
        :param _User: Account
        :type User: str
        :param _ExampleSql: Sample SQL
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExampleSql: str
        :param _Host: Host address of account
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        """
        self._CheckSum = None
        self._Db = None
        self._FingerPrint = None
        self._LockTimeAvg = None
        self._LockTimeMax = None
        self._LockTimeMin = None
        self._LockTimeSum = None
        self._QueryCount = None
        self._QueryTimeAvg = None
        self._QueryTimeMax = None
        self._QueryTimeMin = None
        self._QueryTimeSum = None
        self._RowsExaminedSum = None
        self._RowsSentSum = None
        self._TsMax = None
        self._TsMin = None
        self._User = None
        self._ExampleSql = None
        self._Host = None

    @property
    def CheckSum(self):
        return self._CheckSum

    @CheckSum.setter
    def CheckSum(self, CheckSum):
        self._CheckSum = CheckSum

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def FingerPrint(self):
        return self._FingerPrint

    @FingerPrint.setter
    def FingerPrint(self, FingerPrint):
        self._FingerPrint = FingerPrint

    @property
    def LockTimeAvg(self):
        return self._LockTimeAvg

    @LockTimeAvg.setter
    def LockTimeAvg(self, LockTimeAvg):
        self._LockTimeAvg = LockTimeAvg

    @property
    def LockTimeMax(self):
        return self._LockTimeMax

    @LockTimeMax.setter
    def LockTimeMax(self, LockTimeMax):
        self._LockTimeMax = LockTimeMax

    @property
    def LockTimeMin(self):
        return self._LockTimeMin

    @LockTimeMin.setter
    def LockTimeMin(self, LockTimeMin):
        self._LockTimeMin = LockTimeMin

    @property
    def LockTimeSum(self):
        return self._LockTimeSum

    @LockTimeSum.setter
    def LockTimeSum(self, LockTimeSum):
        self._LockTimeSum = LockTimeSum

    @property
    def QueryCount(self):
        return self._QueryCount

    @QueryCount.setter
    def QueryCount(self, QueryCount):
        self._QueryCount = QueryCount

    @property
    def QueryTimeAvg(self):
        return self._QueryTimeAvg

    @QueryTimeAvg.setter
    def QueryTimeAvg(self, QueryTimeAvg):
        self._QueryTimeAvg = QueryTimeAvg

    @property
    def QueryTimeMax(self):
        return self._QueryTimeMax

    @QueryTimeMax.setter
    def QueryTimeMax(self, QueryTimeMax):
        self._QueryTimeMax = QueryTimeMax

    @property
    def QueryTimeMin(self):
        return self._QueryTimeMin

    @QueryTimeMin.setter
    def QueryTimeMin(self, QueryTimeMin):
        self._QueryTimeMin = QueryTimeMin

    @property
    def QueryTimeSum(self):
        return self._QueryTimeSum

    @QueryTimeSum.setter
    def QueryTimeSum(self, QueryTimeSum):
        self._QueryTimeSum = QueryTimeSum

    @property
    def RowsExaminedSum(self):
        return self._RowsExaminedSum

    @RowsExaminedSum.setter
    def RowsExaminedSum(self, RowsExaminedSum):
        self._RowsExaminedSum = RowsExaminedSum

    @property
    def RowsSentSum(self):
        return self._RowsSentSum

    @RowsSentSum.setter
    def RowsSentSum(self, RowsSentSum):
        self._RowsSentSum = RowsSentSum

    @property
    def TsMax(self):
        return self._TsMax

    @TsMax.setter
    def TsMax(self, TsMax):
        self._TsMax = TsMax

    @property
    def TsMin(self):
        return self._TsMin

    @TsMin.setter
    def TsMin(self, TsMin):
        self._TsMin = TsMin

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ExampleSql(self):
        return self._ExampleSql

    @ExampleSql.setter
    def ExampleSql(self, ExampleSql):
        self._ExampleSql = ExampleSql

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._CheckSum = params.get("CheckSum")
        self._Db = params.get("Db")
        self._FingerPrint = params.get("FingerPrint")
        self._LockTimeAvg = params.get("LockTimeAvg")
        self._LockTimeMax = params.get("LockTimeMax")
        self._LockTimeMin = params.get("LockTimeMin")
        self._LockTimeSum = params.get("LockTimeSum")
        self._QueryCount = params.get("QueryCount")
        self._QueryTimeAvg = params.get("QueryTimeAvg")
        self._QueryTimeMax = params.get("QueryTimeMax")
        self._QueryTimeMin = params.get("QueryTimeMin")
        self._QueryTimeSum = params.get("QueryTimeSum")
        self._RowsExaminedSum = params.get("RowsExaminedSum")
        self._RowsSentSum = params.get("RowsSentSum")
        self._TsMax = params.get("TsMax")
        self._TsMin = params.get("TsMin")
        self._User = params.get("User")
        self._ExampleSql = params.get("ExampleSql")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitShardConfig(AbstractModel):
    """Instance upgrade -- Sharding

    """

    def __init__(self):
        r"""
        :param _ShardInstanceIds: Shard IDs in array
        :type ShardInstanceIds: list of str
        :param _SplitRate: Data split ratio at 50% (fixed)
        :type SplitRate: int
        :param _ShardMemory: Shard memory capacity in GB
        :type ShardMemory: int
        :param _ShardStorage: Shard storage capacity in GB
        :type ShardStorage: int
        """
        self._ShardInstanceIds = None
        self._SplitRate = None
        self._ShardMemory = None
        self._ShardStorage = None

    @property
    def ShardInstanceIds(self):
        return self._ShardInstanceIds

    @ShardInstanceIds.setter
    def ShardInstanceIds(self, ShardInstanceIds):
        self._ShardInstanceIds = ShardInstanceIds

    @property
    def SplitRate(self):
        return self._SplitRate

    @SplitRate.setter
    def SplitRate(self, SplitRate):
        self._SplitRate = SplitRate

    @property
    def ShardMemory(self):
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage


    def _deserialize(self, params):
        self._ShardInstanceIds = params.get("ShardInstanceIds")
        self._SplitRate = params.get("SplitRate")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceHARequest(AbstractModel):
    """SwitchDBInstanceHA request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of tdsql-ow728lmc
        :type InstanceId: str
        :param _Zone: Target AZ. The node with the lowest delay in the target AZ will be automatically promoted to source node.
        :type Zone: str
        """
        self._InstanceId = None
        self._Zone = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceHAResponse(AbstractModel):
    """SwitchDBInstanceHA response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TableColumn(AbstractModel):
    """Database column information

    """

    def __init__(self):
        r"""
        :param _Col: Column name
        :type Col: str
        :param _Type: Column type
        :type Type: str
        """
        self._Col = None
        self._Type = None

    @property
    def Col(self):
        return self._Col

    @Col.setter
    def Col(self, Col):
        self._Col = Col

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Col = params.get("Col")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivilege(AbstractModel):
    """Table permission

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Privileges = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDedicatedDBInstanceRequest(AbstractModel):
    """TerminateDedicatedDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `dcdbt-ow728lmc`
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDedicatedDBInstanceResponse(AbstractModel):
    """TerminateDedicatedDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeHourDCDBInstanceRequest(AbstractModel):
    """UpgradeHourDCDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID to be upgraded in the format of dcdbt-ow728lmc, which can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceId: str
        :param _UpgradeType: Upgrade type. Valid values: 
<li> `ADD`: Add a new shard </li> 
 <li> `EXPAND`: Upgrade the existing shads</li> 
 <li> `SPLIT`: Split data of the existing shads to the new ones</li>
        :type UpgradeType: str
        :param _AddShardConfig: Add shards when `UpgradeType` is `ADD`.
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param _ExpandShardConfig: Expand shard when `UpgradeType` is `EXPAND`.
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param _SplitShardConfig: Split shard when `UpgradeType` is `SPLIT`.
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param _SwitchStartTime: Switch start time in the format of "2019-12-12 07:00:00", which is no less than one hour and within 3 days from the current time.
        :type SwitchStartTime: str
        :param _SwitchEndTime: Switch end time in the format of "2019-12-12 07:15:00", which must be later than the start time.
        :type SwitchEndTime: str
        :param _SwitchAutoRetry: Whether to retry automatically. Valid values: `0` (no), `1` (yes).
        :type SwitchAutoRetry: int
        :param _Zones: The list of new AZs specified in deployment modification. The first one is the source AZ, and the rest are replica AZs.
        :type Zones: list of str
        """
        self._InstanceId = None
        self._UpgradeType = None
        self._AddShardConfig = None
        self._ExpandShardConfig = None
        self._SplitShardConfig = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None
        self._SwitchAutoRetry = None
        self._Zones = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def AddShardConfig(self):
        return self._AddShardConfig

    @AddShardConfig.setter
    def AddShardConfig(self, AddShardConfig):
        self._AddShardConfig = AddShardConfig

    @property
    def ExpandShardConfig(self):
        return self._ExpandShardConfig

    @ExpandShardConfig.setter
    def ExpandShardConfig(self, ExpandShardConfig):
        self._ExpandShardConfig = ExpandShardConfig

    @property
    def SplitShardConfig(self):
        return self._SplitShardConfig

    @SplitShardConfig.setter
    def SplitShardConfig(self, SplitShardConfig):
        self._SplitShardConfig = SplitShardConfig

    @property
    def SwitchStartTime(self):
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime

    @property
    def SwitchAutoRetry(self):
        return self._SwitchAutoRetry

    @SwitchAutoRetry.setter
    def SwitchAutoRetry(self, SwitchAutoRetry):
        self._SwitchAutoRetry = SwitchAutoRetry

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self._AddShardConfig = AddShardConfig()
            self._AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self._ExpandShardConfig = ExpandShardConfig()
            self._ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self._SplitShardConfig = SplitShardConfig()
            self._SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        self._SwitchAutoRetry = params.get("SwitchAutoRetry")
        self._Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeHourDCDBInstanceResponse(AbstractModel):
    """UpgradeHourDCDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ViewPrivileges(AbstractModel):
    """View permission information

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _View: View name
        :type View: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._View = None
        self._Privileges = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def View(self):
        return self._View

    @View.setter
    def View(self, View):
        self._View = View

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._View = params.get("View")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        