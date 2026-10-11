# 具身遥感综述

[English](README.md)

本仓库整理具身遥感相关的公开论文、代码、数据集与资源，关注**地理空间定位与理解**、**自适应观测**和**可验证反馈**之间的联系。

[论文分类目录](docs/papers.md) · [按年份浏览](docs/papers-by-year.md) · [数据集与资源](docs/datasets.md) · [BibTeX 文献](data/references.bib) · [参与维护](CONTRIBUTING.md)

## 领域概述

具身遥感将地理背景、感知行动与观测反馈联系起来。处于物理环境中的感知平台，或其具有明确物理约束的模型，选择在哪里、何时以及如何观测，并根据获得的测量更新状态估计、地图或后续行动，以完成地理空间感知目标。

观测选择可以涉及移动、传感器指向、采集时机、传感器配置和任务调度，适用平台包括无人机、卫星和地面机器人。本目录覆盖连接这些环节的方法：表征与地理关联、目标执行、信息驱动的采集、预测建模以及协同感知。

阅读相关文献时，可以沿着感知过程中的信息流理解各项工作：

1. **建立地理关联：** 将观测、实体和任务目标对应到地理背景。
2. **选择并执行观测：** 综合考虑测量价值、物理可行性与资源约束。
3. **利用返回的证据：** 更新估计、地图、计划或下一步行动。
4. **验证信息更新：** 在将局部发现用于区域信息产品之前，确认空间配准、时间有效性，并提供适当的独立验证证据。

## 研究主题

| 主题 | 核心问题 | 主要内容 |
| --- | --- | --- |
| [C1 · 地理空间定位与理解](docs/papers.md#c1-geospatial-grounding) | 观测或目标位于何处，对应什么地理背景？ | 遥感表征、跨视角匹配、位姿估计、鲁棒定位与目标定位。 |
| [C2 · 导航与任务执行](docs/papers.md#c2-navigation-and-mission-execution) | 如何将给定目标转化为可执行行动？ | 语言引导导航、路线与航点推理、运动控制及任务完成。 |
| [C3 · 自适应采集与建图](docs/papers.md#c3-adaptive-acquisition-and-mapping) | 下一次应获取什么观测？ | 信息路径规划、主动建图、面向学习的数据采集、传感器控制与卫星任务调度。 |
| [C4 · 面向观测与行动的预测模型](docs/papers.md#c4-predictive-models-for-observation-and-action) | 可行的行动会揭示或改变什么？ | 状态表征、空间记忆、未来观测、动作条件预测与规划。 |
| [C5 · 协同感知与信息共享](docs/papers.md#c5-coordinated-sensing-and-information-sharing) | 多个平台如何分配观测并融合信息？ | 多机器人感知、空地协作、卫星调度、通信与资源分配。 |

这些类别描述方法所承担的功能，可以相互交叉。导航负责执行给定目标，自适应采集负责确定值得获取的观测；预测规划可以支持二者，协同信息路径规划则同时涉及采集与协调。记忆、不确定性、学习和多模态融合贯穿各类方法。

## 文献阅读入口

以下工作可作为阅读起点；[完整分类目录](docs/papers.md)提供对应的公开论文及可用的代码或项目来源。

### 地理空间定位与理解

- [SatMAE](docs/papers.md#satmae)：遥感表征学习。
- [Sample4Geo](docs/papers.md#sample4geo)：跨视角地理关联。
- [GeoChat](docs/papers.md#geochat)：面向遥感的语言理解与区域定位。

### 导航与任务执行

- [AerialVLN](docs/papers.md#aerialvln)：空中视觉语言导航。
- [CityNav](docs/papers.md#citynav)：结合地理背景的导航。
- [See, Point, Fly](docs/papers.md#spf)：面向空中导航的视觉航点推理。

### 自适应采集与建图

- [Terrain IPP](docs/papers.md#ipp)：面向地形监测的信息驱动采集。
- [IPP-AL](docs/papers.md#ippal)：面向主动学习和语义建图的采集规划。
- [EO-1 ASE](docs/papers.md#ase)：自主分析、重规划与卫星观测采集。

### 面向观测与行动的预测模型

- [ANWM](docs/papers.md#anwm)：空中视觉预测。
- [WorldVLN](docs/papers.md#worldvln)：面向空中导航的世界与动作建模。
- [NavDreamer](docs/papers.md#navdreamer)：利用视频模型进行导航规划。

### 协同感知与信息共享

- [Multi-UAV IPP](docs/papers.md#multiipp)：多无人机协同自适应路径规划。
- [D-SHIELD](docs/papers.md#dshield)：卫星协同观测规划。
- [AGC-VLN](docs/papers.md#agcvln)：通过共享地图开展空地协同导航。

目录还收录[数据集与平台](docs/papers.md#resources-datasets-benchmarks-platforms-and-imagery-resources)、[背景概念](docs/papers.md#background-background-concepts-and-enabling-interfaces)及[相关综述](docs/papers.md#related_surveys-related-surveys)。

## 数据集与资源选择

资源选择应与任务需要的观测和交互接口相匹配。

| 研究需求 | 资源示例 | 关注内容 |
| --- | --- | --- |
| 跨视角地理关联 | CVUSA、University-1652、VIGOR、SUES-200 | 图像对应、地点检索与定位。 |
| 空中感知与空间理解 | UAVScenes、Dronescapes、SpatialSky | 多模态观测、场景理解与空间推理。 |
| 语言引导的空中导航 | AerialVLN、CityNav、OpenFly | 指令、视觉观测与导航轨迹。 |
| 信息驱动感知 | Waterberry Farms | 环境场及采样决策。 |
| 环境应用 | FloodNet、Sen1Floods11、Agriculture-Vision | 洪灾理解、区域制图与农业感知。 |

[资源目录](docs/datasets.md)提供原始来源链接，并列出模态和支持的任务。

静态图像支持组件能力分析，记录序列支持时序分析，交互环境将行动与后续观测联系起来，物理部署则揭示感知和执行约束。证据形式应与所评估的能力对应。区域信息更新还需要地理配准、采集时间记录和独立验证。

## 研究方向

- **跨尺度、传感器和时间的可靠定位：** 将语义表征与几何、传感器模型及地理参考的时效性结合，在对应关系存在歧义时保留不确定性。
- **面向任务观测的预测：** 建模可见性、测量质量和任务相关不确定性，使预测能够支持物理可行的采集决策。
- **从自适应观测与可验证反馈中学习：** 考虑观测位置及选择原因，描述未访问区域的不确定性，并用独立参考证据验证区域更新。
- **高效协作与部署：** 统筹感知、计算和通信，处理信息延迟、平台约束以及观测不完整时的恢复。

## 数据与引用

结构化目录见 [literature.json](data/literature.json)、[resources.json](data/resources.json) 和 [references.bib](data/references.bib)。使用相关方法或资源时，请引用对应的原始论文。外部论文、软件和数据集的授权条件以各自来源为准。

## 参与维护

欢迎通过 Issue 或 Pull Request 提交补充与更正。添加公开来源和更新目录的方法见[贡献指南](CONTRIBUTING.md)。
