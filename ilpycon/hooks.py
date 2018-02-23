import markdown


class BoxesHookSet(object):

    def parse_content(self, content):
        return markdown.markdown(content)
