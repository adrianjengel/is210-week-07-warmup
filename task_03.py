#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK7 warmup task_03 - testing mutability."""

import data

DIRECTIONS = data.DIRECTIONS

DIRECTIONS = DIRECTIONS[:3] + ('West',)
