#!/usr/bin/python3
class Lockedclass:
    def __slots__ = ("first_name",)

    def __init__(self, first_name=""):
        self.first_name = first_name
