"""
Module with the player structures.
"""

from typing import List

from pygame import Rect
from pygame import Surface

from src.inputs import CapturedInput


class Player:

    _rect: Rect  # contains (x, y) coordinates
    _image: Surface
    _moving_right: bool
    _moving_left: bool
    _speed: List[int]
    _gravity: int

    def __init__(self, x: float, y: float, image: Surface) -> None:
        self._rect = Rect(x, y, image.get_width(), image.get_height())
        self._speed = [0, 0]
        self._image = image
        self._moving_left = False
        self._moving_right = False
        self._gravity = 2

    @property
    def rect(self) -> Rect:
        return self._rect

    @property
    def speed(self) -> List[int]:
        return self._speed

    @property
    def image(self) -> Surface:
        return self._image

    def update(self, captured_inputs: CapturedInput) -> None:
        if captured_inputs.moving_right or captured_inputs.moving_right_stop:
            self._moving_right = not captured_inputs.moving_right_stop

        if captured_inputs.moving_left or captured_inputs.moving_left_stop:
            self._moving_left = not captured_inputs.moving_left_stop

        # speed resetting: allows the player to immediately stop once the key is released
        # if not reset: gives the 'sliding on ice' sensation
        self._speed = [0, 0]

        # x axis
        if self._moving_right:
            self._speed[0] += 2

        if self._moving_left:
            self._speed[0] -= 2

        # y axis: always updated as gravity always drags down
        self._speed[1] += self._gravity

        if self._speed[1] > 3:  # clamping
            self._speed[1] = 3
