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

from .... import Job as _Job_20682b42


@jsii.data_type(
    jsii_type="@gcix/gcix.addons.aws.jobs.BootstrapProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "aws_region": "awsRegion",
        "qualifier": "qualifier",
        "toolkit_stack_name": "toolkitStackName",
        "job_name": "jobName",
        "job_stage": "jobStage",
        "resource_tags": "resourceTags",
    },
)
class BootstrapProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        aws_region: builtins.str,
        qualifier: builtins.str,
        toolkit_stack_name: builtins.str,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Configuration properties for initializing a Bootstrap instance.

        :param aws_account_id: The AWS account ID associated with the Bootstrap configuration.
        :param aws_region: The AWS region in which the Bootstrap will be performed.
        :param qualifier: The qualifier applied to the Bootstrap.
        :param toolkit_stack_name: The name of the toolkit stack used for Bootstrap.
        :param job_name: An optional name for the Bootstrap job.
        :param job_stage: An optional stage for the Bootstrap job.
        :param resource_tags: Optional resource tags that can be applied during Bootstrap.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d2a44fb3ca869efa10ffa9683897288131eee5b226ab78734a337e90f5ba6b0)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
            check_type(argname="argument toolkit_stack_name", value=toolkit_stack_name, expected_type=type_hints["toolkit_stack_name"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument job_stage", value=job_stage, expected_type=type_hints["job_stage"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "aws_region": aws_region,
            "qualifier": qualifier,
            "toolkit_stack_name": toolkit_stack_name,
        }
        if job_name is not None:
            self._values["job_name"] = job_name
        if job_stage is not None:
            self._values["job_stage"] = job_stage
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID associated with the Bootstrap configuration.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_region(self) -> builtins.str:
        '''The AWS region in which the Bootstrap will be performed.'''
        result = self._values.get("aws_region")
        assert result is not None, "Required property 'aws_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def qualifier(self) -> builtins.str:
        '''The qualifier applied to the Bootstrap.'''
        result = self._values.get("qualifier")
        assert result is not None, "Required property 'qualifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def toolkit_stack_name(self) -> builtins.str:
        '''The name of the toolkit stack used for Bootstrap.'''
        result = self._values.get("toolkit_stack_name")
        assert result is not None, "Required property 'toolkit_stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Bootstrap job.'''
        result = self._values.get("job_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Bootstrap job.'''
        result = self._values.get("job_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional resource tags that can be applied during Bootstrap.'''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BootstrapProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@gcix/gcix.addons.aws.jobs.DeployProps",
    jsii_struct_bases=[],
    name_mapping={
        "stacks": "stacks",
        "context": "context",
        "deploy_options": "deployOptions",
        "job_name": "jobName",
        "job_stage": "jobStage",
        "strict": "strict",
        "toolkit_stack_name": "toolkitStackName",
        "wait_for_stack": "waitForStack",
        "wait_for_stack_account_id": "waitForStackAccountId",
        "wait_for_stack_assume_role": "waitForStackAssumeRole",
    },
)
class DeployProps:
    def __init__(
        self,
        *,
        stacks: typing.Sequence[builtins.str],
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        deploy_options: typing.Optional[builtins.str] = None,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
        strict: typing.Optional[builtins.bool] = None,
        toolkit_stack_name: typing.Optional[builtins.str] = None,
        wait_for_stack: typing.Optional[builtins.bool] = None,
        wait_for_stack_account_id: typing.Optional[builtins.str] = None,
        wait_for_stack_assume_role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration properties for initializing a Deploy instance.

        :param stacks: An array of stack names to be deployed.
        :param context: Optional context values to provide additional information for deployment.
        :param deploy_options: Optional deployment options.
        :param job_name: An optional name for the Deploy job.
        :param job_stage: An optional stage for the Deploy job.
        :param strict: Enable strict deployment mode.
        :param toolkit_stack_name: Optional toolkit stack name used for deployment.
        :param wait_for_stack: Wait for stacks to complete deployment.
        :param wait_for_stack_account_id: AWS account ID for stack waiting.
        :param wait_for_stack_assume_role: AWS assume role for stack waiting.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59f2584e4d034817fd59c524bbed4a47eca154fcafb27c786f54876090a2187c)
            check_type(argname="argument stacks", value=stacks, expected_type=type_hints["stacks"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument deploy_options", value=deploy_options, expected_type=type_hints["deploy_options"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument job_stage", value=job_stage, expected_type=type_hints["job_stage"])
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
            check_type(argname="argument toolkit_stack_name", value=toolkit_stack_name, expected_type=type_hints["toolkit_stack_name"])
            check_type(argname="argument wait_for_stack", value=wait_for_stack, expected_type=type_hints["wait_for_stack"])
            check_type(argname="argument wait_for_stack_account_id", value=wait_for_stack_account_id, expected_type=type_hints["wait_for_stack_account_id"])
            check_type(argname="argument wait_for_stack_assume_role", value=wait_for_stack_assume_role, expected_type=type_hints["wait_for_stack_assume_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stacks": stacks,
        }
        if context is not None:
            self._values["context"] = context
        if deploy_options is not None:
            self._values["deploy_options"] = deploy_options
        if job_name is not None:
            self._values["job_name"] = job_name
        if job_stage is not None:
            self._values["job_stage"] = job_stage
        if strict is not None:
            self._values["strict"] = strict
        if toolkit_stack_name is not None:
            self._values["toolkit_stack_name"] = toolkit_stack_name
        if wait_for_stack is not None:
            self._values["wait_for_stack"] = wait_for_stack
        if wait_for_stack_account_id is not None:
            self._values["wait_for_stack_account_id"] = wait_for_stack_account_id
        if wait_for_stack_assume_role is not None:
            self._values["wait_for_stack_assume_role"] = wait_for_stack_assume_role

    @builtins.property
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names to be deployed.'''
        result = self._values.get("stacks")
        assert result is not None, "Required property 'stacks' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for deployment.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def deploy_options(self) -> typing.Optional[builtins.str]:
        '''Optional deployment options.'''
        result = self._values.get("deploy_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Deploy job.'''
        result = self._values.get("job_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Deploy job.'''
        result = self._values.get("job_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def strict(self) -> typing.Optional[builtins.bool]:
        '''Enable strict deployment mode.'''
        result = self._values.get("strict")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def toolkit_stack_name(self) -> typing.Optional[builtins.str]:
        '''Optional toolkit stack name used for deployment.'''
        result = self._values.get("toolkit_stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_stack(self) -> typing.Optional[builtins.bool]:
        '''Wait for stacks to complete deployment.'''
        result = self._values.get("wait_for_stack")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def wait_for_stack_account_id(self) -> typing.Optional[builtins.str]:
        '''AWS account ID for stack waiting.'''
        result = self._values.get("wait_for_stack_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_stack_assume_role(self) -> typing.Optional[builtins.str]:
        '''AWS assume role for stack waiting.'''
        result = self._values.get("wait_for_stack_assume_role")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeployProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@gcix/gcix.addons.aws.jobs.DiffProps",
    jsii_struct_bases=[],
    name_mapping={
        "stacks": "stacks",
        "context": "context",
        "diff_options": "diffOptions",
        "job_name": "jobName",
        "job_stage": "jobStage",
    },
)
class DiffProps:
    def __init__(
        self,
        *,
        stacks: typing.Sequence[builtins.str],
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        diff_options: typing.Optional[builtins.str] = None,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration properties for initializing a Diff instance.

        :param stacks: An array of stack names for which to generate a diff.
        :param context: Optional context values to provide additional information for the diff.
        :param diff_options: Optional diff options to customize the diff process.
        :param job_name: An optional name for the Diff job.
        :param job_stage: An optional stage for the Diff job.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__351fbce9aaf10c14aee0fc39123573062a3fc61591c0220bd85addb0cdbcaa0d)
            check_type(argname="argument stacks", value=stacks, expected_type=type_hints["stacks"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument diff_options", value=diff_options, expected_type=type_hints["diff_options"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument job_stage", value=job_stage, expected_type=type_hints["job_stage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stacks": stacks,
        }
        if context is not None:
            self._values["context"] = context
        if diff_options is not None:
            self._values["diff_options"] = diff_options
        if job_name is not None:
            self._values["job_name"] = job_name
        if job_stage is not None:
            self._values["job_stage"] = job_stage

    @builtins.property
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names for which to generate a diff.'''
        result = self._values.get("stacks")
        assert result is not None, "Required property 'stacks' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for the diff.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def diff_options(self) -> typing.Optional[builtins.str]:
        '''Optional diff options to customize the diff process.'''
        result = self._values.get("diff_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Diff job.'''
        result = self._values.get("job_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Diff job.'''
        result = self._values.get("job_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiffProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@gcix/gcix.addons.aws.jobs.IBootstrap")
class IBootstrap(typing_extensions.Protocol):
    '''Represents the interface that a Bootstrap instance adheres to.'''

    @builtins.property
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID associated with the Bootstrap configuration.'''
        ...

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        '''The AWS region in which the Bootstrap will be performed.'''
        ...

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> builtins.str:
        '''The name of the Bootstrap job.'''
        ...

    @job_name.setter
    def job_name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> builtins.str:
        '''The stage of the Bootstrap job.'''
        ...

    @job_stage.setter
    def job_stage(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        '''The qualifier applied to the Bootstrap.'''
        ...

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="toolkitStackName")
    def toolkit_stack_name(self) -> builtins.str:
        '''The name of the toolkit stack used for Bootstrap.'''
        ...

    @toolkit_stack_name.setter
    def toolkit_stack_name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional resource tags that can be applied during Bootstrap.'''
        ...

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        ...


class _IBootstrapProxy:
    '''Represents the interface that a Bootstrap instance adheres to.'''

    __jsii_type__: typing.ClassVar[str] = "@gcix/gcix.addons.aws.jobs.IBootstrap"

    @builtins.property
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID associated with the Bootstrap configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a9142a4593bcbe582b4814a06d0b7a9ac66657945b4c816d5868943291eb84f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        '''The AWS region in which the Bootstrap will be performed.'''
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8417ff02e922ff4c240d609259504f6c4b0d12740acb4bd40e312791d7a2eb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> builtins.str:
        '''The name of the Bootstrap job.'''
        return typing.cast(builtins.str, jsii.get(self, "jobName"))

    @job_name.setter
    def job_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa1e95f380f1d85d73da09b5621654ec493e9e2da172be508fcf304ddc408ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobName", value)

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> builtins.str:
        '''The stage of the Bootstrap job.'''
        return typing.cast(builtins.str, jsii.get(self, "jobStage"))

    @job_stage.setter
    def job_stage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e14fb5c9f5bf52b2edd4a4e64691d53fde0fe45e55e45feeec985ad7476d2a4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobStage", value)

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        '''The qualifier applied to the Bootstrap.'''
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1053cb4f0c8daf5a0fd4b84076b2a2f1e75454c6ad3f42a57d195ebddce43e0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)

    @builtins.property
    @jsii.member(jsii_name="toolkitStackName")
    def toolkit_stack_name(self) -> builtins.str:
        '''The name of the toolkit stack used for Bootstrap.'''
        return typing.cast(builtins.str, jsii.get(self, "toolkitStackName"))

    @toolkit_stack_name.setter
    def toolkit_stack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14b4976d4677f0d1ef54e2d91c17507ffb47f02b03dc965fbe661266807b4fe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolkitStackName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional resource tags that can be applied during Bootstrap.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eae2090515a27a74b2e6b6498f793078a0c52d257545b74b642c2962478cc88c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBootstrap).__jsii_proxy_class__ = lambda : _IBootstrapProxy


@jsii.interface(jsii_type="@gcix/gcix.addons.aws.jobs.IDeploy")
class IDeploy(typing_extensions.Protocol):
    '''Represents the interface that a Deploy instance adheres to.'''

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names to be deployed.'''
        ...

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="strict")
    def strict(self) -> builtins.bool:
        '''Flag indicating if strict deployment mode is enabled.'''
        ...

    @strict.setter
    def strict(self, value: builtins.bool) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="waitForStack")
    def wait_for_stack(self) -> builtins.bool:
        '''Flag indicating if the deployment should wait for stack completion.'''
        ...

    @wait_for_stack.setter
    def wait_for_stack(self, value: builtins.bool) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for deployment.'''
        ...

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="deployOptions")
    def deploy_options(self) -> typing.Optional[builtins.str]:
        '''Optional deployment options.'''
        ...

    @deploy_options.setter
    def deploy_options(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Deploy job.'''
        ...

    @job_name.setter
    def job_name(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Deploy job.'''
        ...

    @job_stage.setter
    def job_stage(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="toolkitStackName")
    def toolkit_stack_name(self) -> typing.Optional[builtins.str]:
        '''Optional toolkit stack name used for deployment.'''
        ...

    @toolkit_stack_name.setter
    def toolkit_stack_name(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="waitForStackAccountId")
    def wait_for_stack_account_id(self) -> typing.Optional[builtins.str]:
        '''AWS account ID for stack waiting.'''
        ...

    @wait_for_stack_account_id.setter
    def wait_for_stack_account_id(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="waitForStackAssumeRole")
    def wait_for_stack_assume_role(self) -> typing.Optional[builtins.str]:
        '''AWS assume role for stack waiting.'''
        ...

    @wait_for_stack_assume_role.setter
    def wait_for_stack_assume_role(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IDeployProxy:
    '''Represents the interface that a Deploy instance adheres to.'''

    __jsii_type__: typing.ClassVar[str] = "@gcix/gcix.addons.aws.jobs.IDeploy"

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names to be deployed.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stacks"))

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b01dd19d5ca3efdc053b5a803f70ffafa8cefd761151bac56a3d62123c133fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stacks", value)

    @builtins.property
    @jsii.member(jsii_name="strict")
    def strict(self) -> builtins.bool:
        '''Flag indicating if strict deployment mode is enabled.'''
        return typing.cast(builtins.bool, jsii.get(self, "strict"))

    @strict.setter
    def strict(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87251f92d02a841e0d63712e168c2ab971883303ef4fdc2b0dc4baec59faf223)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strict", value)

    @builtins.property
    @jsii.member(jsii_name="waitForStack")
    def wait_for_stack(self) -> builtins.bool:
        '''Flag indicating if the deployment should wait for stack completion.'''
        return typing.cast(builtins.bool, jsii.get(self, "waitForStack"))

    @wait_for_stack.setter
    def wait_for_stack(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd192aafcd22f8e1867906fc98cfc5f74e6d9370da8745c6605a6836ef2dc75f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForStack", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for deployment.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "context"))

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89de7c705e192783340b76c27adf66bb20171efa5eccc883ed318cefdd19a228)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="deployOptions")
    def deploy_options(self) -> typing.Optional[builtins.str]:
        '''Optional deployment options.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deployOptions"))

    @deploy_options.setter
    def deploy_options(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a886794564bb0a88c37c83257d909d19320c68ad7b2f215d49bfd3646ca34e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOptions", value)

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Deploy job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobName"))

    @job_name.setter
    def job_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c627c70892f8898481ad02703db9444bdf4453c29772376f049f63d51bda230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobName", value)

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Deploy job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobStage"))

    @job_stage.setter
    def job_stage(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf38f7af0f98d306556583c9eb4ef20f38557d406f379ac70b29bd32f1bf860f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobStage", value)

    @builtins.property
    @jsii.member(jsii_name="toolkitStackName")
    def toolkit_stack_name(self) -> typing.Optional[builtins.str]:
        '''Optional toolkit stack name used for deployment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "toolkitStackName"))

    @toolkit_stack_name.setter
    def toolkit_stack_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c81a8ecb26d8a14a9d7112bf1a2847b803a3d6304054230c5d23f5ab0f5f05a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolkitStackName", value)

    @builtins.property
    @jsii.member(jsii_name="waitForStackAccountId")
    def wait_for_stack_account_id(self) -> typing.Optional[builtins.str]:
        '''AWS account ID for stack waiting.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitForStackAccountId"))

    @wait_for_stack_account_id.setter
    def wait_for_stack_account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9f384ea5c8fae10c07bcfe99252715298d021c12f3d13ea119442b2088aef33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForStackAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="waitForStackAssumeRole")
    def wait_for_stack_assume_role(self) -> typing.Optional[builtins.str]:
        '''AWS assume role for stack waiting.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitForStackAssumeRole"))

    @wait_for_stack_assume_role.setter
    def wait_for_stack_assume_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23af397d485cf6bfba16d1918da8fc9fc39b9faad19959e1770ba27577460a23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForStackAssumeRole", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploy).__jsii_proxy_class__ = lambda : _IDeployProxy


@jsii.interface(jsii_type="@gcix/gcix.addons.aws.jobs.IDiff")
class IDiff(typing_extensions.Protocol):
    '''Represents the interface that a Diff instance adheres to.'''

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names for which to generate a diff.'''
        ...

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for the diff.'''
        ...

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="diffOptions")
    def diff_options(self) -> typing.Optional[builtins.str]:
        '''Optional diff options to customize the diff process.'''
        ...

    @diff_options.setter
    def diff_options(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Diff job.'''
        ...

    @job_name.setter
    def job_name(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Diff job.'''
        ...

    @job_stage.setter
    def job_stage(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IDiffProxy:
    '''Represents the interface that a Diff instance adheres to.'''

    __jsii_type__: typing.ClassVar[str] = "@gcix/gcix.addons.aws.jobs.IDiff"

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names for which to generate a diff.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stacks"))

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eebe8871ebe2716b27739b42ae2a98ffedeb3bcd7da37d22e2170f144123e87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stacks", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for the diff.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "context"))

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74bf646fd8dac476ea2923b939e37030a0dd7326abfa20745f773e4bf8fded41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="diffOptions")
    def diff_options(self) -> typing.Optional[builtins.str]:
        '''Optional diff options to customize the diff process.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diffOptions"))

    @diff_options.setter
    def diff_options(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__165ae52d2e2c5a3a3d7a4ee4f54664152e8fbe455d53855c036ec0094489d255)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diffOptions", value)

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Diff job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobName"))

    @job_name.setter
    def job_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c27e61e152aedff8b8e20880b7a2980b5aaff339adea8c0dc23401e7fdaa287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobName", value)

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Diff job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobStage"))

    @job_stage.setter
    def job_stage(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6957796f54a4eff05fe9fc84219336c0a39b5cf8082c21554744d8c9db4d0a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobStage", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiff).__jsii_proxy_class__ = lambda : _IDiffProxy


@jsii.implements(IBootstrap)
class Bootstrap(
    _Job_20682b42,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gcix/gcix.addons.aws.jobs.Bootstrap",
):
    '''Creates an instance of Bootstrap.'''

    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        aws_region: builtins.str,
        qualifier: builtins.str,
        toolkit_stack_name: builtins.str,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID associated with the Bootstrap configuration.
        :param aws_region: The AWS region in which the Bootstrap will be performed.
        :param qualifier: The qualifier applied to the Bootstrap.
        :param toolkit_stack_name: The name of the toolkit stack used for Bootstrap.
        :param job_name: An optional name for the Bootstrap job.
        :param job_stage: An optional stage for the Bootstrap job.
        :param resource_tags: Optional resource tags that can be applied during Bootstrap.
        '''
        props = BootstrapProps(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            qualifier=qualifier,
            toolkit_stack_name=toolkit_stack_name,
            job_name=job_name,
            job_stage=job_stage,
            resource_tags=resource_tags,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Returns a representation of any object which implements ``IBase``.

        The rendered representation is used by the ``gcix`` to dump it
        in YAML format as part of the ``.gitlab-ci.yml`` pipeline.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID associated with the Bootstrap configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ba68113af0aa66f1508f6342de5bf4e85fb5f9a684bbd14682124f37feea05f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        '''The AWS region in which the Bootstrap will be performed.'''
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2c4e3f3afd94eb901ffa0aeba77342e498471062bae1160bd9ca2151f70182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> builtins.str:
        '''The name of the Bootstrap job.'''
        return typing.cast(builtins.str, jsii.get(self, "jobName"))

    @job_name.setter
    def job_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__633dc4b91d8fc76e63dbc22de948af25f2fa1f6b27c8d7ba8f60452ef17afb4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobName", value)

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> builtins.str:
        '''The stage of the Bootstrap job.'''
        return typing.cast(builtins.str, jsii.get(self, "jobStage"))

    @job_stage.setter
    def job_stage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a84af947ac4f83b0c2ff625cfe36776a23c521d43dc6723784954afbadd0c50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobStage", value)

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        '''The qualifier applied to the Bootstrap.'''
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19f1719acb5481acda968f04e55be4e1e07d51d9c8332553ed2940321c121248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)

    @builtins.property
    @jsii.member(jsii_name="toolkitStackName")
    def toolkit_stack_name(self) -> builtins.str:
        '''The name of the toolkit stack used for Bootstrap.'''
        return typing.cast(builtins.str, jsii.get(self, "toolkitStackName"))

    @toolkit_stack_name.setter
    def toolkit_stack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__305dd577b763b67887b3505600b4336edfe14f7a2d429fd80c3e68bf5c8e7397)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolkitStackName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional resource tags that can be applied during Bootstrap.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d0b8a872792a95c7f493f9fa8404ef83222dae20d6940c6acd63ceb2fcf7bae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value)


@jsii.implements(IDeploy)
class Deploy(
    _Job_20682b42,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gcix/gcix.addons.aws.jobs.Deploy",
):
    '''A class that manages the configuration and rendering of a Deploy job.

    Inherits from the base Job class and implements the IDeploy interface.
    '''

    def __init__(
        self,
        *,
        stacks: typing.Sequence[builtins.str],
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        deploy_options: typing.Optional[builtins.str] = None,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
        strict: typing.Optional[builtins.bool] = None,
        toolkit_stack_name: typing.Optional[builtins.str] = None,
        wait_for_stack: typing.Optional[builtins.bool] = None,
        wait_for_stack_account_id: typing.Optional[builtins.str] = None,
        wait_for_stack_assume_role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates an instance of Deploy.

        :param stacks: An array of stack names to be deployed.
        :param context: Optional context values to provide additional information for deployment.
        :param deploy_options: Optional deployment options.
        :param job_name: An optional name for the Deploy job.
        :param job_stage: An optional stage for the Deploy job.
        :param strict: Enable strict deployment mode.
        :param toolkit_stack_name: Optional toolkit stack name used for deployment.
        :param wait_for_stack: Wait for stacks to complete deployment.
        :param wait_for_stack_account_id: AWS account ID for stack waiting.
        :param wait_for_stack_assume_role: AWS assume role for stack waiting.
        '''
        props = DeployProps(
            stacks=stacks,
            context=context,
            deploy_options=deploy_options,
            job_name=job_name,
            job_stage=job_stage,
            strict=strict,
            toolkit_stack_name=toolkit_stack_name,
            wait_for_stack=wait_for_stack,
            wait_for_stack_account_id=wait_for_stack_account_id,
            wait_for_stack_assume_role=wait_for_stack_assume_role,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Renders the Deploy job's configuration and scripts.

        :return: The rendered configuration and scripts.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names to be deployed.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stacks"))

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__255c01a37006f8a8caf0863f338768eb749eeba32d3cd563ce26b971e6954cb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stacks", value)

    @builtins.property
    @jsii.member(jsii_name="strict")
    def strict(self) -> builtins.bool:
        '''Flag indicating if strict deployment mode is enabled.'''
        return typing.cast(builtins.bool, jsii.get(self, "strict"))

    @strict.setter
    def strict(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9651e4d62bde4499e7ea8a3910c9dddf6f77eddfe7e81668b580289e1d95aa64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strict", value)

    @builtins.property
    @jsii.member(jsii_name="waitForStack")
    def wait_for_stack(self) -> builtins.bool:
        '''Flag indicating if the deployment should wait for stack completion.'''
        return typing.cast(builtins.bool, jsii.get(self, "waitForStack"))

    @wait_for_stack.setter
    def wait_for_stack(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0faee79ddddbeef41ced46199207e3a59d9fa9ae2ca9cafd9420f9d344788dd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForStack", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for deployment.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "context"))

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8166e734a947562b789bc1611cfd861963e09b2d3c81bc0cde7591b8bcba6de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="deployOptions")
    def deploy_options(self) -> typing.Optional[builtins.str]:
        '''Optional deployment options.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deployOptions"))

    @deploy_options.setter
    def deploy_options(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6aeb60213fd15e489c660d7fe83eaf43599d8011b076c8c3e98ba4d59e90873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOptions", value)

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Deploy job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobName"))

    @job_name.setter
    def job_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b18e794604241c552bfdae53a89f21eed04bbf003992dbfd0561ed3ccb013fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobName", value)

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Deploy job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobStage"))

    @job_stage.setter
    def job_stage(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265a20fd6e6b6e0ff4b37ee473ce0c2590378218553f6917655cd1b9f2ebff1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobStage", value)

    @builtins.property
    @jsii.member(jsii_name="toolkitStackName")
    def toolkit_stack_name(self) -> typing.Optional[builtins.str]:
        '''Optional toolkit stack name used for deployment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "toolkitStackName"))

    @toolkit_stack_name.setter
    def toolkit_stack_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d04d3c7a3155f536bb50128df23e4236fd0a4808c03995c76be7ce970114aba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolkitStackName", value)

    @builtins.property
    @jsii.member(jsii_name="waitForStackAccountId")
    def wait_for_stack_account_id(self) -> typing.Optional[builtins.str]:
        '''AWS account ID for stack waiting.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitForStackAccountId"))

    @wait_for_stack_account_id.setter
    def wait_for_stack_account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb080d4dbe6719360708950c6ef41095f1c976c0a292f0f7ce1aa620de96a65c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForStackAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="waitForStackAssumeRole")
    def wait_for_stack_assume_role(self) -> typing.Optional[builtins.str]:
        '''AWS assume role for stack waiting.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitForStackAssumeRole"))

    @wait_for_stack_assume_role.setter
    def wait_for_stack_assume_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85fa1e83e23d6d6aef5862d6ed4dfa6405eb2989042009c994db722bd69290dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForStackAssumeRole", value)


@jsii.implements(IDiff)
class Diff(
    _Job_20682b42,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gcix/gcix.addons.aws.jobs.Diff",
):
    '''A class that manages the configuration and rendering of a Diff job.

    Inherits from the base Job class and implements the IDiff interface.
    '''

    def __init__(
        self,
        *,
        stacks: typing.Sequence[builtins.str],
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        diff_options: typing.Optional[builtins.str] = None,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates an instance of Diff.

        :param stacks: An array of stack names for which to generate a diff.
        :param context: Optional context values to provide additional information for the diff.
        :param diff_options: Optional diff options to customize the diff process.
        :param job_name: An optional name for the Diff job.
        :param job_stage: An optional stage for the Diff job.
        '''
        props = DiffProps(
            stacks=stacks,
            context=context,
            diff_options=diff_options,
            job_name=job_name,
            job_stage=job_stage,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Returns a representation of any object which implements ``IBase``.

        The rendered representation is used by the ``gcix`` to dump it
        in YAML format as part of the ``.gitlab-ci.yml`` pipeline.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[builtins.str]:
        '''An array of stack names for which to generate a diff.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stacks"))

    @stacks.setter
    def stacks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1283da360a175b91ecc201f343c7fd476ba5b92dc44bf3cab0de8bbe6bab2f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stacks", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional context values to provide additional information for the diff.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "context"))

    @context.setter
    def context(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33ba419f1a95fac7e30e7ccfd64b64bac60075e3cc560a3d8a1de05bd3b45b4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="diffOptions")
    def diff_options(self) -> typing.Optional[builtins.str]:
        '''Optional diff options to customize the diff process.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diffOptions"))

    @diff_options.setter
    def diff_options(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df3a29dfac8763155a138b3fc937eb04ec0c445ed4336cd50e72d800ac75860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diffOptions", value)

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the Diff job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobName"))

    @job_name.setter
    def job_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1cbabba0803153d9c4806d10f44ab7d9cba6a69b1daca817cdaa729a6cd05e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobName", value)

    @builtins.property
    @jsii.member(jsii_name="jobStage")
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''An optional stage for the Diff job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobStage"))

    @job_stage.setter
    def job_stage(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c66c5c5d3b12d4610b188a23aaa506d70243c5c2f21c68edafd831d86581e65d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobStage", value)


__all__ = [
    "Bootstrap",
    "BootstrapProps",
    "Deploy",
    "DeployProps",
    "Diff",
    "DiffProps",
    "IBootstrap",
    "IDeploy",
    "IDiff",
]

publication.publish()

def _typecheckingstub__3d2a44fb3ca869efa10ffa9683897288131eee5b226ab78734a337e90f5ba6b0(
    *,
    aws_account_id: builtins.str,
    aws_region: builtins.str,
    qualifier: builtins.str,
    toolkit_stack_name: builtins.str,
    job_name: typing.Optional[builtins.str] = None,
    job_stage: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f2584e4d034817fd59c524bbed4a47eca154fcafb27c786f54876090a2187c(
    *,
    stacks: typing.Sequence[builtins.str],
    context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    deploy_options: typing.Optional[builtins.str] = None,
    job_name: typing.Optional[builtins.str] = None,
    job_stage: typing.Optional[builtins.str] = None,
    strict: typing.Optional[builtins.bool] = None,
    toolkit_stack_name: typing.Optional[builtins.str] = None,
    wait_for_stack: typing.Optional[builtins.bool] = None,
    wait_for_stack_account_id: typing.Optional[builtins.str] = None,
    wait_for_stack_assume_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351fbce9aaf10c14aee0fc39123573062a3fc61591c0220bd85addb0cdbcaa0d(
    *,
    stacks: typing.Sequence[builtins.str],
    context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    diff_options: typing.Optional[builtins.str] = None,
    job_name: typing.Optional[builtins.str] = None,
    job_stage: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a9142a4593bcbe582b4814a06d0b7a9ac66657945b4c816d5868943291eb84f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8417ff02e922ff4c240d609259504f6c4b0d12740acb4bd40e312791d7a2eb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa1e95f380f1d85d73da09b5621654ec493e9e2da172be508fcf304ddc408ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e14fb5c9f5bf52b2edd4a4e64691d53fde0fe45e55e45feeec985ad7476d2a4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1053cb4f0c8daf5a0fd4b84076b2a2f1e75454c6ad3f42a57d195ebddce43e0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b4976d4677f0d1ef54e2d91c17507ffb47f02b03dc965fbe661266807b4fe3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae2090515a27a74b2e6b6498f793078a0c52d257545b74b642c2962478cc88c(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b01dd19d5ca3efdc053b5a803f70ffafa8cefd761151bac56a3d62123c133fd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87251f92d02a841e0d63712e168c2ab971883303ef4fdc2b0dc4baec59faf223(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd192aafcd22f8e1867906fc98cfc5f74e6d9370da8745c6605a6836ef2dc75f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89de7c705e192783340b76c27adf66bb20171efa5eccc883ed318cefdd19a228(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a886794564bb0a88c37c83257d909d19320c68ad7b2f215d49bfd3646ca34e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c627c70892f8898481ad02703db9444bdf4453c29772376f049f63d51bda230(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf38f7af0f98d306556583c9eb4ef20f38557d406f379ac70b29bd32f1bf860f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c81a8ecb26d8a14a9d7112bf1a2847b803a3d6304054230c5d23f5ab0f5f05a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9f384ea5c8fae10c07bcfe99252715298d021c12f3d13ea119442b2088aef33(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23af397d485cf6bfba16d1918da8fc9fc39b9faad19959e1770ba27577460a23(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eebe8871ebe2716b27739b42ae2a98ffedeb3bcd7da37d22e2170f144123e87(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74bf646fd8dac476ea2923b939e37030a0dd7326abfa20745f773e4bf8fded41(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165ae52d2e2c5a3a3d7a4ee4f54664152e8fbe455d53855c036ec0094489d255(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c27e61e152aedff8b8e20880b7a2980b5aaff339adea8c0dc23401e7fdaa287(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6957796f54a4eff05fe9fc84219336c0a39b5cf8082c21554744d8c9db4d0a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ba68113af0aa66f1508f6342de5bf4e85fb5f9a684bbd14682124f37feea05f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2c4e3f3afd94eb901ffa0aeba77342e498471062bae1160bd9ca2151f70182(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__633dc4b91d8fc76e63dbc22de948af25f2fa1f6b27c8d7ba8f60452ef17afb4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a84af947ac4f83b0c2ff625cfe36776a23c521d43dc6723784954afbadd0c50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f1719acb5481acda968f04e55be4e1e07d51d9c8332553ed2940321c121248(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__305dd577b763b67887b3505600b4336edfe14f7a2d429fd80c3e68bf5c8e7397(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d0b8a872792a95c7f493f9fa8404ef83222dae20d6940c6acd63ceb2fcf7bae(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__255c01a37006f8a8caf0863f338768eb749eeba32d3cd563ce26b971e6954cb2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9651e4d62bde4499e7ea8a3910c9dddf6f77eddfe7e81668b580289e1d95aa64(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0faee79ddddbeef41ced46199207e3a59d9fa9ae2ca9cafd9420f9d344788dd7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8166e734a947562b789bc1611cfd861963e09b2d3c81bc0cde7591b8bcba6de(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6aeb60213fd15e489c660d7fe83eaf43599d8011b076c8c3e98ba4d59e90873(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b18e794604241c552bfdae53a89f21eed04bbf003992dbfd0561ed3ccb013fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265a20fd6e6b6e0ff4b37ee473ce0c2590378218553f6917655cd1b9f2ebff1a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d04d3c7a3155f536bb50128df23e4236fd0a4808c03995c76be7ce970114aba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb080d4dbe6719360708950c6ef41095f1c976c0a292f0f7ce1aa620de96a65c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85fa1e83e23d6d6aef5862d6ed4dfa6405eb2989042009c994db722bd69290dd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1283da360a175b91ecc201f343c7fd476ba5b92dc44bf3cab0de8bbe6bab2f7b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33ba419f1a95fac7e30e7ccfd64b64bac60075e3cc560a3d8a1de05bd3b45b4a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df3a29dfac8763155a138b3fc937eb04ec0c445ed4336cd50e72d800ac75860(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1cbabba0803153d9c4806d10f44ab7d9cba6a69b1daca817cdaa729a6cd05e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c66c5c5d3b12d4610b188a23aaa506d70243c5c2f21c68edafd831d86581e65d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass
