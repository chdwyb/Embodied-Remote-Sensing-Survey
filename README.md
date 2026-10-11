# Embodied Remote Sensing Survey

[简体中文](README_zh-CN.md)

A curated collection of public papers, code, datasets and resources connecting **geospatial grounding**, **adaptive observation** and **verified feedback**.

[Browse papers](docs/papers.md) · [Browse by year](docs/papers-by-year.md) · [Datasets and resources](docs/datasets.md) · [BibTeX](data/references.bib) · [Contribute](CONTRIBUTING.md)

## Overview

Embodied remote sensing connects geographic context with sensing actions and feedback. A physically situated platform, or an explicit physical model of one, chooses where, when or how to observe. The resulting measurements update its beliefs, maps or subsequent actions toward a geospatial objective.

Acquisition can involve movement, sensor pointing, observation timing, sensor configuration or task selection. Relevant platforms include aerial vehicles, satellites and ground robots. The collection spans the interfaces that connect these choices: representations and geographic association, goal execution, informative acquisition, prediction and cooperation.

A useful way to read the literature is to follow the information through a sensing process:

1. **Ground the task:** relate observations, entities and goals to geographic context.
2. **Choose and execute an observation:** account for measurement value, physical feasibility and available resources.
3. **Use the returned evidence:** revise an estimate, map, plan or subsequent action.
4. **Verify the update:** establish spatial alignment, temporal validity and appropriate independent evidence before reusing a local finding in a regional information product.

## Research topics

| Topic | Main question | Areas covered |
| --- | --- | --- |
| [C1 · Geospatial Grounding](docs/papers.md#c1-geospatial-grounding) | Where is an observation or goal, and what geographic context does it refer to? | Remote sensing representations, cross-view matching, pose estimation, robustness and goal grounding. |
| [C2 · Navigation and Mission Execution](docs/papers.md#c2-navigation-and-mission-execution) | How can a specified goal become executable actions? | Language-guided navigation, route and waypoint reasoning, motion control and mission completion. |
| [C3 · Adaptive Acquisition and Mapping](docs/papers.md#c3-adaptive-acquisition-and-mapping) | Which observation is worth acquiring next? | Informative path planning, active mapping, acquisition for learning, sensor control and satellite tasking. |
| [C4 · Predictive Models for Observation and Action](docs/papers.md#c4-predictive-models-for-observation-and-action) | What could a feasible action reveal or change? | State representations, spatial memory, future observations, action-conditioned prediction and planning. |
| [C5 · Coordinated Sensing and Information Sharing](docs/papers.md#c5-coordinated-sensing-and-information-sharing) | How should platforms allocate observations and combine information? | Multi-robot sensing, air–ground cooperation, satellite scheduling, communication and resource allocation. |

The categories describe functional roles and can overlap. Navigation executes a goal, while adaptive acquisition determines which observation to pursue. A predictive planner can contribute to both; cooperative informative planning connects acquisition with coordination. Memory, uncertainty, learning and multimodal fusion cut across the categories.

## Selected reading

These entries provide starting points for the [full topic catalogue](docs/papers.md). Each linked record includes its public paper and available code or project sources.

### Geospatial grounding

- [SatMAE](docs/papers.md#satmae) — remote sensing representation learning.
- [Sample4Geo](docs/papers.md#sample4geo) — cross-view geographic association.
- [GeoChat](docs/papers.md#geochat) — grounded language interfaces for remote sensing.

### Navigation and mission execution

- [AerialVLN](docs/papers.md#aerialvln) — aerial vision-and-language navigation.
- [CityNav](docs/papers.md#citynav) — navigation with geographic context.
- [See, Point, Fly](docs/papers.md#spf) — visual waypoint reasoning for aerial navigation.

### Adaptive acquisition and mapping

- [Terrain IPP](docs/papers.md#ipp) — informative acquisition for terrain monitoring.
- [IPP-AL](docs/papers.md#ippal) — acquisition planning for active learning and semantic mapping.
- [EO-1 ASE](docs/papers.md#ase) — autonomous analysis, replanning and satellite acquisition.

### Predictive models for observation and action

- [ANWM](docs/papers.md#anwm) — aerial visual prediction.
- [WorldVLN](docs/papers.md#worldvln) — world and action modeling for aerial navigation.
- [NavDreamer](docs/papers.md#navdreamer) — video-based planning for navigation.

### Coordinated sensing and information sharing

- [Multi-UAV IPP](docs/papers.md#multiipp) — cooperative adaptive path planning.
- [D-SHIELD](docs/papers.md#dshield) — coordinated satellite observation planning.
- [AGC-VLN](docs/papers.md#agcvln) — air–ground navigation through shared maps.

The catalogue also contains [datasets and platforms](docs/papers.md#resources-datasets-benchmarks-platforms-and-imagery-resources), [background concepts](docs/papers.md#background-background-concepts-and-enabling-interfaces) and [related surveys](docs/papers.md#related_surveys-related-surveys).

## Datasets and resource selection

Choose resources according to the observations and interfaces a task requires.

| Research need | Example resources | Useful entry point |
| --- | --- | --- |
| Cross-view geographic association | CVUSA, University-1652, VIGOR, SUES-200 | Image correspondence, place retrieval and localization. |
| Aerial perception and spatial understanding | UAVScenes, Dronescapes, SpatialSky | Multimodal observations, scene understanding and spatial reasoning. |
| Language-guided aerial navigation | AerialVLN, CityNav, OpenFly | Instructions, visual observations and navigation trajectories. |
| Informative sensing | Waterberry Farms | Environmental fields and sampling decisions. |
| Environmental applications | FloodNet, Sen1Floods11, Agriculture-Vision | Flood understanding, regional mapping and agricultural perception. |

The [resource directory](docs/datasets.md) links to primary sources and describes modalities and supported tasks.

Static image collections support component analysis; recorded sequences support temporal analysis; interactive environments connect actions to subsequent observations; physical deployments reveal sensing and execution constraints. The form of evidence should match the capability being assessed. Regional information updates additionally require geographic registration, acquisition timing and independent verification.

## Research directions

- **Reliable grounding across scales, sensors and time:** combine semantic representations with geometry, sensor models and the age of geographic references; retain uncertainty when correspondences are ambiguous.
- **Prediction for task-driven observation:** model visibility, measurement quality and task-relevant uncertainty so that predictions can guide feasible acquisition choices.
- **Learning from adaptive observations and verified feedback:** account for where and why observations were selected, track uncertainty in unvisited regions and validate regional updates with independent reference evidence.
- **Efficient cooperation and deployment:** coordinate sensing, computation and communication while accounting for delayed information, platform constraints and recovery from incomplete observations.

## Data and citations

The directory is available as [literature.json](data/literature.json), [resources.json](data/resources.json) and [references.bib](data/references.bib). Cite the original publications when using their methods or resources. Linked papers, software and datasets retain their respective licenses.

## Contributing

Suggestions and corrections are welcome through issues or pull requests. Follow the [contribution guide](CONTRIBUTING.md) to add public sources and update the catalogue.
