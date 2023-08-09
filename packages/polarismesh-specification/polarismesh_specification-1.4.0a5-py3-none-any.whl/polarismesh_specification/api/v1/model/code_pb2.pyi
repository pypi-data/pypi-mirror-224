from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    Unknown: _ClassVar[Code]
    ExecuteSuccess: _ClassVar[Code]
    DataNoChange: _ClassVar[Code]
    NoNeedUpdate: _ClassVar[Code]
    BadRequest: _ClassVar[Code]
    ParseException: _ClassVar[Code]
    EmptyRequest: _ClassVar[Code]
    BatchSizeOverLimit: _ClassVar[Code]
    InvalidDiscoverResource: _ClassVar[Code]
    InvalidRequestID: _ClassVar[Code]
    InvalidUserName: _ClassVar[Code]
    InvalidUserToken: _ClassVar[Code]
    InvalidParameter: _ClassVar[Code]
    EmptyQueryParameter: _ClassVar[Code]
    InvalidQueryInsParameter: _ClassVar[Code]
    InvalidNamespaceName: _ClassVar[Code]
    InvalidNamespaceOwners: _ClassVar[Code]
    InvalidNamespaceToken: _ClassVar[Code]
    InvalidServiceName: _ClassVar[Code]
    InvalidServiceOwners: _ClassVar[Code]
    InvalidServiceToken: _ClassVar[Code]
    InvalidServiceMetadata: _ClassVar[Code]
    InvalidServicePorts: _ClassVar[Code]
    InvalidServiceBusiness: _ClassVar[Code]
    InvalidServiceDepartment: _ClassVar[Code]
    InvalidServiceCMDB: _ClassVar[Code]
    InvalidServiceComment: _ClassVar[Code]
    InvalidServiceAliasComment: _ClassVar[Code]
    InvalidInstanceID: _ClassVar[Code]
    InvalidInstanceHost: _ClassVar[Code]
    InvalidInstancePort: _ClassVar[Code]
    InvalidServiceAlias: _ClassVar[Code]
    InvalidNamespaceWithAlias: _ClassVar[Code]
    InvalidServiceAliasOwners: _ClassVar[Code]
    InvalidInstanceProtocol: _ClassVar[Code]
    InvalidInstanceVersion: _ClassVar[Code]
    InvalidInstanceLogicSet: _ClassVar[Code]
    InvalidInstanceIsolate: _ClassVar[Code]
    HealthCheckNotOpen: _ClassVar[Code]
    HeartbeatOnDisabledIns: _ClassVar[Code]
    HeartbeatExceedLimit: _ClassVar[Code]
    HeartbeatTypeNotFound: _ClassVar[Code]
    InvalidMetadata: _ClassVar[Code]
    InvalidRateLimitID: _ClassVar[Code]
    InvalidRateLimitLabels: _ClassVar[Code]
    InvalidRateLimitAmounts: _ClassVar[Code]
    InvalidRateLimitName: _ClassVar[Code]
    InvalidCircuitBreakerID: _ClassVar[Code]
    InvalidCircuitBreakerVersion: _ClassVar[Code]
    InvalidCircuitBreakerName: _ClassVar[Code]
    InvalidCircuitBreakerNamespace: _ClassVar[Code]
    InvalidCircuitBreakerOwners: _ClassVar[Code]
    InvalidCircuitBreakerToken: _ClassVar[Code]
    InvalidCircuitBreakerBusiness: _ClassVar[Code]
    InvalidCircuitBreakerDepartment: _ClassVar[Code]
    InvalidCircuitBreakerComment: _ClassVar[Code]
    CircuitBreakerRuleExisted: _ClassVar[Code]
    InvalidRoutingID: _ClassVar[Code]
    InvalidRoutingPolicy: _ClassVar[Code]
    InvalidRoutingName: _ClassVar[Code]
    InvalidRoutingPriority: _ClassVar[Code]
    InvalidFaultDetectID: _ClassVar[Code]
    InvalidFaultDetectName: _ClassVar[Code]
    InvalidFaultDetectNamespace: _ClassVar[Code]
    FaultDetectRuleExisted: _ClassVar[Code]
    ServicesExistedMesh: _ClassVar[Code]
    ResourcesExistedMesh: _ClassVar[Code]
    InvalidMeshParameter: _ClassVar[Code]
    InvalidPlatformID: _ClassVar[Code]
    InvalidPlatformName: _ClassVar[Code]
    InvalidPlatformDomain: _ClassVar[Code]
    InvalidPlatformQPS: _ClassVar[Code]
    InvalidPlatformToken: _ClassVar[Code]
    InvalidPlatformOwner: _ClassVar[Code]
    InvalidPlatformDepartment: _ClassVar[Code]
    InvalidPlatformComment: _ClassVar[Code]
    NotFoundPlatform: _ClassVar[Code]
    InvalidFluxRateLimitId: _ClassVar[Code]
    InvalidFluxRateLimitQps: _ClassVar[Code]
    InvalidFluxRateLimitSetKey: _ClassVar[Code]
    ExistedResource: _ClassVar[Code]
    NotFoundResource: _ClassVar[Code]
    NamespaceExistedServices: _ClassVar[Code]
    ServiceExistedInstances: _ClassVar[Code]
    ServiceExistedRoutings: _ClassVar[Code]
    ServiceExistedRateLimits: _ClassVar[Code]
    ExistReleasedConfig: _ClassVar[Code]
    SameInstanceRequest: _ClassVar[Code]
    ServiceExistedCircuitBreakers: _ClassVar[Code]
    ServiceExistedAlias: _ClassVar[Code]
    NamespaceExistedMeshResources: _ClassVar[Code]
    NamespaceExistedCircuitBreakers: _ClassVar[Code]
    ServiceSubscribedByMeshes: _ClassVar[Code]
    ServiceExistedFluxRateLimits: _ClassVar[Code]
    NamespaceExistedConfigGroups: _ClassVar[Code]
    NotFoundService: _ClassVar[Code]
    NotFoundRouting: _ClassVar[Code]
    NotFoundInstance: _ClassVar[Code]
    NotFoundServiceAlias: _ClassVar[Code]
    NotFoundNamespace: _ClassVar[Code]
    NotFoundSourceService: _ClassVar[Code]
    NotFoundRateLimit: _ClassVar[Code]
    NotFoundCircuitBreaker: _ClassVar[Code]
    NotFoundMasterConfig: _ClassVar[Code]
    NotFoundTagConfig: _ClassVar[Code]
    NotFoundTagConfigOrService: _ClassVar[Code]
    ClientAPINotOpen: _ClassVar[Code]
    NotAllowBusinessService: _ClassVar[Code]
    NotAllowAliasUpdate: _ClassVar[Code]
    NotAllowAliasCreateInstance: _ClassVar[Code]
    NotAllowAliasCreateRouting: _ClassVar[Code]
    NotAllowCreateAliasForAlias: _ClassVar[Code]
    NotAllowAliasCreateRateLimit: _ClassVar[Code]
    NotAllowAliasBindRule: _ClassVar[Code]
    NotAllowDifferentNamespaceBindRule: _ClassVar[Code]
    Unauthorized: _ClassVar[Code]
    NotAllowedAccess: _ClassVar[Code]
    CMDBNotFindHost: _ClassVar[Code]
    DataConflict: _ClassVar[Code]
    InstanceTooManyRequests: _ClassVar[Code]
    IPRateLimit: _ClassVar[Code]
    APIRateLimit: _ClassVar[Code]
    ExecuteException: _ClassVar[Code]
    StoreLayerException: _ClassVar[Code]
    CMDBPluginException: _ClassVar[Code]
    ParseRoutingException: _ClassVar[Code]
    ParseRateLimitException: _ClassVar[Code]
    ParseCircuitBreakerException: _ClassVar[Code]
    HeartbeatException: _ClassVar[Code]
    InstanceRegisTimeout: _ClassVar[Code]
    InvalidConfigFileGroupName: _ClassVar[Code]
    InvalidConfigFileName: _ClassVar[Code]
    InvalidConfigFileContentLength: _ClassVar[Code]
    InvalidConfigFileFormat: _ClassVar[Code]
    InvalidConfigFileTags: _ClassVar[Code]
    InvalidWatchConfigFileFormat: _ClassVar[Code]
    NotFoundResourceConfigFile: _ClassVar[Code]
    InvalidConfigFileTemplateName: _ClassVar[Code]
    EncryptConfigFileException: _ClassVar[Code]
    DecryptConfigFileException: _ClassVar[Code]
    InvalidUserOwners: _ClassVar[Code]
    InvalidUserID: _ClassVar[Code]
    InvalidUserPassword: _ClassVar[Code]
    InvalidUserMobile: _ClassVar[Code]
    InvalidUserEmail: _ClassVar[Code]
    InvalidUserGroupOwners: _ClassVar[Code]
    InvalidUserGroupID: _ClassVar[Code]
    InvalidAuthStrategyOwners: _ClassVar[Code]
    InvalidAuthStrategyName: _ClassVar[Code]
    InvalidAuthStrategyID: _ClassVar[Code]
    InvalidPrincipalType: _ClassVar[Code]
    UserExisted: _ClassVar[Code]
    UserGroupExisted: _ClassVar[Code]
    AuthStrategyRuleExisted: _ClassVar[Code]
    SubAccountExisted: _ClassVar[Code]
    NotFoundUser: _ClassVar[Code]
    NotFoundOwnerUser: _ClassVar[Code]
    NotFoundUserGroup: _ClassVar[Code]
    NotFoundAuthStrategyRule: _ClassVar[Code]
    NotAllowModifyDefaultStrategyPrincipal: _ClassVar[Code]
    NotAllowModifyOwnerDefaultStrategy: _ClassVar[Code]
    EmptyAutToken: _ClassVar[Code]
    TokenDisabled: _ClassVar[Code]
    TokenNotExisted: _ClassVar[Code]
    AuthTokenForbidden: _ClassVar[Code]
    OperationRoleForbidden: _ClassVar[Code]
