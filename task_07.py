#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""

import task_06

WORDS = task_06.WORDS
if 'granaries' in WORDS:
    GRANARIES_EXIST = "True"
else:
    GRANARIES_EXIST = "NOT True"
print GRANARIES_EXIST
