import concurrent
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional

import typer
from google.protobuf.json_format import MessageToDict

from ascend_io_cli.support import get_client, print_response, COMPONENT_PAUSE_METHODS

app = typer.Typer(help='Pause component execution optionally filtered by state', no_args_is_help=True)


@app.command()
def component(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id containing the component to pause', show_default=False),
    dataflow_id: str = typer.Argument(..., help='Dataflow id containing the component to pause', show_default=False),
    component_id: List[str] = typer.Argument(..., help='List of component ids to pause', show_default=False),
    state: Optional[List[str]] = typer.Option([], help='List of states of components to pause (uptodate, running, outofdate, error)'),
):
  """Pause a list of components"""
  pause_resume_components(ctx, True, data_service_id, dataflow_id, component_id, state)


@app.command()
def dataflow(
    ctx: typer.Context,
    data_service_id: str = typer.Argument(..., help='Data Service id containing dataflow to pause', show_default=False),
    dataflow_id: str = typer.Argument(..., help='Dataflow id to pause all components', show_default=False),
    state: Optional[List[str]] = typer.Option([], help='List of states of components to pause (uptodate, running, outofdate, error)'),
):
  """Pause all components in a dataflow"""
  pause_resume_components(ctx, True, data_service_id, dataflow_id, [], state)


def pause_resume_components(ctx: typer.Context, pause_flag: bool, service_id: str, flow_id: str, component_id: List[str], state: List[str]):
  client = get_client(ctx)

  def _pause_resume(target_component, pause: bool):
    if COMPONENT_PAUSE_METHODS.get(target_component.type, None):
      return getattr(client, COMPONENT_PAUSE_METHODS[target_component.type])(data_service_id=c.organization.id,
                                                                             dataflow_id=c.project.id,
                                                                             id=c.id,
                                                                             body='{}',
                                                                             paused=pause).data
    return None

  results = []
  if service_id and flow_id:
    components = client.list_dataflow_components(service_id, flow_id, deep=False, kind='source,view,sink', state=','.join(state)).data
    futures = []
    with ThreadPoolExecutor(max_workers=1) as executor:
      for c in components:
        if not component_id or (c.id in component_id):
          futures.append(executor.submit(_pause_resume, c, pause_flag))

    for future in concurrent.futures.as_completed(futures):
      result = future.result(10)
      results.append(MessageToDict(result))

  print_response(ctx, results)
