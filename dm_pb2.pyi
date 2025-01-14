from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AvatarTypeNone: _ClassVar[AvatarType]
    AvatarTypeNFT: _ClassVar[AvatarType]

class BubbleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BubbleTypeNone: _ClassVar[BubbleType]
    BubbleTypeClickButton: _ClassVar[BubbleType]
    BubbleTypeDmSettingPanel: _ClassVar[BubbleType]

class CheckboxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CheckboxTypeNone: _ClassVar[CheckboxType]
    CheckboxTypeEncourage: _ClassVar[CheckboxType]
    CheckboxTypeColorDM: _ClassVar[CheckboxType]

class DMAttrBit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DMAttrBitProtect: _ClassVar[DMAttrBit]
    DMAttrBitFromLive: _ClassVar[DMAttrBit]
    DMAttrHighLike: _ClassVar[DMAttrBit]

class DmColorfulType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NoneType: _ClassVar[DmColorfulType]
    VipGradualColor: _ClassVar[DmColorfulType]

class ExposureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ExposureTypeNone: _ClassVar[ExposureType]
    ExposureTypeDMSend: _ClassVar[ExposureType]

class PostPanelBizType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PostPanelBizTypeNone: _ClassVar[PostPanelBizType]
    PostPanelBizTypeEncourage: _ClassVar[PostPanelBizType]
    PostPanelBizTypeColorDM: _ClassVar[PostPanelBizType]
    PostPanelBizTypeNFTDM: _ClassVar[PostPanelBizType]
    PostPanelBizTypeFragClose: _ClassVar[PostPanelBizType]
    PostPanelBizTypeRecommend: _ClassVar[PostPanelBizType]

class PostStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PostStatusNormal: _ClassVar[PostStatus]
    PostStatusClosed: _ClassVar[PostStatus]

class RenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RenderTypeNone: _ClassVar[RenderType]
    RenderTypeSingle: _ClassVar[RenderType]
    RenderTypeRotation: _ClassVar[RenderType]

class SubtitleAiStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    None: _ClassVar[SubtitleAiStatus]
    Exposure: _ClassVar[SubtitleAiStatus]
    Assist: _ClassVar[SubtitleAiStatus]

class SubtitleAiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Normal: _ClassVar[SubtitleAiType]
    Translate: _ClassVar[SubtitleAiType]

class SubtitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CC: _ClassVar[SubtitleType]
    AI: _ClassVar[SubtitleType]

class ToastFunctionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ToastFunctionTypeNone: _ClassVar[ToastFunctionType]
    ToastFunctionTypePostPanel: _ClassVar[ToastFunctionType]
AvatarTypeNone: AvatarType
AvatarTypeNFT: AvatarType
BubbleTypeNone: BubbleType
BubbleTypeClickButton: BubbleType
BubbleTypeDmSettingPanel: BubbleType
CheckboxTypeNone: CheckboxType
CheckboxTypeEncourage: CheckboxType
CheckboxTypeColorDM: CheckboxType
DMAttrBitProtect: DMAttrBit
DMAttrBitFromLive: DMAttrBit
DMAttrHighLike: DMAttrBit
NoneType: DmColorfulType
VipGradualColor: DmColorfulType
ExposureTypeNone: ExposureType
ExposureTypeDMSend: ExposureType
PostPanelBizTypeNone: PostPanelBizType
PostPanelBizTypeEncourage: PostPanelBizType
PostPanelBizTypeColorDM: PostPanelBizType
PostPanelBizTypeNFTDM: PostPanelBizType
PostPanelBizTypeFragClose: PostPanelBizType
PostPanelBizTypeRecommend: PostPanelBizType
PostStatusNormal: PostStatus
PostStatusClosed: PostStatus
RenderTypeNone: RenderType
RenderTypeSingle: RenderType
RenderTypeRotation: RenderType
None: SubtitleAiStatus
Exposure: SubtitleAiStatus
Assist: SubtitleAiStatus
Normal: SubtitleAiType
Translate: SubtitleAiType
CC: SubtitleType
AI: SubtitleType
ToastFunctionTypeNone: ToastFunctionType
ToastFunctionTypePostPanel: ToastFunctionType

class Avatar(_message.Message):
    __slots__ = ("id", "url", "avatar_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    avatar_type: AvatarType
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., avatar_type: _Optional[_Union[AvatarType, str]] = ...) -> None: ...

