from cooptools.matrixManipulation import point_transform_3d, scaled_array
from coopstructs.geometry import Line
import pygame
import numpy as np
from typing import List, Dict
from dataclasses import dataclass
from cooptools.colors import Color
import coopgame.pointdrawing.point_draw_utils as putils

@dataclass(frozen=True)
class DrawLineArgs:
    color: Color = None
    width: int = None
    control_point_args: putils.DrawPointArgs = None

    @property
    def BaseArgs(self):
        return DrawLineArgs(
            color=self.color,
            width=self.width
        )

def draw_lines(lines: Dict[Line, DrawLineArgs],
               surface: pygame.Surface,
               draw_scale_matrix: None):
    for line, args in lines.items():
        if args is None:
            continue

        # Convert Origin/Destination into np.arrays
        origin = np.array([line.origin[0], line.origin[1], 0, 1])
        destination = np.array([line.destination[0], line.destination[1], 0, 1])

        # Translate the points via the scaling matrix
        scaled = scaled_array(
            lst_point_array=np.array([origin, destination]),
            lh_matrix=draw_scale_matrix
        )

        # Draw the lines
        if args.color:
            w = args.width if args.width is not None else 1
            pygame.draw.line(surface,
                             args.color.value,
                             (scaled[0][0], scaled[0][1]),
                             (scaled[1][0], scaled[1][1]),
                             width=w)

        # Draw the points
        if args.control_point_args:
            putils.draw_points(
                points={
                    (x[0], x[1]): args.control_point_args for x in scaled
                },
                surface=surface,
                draw_scale_matrix=draw_scale_matrix
            )
