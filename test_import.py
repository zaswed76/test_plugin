#!/usr/bin/env python
# -*- coding: utf-8 -*-


from importlib import import_module

path = "plugins.game1.game"


mod = import_module(path)
obj = getattr(mod, "GamePlugin")

print(obj)
# met = getattr(mod, m)

# met()