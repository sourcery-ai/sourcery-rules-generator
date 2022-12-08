from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO


class MyYAML(YAML):
    def dumps(self, data, stream=None, **kw):
        inefficient = False
        if stream is None:
            inefficient = True
            stream = StringIO()
        YAML.dump(self, data, stream, **kw)
        if inefficient:
            return stream.getvalue()


def dumps(obj) -> str:
    yaml = MyYAML()  # or typ='safe'/'unsafe' etc
    return yaml.dumps(obj)
