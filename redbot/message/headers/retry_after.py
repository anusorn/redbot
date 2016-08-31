#!/usr/bin/env python


import redbot.message.headers as headers
from redbot.speak import Note, c as categories, l as levels
from redbot.message.headers import HttpHeader, HeaderTest
from redbot.syntax import rfc7231

class retry_after(HttpHeader):
  canonical_name = u"Retry-after"
  description = u"""\
The `Retry-After` header can be used with a `503 Service Unavailable` response to indicate how long
the service is expected to be unavailable to the requesting client.

The value of this field can be either a date or an integer number of seconds."""
  reference = u"%s#header.retry-after" % rfc7231.SPEC_URL
  syntax = rfc7231.Retry_After
  list_header = False
  deprecated = False
  valid_in_requests = False
  valid_in_responses = True
