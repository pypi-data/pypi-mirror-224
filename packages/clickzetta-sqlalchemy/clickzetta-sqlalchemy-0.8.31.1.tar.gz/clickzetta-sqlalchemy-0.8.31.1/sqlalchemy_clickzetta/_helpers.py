import functools
import re

import sqlalchemy
import base64
import json
from clickzetta.client import Client
from clickzetta.enums import LoginParams

USER_AGENT_TEMPLATE = "sqlalchemy/{}"


def create_clickzetta_client(
        username=None,
        password=None,
        instance=None,
        workspace=None,
        vcluster=None,
        service=None,
        schema=None,

):

    return Client(
        username=username,
        password=password,
        workspace=workspace,
        instance=instance,
        vcluster=vcluster,
        service=service,
        schema=schema,
    )


def substitute_re_method(r, flags=0, repl=None):
    if repl is None:
        return lambda f: substitute_re_method(r, flags, f)

    r = re.compile(r, flags)

    @functools.wraps(repl)
    def sub(self, s, *args, **kw):
        def repl_(m):
            return repl(self, m, *args, **kw)

        return r.sub(repl_, s)

    return sub


def substitute_string_re_method(r, *, repl, flags=0):
    r = re.compile(r, flags)
    return lambda self, s: r.sub(repl, s)
