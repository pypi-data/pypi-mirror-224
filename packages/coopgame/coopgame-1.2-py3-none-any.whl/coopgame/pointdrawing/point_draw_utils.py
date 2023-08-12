from cooptools.matrixManipulation import point_transform_3d, scaled_array
import pygame
import numpy as np
from typing import List, Dict, Tuple
from dataclasses import dataclass
from cooptools.colors import Color


@dataclass(frozen=True)
class DrawPointArgs:
    color: Color = None
    outline_color: Color = None
    radius: int = None
    outline_width: int = None

def draw_points(points: Dict[Tuple[int, int], DrawPointArgs],
               surface: pygame.Surface,
               draw_scale_matrix: np.ndarray = None):

    pt_args = [(k, v) for k, v in points.items()]

    # Translate the points via the scaling matrix
    scaled = point_transform_3d(
        points=[x[0] for x in pt_args],
        lh_matrix=draw_scale_matrix
    )

    for ii, x in enumerate(pt_args):
        args = x[1]
        if args.color:
            pygame.draw.circle(surface,
                               args.color.value,
                               center=scaled[ii][:2],
                               radius=args.radius,
                               )

        if args.outline_color:
            olw = args.outline_width if args.outline_width is not None else 1
            pygame.draw.circle(surface,
                               args.outline_color.value,
                               center=scaled[ii][:2],
                               width=olw,
                               radius=args.radius,
                               )