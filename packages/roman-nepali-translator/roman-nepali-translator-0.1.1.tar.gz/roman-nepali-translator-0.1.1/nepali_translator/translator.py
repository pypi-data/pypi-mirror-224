from dataclasses import dataclass
from typing import List, TypeVar, Tuple

from mappings import (
    get_mappings,
    consonant_kaars,
    get_word_maps,
    Mappings,
    amkaar,
    aNNkaar,
    Ri,
)


@dataclass
class State:
    remaining: str = ''
    consumed: str = ''
    processed: str = ''
    as_is: bool = False

    def copy(self, **kwargs):
        return State(self.remaining, self.consumed, self.processed, **kwargs)


class Converter:
    def __init__(self):
        self.mappings = get_mappings()
        self.word_maps = get_word_maps()

    def consume(self, state: State) -> State:
        current = state.remaining
        consumed = state.consumed
        processed = state.processed

        if state.as_is:
            if current[0] == '}':
                return State(current[1:], consumed + current[:1], processed, False)
            else:
                return State(current[1:], consumed + current[0], processed + current[0], True)

        # Handle escape sequences
        if current.startswith('{{'):
            return State(current[2:], consumed + current[:2], processed + '{')
        if current.startswith('{'):
            return State(current[1:], consumed + current[:1], processed, True)

        # Check if word is in direct word mappings
        direct_mapping = self.word_maps.get(current)
        if direct_mapping:
            return State(current[len(direct_mapping):], consumed + current[:len(direct_mapping)], processed + direct_mapping)

        # Handle amkaar and aaNkar
        if current.startswith('M'):
            return State(current[1:], consumed + current[0], processed + amkaar)
        if current.startswith('NN'):
            return State(current[2:], consumed + current[:2], processed + aNNkaar)

        # Special case for Ri and Ree
        if current.startswith('RI'):
            if consumed[-1] != 'a':
                return State(current[2:], consumed + current[:2], processed[:-1] + Ri)
            else:
                return State(current[2:], consumed + current[:2], processed + Ri)

        # Handle other mappings
        for k, v in self.mappings.items():
            if current.startswith(k):
                return State(current[len(k):], consumed + current[:len(k)], processed + v)

        # Default case
        return State(current[1:], consumed + current[0], processed + current[0])

    def convert(self, text: str) -> str:
        if not text:
            return text
        state = State(text)
        while state.remaining:
            state = self.consume(state)
        return state.processed