class Bubble(_message.Message):
    __slots__ = ("text", "url")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    text: str
    url: str
    def __init__(self, text: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class BubbleV2(_message.Message):
    __slots__ = ("text", "url", "bubble_type", "exposure_once", "exposure_type")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    text: str
    url: str
    bubble_type: BubbleType
    exposure_once: bool
    exposure_type: ExposureType
    def __init__(self, text: _Optional[str] = ..., url: _Optional[str] = ..., bubble_type: _Optional[_Union[BubbleType, str]] = ..., exposure_once: bool = ..., exposure_type: _Optional[_Union[ExposureType, str]] = ...) -> None: ...

class Button(_message.Message):
    __slots__ = ("text", "action")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    text: str
    action: int
    def __init__(self, text: _Optional[str] = ..., action: _Optional[int] = ...) -> None: ...

class BuzzwordConfig(_message.Message):
    __slots__ = ("keywords",)
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    keywords: _containers.RepeatedCompositeFieldContainer[BuzzwordShowConfig]
    def __init__(self, keywords: _Optional[_Iterable[_Union[BuzzwordShowConfig, _Mapping]]] = ...) -> None: ...

class BuzzwordShowConfig(_message.Message):
    __slots__ = ("name", "schema", "source", "id", "buzzword_id", "schema_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BUZZWORD_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    schema: str
    source: int
    id: int
    buzzword_id: int
    schema_type: int
    def __init__(self, name: _Optional[str] = ..., schema: _Optional[str] = ..., source: _Optional[int] = ..., id: _Optional[int] = ..., buzzword_id: _Optional[int] = ..., schema_type: _Optional[int] = ...) -> None: ...

class CheckBox(_message.Message):
    __slots__ = ("text", "type", "default_value", "show")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    text: str
    type: CheckboxType
    default_value: bool
    show: bool
    def __init__(self, text: _Optional[str] = ..., type: _Optional[_Union[CheckboxType, str]] = ..., default_value: bool = ..., show: bool = ...) -> None: ...

class CheckBoxV2(_message.Message):
    __slots__ = ("text", "type", "default_value")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    text: str
    type: int
    default_value: bool
    def __init__(self, text: _Optional[str] = ..., type: _Optional[int] = ..., default_value: bool = ...) -> None: ...

class ClickButton(_message.Message):
    __slots__ = ("portrait_text", "landscape_text", "portrait_text_focus", "landscape_text_focus", "render_type", "show", "bubble")
    PORTRAIT_TEXT_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_TEXT_FIELD_NUMBER: _ClassVar[int]
    PORTRAIT_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_FIELD_NUMBER: _ClassVar[int]
    portrait_text: _containers.RepeatedScalarFieldContainer[str]
    landscape_text: _containers.RepeatedScalarFieldContainer[str]
    portrait_text_focus: _containers.RepeatedScalarFieldContainer[str]
    landscape_text_focus: _containers.RepeatedScalarFieldContainer[str]
    render_type: RenderType
    show: bool
    bubble: Bubble
    def __init__(self, portrait_text: _Optional[_Iterable[str]] = ..., landscape_text: _Optional[_Iterable[str]] = ..., portrait_text_focus: _Optional[_Iterable[str]] = ..., landscape_text_focus: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., show: bool = ..., bubble: _Optional[_Union[Bubble, _Mapping]] = ...) -> None: ...

class ClickButtonV2(_message.Message):
    __slots__ = ("portrait_text", "landscape_text", "portrait_text_focus", "landscape_text_focus", "render_type", "text_input_post", "exposure_once", "exposure_type")
    PORTRAIT_TEXT_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_TEXT_FIELD_NUMBER: _ClassVar[int]
    PORTRAIT_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_POST_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    portrait_text: _containers.RepeatedScalarFieldContainer[str]
    landscape_text: _containers.RepeatedScalarFieldContainer[str]
    portrait_text_focus: _containers.RepeatedScalarFieldContainer[str]
    landscape_text_focus: _containers.RepeatedScalarFieldContainer[str]
    render_type: int
    text_input_post: bool
    exposure_once: bool
    exposure_type: int
    def __init__(self, portrait_text: _Optional[_Iterable[str]] = ..., landscape_text: _Optional[_Iterable[str]] = ..., portrait_text_focus: _Optional[_Iterable[str]] = ..., landscape_text_focus: _Optional[_Iterable[str]] = ..., render_type: _Optional[int] = ..., text_input_post: bool = ..., exposure_once: bool = ..., exposure_type: _Optional[int] = ...) -> None: ...

class CommandDm(_message.Message):
    __slots__ = ("id", "oid", "mid", "command", "content", "progress", "ctime", "mtime", "extra", "idStr")
    ID_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    IDSTR_FIELD_NUMBER: _ClassVar[int]
    id: int
    oid: int
    mid: str
    command: str
    content: str
    progress: int
    ctime: str
    mtime: str
    extra: str
    idStr: str
    def __init__(self, id: _Optional[int] = ..., oid: _Optional[int] = ..., mid: _Optional[str] = ..., command: _Optional[str] = ..., content: _Optional[str] = ..., progress: _Optional[int] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., extra: _Optional[str] = ..., idStr: _Optional[str] = ...) -> None: ...

class DanmakuAIFlag(_message.Message):
    __slots__ = ("dm_flags",)
    DM_FLAGS_FIELD_NUMBER: _ClassVar[int]
    dm_flags: _containers.RepeatedCompositeFieldContainer[DanmakuFlag]
    def __init__(self, dm_flags: _Optional[_Iterable[_Union[DanmakuFlag, _Mapping]]] = ...) -> None: ...

class DanmakuElem(_message.Message):
    __slots__ = ("id", "progress", "mode", "fontsize", "color", "midHash", "content", "ctime", "weight", "action", "pool", "idStr", "attr", "animation", "colorful")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    MIDHASH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    POOL_FIELD_NUMBER: _ClassVar[int]
    IDSTR_FIELD_NUMBER: _ClassVar[int]
    ATTR_FIELD_NUMBER: _ClassVar[int]
    ANIMATION_FIELD_NUMBER: _ClassVar[int]
    COLORFUL_FIELD_NUMBER: _ClassVar[int]
    id: int
    progress: int
    mode: int
    fontsize: int
    color: int
    midHash: str
    content: str
    ctime: int
    weight: int
    action: str
    pool: int
    idStr: str
    attr: int
    animation: str
    colorful: DmColorfulType
    def __init__(self, id: _Optional[int] = ..., progress: _Optional[int] = ..., mode: _Optional[int] = ..., fontsize: _Optional[int] = ..., color: _Optional[int] = ..., midHash: _Optional[str] = ..., content: _Optional[str] = ..., ctime: _Optional[int] = ..., weight: _Optional[int] = ..., action: _Optional[str] = ..., pool: _Optional[int] = ..., idStr: _Optional[str] = ..., attr: _Optional[int] = ..., animation: _Optional[str] = ..., colorful: _Optional[_Union[DmColorfulType, str]] = ...) -> None: ...

class DanmakuFlag(_message.Message):
    __slots__ = ("dmid", "flag")
    DMID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    dmid: int
    flag: int
    def __init__(self, dmid: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class DanmakuFlagConfig(_message.Message):
    __slots__ = ("rec_flag", "rec_text", "rec_switch")
    REC_FLAG_FIELD_NUMBER: _ClassVar[int]
    REC_TEXT_FIELD_NUMBER: _ClassVar[int]
    REC_SWITCH_FIELD_NUMBER: _ClassVar[int]
    rec_flag: int
    rec_text: str
    rec_switch: int
    def __init__(self, rec_flag: _Optional[int] = ..., rec_text: _Optional[str] = ..., rec_switch: _Optional[int] = ...) -> None: ...

class DanmuDefaultPlayerConfig(_message.Message):
    __slots__ = ("player_danmaku_use_default_config", "player_danmaku_ai_recommended_switch", "player_danmaku_ai_recommended_level", "player_danmaku_blocktop", "player_danmaku_blockscroll", "player_danmaku_blockbottom", "player_danmaku_blockcolorful", "player_danmaku_blockrepeat", "player_danmaku_blockspecial", "player_danmaku_opacity", "player_danmaku_scalingfactor", "player_danmaku_domain", "player_danmaku_speed", "inline_player_danmaku_switch", "player_danmaku_senior_mode_switch", "player_danmaku_ai_recommended_level_v2", "player_danmaku_ai_recommended_level_v2_map")
    class PlayerDanmakuAiRecommendedLevelV2MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PLAYER_DANMAKU_USE_DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_AI_RECOMMENDED_SWITCH_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKTOP_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKSCROLL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKBOTTOM_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKCOLORFUL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKREPEAT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKSPECIAL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_OPACITY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_SCALINGFACTOR_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_SPEED_FIELD_NUMBER: _ClassVar[int]
    INLINE_PLAYER_DANMAKU_SWITCH_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_V2_MAP_FIELD_NUMBER: _ClassVar[int]
    player_danmaku_use_default_config: bool
    player_danmaku_ai_recommended_switch: bool
    player_danmaku_ai_recommended_level: int
    player_danmaku_blocktop: bool
    player_danmaku_blockscroll: bool
    player_danmaku_blockbottom: bool
    player_danmaku_blockcolorful: bool
    player_danmaku_blockrepeat: bool
    player_danmaku_blockspecial: bool
    player_danmaku_opacity: float
    player_danmaku_scalingfactor: float
    player_danmaku_domain: float
    player_danmaku_speed: int
    inline_player_danmaku_switch: bool
    player_danmaku_senior_mode_switch: int
    player_danmaku_ai_recommended_level_v2: int
    player_danmaku_ai_recommended_level_v2_map: _containers.ScalarMap[int, int]
    def __init__(self, player_danmaku_use_default_config: bool = ..., player_danmaku_ai_recommended_switch: bool = ..., player_danmaku_ai_recommended_level: _Optional[int] = ..., player_danmaku_blocktop: bool = ..., player_danmaku_blockscroll: bool = ..., player_danmaku_blockbottom: bool = ..., player_danmaku_blockcolorful: bool = ..., player_danmaku_blockrepeat: bool = ..., player_danmaku_blockspecial: bool = ..., player_danmaku_opacity: _Optional[float] = ..., player_danmaku_scalingfactor: _Optional[float] = ..., player_danmaku_domain: _Optional[float] = ..., player_danmaku_speed: _Optional[int] = ..., inline_player_danmaku_switch: bool = ..., player_danmaku_senior_mode_switch: _Optional[int] = ..., player_danmaku_ai_recommended_level_v2: _Optional[int] = ..., player_danmaku_ai_recommended_level_v2_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class DanmuPlayerConfig(_message.Message):
    __slots__ = ("player_danmaku_switch", "player_danmaku_switch_save", "player_danmaku_use_default_config", "player_danmaku_ai_recommended_switch", "player_danmaku_ai_recommended_level", "player_danmaku_blocktop", "player_danmaku_blockscroll", "player_danmaku_blockbottom", "player_danmaku_blockcolorful", "player_danmaku_blockrepeat", "player_danmaku_blockspecial", "player_danmaku_opacity", "player_danmaku_scalingfactor", "player_danmaku_domain", "player_danmaku_speed", "player_danmaku_enableblocklist", "inline_player_danmaku_switch", "inline_player_danmaku_config", "player_danmaku_ios_switch_save", "player_danmaku_senior_mode_switch", "player_danmaku_ai_recommended_level_v2", "player_danmaku_ai_recommended_level_v2_map")
    class PlayerDanmakuAiRecommendedLevelV2MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PLAYER_DANMAKU_SWITCH_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_SWITCH_SAVE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_USE_DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_AI_RECOMMENDED_SWITCH_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKTOP_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKSCROLL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKBOTTOM_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKCOLORFUL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKREPEAT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_BLOCKSPECIAL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_OPACITY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_SCALINGFACTOR_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_SPEED_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_ENABLEBLOCKLIST_FIELD_NUMBER: _ClassVar[int]
    INLINE_PLAYER_DANMAKU_SWITCH_FIELD_NUMBER: _ClassVar[int]
    INLINE_PLAYER_DANMAKU_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_IOS_SWITCH_SAVE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_V2_MAP_FIELD_NUMBER: _ClassVar[int]
    player_danmaku_switch: bool
    player_danmaku_switch_save: bool
    player_danmaku_use_default_config: bool
    player_danmaku_ai_recommended_switch: bool
    player_danmaku_ai_recommended_level: int
    player_danmaku_blocktop: bool
    player_danmaku_blockscroll: bool
    player_danmaku_blockbottom: bool
    player_danmaku_blockcolorful: bool
    player_danmaku_blockrepeat: bool
    player_danmaku_blockspecial: bool
    player_danmaku_opacity: float
    player_danmaku_scalingfactor: float
    player_danmaku_domain: float
    player_danmaku_speed: int
    player_danmaku_enableblocklist: bool
    inline_player_danmaku_switch: bool
    inline_player_danmaku_config: int
    player_danmaku_ios_switch_save: int
    player_danmaku_senior_mode_switch: int
    player_danmaku_ai_recommended_level_v2: int
    player_danmaku_ai_recommended_level_v2_map: _containers.ScalarMap[int, int]
    def __init__(self, player_danmaku_switch: bool = ..., player_danmaku_switch_save: bool = ..., player_danmaku_use_default_config: bool = ..., player_danmaku_ai_recommended_switch: bool = ..., player_danmaku_ai_recommended_level: _Optional[int] = ..., player_danmaku_blocktop: bool = ..., player_danmaku_blockscroll: bool = ..., player_danmaku_blockbottom: bool = ..., player_danmaku_blockcolorful: bool = ..., player_danmaku_blockrepeat: bool = ..., player_danmaku_blockspecial: bool = ..., player_danmaku_opacity: _Optional[float] = ..., player_danmaku_scalingfactor: _Optional[float] = ..., player_danmaku_domain: _Optional[float] = ..., player_danmaku_speed: _Optional[int] = ..., player_danmaku_enableblocklist: bool = ..., inline_player_danmaku_switch: bool = ..., inline_player_danmaku_config: _Optional[int] = ..., player_danmaku_ios_switch_save: _Optional[int] = ..., player_danmaku_senior_mode_switch: _Optional[int] = ..., player_danmaku_ai_recommended_level_v2: _Optional[int] = ..., player_danmaku_ai_recommended_level_v2_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class DanmuPlayerConfigPanel(_message.Message):
    __slots__ = ("selection_text",)
    SELECTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    selection_text: str
    def __init__(self, selection_text: _Optional[str] = ...) -> None: ...

class DanmuPlayerDynamicConfig(_message.Message):
    __slots__ = ("progress", "player_danmaku_domain")
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DANMAKU_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    progress: int
    player_danmaku_domain: float
    def __init__(self, progress: _Optional[int] = ..., player_danmaku_domain: _Optional[float] = ...) -> None: ...

class DanmuPlayerViewConfig(_message.Message):
    __slots__ = ("danmuku_default_player_config", "danmuku_player_config", "danmuku_player_dynamic_config", "danmuku_player_config_panel")
    DANMUKU_DEFAULT_PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DANMUKU_PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DANMUKU_PLAYER_DYNAMIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DANMUKU_PLAYER_CONFIG_PANEL_FIELD_NUMBER: _ClassVar[int]
    danmuku_default_player_config: DanmuDefaultPlayerConfig
    danmuku_player_config: DanmuPlayerConfig
    danmuku_player_dynamic_config: _containers.RepeatedCompositeFieldContainer[DanmuPlayerDynamicConfig]
    danmuku_player_config_panel: DanmuPlayerConfigPanel
    def __init__(self, danmuku_default_player_config: _Optional[_Union[DanmuDefaultPlayerConfig, _Mapping]] = ..., danmuku_player_config: _Optional[_Union[DanmuPlayerConfig, _Mapping]] = ..., danmuku_player_dynamic_config: _Optional[_Iterable[_Union[DanmuPlayerDynamicConfig, _Mapping]]] = ..., danmuku_player_config_panel: _Optional[_Union[DanmuPlayerConfigPanel, _Mapping]] = ...) -> None: ...

class DanmuWebPlayerConfig(_message.Message):
    __slots__ = ("dm_switch", "ai_switch", "ai_level", "blocktop", "blockscroll", "blockbottom", "blockcolor", "blockspecial", "preventshade", "dmask", "opacity", "dmarea", "speedplus", "fontsize", "screensync", "speedsync", "fontfamily", "bold", "fontborder", "draw_type", "senior_mode_switch", "ai_level_v2", "ai_level_v2_map")
    class AiLevelV2MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    DM_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AI_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AI_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BLOCKTOP_FIELD_NUMBER: _ClassVar[int]
    BLOCKSCROLL_FIELD_NUMBER: _ClassVar[int]
    BLOCKBOTTOM_FIELD_NUMBER: _ClassVar[int]
    BLOCKCOLOR_FIELD_NUMBER: _ClassVar[int]
    BLOCKSPECIAL_FIELD_NUMBER: _ClassVar[int]
    PREVENTSHADE_FIELD_NUMBER: _ClassVar[int]
    DMASK_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    DMAREA_FIELD_NUMBER: _ClassVar[int]
    SPEEDPLUS_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    SCREENSYNC_FIELD_NUMBER: _ClassVar[int]
    SPEEDSYNC_FIELD_NUMBER: _ClassVar[int]
    FONTFAMILY_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    FONTBORDER_FIELD_NUMBER: _ClassVar[int]
    DRAW_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AI_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
    AI_LEVEL_V2_MAP_FIELD_NUMBER: _ClassVar[int]
    dm_switch: bool
    ai_switch: bool
    ai_level: int
    blocktop: bool
    blockscroll: bool
    blockbottom: bool
    blockcolor: bool
    blockspecial: bool
    preventshade: bool
    dmask: bool
    opacity: float
    dmarea: int
    speedplus: float
    fontsize: float
    screensync: bool
    speedsync: bool
    fontfamily: str
    bold: bool
    fontborder: int
    draw_type: str
    senior_mode_switch: int
    ai_level_v2: int
    ai_level_v2_map: _containers.ScalarMap[int, int]
    def __init__(self, dm_switch: bool = ..., ai_switch: bool = ..., ai_level: _Optional[int] = ..., blocktop: bool = ..., blockscroll: bool = ..., blockbottom: bool = ..., blockcolor: bool = ..., blockspecial: bool = ..., preventshade: bool = ..., dmask: bool = ..., opacity: _Optional[float] = ..., dmarea: _Optional[int] = ..., speedplus: _Optional[float] = ..., fontsize: _Optional[float] = ..., screensync: bool = ..., speedsync: bool = ..., fontfamily: _Optional[str] = ..., bold: bool = ..., fontborder: _Optional[int] = ..., draw_type: _Optional[str] = ..., senior_mode_switch: _Optional[int] = ..., ai_level_v2: _Optional[int] = ..., ai_level_v2_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class DmColorful(_message.Message):
    __slots__ = ("type", "src")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    type: DmColorfulType
    src: str
    def __init__(self, type: _Optional[_Union[DmColorfulType, str]] = ..., src: _Optional[str] = ...) -> None: ...

class DmExpoReportReq(_message.Message):
    __slots__ = ("session_id", "oid", "spmid")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    SPMID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    oid: int
    spmid: str
    def __init__(self, session_id: _Optional[str] = ..., oid: _Optional[int] = ..., spmid: _Optional[str] = ...) -> None: ...

class DmExpoReportRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DmPlayerConfigReq(_message.Message):
    __slots__ = ("ts", "switch", "switch_save", "use_default_config", "ai_recommended_switch", "ai_recommended_level", "blocktop", "blockscroll", "blockbottom", "blockcolorful", "blockrepeat", "blockspecial", "opacity", "scalingfactor", "domain", "speed", "enableblocklist", "inlinePlayerDanmakuSwitch", "senior_mode_switch", "ai_recommended_level_v2")
    TS_FIELD_NUMBER: _ClassVar[int]
    SWITCH_FIELD_NUMBER: _ClassVar[int]
    SWITCH_SAVE_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AI_RECOMMENDED_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AI_RECOMMENDED_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BLOCKTOP_FIELD_NUMBER: _ClassVar[int]
    BLOCKSCROLL_FIELD_NUMBER: _ClassVar[int]
    BLOCKBOTTOM_FIELD_NUMBER: _ClassVar[int]
    BLOCKCOLORFUL_FIELD_NUMBER: _ClassVar[int]
    BLOCKREPEAT_FIELD_NUMBER: _ClassVar[int]
    BLOCKSPECIAL_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    SCALINGFACTOR_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    ENABLEBLOCKLIST_FIELD_NUMBER: _ClassVar[int]
    INLINEPLAYERDANMAKUSWITCH_FIELD_NUMBER: _ClassVar[int]
    SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AI_RECOMMENDED_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
    ts: int
    switch: PlayerDanmakuSwitch
    switch_save: PlayerDanmakuSwitchSave
    use_default_config: PlayerDanmakuUseDefaultConfig
    ai_recommended_switch: PlayerDanmakuAiRecommendedSwitch
    ai_recommended_level: PlayerDanmakuAiRecommendedLevel
    blocktop: PlayerDanmakuBlocktop
    blockscroll: PlayerDanmakuBlockscroll
    blockbottom: PlayerDanmakuBlockbottom
    blockcolorful: PlayerDanmakuBlockcolorful
    blockrepeat: PlayerDanmakuBlockrepeat
    blockspecial: PlayerDanmakuBlockspecial
    opacity: PlayerDanmakuOpacity
    scalingfactor: PlayerDanmakuScalingfactor
    domain: PlayerDanmakuDomain
    speed: PlayerDanmakuSpeed
    enableblocklist: PlayerDanmakuEnableblocklist
    inlinePlayerDanmakuSwitch: InlinePlayerDanmakuSwitch
    senior_mode_switch: PlayerDanmakuSeniorModeSwitch
    ai_recommended_level_v2: PlayerDanmakuAiRecommendedLevelV2
    def __init__(self, ts: _Optional[int] = ..., switch: _Optional[_Union[PlayerDanmakuSwitch, _Mapping]] = ..., switch_save: _Optional[_Union[PlayerDanmakuSwitchSave, _Mapping]] = ..., use_default_config: _Optional[_Union[PlayerDanmakuUseDefaultConfig, _Mapping]] = ..., ai_recommended_switch: _Optional[_Union[PlayerDanmakuAiRecommendedSwitch, _Mapping]] = ..., ai_recommended_level: _Optional[_Union[PlayerDanmakuAiRecommendedLevel, _Mapping]] = ..., blocktop: _Optional[_Union[PlayerDanmakuBlocktop, _Mapping]] = ..., blockscroll: _Optional[_Union[PlayerDanmakuBlockscroll, _Mapping]] = ..., blockbottom: _Optional[_Union[PlayerDanmakuBlockbottom, _Mapping]] = ..., blockcolorful: _Optional[_Union[PlayerDanmakuBlockcolorful, _Mapping]] = ..., blockrepeat: _Optional[_Union[PlayerDanmakuBlockrepeat, _Mapping]] = ..., blockspecial: _Optional[_Union[PlayerDanmakuBlockspecial, _Mapping]] = ..., opacity: _Optional[_Union[PlayerDanmakuOpacity, _Mapping]] = ..., scalingfactor: _Optional[_Union[PlayerDanmakuScalingfactor, _Mapping]] = ..., domain: _Optional[_Union[PlayerDanmakuDomain, _Mapping]] = ..., speed: _Optional[_Union[PlayerDanmakuSpeed, _Mapping]] = ..., enableblocklist: _Optional[_Union[PlayerDanmakuEnableblocklist, _Mapping]] = ..., inlinePlayerDanmakuSwitch: _Optional[_Union[InlinePlayerDanmakuSwitch, _Mapping]] = ..., senior_mode_switch: _Optional[_Union[PlayerDanmakuSeniorModeSwitch, _Mapping]] = ..., ai_recommended_level_v2: _Optional[_Union[PlayerDanmakuAiRecommendedLevelV2, _Mapping]] = ...) -> None: ...

class DmSegConfig(_message.Message):
    __slots__ = ("page_size", "total")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    total: int
    def __init__(self, page_size: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class DmSegMobileReply(_message.Message):
    __slots__ = ("elems", "state", "ai_flag", "colorfulSrc")
    ELEMS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AI_FLAG_FIELD_NUMBER: _ClassVar[int]
    COLORFULSRC_FIELD_NUMBER: _ClassVar[int]
    elems: _containers.RepeatedCompositeFieldContainer[DanmakuElem]
    state: int
    ai_flag: DanmakuAIFlag
    colorfulSrc: _containers.RepeatedCompositeFieldContainer[DmColorful]
    def __init__(self, elems: _Optional[_Iterable[_Union[DanmakuElem, _Mapping]]] = ..., state: _Optional[int] = ..., ai_flag: _Optional[_Union[DanmakuAIFlag, _Mapping]] = ..., colorfulSrc: _Optional[_Iterable[_Union[DmColorful, _Mapping]]] = ...) -> None: ...

class DmSegMobileReq(_message.Message):
    __slots__ = ("pid", "oid", "type", "segment_index", "teenagers_mode", "ps", "pe", "pull_mode", "from_scene")
    PID_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    TEENAGERS_MODE_FIELD_NUMBER: _ClassVar[int]
    PS_FIELD_NUMBER: _ClassVar[int]
    PE_FIELD_NUMBER: _ClassVar[int]
    PULL_MODE_FIELD_NUMBER: _ClassVar[int]
    FROM_SCENE_FIELD_NUMBER: _ClassVar[int]
    pid: int
    oid: int
    type: int
    segment_index: int
    teenagers_mode: int
    ps: int
    pe: int
    pull_mode: int
    from_scene: int
    def __init__(self, pid: _Optional[int] = ..., oid: _Optional[int] = ..., type: _Optional[int] = ..., segment_index: _Optional[int] = ..., teenagers_mode: _Optional[int] = ..., ps: _Optional[int] = ..., pe: _Optional[int] = ..., pull_mode: _Optional[int] = ..., from_scene: _Optional[int] = ...) -> None: ...

class DmSegOttReply(_message.Message):
    __slots__ = ("closed", "elems")
    CLOSED_FIELD_NUMBER: _ClassVar[int]
    ELEMS_FIELD_NUMBER: _ClassVar[int]
    closed: bool
    elems: _containers.RepeatedCompositeFieldContainer[DanmakuElem]
    def __init__(self, closed: bool = ..., elems: _Optional[_Iterable[_Union[DanmakuElem, _Mapping]]] = ...) -> None: ...

class DmSegOttReq(_message.Message):
    __slots__ = ("pid", "oid", "type", "segment_index")
    PID_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    pid: int
    oid: int
    type: int
    segment_index: int
    def __init__(self, pid: _Optional[int] = ..., oid: _Optional[int] = ..., type: _Optional[int] = ..., segment_index: _Optional[int] = ...) -> None: ...

class DmSegSDKReply(_message.Message):
    __slots__ = ("closed", "elems")
    CLOSED_FIELD_NUMBER: _ClassVar[int]
    ELEMS_FIELD_NUMBER: _ClassVar[int]
    closed: bool
    elems: _containers.RepeatedCompositeFieldContainer[DanmakuElem]
    def __init__(self, closed: bool = ..., elems: _Optional[_Iterable[_Union[DanmakuElem, _Mapping]]] = ...) -> None: ...

class DmSegSDKReq(_message.Message):
    __slots__ = ("pid", "oid", "type", "segment_index")
    PID_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    pid: int
    oid: int
    type: int
    segment_index: int
    def __init__(self, pid: _Optional[int] = ..., oid: _Optional[int] = ..., type: _Optional[int] = ..., segment_index: _Optional[int] = ...) -> None: ...

class DmViewReply(_message.Message):
    __slots__ = ("closed", "mask", "subtitle", "special_dms", "ai_flag", "player_config", "send_box_style", "allow", "check_box", "check_box_show_msg", "text_placeholder", "input_placeholder", "report_filter_content", "expo_report", "buzzword_config", "expressions", "post_panel", "activity_meta", "post_panel2")
    CLOSED_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_DMS_FIELD_NUMBER: _ClassVar[int]
    AI_FLAG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEND_BOX_STYLE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
    CHECK_BOX_SHOW_MSG_FIELD_NUMBER: _ClassVar[int]
    TEXT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    INPUT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    REPORT_FILTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPO_REPORT_FIELD_NUMBER: _ClassVar[int]
    BUZZWORD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    POST_PANEL_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_META_FIELD_NUMBER: _ClassVar[int]
    POST_PANEL2_FIELD_NUMBER: _ClassVar[int]
    closed: bool
    mask: VideoMask
    subtitle: VideoSubtitle
    special_dms: _containers.RepeatedScalarFieldContainer[str]
    ai_flag: DanmakuFlagConfig
    player_config: DanmuPlayerViewConfig
    send_box_style: int
    allow: bool
    check_box: str
    check_box_show_msg: str
    text_placeholder: str
    input_placeholder: str
    report_filter_content: _containers.RepeatedScalarFieldContainer[str]
    expo_report: ExpoReport
    buzzword_config: BuzzwordConfig
    expressions: _containers.RepeatedCompositeFieldContainer[Expressions]
    post_panel: _containers.RepeatedCompositeFieldContainer[PostPanel]
    activity_meta: _containers.RepeatedScalarFieldContainer[str]
    post_panel2: _containers.RepeatedCompositeFieldContainer[PostPanelV2]
    def __init__(self, closed: bool = ..., mask: _Optional[_Union[VideoMask, _Mapping]] = ..., subtitle: _Optional[_Union[VideoSubtitle, _Mapping]] = ..., special_dms: _Optional[_Iterable[str]] = ..., ai_flag: _Optional[_Union[DanmakuFlagConfig, _Mapping]] = ..., player_config: _Optional[_Union[DanmuPlayerViewConfig, _Mapping]] = ..., send_box_style: _Optional[int] = ..., allow: bool = ..., check_box: _Optional[str] = ..., check_box_show_msg: _Optional[str] = ..., text_placeholder: _Optional[str] = ..., input_placeholder: _Optional[str] = ..., report_filter_content: _Optional[_Iterable[str]] = ..., expo_report: _Optional[_Union[ExpoReport, _Mapping]] = ..., buzzword_config: _Optional[_Union[BuzzwordConfig, _Mapping]] = ..., expressions: _Optional[_Iterable[_Union[Expressions, _Mapping]]] = ..., post_panel: _Optional[_Iterable[_Union[PostPanel, _Mapping]]] = ..., activity_meta: _Optional[_Iterable[str]] = ..., post_panel2: _Optional[_Iterable[_Union[PostPanelV2, _Mapping]]] = ...) -> None: ...

class DmViewReq(_message.Message):
    __slots__ = ("pid", "oid", "type", "spmid", "is_hard_boot")
    PID_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SPMID_FIELD_NUMBER: _ClassVar[int]
    IS_HARD_BOOT_FIELD_NUMBER: _ClassVar[int]
    pid: int
    oid: int
    type: int
    spmid: str
    is_hard_boot: int
    def __init__(self, pid: _Optional[int] = ..., oid: _Optional[int] = ..., type: _Optional[int] = ..., spmid: _Optional[str] = ..., is_hard_boot: _Optional[int] = ...) -> None: ...

class DmWebViewReply(_message.Message):
    __slots__ = ("state", "text", "text_side", "dm_sge", "flag", "special_dms", "check_box", "count", "commandDms", "player_config", "report_filter_content", "expressions", "post_panel", "activity_meta")
    STATE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TEXT_SIDE_FIELD_NUMBER: _ClassVar[int]
    DM_SGE_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_DMS_FIELD_NUMBER: _ClassVar[int]
    CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDDMS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REPORT_FILTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    POST_PANEL_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_META_FIELD_NUMBER: _ClassVar[int]
    state: int
    text: str
    text_side: str
    dm_sge: DmSegConfig
    flag: DanmakuFlagConfig
    special_dms: _containers.RepeatedScalarFieldContainer[str]
    check_box: bool
    count: int
    commandDms: _containers.RepeatedCompositeFieldContainer[CommandDm]
    player_config: DanmuWebPlayerConfig
    report_filter_content: _containers.RepeatedScalarFieldContainer[str]
    expressions: _containers.RepeatedCompositeFieldContainer[Expressions]
    post_panel: _containers.RepeatedCompositeFieldContainer[PostPanel]
    activity_meta: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, state: _Optional[int] = ..., text: _Optional[str] = ..., text_side: _Optional[str] = ..., dm_sge: _Optional[_Union[DmSegConfig, _Mapping]] = ..., flag: _Optional[_Union[DanmakuFlagConfig, _Mapping]] = ..., special_dms: _Optional[_Iterable[str]] = ..., check_box: bool = ..., count: _Optional[int] = ..., commandDms: _Optional[_Iterable[_Union[CommandDm, _Mapping]]] = ..., player_config: _Optional[_Union[DanmuWebPlayerConfig, _Mapping]] = ..., report_filter_content: _Optional[_Iterable[str]] = ..., expressions: _Optional[_Iterable[_Union[Expressions, _Mapping]]] = ..., post_panel: _Optional[_Iterable[_Union[PostPanel, _Mapping]]] = ..., activity_meta: _Optional[_Iterable[str]] = ...) -> None: ...

class ExpoReport(_message.Message):
    __slots__ = ("should_report_at_end",)
    SHOULD_REPORT_AT_END_FIELD_NUMBER: _ClassVar[int]
    should_report_at_end: bool
    def __init__(self, should_report_at_end: bool = ...) -> None: ...

class Expression(_message.Message):
    __slots__ = ("keyword", "url", "period")
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    keyword: _containers.RepeatedScalarFieldContainer[str]
    url: str
    period: _containers.RepeatedCompositeFieldContainer[Period]
    def __init__(self, keyword: _Optional[_Iterable[str]] = ..., url: _Optional[str] = ..., period: _Optional[_Iterable[_Union[Period, _Mapping]]] = ...) -> None: ...

class Expressions(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Expression]
    def __init__(self, data: _Optional[_Iterable[_Union[Expression, _Mapping]]] = ...) -> None: ...

class InlinePlayerDanmakuSwitch(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class Label(_message.Message):
    __slots__ = ("title", "content")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, title: _Optional[str] = ..., content: _Optional[_Iterable[str]] = ...) -> None: ...

class LabelV2(_message.Message):
    __slots__ = ("title", "content", "exposure_once", "exposure_type")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: _containers.RepeatedScalarFieldContainer[str]
    exposure_once: bool
    exposure_type: int
    def __init__(self, title: _Optional[str] = ..., content: _Optional[_Iterable[str]] = ..., exposure_once: bool = ..., exposure_type: _Optional[int] = ...) -> None: ...

class Period(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class PlayerDanmakuAiRecommendedLevel(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuAiRecommendedLevelV2(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class PlayerDanmakuAiRecommendedSwitch(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockbottom(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockcolorful(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockrepeat(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockscroll(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockspecial(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlocktop(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuDomain(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class PlayerDanmakuEnableblocklist(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuOpacity(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class PlayerDanmakuScalingfactor(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class PlayerDanmakuSeniorModeSwitch(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class PlayerDanmakuSpeed(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class PlayerDanmakuSwitch(_message.Message):
    __slots__ = ("value", "can_ignore")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CAN_IGNORE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    can_ignore: bool
    def __init__(self, value: bool = ..., can_ignore: bool = ...) -> None: ...

class PlayerDanmakuSwitchSave(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuUseDefaultConfig(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class PostPanel(_message.Message):
    __slots__ = ("start", "end", "priority", "biz_id", "biz_type", "click_button", "text_input", "check_box", "toast")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    BIZ_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLICK_BUTTON_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
    TOAST_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    priority: int
    biz_id: int
    biz_type: PostPanelBizType
    click_button: ClickButton
    text_input: TextInput
    check_box: CheckBox
    toast: Toast
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., priority: _Optional[int] = ..., biz_id: _Optional[int] = ..., biz_type: _Optional[_Union[PostPanelBizType, str]] = ..., click_button: _Optional[_Union[ClickButton, _Mapping]] = ..., text_input: _Optional[_Union[TextInput, _Mapping]] = ..., check_box: _Optional[_Union[CheckBox, _Mapping]] = ..., toast: _Optional[_Union[Toast, _Mapping]] = ...) -> None: ...

class PostPanelV2(_message.Message):
    __slots__ = ("start", "end", "biz_type", "click_button", "text_input", "check_box", "toast", "bubble", "label", "post_status")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    BIZ_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLICK_BUTTON_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
    TOAST_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    POST_STATUS_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    biz_type: int
    click_button: ClickButtonV2
    text_input: TextInputV2
    check_box: CheckBoxV2
    toast: ToastV2
    bubble: BubbleV2
    label: LabelV2
    post_status: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., biz_type: _Optional[int] = ..., click_button: _Optional[_Union[ClickButtonV2, _Mapping]] = ..., text_input: _Optional[_Union[TextInputV2, _Mapping]] = ..., check_box: _Optional[_Union[CheckBoxV2, _Mapping]] = ..., toast: _Optional[_Union[ToastV2, _Mapping]] = ..., bubble: _Optional[_Union[BubbleV2, _Mapping]] = ..., label: _Optional[_Union[LabelV2, _Mapping]] = ..., post_status: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class SubtitleItem(_message.Message):
    __slots__ = ("id", "id_str", "lan", "lan_doc", "subtitle_url", "author", "type", "lan_doc_brief", "ai_type", "ai_status")
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_STR_FIELD_NUMBER: _ClassVar[int]
    LAN_FIELD_NUMBER: _ClassVar[int]
    LAN_DOC_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LAN_DOC_BRIEF_FIELD_NUMBER: _ClassVar[int]
    AI_TYPE_FIELD_NUMBER: _ClassVar[int]
    AI_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    id_str: str
    lan: str
    lan_doc: str
    subtitle_url: str
    author: UserInfo
    type: SubtitleType
    lan_doc_brief: str
    ai_type: SubtitleAiType
    ai_status: SubtitleAiStatus
    def __init__(self, id: _Optional[int] = ..., id_str: _Optional[str] = ..., lan: _Optional[str] = ..., lan_doc: _Optional[str] = ..., subtitle_url: _Optional[str] = ..., author: _Optional[_Union[UserInfo, _Mapping]] = ..., type: _Optional[_Union[SubtitleType, str]] = ..., lan_doc_brief: _Optional[str] = ..., ai_type: _Optional[_Union[SubtitleAiType, str]] = ..., ai_status: _Optional[_Union[SubtitleAiStatus, str]] = ...) -> None: ...

class TextInput(_message.Message):
    __slots__ = ("portrait_placeholder", "landscape_placeholder", "render_type", "placeholder_post", "show", "avatar", "post_status", "label")
    PORTRAIT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_POST_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    POST_STATUS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    portrait_placeholder: _containers.RepeatedScalarFieldContainer[str]
    landscape_placeholder: _containers.RepeatedScalarFieldContainer[str]
    render_type: RenderType
    placeholder_post: bool
    show: bool
    avatar: _containers.RepeatedCompositeFieldContainer[Avatar]
    post_status: PostStatus
    label: Label
    def __init__(self, portrait_placeholder: _Optional[_Iterable[str]] = ..., landscape_placeholder: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., placeholder_post: bool = ..., show: bool = ..., avatar: _Optional[_Iterable[_Union[Avatar, _Mapping]]] = ..., post_status: _Optional[_Union[PostStatus, str]] = ..., label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...

class TextInputV2(_message.Message):
    __slots__ = ("portrait_placeholder", "landscape_placeholder", "render_type", "placeholder_post", "avatar", "text_input_limit")
    PORTRAIT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_POST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    portrait_placeholder: _containers.RepeatedScalarFieldContainer[str]
    landscape_placeholder: _containers.RepeatedScalarFieldContainer[str]
    render_type: RenderType
    placeholder_post: bool
    avatar: _containers.RepeatedCompositeFieldContainer[Avatar]
    text_input_limit: int
    def __init__(self, portrait_placeholder: _Optional[_Iterable[str]] = ..., landscape_placeholder: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., placeholder_post: bool = ..., avatar: _Optional[_Iterable[_Union[Avatar, _Mapping]]] = ..., text_input_limit: _Optional[int] = ...) -> None: ...

class Toast(_message.Message):
    __slots__ = ("text", "duration", "show", "button")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    text: str
    duration: int
    show: bool
    button: Button
    def __init__(self, text: _Optional[str] = ..., duration: _Optional[int] = ..., show: bool = ..., button: _Optional[_Union[Button, _Mapping]] = ...) -> None: ...

class ToastButtonV2(_message.Message):
    __slots__ = ("text", "action")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    text: str
    action: int
    def __init__(self, text: _Optional[str] = ..., action: _Optional[int] = ...) -> None: ...

class ToastV2(_message.Message):
    __slots__ = ("text", "duration", "toast_button_v2")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TOAST_BUTTON_V2_FIELD_NUMBER: _ClassVar[int]
    text: str
    duration: int
    toast_button_v2: ToastButtonV2
    def __init__(self, text: _Optional[str] = ..., duration: _Optional[int] = ..., toast_button_v2: _Optional[_Union[ToastButtonV2, _Mapping]] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("mid", "name", "sex", "face", "sign", "rank")
    MID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    SIGN_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    mid: int
    name: str
    sex: str
    face: str
    sign: str
    rank: int
    def __init__(self, mid: _Optional[int] = ..., name: _Optional[str] = ..., sex: _Optional[str] = ..., face: _Optional[str] = ..., sign: _Optional[str] = ..., rank: _Optional[int] = ...) -> None: ...

class VideoMask(_message.Message):
    __slots__ = ("cid", "plat", "fps", "time", "mask_url")
    CID_FIELD_NUMBER: _ClassVar[int]
    PLAT_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    MASK_URL_FIELD_NUMBER: _ClassVar[int]
    cid: int
    plat: int
    fps: int
    time: int
    mask_url: str
    def __init__(self, cid: _Optional[int] = ..., plat: _Optional[int] = ..., fps: _Optional[int] = ..., time: _Optional[int] = ..., mask_url: _Optional[str] = ...) -> None: ...

class VideoSubtitle(_message.Message):
    __slots__ = ("lan", "lanDoc", "subtitles")
    LAN_FIELD_NUMBER: _ClassVar[int]
    LANDOC_FIELD_NUMBER: _ClassVar[int]
    SUBTITLES_FIELD_NUMBER: _ClassVar[int]
    lan: str
    lanDoc: str
    subtitles: _containers.RepeatedCompositeFieldContainer[SubtitleItem]
    def __init__(self, lan: _Optional[str] = ..., lanDoc: _Optional[str] = ..., subtitles: _Optional[_Iterable[_Union[SubtitleItem, _Mapping]]] = ...) -> None: ...
