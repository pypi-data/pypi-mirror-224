#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from string import Template
from urllib import request
import urllib.error

# --- Http post with json payload ----

class webhook_error(Exception):
    pass

class webhook_post:
    def __init__(self, a_sURL):
        self.sURL = a_sURL
    # Not fancy, but should work for MS Teams

    # Fill in template with values from dictionary and post it
    def post_template(self, a_sMsgTemplateFile, a_tMsgTemplateDict):
        try:
            with open(a_sMsgTemplateFile, 'r') as f:
                tpl = Template(f.read())
                msg = tpl.safe_substitute(a_tMsgTemplateDict)
                self.post( msg)
        except OSError as e:
               raise webhook_error(f'Could not read template file {f}: {str(e)}')

    # Simple html formatting: bold caption, unmodified body
    def post_formatted(self, a_sCaption, a_sBody):
        sMsg = f'<h2><strong>{a_sCaption}</strong></h2><br>{a_sBody}'
        self.post(sMsg)

    # Base function, post raw message
    def post(self, a_sMsg):
        post = request.Request(url=self.sURL, method="POST")
        post.add_header(key="Content-Type", val="application/json")
        try:
            with request.urlopen(url = post, data = json.dumps({"text": a_sMsg}).encode() ) as response:
                if response.status != 200:
                    raise webhook_error("Error response from receiver: " + response.reason)
        except urllib.error.URLError as e:
            raise webhook_error("Could not send HTTP POST: " + str(e))
