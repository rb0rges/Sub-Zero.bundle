# coding=utf-8

import re

from subzero.modification.mods import SubtitleTextModification
from subzero.modification.processors.string_processor import StringProcessor
from subzero.modification.processors.re_processor import NReProcessor
from subzero.modification import registry


class CommonFixes(SubtitleTextModification):
    identifier = "common"
    description = "Basic common fixes"
    exclusive = True

    long_description = """\
    Fixes common whitespace/punctuation issues in subtitles
    """

    processors = [
        # no space after ellipsis
        NReProcessor(re.compile(r'(?u)\.\.\.(?![\s.,!?\'"])(?!$)'), "... ", name="CM_ellipsis_no_space"),

        # multiple spaces
        NReProcessor(re.compile(r'(?u)[\s]{2,}'), " ", name="CM_multiple_spaces"),

        # no space after starting dash
        NReProcessor(re.compile(r'(?u)^-(?![\s-])'), "- ", name="CM_dash_space"),

        # '' = "
        StringProcessor("''", '"', name="CM_double_apostrophe"),

        # space missing before doublequote
        #ReProcessor(re.compile(r'(?u)(?<!^)(?<![\s(\["])("[^"]+")'), r' \1', name="CM_space_before_dblquote"),

        # space missing after doublequote
        #ReProcessor(re.compile(r'(?u)("[^"\s][^"]+")([^\s.,!?)\]]+)'), r"\1 \2", name="CM_space_after_dblquote"),

        # space before ending doublequote?

        # -- = ...
        StringProcessor("-- ", '... ', name="CM_doubledash"),

        # remove >>
        NReProcessor(re.compile(r'(?u)^>>[\s]*'), "", name="CM_leading_crocodiles"),

        # remove leading ...
        NReProcessor(re.compile(r'(?u)^\.\.\.[\s]*'), "", name="CM_leading_ellipsis"),

        # replace uppercase I with lowercase L in words
        NReProcessor(re.compile(r'(?u)([A-z]+)I([a-z]+)'), r"\1l\2", name="CM_uppercase_i_in_word"),

        # fix spaces in numbers
        NReProcessor(re.compile(r'(?u)([0-9]+)[\s]+([0-9:.]*[0-9]+)'), r"\1\2", name="CM_spaces_in_numbers"),
    ]


registry.register(CommonFixes)