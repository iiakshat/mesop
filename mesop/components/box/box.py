from typing import Any, Callable

from pydantic import validate_arguments

import mesop.components.box.box_pb2 as box_pb
from mesop.component_helpers import (
  insert_composite_component,
  register_event_handler,
)
from mesop.events import ClickEvent


@validate_arguments
def box(
  *,
  style: str = "",
  on_click: Callable[[ClickEvent], Any] | None = None,
  key: str | None = None,
):
  """
  This function creates a box.

  Args:
      style: Style to apply to component. Follows [HTML Element inline style API](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style).
  """
  return insert_composite_component(
    key=key,
    type_name="box",
    proto=box_pb.BoxType(
      style=style,
      on_click_handler_id=register_event_handler(on_click, event=ClickEvent)
      if on_click
      else "",
    ),
  )
