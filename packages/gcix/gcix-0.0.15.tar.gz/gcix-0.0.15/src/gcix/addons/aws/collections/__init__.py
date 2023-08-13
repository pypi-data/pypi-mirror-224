import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ...._jsii import *

from .... import JobCollection as _JobCollection_0289800c
from ..jobs import Deploy as _Deploy_9c01aae8, Diff as _Diff_64469896


@jsii.data_type(
    jsii_type="@gcix/gcix.addons.aws.collections.DiffDeployProps",
    jsii_struct_bases=[],
    name_mapping={"stacks": "stacks", "context": "context"},
)
class DiffDeployProps:
    def __init__(
        self,
        *,
        stacks: typing.Sequence[builtins.str],
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Configuration properties for initializing a DiffDeploy instance.

        :param stacks: An array of stack names for which to generate a diff and perform deployment.
        :param context: Optional context values to provide additional information for the diff and deployment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__933de1505fc5f3f59ab6b73f924a990e955aeac2aee53b426a16b07ac4c7888f)
            check_type(argname="argument stacks", value=stacks, expected_type=type_hints["stacks"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stacks": stacks,
        }
        if context is not None:
            self._values["context"] = context

    @builtins.property
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names for which to generate a diff and perform deployment.'''
        result = self._values.get("stacks")
        assert result is not None, "Required property 'stacks' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for the diff and deployment.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiffDeployProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@gcix/gcix.addons.aws.collections.IDiffDeploy")
class IDiffDeploy(typing_extensions.Protocol):
    '''Represents the interface that a DiffDeploy instance adheres to.'''

    @builtins.property
    @jsii.member(jsii_name="deployJob")
    def deploy_job(self) -> _Deploy_9c01aae8:
        '''The instance of the Deploy job associated with this DiffDeploy instance.'''
        ...

    @deploy_job.setter
    def deploy_job(self, value: _Deploy_9c01aae8) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="diffJob")
    def diff_job(self) -> _Diff_64469896:
        '''The instance of the Diff job associated with this DiffDeploy instance.'''
        ...

    @diff_job.setter
    def diff_job(self, value: _Diff_64469896) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names for which to generate a diff and perform deployment.'''
        ...

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for the diff and deployment.'''
        ...

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        ...


class _IDiffDeployProxy:
    '''Represents the interface that a DiffDeploy instance adheres to.'''

    __jsii_type__: typing.ClassVar[str] = "@gcix/gcix.addons.aws.collections.IDiffDeploy"

    @builtins.property
    @jsii.member(jsii_name="deployJob")
    def deploy_job(self) -> _Deploy_9c01aae8:
        '''The instance of the Deploy job associated with this DiffDeploy instance.'''
        return typing.cast(_Deploy_9c01aae8, jsii.get(self, "deployJob"))

    @deploy_job.setter
    def deploy_job(self, value: _Deploy_9c01aae8) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ff6536f68ecd61665f11178eb69577b8acd1bdbf49f298c38622b21fb518c44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployJob", value)

    @builtins.property
    @jsii.member(jsii_name="diffJob")
    def diff_job(self) -> _Diff_64469896:
        '''The instance of the Diff job associated with this DiffDeploy instance.'''
        return typing.cast(_Diff_64469896, jsii.get(self, "diffJob"))

    @diff_job.setter
    def diff_job(self, value: _Diff_64469896) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fd9399660aff0e236bf4c7b858ffc1370885c7004c2233eafd18061d6ade1ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diffJob", value)

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names for which to generate a diff and perform deployment.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stacks"))

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ebed8e614754cba3161b9480b8dc436541c7b9ce137b5471fea66726d0ec006)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stacks", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for the diff and deployment.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "context"))

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__343211913065ed4fd702e76fcee79130a879d6248962be05ca8639db1ff1a51c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiffDeploy).__jsii_proxy_class__ = lambda : _IDiffDeployProxy


@jsii.implements(IDiffDeploy)
class DiffDeploy(
    _JobCollection_0289800c,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gcix/gcix.addons.aws.collections.DiffDeploy",
):
    '''A class that manages the configuration and execution of combined Diff and Deploy operations.

    Inherits from the base JobCollection class and implements the IDiffDeploy interface.
    '''

    def __init__(
        self,
        *,
        stacks: typing.Sequence[builtins.str],
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Creates an instance of DiffDeploy.

        :param stacks: An array of stack names for which to generate a diff and perform deployment.
        :param context: Optional context values to provide additional information for the diff and deployment.
        '''
        props = DiffDeployProps(stacks=stacks, context=context)

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="deployJob")
    def deploy_job(self) -> _Deploy_9c01aae8:
        '''The instance of the Deploy job associated with this DiffDeploy instance.'''
        return typing.cast(_Deploy_9c01aae8, jsii.get(self, "deployJob"))

    @deploy_job.setter
    def deploy_job(self, value: _Deploy_9c01aae8) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1953690017b04d81cd8ca9dfe0d049a55b48889ab03968526da7714cf670423c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployJob", value)

    @builtins.property
    @jsii.member(jsii_name="diffJob")
    def diff_job(self) -> _Diff_64469896:
        '''The instance of the Diff job associated with this DiffDeploy instance.'''
        return typing.cast(_Diff_64469896, jsii.get(self, "diffJob"))

    @diff_job.setter
    def diff_job(self, value: _Diff_64469896) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bf41ce3668b1f4a37fe6b9326c647054719c8a2bdc8ca5191474b7cfbcadcff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diffJob", value)

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names for which to generate a diff and perform deployment.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stacks"))

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47af98d839304125442aff4874a894a5800662969566bad202898d3f335e89f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stacks", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for the diff and deployment.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "context"))

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2dbf520ffc1ff31d894f358873474b2c02b3380127f1ad17c586fcaec90d394)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)


__all__ = [
    "DiffDeploy",
    "DiffDeployProps",
    "IDiffDeploy",
]

publication.publish()

def _typecheckingstub__933de1505fc5f3f59ab6b73f924a990e955aeac2aee53b426a16b07ac4c7888f(
    *,
    stacks: typing.Sequence[builtins.str],
    context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff6536f68ecd61665f11178eb69577b8acd1bdbf49f298c38622b21fb518c44(
    value: _Deploy_9c01aae8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fd9399660aff0e236bf4c7b858ffc1370885c7004c2233eafd18061d6ade1ef(
    value: _Diff_64469896,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ebed8e614754cba3161b9480b8dc436541c7b9ce137b5471fea66726d0ec006(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__343211913065ed4fd702e76fcee79130a879d6248962be05ca8639db1ff1a51c(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1953690017b04d81cd8ca9dfe0d049a55b48889ab03968526da7714cf670423c(
    value: _Deploy_9c01aae8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bf41ce3668b1f4a37fe6b9326c647054719c8a2bdc8ca5191474b7cfbcadcff(
    value: _Diff_64469896,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47af98d839304125442aff4874a894a5800662969566bad202898d3f335e89f4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2dbf520ffc1ff31d894f358873474b2c02b3380127f1ad17c586fcaec90d394(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass
