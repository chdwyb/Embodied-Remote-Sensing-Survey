# Datasets and resources

Public datasets and benchmarks supporting geospatial grounding, aerial perception, navigation, adaptive sensing, and environmental understanding. Links lead to primary papers or author project pages.

The supplied observations and interfaces determine which tasks a resource supports. Static images, recorded trajectories, interactive environments, and application datasets provide different capabilities.

The machine-readable directory is available in [resources.json](../data/resources.json).

| Resource | Modalities | Supported task |
| --- | --- | --- |
| [CVUSA (standard subset)](https://openaccess.thecvf.com/content_cvpr_2017/html/Zhai_Predicting_Ground-Level_Scene_CVPR_2017_paper.html) | Ground / overhead RGB | Cross-view matching |
| [CVACT](https://openaccess.thecvf.com/content_CVPR_2019/papers/Liu_Lending_Orientation_to_Neural_Networks_for_Cross-View_Geo-Localization_CVPR_2019_paper.pdf) | Ground panoramas / overhead RGB | Cross-view matching |
| [University-1652](https://arxiv.org/abs/2002.12186) | Satellite / synthetic drone / ground RGB | Multi-view place retrieval |
| [VIGOR](https://arxiv.org/abs/2011.12172) | Panoramas / overlapping overhead RGB | Retrieval and metric offset |
| [SUES-200](https://arxiv.org/abs/2204.10704) | Real drone RGB / satellite RGB | Height-dependent retrieval |
| [DenseUAV](https://github.com/Dmmm1997/DenseUAV) | Real drone RGB / satellite RGB | Low-altitude self-localization |
| [UAV-VisLoc](https://arxiv.org/abs/2405.11936) | Real nadir UAV RGB / satellite maps | UAV map localization |
| [VPAIR](https://arxiv.org/abs/2205.11567) | Aircraft RGB / reference render / depth | Place recognition and 6-DoF pose |
| [GTA-UAV](https://arxiv.org/abs/2409.16925) | Game-rendered UAV / overhead RGB | Partial-overlap map localization |
| [MMGeo](https://openaccess.thecvf.com/content/ICCV2025/html/Ji_MMGeo_Multimodal_Compositional_Geo-Localization_for_UAVs_ICCV_2025_paper.html) | RGB / point cloud / depth / text | Compositional geo-localization |
| [OrthoLoC](https://arxiv.org/abs/2509.18350) | UAV RGB / orthophoto / DSM / point maps | 6-DoF pose and calibration |
| [CrossLoc](https://crossloc.github.io/) | Real / rendered RGB; geometry; semantics | Sim-to-real absolute pose |
| [UAVD4L](https://arxiv.org/abs/2401.05971) | Real / synthetic RGB; 3D model; sensor data | 6-DoF aerial localization |
| [GeoText-1652](https://github.com/MultimodalGeo/GeoText-1652) | Drone / satellite RGB and text | Language-assisted geo-localization |
| [RefDrone](https://arxiv.org/abs/2502.00392) | Aerial RGB; expressions; object boxes | Referring-expression grounding |
| [UAVScenes](https://arxiv.org/abs/2507.22412) | Camera / LiDAR / semantics / pose | Multimodal perception and localization |
| [Mid-Air](https://midair.ulg.ac.be/) | RGB / depth / semantics / IMU / pose | State estimation under appearance change |
| [Dronescapes](https://arxiv.org/abs/2308.07615) | Real aerial video; semantics; depth / normals | Multi-task aerial understanding |
| [ClaraVid](https://openaccess.thecvf.com/content/ICCV2025/html/Beche_ClaraVid_A_Holistic_Scene_Reconstruction_Benchmark_From_Aerial_Perspective_With_ICCV_2025_paper.html) | Synthetic RGB / depth / panoptic / point clouds | Holistic aerial reconstruction |
| [AeroBench (Aero-World)](https://arxiv.org/abs/2605.19728) | FPV video / synchronized IMU | Motion-conditioned future observation |
| [UrbanVideo-Bench](https://aclanthology.org/2025.acl-long.1558/) | Real / simulated UAV video; questions | Embodied video reasoning |
| [SpatialSky](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Is_your_VLM_Sky-Ready_A_Comprehensive_Spatial_Intelligence_Benchmark_for_CVPR_2026_paper.html) | RGB / LiDAR-derived spatial QA | Spatial perception and reasoning |
| [AVDN](https://aclanthology.org/2023.findings-acl.190/) | Overhead views / navigation dialogs | Aerial vision-and-dialog navigation |
| [AerialVLN](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_AerialVLN_Vision-and-Language_Navigation_for_UAVs_ICCV_2023_paper.html) | Simulated aerial RGB-D / instructions | Instruction-following navigation |
| [CityNav](https://arxiv.org/abs/2406.14240) | City-derived scenes / language / geographic context | Geographic-goal navigation |
| [OpenFly](https://arxiv.org/abs/2502.18041) | Aerial images / instructions / trajectories | Aerial VLN across rendering sources |
| [TravelUAV / UAV-Need-Help](https://openreview.net/forum?id=rUvCIvI4eB) | Multi-view RGB / instructions / guidance | Continuous UAV target navigation |
| [UAV-ON](https://arxiv.org/abs/2508.00288) | Multi-view RGB-D / semantic object goals | Aerial object-goal navigation |
| [BEDI](https://arxiv.org/abs/2505.18229) | UAV perception / tools / planning / action tasks | Multi-capability agent benchmark |
| [HaL-13k / AeroDuo](https://arxiv.org/abs/2508.15232) | Synchronized high / low UAV RGB / LiDAR / text | Dual-altitude collaborative navigation |
| [Waterberry Farms](https://arxiv.org/abs/2305.06243) | Simulated humidity / disease fields and samples | Informative single / multi-robot sensing |
| [FloodNet](https://arxiv.org/abs/2012.02951) | UAV post-flood RGB / labels | Local disaster understanding |
| [Sen1Floods11](https://github.com/cloudtostreet/Sen1Floods11) | Satellite SAR / optical reference / flood labels | Regional flood mapping |
| [Agriculture-Vision](https://arxiv.org/abs/2001.01306) | Aerial RGB / NIR / pattern masks | Agricultural pattern segmentation |
