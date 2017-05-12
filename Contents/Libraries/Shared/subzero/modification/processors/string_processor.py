# coding=utf-8

import logging

from subzero.modification.processors import Processor

logger = logging.getLogger(__name__)


class StringProcessor(Processor):
    """
    String replacement processor base
    """

    def __init__(self, search, replace, name=None, parent=None):
        super(StringProcessor, self).__init__(name=name)
        self.search = search
        self.replace = replace

    def process(self, content, debug=False):
        return content.replace(self.search, self.replace)


class MultipleLineProcessor(Processor):
    """
    replaces stuff in whole lines
    
    takes a search/replace dict as first argument
    Expects a dictionary in the form of:
    dict = {
        "data": {"old_value": "new_value"}
    }
    """
    def __init__(self, snr_dict, name=None, parent=None):
        super(MultipleLineProcessor, self).__init__(name=name)
        self.snr_dict = snr_dict

    def process(self, content, debug=False):
        if not self.snr_dict["data"]:
            return content

        out = []
        for cnt in content.split(ur"\N"):
            cnt_ = cnt
            for key, value in self.snr_dict["data"].iteritems():
                if debug and key in cnt_:
                    logger.debug(u"Replacing '%s' with '%s' in '%s'", key, value, cnt_)

                cnt_ = cnt_.replace(key, value)
            out.append(cnt_)

        return ur"\N".join(out)


class WholeLineProcessor(MultipleLineProcessor):
    def process(self, content, debug=False):
        if not self.snr_dict["data"]:
            return content
        content = content.strip()

        for key, value in self.snr_dict["data"].iteritems():
            if content == key:
                if debug:
                    logger.debug(u"Replacing '%s' with '%s'", key, value)

                content = value
                break

        return content


class MultipleWordProcessor(MultipleLineProcessor):
    """
    replaces words

    takes a search/replace dict as first argument
    Expects a dictionary in the form of:
    dict = {
        "data": {"old_value": "new_value"}
    }
    """
    def process(self, content, debug=False):
        new_lines = []
        for line in content.split(u"\\N"):
            words = line.split(u" ")
            new_words = []
            for word in words:
                new_words.append(self.snr_dict.get(word, word))

            new_lines.append(u" ".join(new_words))

        return u"\\N".join(new_lines)