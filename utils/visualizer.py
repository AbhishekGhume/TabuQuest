import plotly.express as px
import pandas as pd
from typing import Optional

class Visualizer:
    @staticmethod
    def custom_visualize(data, x_axis: str, y_axis: Optional[str] = None, chart_type: str = "scatter"):
        """Create visualization based on user-selected axes and chart type"""
        try:
            if isinstance(data, pd.Series):
                data = data.to_frame()

            if len(data) == 0:
                return None

            # Validate columns
            if x_axis not in data.columns:
                raise ValueError(f"Column '{x_axis}' not found in data")
            if y_axis and y_axis not in data.columns:
                raise ValueError(f"Column '{y_axis}' not found in data")

            # Create visualization based on chart type
            if chart_type == "scatter":
                return px.scatter(data, x=x_axis, y=y_axis) if y_axis else px.scatter(data, x=x_axis)
            elif chart_type == "line":
                return px.line(data, x=x_axis, y=y_axis) if y_axis else px.line(data, x=x_axis)
            elif chart_type == "bar":
                return px.bar(data, x=x_axis, y=y_axis) if y_axis else px.bar(data, x=x_axis)
            elif chart_type == "histogram":
                return px.histogram(data, x=x_axis)
            elif chart_type == "box":
                return px.box(data, x=x_axis, y=y_axis) if y_axis else px.box(data, x=x_axis)
            else:
                raise ValueError(f"Unsupported chart type: {chart_type}")
        except Exception as e:
            raise RuntimeError(f"Custom visualization failed: {str(e)}")