Unknown: Code
ExecuteSuccess: Code
DataNoChange: Code
NoNeedUpdate: Code
BadRequest: Code
ParseException: Code
EmptyRequest: Code
BatchSizeOverLimit: Code
InvalidDiscoverResource: Code
InvalidRequestID: Code
InvalidUserName: Code
InvalidUserToken: Code
InvalidParameter: Code
EmptyQueryParameter: Code
InvalidQueryInsParameter: Code
InvalidNamespaceName: Code
InvalidNamespaceOwners: Code
InvalidNamespaceToken: Code
InvalidServiceName: Code
InvalidServiceOwners: Code
InvalidServiceToken: Code
InvalidServiceMetadata: Code
InvalidServicePorts: Code
InvalidServiceBusiness: Code
InvalidServiceDepartment: Code
InvalidServiceCMDB: Code
InvalidServiceComment: Code
InvalidServiceAliasComment: Code
InvalidInstanceID: Code
InvalidInstanceHost: Code
InvalidInstancePort: Code
InvalidServiceAlias: Code
InvalidNamespaceWithAlias: Code
InvalidServiceAliasOwners: Code
InvalidInstanceProtocol: Code
InvalidInstanceVersion: Code
InvalidInstanceLogicSet: Code
InvalidInstanceIsolate: Code
HealthCheckNotOpen: Code
HeartbeatOnDisabledIns: Code
HeartbeatExceedLimit: Code
HeartbeatTypeNotFound: Code
InvalidMetadata: Code
InvalidRateLimitID: Code
InvalidRateLimitLabels: Code
InvalidRateLimitAmounts: Code
InvalidRateLimitName: Code
InvalidCircuitBreakerID: Code
InvalidCircuitBreakerVersion: Code
InvalidCircuitBreakerName: Code
InvalidCircuitBreakerNamespace: Code
InvalidCircuitBreakerOwners: Code
InvalidCircuitBreakerToken: Code
InvalidCircuitBreakerBusiness: Code
InvalidCircuitBreakerDepartment: Code
InvalidCircuitBreakerComment: Code
CircuitBreakerRuleExisted: Code
InvalidRoutingID: Code
InvalidRoutingPolicy: Code
InvalidRoutingName: Code
InvalidRoutingPriority: Code
InvalidFaultDetectID: Code
InvalidFaultDetectName: Code
InvalidFaultDetectNamespace: Code
FaultDetectRuleExisted: Code
ServicesExistedMesh: Code
ResourcesExistedMesh: Code
InvalidMeshParameter: Code
InvalidPlatformID: Code
InvalidPlatformName: Code
InvalidPlatformDomain: Code
InvalidPlatformQPS: Code
InvalidPlatformToken: Code
InvalidPlatformOwner: Code
InvalidPlatformDepartment: Code
InvalidPlatformComment: Code
NotFoundPlatform: Code
InvalidFluxRateLimitId: Code
InvalidFluxRateLimitQps: Code
InvalidFluxRateLimitSetKey: Code
ExistedResource: Code
NotFoundResource: Code
NamespaceExistedServices: Code
ServiceExistedInstances: Code
ServiceExistedRoutings: Code
ServiceExistedRateLimits: Code
ExistReleasedConfig: Code
SameInstanceRequest: Code
ServiceExistedCircuitBreakers: Code
ServiceExistedAlias: Code
NamespaceExistedMeshResources: Code
NamespaceExistedCircuitBreakers: Code
ServiceSubscribedByMeshes: Code
ServiceExistedFluxRateLimits: Code
NamespaceExistedConfigGroups: Code
NotFoundService: Code
NotFoundRouting: Code
NotFoundInstance: Code
NotFoundServiceAlias: Code
NotFoundNamespace: Code
NotFoundSourceService: Code
NotFoundRateLimit: Code
NotFoundCircuitBreaker: Code
NotFoundMasterConfig: Code
NotFoundTagConfig: Code
NotFoundTagConfigOrService: Code
ClientAPINotOpen: Code
NotAllowBusinessService: Code
NotAllowAliasUpdate: Code
NotAllowAliasCreateInstance: Code
NotAllowAliasCreateRouting: Code
NotAllowCreateAliasForAlias: Code
NotAllowAliasCreateRateLimit: Code
NotAllowAliasBindRule: Code
NotAllowDifferentNamespaceBindRule: Code
Unauthorized: Code
NotAllowedAccess: Code
CMDBNotFindHost: Code
DataConflict: Code
InstanceTooManyRequests: Code
IPRateLimit: Code
APIRateLimit: Code
ExecuteException: Code
StoreLayerException: Code
CMDBPluginException: Code
ParseRoutingException: Code
ParseRateLimitException: Code
ParseCircuitBreakerException: Code
HeartbeatException: Code
InstanceRegisTimeout: Code
InvalidConfigFileGroupName: Code
InvalidConfigFileName: Code
InvalidConfigFileContentLength: Code
InvalidConfigFileFormat: Code
InvalidConfigFileTags: Code
InvalidWatchConfigFileFormat: Code
NotFoundResourceConfigFile: Code
InvalidConfigFileTemplateName: Code
EncryptConfigFileException: Code
DecryptConfigFileException: Code
InvalidUserOwners: Code
InvalidUserID: Code
InvalidUserPassword: Code
InvalidUserMobile: Code
InvalidUserEmail: Code
InvalidUserGroupOwners: Code
InvalidUserGroupID: Code
InvalidAuthStrategyOwners: Code
InvalidAuthStrategyName: Code
InvalidAuthStrategyID: Code
InvalidPrincipalType: Code
UserExisted: Code
UserGroupExisted: Code
AuthStrategyRuleExisted: Code
SubAccountExisted: Code
NotFoundUser: Code
NotFoundOwnerUser: Code
NotFoundUserGroup: Code
NotFoundAuthStrategyRule: Code
NotAllowModifyDefaultStrategyPrincipal: Code
NotAllowModifyOwnerDefaultStrategy: Code
EmptyAutToken: Code
TokenDisabled: Code
TokenNotExisted: Code
AuthTokenForbidden: Code
OperationRoleForbidden: Code
