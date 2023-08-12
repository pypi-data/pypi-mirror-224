from itertools import product
from typing import List, Optional

from tqdm.auto import tqdm

from promptquality.helpers import create_project, get_estimated_cost
from promptquality.run import run
from promptquality.set_config import set_config
from promptquality.types.settings import Settings
from promptquality.utils.dataset import DatasetType


def create_settings_combinations(
    model_aliases: List[Optional[str]], temperatures: List[Optional[float]]
) -> List[Settings]:
    # Create all combinations of settings objects.
    model_aliases = model_aliases or [None]
    temperatures = temperatures or [None]
    return [
        Settings(model_alias=model_alias, temperature=temperature)
        for model_alias, temperature in product(model_aliases, temperatures)
    ]


def run_batch(
    templates: List[str],
    dataset: DatasetType,
    project_name: Optional[str] = None,
    model_aliases: Optional[List[str]] = None,
    temperatures: Optional[List[float]] = None,
    execute: bool = False,
    wait: bool = True,
) -> None:
    """
    Run a batch of prompts.
    """
    config = set_config()
    # Create project.
    project = create_project(project_name, config)

    # Estimate cost.
    estimated_costs = []
    aliases: List[Optional[str]] = list(model_aliases) if model_aliases else [None]
    all_temperatures: List[Optional[float]] = (
        list(temperatures) if temperatures else [None]
    )
    all_settings = create_settings_combinations(aliases, all_temperatures)
    all_combinations = list(product(templates, all_settings))
    for template, settings in all_combinations:
        estimated_costs.append(
            get_estimated_cost(
                dataset=dataset,
                template=template,
                settings=settings,
                project_id=project.id,
                config=config,
            )
        )
    print(
        f"Estimated total cost for {len(estimated_costs)} runs: "
        f"${sum(estimated_costs)}."
    )
    if not execute:
        print(
            "If you want to execute this run, invoke this function again with "
            "`execute=True`."
        )
    else:
        print(f"Running batch with {len(all_combinations)} runs...")
        for template, settings in tqdm(all_combinations):
            run(
                template=template,
                dataset=dataset,
                project_name=project.name,
                settings=settings,
                config=config,
                wait=wait,
            )
