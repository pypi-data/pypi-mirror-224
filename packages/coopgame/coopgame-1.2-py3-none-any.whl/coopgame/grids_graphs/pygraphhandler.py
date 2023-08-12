from coopgame.colors import Color
import pygame
from coopgraph.graphs import Graph
import coopgame.pygamehelpers as help
from typing import List
import coopgame.grids_graphs.draw_graph_utils as utils
from cooptools.coopEnum import CoopEnum
from coopgame.surfaceManager import SurfaceManager, SurfaceDrawCallback

class GraphSurfaceType(CoopEnum):
    EDGES_SURFACE_ID = 'EDGES_SURFACE_ID'
    NODES_SURFACE_ID = 'NODES_SURFACE_ID'
    NODE_LABELS_SURFACE_ID = 'NODE_LABELS_SURFACE_ID'
    EDGE_LABELS_SURFACE_ID = 'EDGE_LABELS_SURFACE_ID'
    OVERLAY_SURFACE_ID = 'OVERLAY_SURFACE_ID'

class PyGraphHandler:
    def __init__(self,
                 screen: pygame.Surface,
                 graph: Graph,
                 draw_config: utils.GraphDrawArgs = None):
        self.parent_screen = screen
        self.graph = graph
        self._draw_config: utils.GraphDrawArgs = draw_config if draw_config else utils.GraphDrawArgs(
            coordinate_converter= lambda x: x,
            node_color= Color.DARK_BLUE,
            node_radius= 3,
            enabled_edge_color= Color.ORANGE,
            disabled_edge_color= Color.BROWN,
            node_label_color= Color.WHEAT,
            edge_label_color= Color.WHEAT,
            articulation_points_color= Color.PURPLE,
            directionality_indicators_color= Color.GREEN
        )

        self.surface_manager = SurfaceManager(
            surface_draw_callbacks=[
                SurfaceDrawCallback(GraphSurfaceType.EDGES_SURFACE_ID.value, self.redraw_edges_surface),
                SurfaceDrawCallback(GraphSurfaceType.NODES_SURFACE_ID.value, self.redraw_nodes_surface),
                SurfaceDrawCallback(GraphSurfaceType.NODE_LABELS_SURFACE_ID.value, self.redraw_edge_labels_surface),
                SurfaceDrawCallback(GraphSurfaceType.EDGE_LABELS_SURFACE_ID.value, self.redraw_node_labels_surface),
                SurfaceDrawCallback(GraphSurfaceType.OVERLAY_SURFACE_ID.value, self.redraw_overlay_surface),
            ]
        )

    def set_config(self,
                   draw_config: utils.GraphDrawArgs):
        self._draw_config = draw_config

    def redraw_edges_surface(self):
        surf = help.init_surface(self.parent_screen.get_size())
        utils.draw_to_surface(
            surface=surf,
            graph=self.graph,
            enabled_edge_color=self._draw_config.enabled_edge_color,
            disabled_edge_color=self._draw_config.disabled_edge_color,
        )
        return surf

    def redraw_nodes_surface(self):
        surf = help.init_surface(self.parent_screen.get_size())
        utils.draw_to_surface(
            surface=surf,
            graph=self.graph,
            node_color=self._draw_config.node_color,
            node_radius=self._draw_config.node_radius
        )
        return surf

    def redraw_node_labels_surface(self):
        surf = help.init_surface(self.parent_screen.get_size())
        utils.draw_to_surface(
            surface=surf,
            graph=self.graph,
            node_label_color=self._draw_config.node_label_color
        )
        return surf

    def redraw_edge_labels_surface(self):
        surf = help.init_surface(self.parent_screen.get_size())
        utils.draw_to_surface(
            surface=surf,
            graph=self.graph,
            edge_label_color=self._draw_config.edge_label_color
        )
        return surf

    def redraw_overlay_surface(self):
        surf = help.init_surface(self.parent_screen.get_size())
        utils.draw_to_surface(
            surface=surf,
            graph=self.graph,
            articulation_points_color=self._draw_config.articulation_points_color,
            directionality_indicators_color=self._draw_config.directionality_indicators_color,
            directionality_indicator_size=self._draw_config.directionality_indicators_size
        )
        return surf

    def update(self):
        # No surfaces require redrawing every iteration
        pass

    def redraw(self):
        self.surface_manager.redraw([x.name for x in GraphSurfaceType])

    def render(self,
               surface: pygame.Surface):
        self.update()
        self.surface_manager.render(surface)

    def toggle_surface(self, graphSurfaceTypes: List[GraphSurfaceType]):
        self.surface_manager.toggle_visible([x.value for x in graphSurfaceTypes])

    def show_all(self):
        self.surface_manager.show_all()

    def hide_all(self):
        self.surface_manager.hide_all()
