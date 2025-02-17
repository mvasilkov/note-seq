"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GeneratorDetails(google.protobuf.message.Message):
    """Details about a Generator."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    id: typing.Text
    """A unique ID for the generator on this server."""

    description: typing.Text
    """A short, human-readable description of the generator."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        description: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","id",b"id"]) -> None: ...
global___GeneratorDetails = GeneratorDetails

class GeneratorOptions(google.protobuf.message.Message):
    """Options for generating a sequence."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class SequenceSection(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        START_TIME_FIELD_NUMBER: builtins.int
        END_TIME_FIELD_NUMBER: builtins.int
        start_time: builtins.float
        """Start time for the section in seconds, inclusive."""

        end_time: builtins.float
        """End time for the section in seconds, exclusive."""

        def __init__(self,
            *,
            start_time: builtins.float = ...,
            end_time: builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["end_time",b"end_time","start_time",b"start_time"]) -> None: ...

    class ArgValue(google.protobuf.message.Message):
        """Map of argument name to argument value for additional arguments.
        Generators should ignore unsupported arguments.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        BYTE_VALUE_FIELD_NUMBER: builtins.int
        INT_VALUE_FIELD_NUMBER: builtins.int
        FLOAT_VALUE_FIELD_NUMBER: builtins.int
        BOOL_VALUE_FIELD_NUMBER: builtins.int
        STRING_VALUE_FIELD_NUMBER: builtins.int
        byte_value: builtins.bytes
        int_value: builtins.int
        float_value: builtins.float
        bool_value: builtins.bool
        string_value: typing.Text
        def __init__(self,
            *,
            byte_value: builtins.bytes = ...,
            int_value: builtins.int = ...,
            float_value: builtins.float = ...,
            bool_value: builtins.bool = ...,
            string_value: typing.Text = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["bool_value",b"bool_value","byte_value",b"byte_value","float_value",b"float_value","int_value",b"int_value","kind",b"kind","string_value",b"string_value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["bool_value",b"bool_value","byte_value",b"byte_value","float_value",b"float_value","int_value",b"int_value","kind",b"kind","string_value",b"string_value"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["kind",b"kind"]) -> typing.Optional[typing_extensions.Literal["byte_value","int_value","float_value","bool_value","string_value"]]: ...

    class ArgsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> global___GeneratorOptions.ArgValue: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___GeneratorOptions.ArgValue] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    INPUT_SECTIONS_FIELD_NUMBER: builtins.int
    GENERATE_SECTIONS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def input_sections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GeneratorOptions.SequenceSection]:
        """Sections of input sequence to condition on."""
        pass
    @property
    def generate_sections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GeneratorOptions.SequenceSection]:
        """Sections of sequence to generate."""
        pass
    @property
    def args(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___GeneratorOptions.ArgValue]: ...
    def __init__(self,
        *,
        input_sections: typing.Optional[typing.Iterable[global___GeneratorOptions.SequenceSection]] = ...,
        generate_sections: typing.Optional[typing.Iterable[global___GeneratorOptions.SequenceSection]] = ...,
        args: typing.Optional[typing.Mapping[typing.Text, global___GeneratorOptions.ArgValue]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","generate_sections",b"generate_sections","input_sections",b"input_sections"]) -> None: ...
global___GeneratorOptions = GeneratorOptions

class GeneratorBundle(google.protobuf.message.Message):
    """Bundle for wrapping a generator id, checkpoint file, and metagraph.
    Intended to make sharing pre-trained models easier.
    Next ID: 5
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class BundleDetails(google.protobuf.message.Message):
        """Details about this specific bundle."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        DESCRIPTION_FIELD_NUMBER: builtins.int
        description: typing.Text
        """A short, human-readable text description of the bundle (e.g., training
        data, hyper parameters, etc.).
        """

        def __init__(self,
            *,
            description: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["description",b"description"]) -> None: ...

    GENERATOR_DETAILS_FIELD_NUMBER: builtins.int
    BUNDLE_DETAILS_FIELD_NUMBER: builtins.int
    CHECKPOINT_FILE_FIELD_NUMBER: builtins.int
    METAGRAPH_FILE_FIELD_NUMBER: builtins.int
    @property
    def generator_details(self) -> global___GeneratorDetails:
        """Details about the generator that created this bundle."""
        pass
    @property
    def bundle_details(self) -> global___GeneratorBundle.BundleDetails: ...
    @property
    def checkpoint_file(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """The contents of the checkpoint file generated by the Saver.
        This is a repeated field so we can eventually support sharded checkpoints.
        But for now, we support only 1 file.
        """
        pass
    metagraph_file: builtins.bytes
    """The contents of the metagraph file generated by the Saver."""

    def __init__(self,
        *,
        generator_details: typing.Optional[global___GeneratorDetails] = ...,
        bundle_details: typing.Optional[global___GeneratorBundle.BundleDetails] = ...,
        checkpoint_file: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        metagraph_file: builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bundle_details",b"bundle_details","generator_details",b"generator_details"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bundle_details",b"bundle_details","checkpoint_file",b"checkpoint_file","generator_details",b"generator_details","metagraph_file",b"metagraph_file"]) -> None: ...
global___GeneratorBundle = GeneratorBundle
