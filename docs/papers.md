# Papers by category

Public literature on geospatial grounding, aerial navigation, adaptive sensing, predictive models, and cooperative observation, with related datasets and background work. Categories overlap; each entry's primary category provides a navigation aid.

Each entry links to its available public paper, code and project sources.

[Repository overview](../README.md) · [Datasets](datasets.md) · [Bibliography](../data/references.bib) · [Machine-readable catalogue](../data/literature.json)

## Navigation

- [C1: Geospatial Grounding](#c1-geospatial-grounding)
- [C2: Navigation and Mission Execution](#c2-navigation-and-mission-execution)
- [C3: Adaptive Acquisition and Mapping](#c3-adaptive-acquisition-and-mapping)
- [C4: Predictive Models for Observation and Action](#c4-predictive-models-for-observation-and-action)
- [C5: Coordinated Sensing and Information Sharing](#c5-coordinated-sensing-and-information-sharing)
- [resources: Datasets, benchmarks, platforms and imagery resources](#resources-datasets-benchmarks-platforms-and-imagery-resources)
- [background: Background concepts and enabling interfaces](#background-background-concepts-and-enabling-interfaces)
- [related_surveys: Related surveys](#related_surveys-related-surveys)

## C1: Geospatial Grounding

| Paper | Venue / year | Category | Links |
| --- | --- | --- | --- |
| <a id="arcloc"></a>ARC-Loc: Leveraging Azimuthal Ray Convergence as a Geometric Cue for Direct Cross-View Localization | arXiv 2026 | C1 | [Paper](https://arxiv.org/abs/2609.04965) · [Paper](https://doi.org/10.48550/arXiv.2609.04965) |
| <a id="bearing"></a>Beyond Matching to Tiles: Bridging Unaligned Aerial and Satellite Views for Vision-Only UAV Navigation | CVPR 2026 | C1 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Beyond_Matching_to_Tiles_Bridging_Unaligned_Aerial_and_Satellite_Views_CVPR_2026_paper.html) |
| <a id="bevsplat"></a>BevSplat: Resolving Height Ambiguity via Feature-Based Gaussian Primitives for Weakly-Supervised Cross-View Localization | NeurIPS 2025 | C1 | [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/e5ba3d6d93213db6b1d1931c6517fe1a-Abstract-Conference.html) · [Paper](https://doi.org/10.52202/085713-5235) |
| <a id="geodistill"></a>GeoDistill: Geometry-Guided Self-Distillation for Weakly Supervised Cross-View Localization | ICCV 2025 | C1 | [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Tong_GeoDistill_Geometry-Guided_Self-Distillation_for_Weakly_Supervised_Cross-View_Localization_ICCV_2025_paper.html) |
| <a id="mean"></a>Multilevel Embedding and Alignment Network With Consistency and Invariance Learning for Cross-View Geo-Localization | IEEE Transactions on Geoscience and Remote Sensing 2025 | C1 | [Paper](https://doi.org/10.1109/tgrs.2025.3572775) · [Code](https://github.com/ISChenawei/MEAN) |
| <a id="rascl"></a>RaSCL: Radar to Satellite Crossview Localization | arXiv 2025 | C1 | [Paper](https://arxiv.org/abs/2504.15899) · [Paper](https://doi.org/10.48550/arXiv.2504.15899) |
| <a id="bevloc"></a>BEVLoc: Cross-View Localization and Matching via Birds-Eye-View Synthesis | IEEE/RSJ International Conference on Intelligent Robots and Systems 2024 | C1 | [Paper](https://arxiv.org/abs/2410.06410) |
| <a id="camp"></a>CAMP: A Cross-View Geo-Localization Method Using Contrastive Attributes Mining and Position-Aware Partitioning | IEEE Transactions on Geoscience and Remote Sensing 2024 | C1 | [Paper](https://doi.org/10.1109/tgrs.2024.3448499) · [Code](https://github.com/Mabel0403/CAMP) |
| <a id="congeo"></a>ConGeo: Robust Cross-view Geo-localization across Ground View Variations | arXiv:2403.13965 2024 | C1 | [Paper](https://arxiv.org/abs/2403.13965) · [Paper](https://doi.org/10.48550/arXiv.2403.13965) · [Code](https://github.com/eceo-epfl/ConGeo) |
| <a id="dac"></a>Enhancing Cross-View Geo-Localization With Domain Alignment and Scene Consistency | IEEE Transactions on Circuits and Systems for Video Technology 2024 | C1 | [Paper](https://doi.org/10.1109/tcsvt.2024.3443510) · [Code](https://github.com/SummerpanKing/DAC) |
| <a id="geochat"></a>GeoChat: Grounded Large Vision-Language Model for Remote Sensing | CVPR 2024 | C1 | [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Kuckreja_GeoChat_Grounded_Large_Vision-Language_Model_for_Remote_Sensing_CVPR_2024_paper.html) · [Code](https://github.com/mbzuai-oryx/GeoChat) · [Paper](https://arxiv.org/abs/2311.15826) |
| <a id="unlabelled"></a>Learning Cross-view Visual Geo-localization without Ground Truth | arXiv:2403.12702 2024 | C1 | [Paper](https://arxiv.org/abs/2403.12702) · [Paper](https://doi.org/10.48550/arXiv.2403.12702) |
| <a id="mccg"></a>MCCG: A ConvNeXt-Based Multiple-Classifier Method for Cross-View Geo-Localization | IEEE Transactions on Circuits and Systems for Video Technology 2024 | C1 | [Paper](https://doi.org/10.1109/tcsvt.2023.3296074) · [Code](https://github.com/mode-str/crossview) |
| <a id="mfrgn"></a>MFRGN: Multi-scale Feature Representation Generalization Network for Ground-to-Aerial Geo-localization | Proceedings of the 32nd ACM International Conference on Multimedia 2024 | C1 | [Paper](https://doi.org/10.1145/3664647.3681431) · [Code](https://github.com/ytao-wang/MFRGN) |
| <a id="dofa"></a>Neural Plasticity-Inspired Multimodal Foundation Model for Earth Observation | arXiv:2403.15356 2024 | C1 | [Paper](https://arxiv.org/abs/2403.15356) · [Paper](https://doi.org/10.48550/arXiv.2403.15356) |
| <a id="sdpl"></a>SDPL: Shifting-Dense Partition Learning for UAV-View Geo-Localization | IEEE Transactions on Circuits and Systems for Video Technology 2024 | C1 | [Paper](https://doi.org/10.1109/tcsvt.2024.3424196) · [Code](https://github.com/C-water/SDPL_release) |
| <a id="geotext"></a>Towards Natural Language-Guided Drones: GeoText-1652 Benchmark with Spatial Relation Matching | European Conference on Computer Vision 2024 | C1 | [Project](https://github.com/MultimodalGeo/GeoText-1652) |
| <a id="boost"></a>Boosting 3-DoF Ground-to-Satellite Camera Localization Accuracy via Geometry-Guided Cross-View Transformer | IEEE/CVF International Conference on Computer Vision 2023 | C1 | [Project](https://github.com/YujiaoShi/Boosting3DoFAccuracy) |
| <a id="cbev"></a>C-BEV: Contrastive Bird's Eye View Training for Cross-View Image Retrieval and 3-DoF Pose Estimation | arXiv:2312.08060 2023 | C1 | [Paper](https://arxiv.org/abs/2312.08060) · [Paper](https://doi.org/10.48550/arXiv.2312.08060) |
| <a id="croma"></a>CROMA: Remote Sensing Representations with Contrastive Radar-Optical Masked Autoencoders | NeurIPS 2023 | C1 | [Paper](https://papers.neurips.cc/paper_files/paper/2023/hash/11822e84689e631615199db3b75cd0e4-Abstract-Conference.html) · [Code](https://github.com/antofuller/CROMA) |
| <a id="denseflow"></a>Learning Dense Flow Field for Highly-accurate Cross-view Camera Localization | arXiv:2309.15556 2023 | C1 | [Paper](https://arxiv.org/abs/2309.15556) · [Paper](https://doi.org/10.48550/arXiv.2309.15556) |
| <a id="remoteclip"></a>RemoteCLIP: A Vision Language Foundation Model for Remote Sensing | arXiv:2306.11029 2023 | C1 | [Paper](https://arxiv.org/abs/2306.11029) · [Paper](https://doi.org/10.48550/arXiv.2306.11029) |
| <a id="rendercompare"></a>Render-and-Compare: Cross-View 6 DoF Localization from Noisy Prior | arXiv:2302.06287 2023 | C1 | [Paper](https://arxiv.org/abs/2302.06287) · [Paper](https://doi.org/10.48550/arXiv.2302.06287) |
| <a id="sample4geo"></a>Sample4Geo: Hard Negative Sampling For Cross-View Geo-Localisation | ICCV 2023 | C1 | [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Deuser_Sample4Geo_Hard_Negative_Sampling_For_Cross-View_Geo-Localisation_ICCV_2023_paper.html) · [Code](https://github.com/Skyy93/Sample4Geo) |
| <a id="satlas"></a>SatlasPretrain: A Large-Scale Dataset for Remote Sensing Image Understanding | IEEE/CVF International Conference on Computer Vision 2023 | C1 | [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Bastani_SatlasPretrain_A_Large-Scale_Dataset_for_Remote_Sensing_Image_Understanding_ICCV_2023_paper.html) |
| <a id="scalemae"></a>Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning | IEEE/CVF International Conference on Computer Vision 2023 | C1 | [Project](https://ai-climate.berkeley.edu/scale-mae-website/) |
| <a id="skyscript"></a>SkyScript: A Large and Semantically Diverse Vision-Language Dataset for Remote Sensing | arXiv:2312.12856 2023 | C1 | [Paper](https://arxiv.org/abs/2312.12856) · [Paper](https://doi.org/10.48550/arXiv.2312.12856) |
| <a id="mbf"></a>UAV's Status Is Worth Considering: A Fusion Representations Matching Method for Geo-Localization | Sensors 2023 | C1 | [Paper](https://doi.org/10.3390/s23020720) · [Code](https://github.com/Reza-Zhu/MBF) |
| <a id="metric"></a>Beyond Cross-view Image Retrieval: Highly Accurate Vehicle Localization Using Satellite Image | IEEE/CVF Conference on Computer Vision and Pattern Recognition 2022 | C1 | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Shi_Beyond_Cross-View_Image_Retrieval_Highly_Accurate_Vehicle_Localization_Using_Satellite_CVPR_2022_paper.html) |
| <a id="cvlnet"></a>CVLNet: Cross-View Semantic Correspondence Learning for Video-based Camera Localization | arXiv:2208.03660 2022 | C1 | [Paper](https://arxiv.org/abs/2208.03660) · [Paper](https://doi.org/10.48550/arXiv.2208.03660) |
| <a id="lpn"></a>Each Part Matters: Local Patterns Facilitate Cross-View Geo-Localization | IEEE Trans Circuits Syst Video Technol 2022 | C1 | [Paper](https://arxiv.org/abs/2008.11646) · [Paper](https://doi.org/10.1109/TCSVT.2021.3061265) · [Code](https://github.com/wtyhub/LPN) · [Code](https://github.com/Reza-Zhu/SUES-200-Benchmark) |
| <a id="rknet"></a>Joint Representation Learning and Keypoint Detection for Cross-View Geo-Localization | IEEE Transactions on Image Processing 2022 | C1 | [Paper](https://doi.org/10.1109/tip.2022.3175601) · [Code](https://github.com/AggMan96/RK-Net) |
| <a id="satmae"></a>SatMAE: Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery | NeurIPS 2022 | C1 | [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/01c561df365429f33fcd7a7faa44c985-Abstract-Conference.html) · [Code](https://github.com/sustainlab-group/SatMAE) · [Project](https://sustainlab-group.github.io/SatMAE/) |
| <a id="slicematch"></a>SliceMatch: Geometry-guided Aggregation for Cross-View Pose Estimation | arXiv:2211.14651 2022 | C1 | [Paper](https://arxiv.org/abs/2211.14651) · [Paper](https://doi.org/10.48550/arXiv.2211.14651) |
| <a id="transgeo"></a>TransGeo: Transformer Is All You Need for Cross-view Image Geo-localization | CVPR 2022 | C1 | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Zhu_TransGeo_Transformer_Is_All_You_Need_for_Cross-View_Image_Geo-Localization_CVPR_2022_paper.html) · [Code](https://github.com/Jeff-Zilence/TransGeo2022) · [Paper](https://arxiv.org/abs/2204.00097) |
| <a id="dense"></a>Visual Cross-View Metric Localization with Dense Uncertainty Estimates | arXiv:2208.08519 2022 | C1 | [Paper](https://arxiv.org/abs/2208.08519) · [Paper](https://doi.org/10.48550/arXiv.2208.08519) |
| <a id="lcm"></a>A Practical Cross-View Image Matching Method between UAV and Satellite for UAV-Based Geo-Localization | Remote Sens 2021 | C1 | [Paper](https://www.mdpi.com/2072-4292/13/1/47) · [Paper](https://doi.org/10.3390/rs13010047) |
| <a id="lidarcross"></a>Any Way You Look At It: Semantic Crossview Localization and Mapping with LiDAR | IEEE Robotics and Automation Letters 2021 | C1 | [Paper](https://arxiv.org/abs/2203.08925) · [Paper](https://doi.org/10.1109/LRA.2021.3061332) |
| <a id="seco"></a>Seasonal Contrast: Unsupervised Pre-Training from Uncurated Remote Sensing Data | IEEE/CVF International Conference on Computer Vision 2021 | C1 | [Paper](https://openaccess.thecvf.com/content/ICCV2021/papers/Manas_Seasonal_Contrast_Unsupervised_Pre-Training_From_Uncurated_Remote_Sensing_Data_ICCV_2021_paper.pdf) |
| <a id="vigor"></a>VIGOR: Cross-View Image Geo-Localization Beyond One-to-One Retrieval | CVPR 2021 | C1 | [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Zhu_VIGOR_Cross-View_Image_Geo-Localization_Beyond_One-to-One_Retrieval_CVPR_2021_paper.html) · [Code](https://github.com/Jeff-Zilence/VIGOR) · [Paper](https://arxiv.org/abs/2011.12172) |
| <a id="cvact"></a>Lending Orientation to Neural Networks for Cross-view Geo-localization | IEEE/CVF Conference on Computer Vision and Pattern Recognition 2019 | C1 | [Paper](https://openaccess.thecvf.com/content_CVPR_2019/papers/Liu_Lending_Orientation_to_Neural_Networks_for_Cross-View_Geo-Localization_CVPR_2019_paper.pdf) |
| <a id="cvft"></a>Optimal Feature Transport for Cross-View Image Geo-Localization | arXiv:1907.05021 2019 | C1 | [Paper](https://arxiv.org/abs/1907.05021) · [Paper](https://doi.org/10.48550/arXiv.1907.05021) |
| <a id="safa"></a>Spatial-Aware Feature Aggregation for Image based Cross-View Geo-Localization | NeurIPS 2019 | C1 | [Paper](https://proceedings.neurips.cc/paper/2019/hash/ba2f0015122a5955f8b3a50240fb91b2-Abstract.html) · [Code](https://github.com/YujiaoShi/cross_view_localization_SAFA) |
| <a id="cvm"></a>CVM-Net: Cross-View Matching Network for Image-Based Ground-to-Aerial Geo-Localization | CVPR 2018 | C1 | [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Hu_CVM-Net_Cross-View_Matching_CVPR_2018_paper.html) · [Code](https://github.com/david-husx/crossview_localisation) |
| <a id="uavpose"></a>UAV Pose Estimation using Cross-view Geolocalization with Satellite Imagery | arXiv:1809.05979 2018 | C1 | [Paper](https://arxiv.org/abs/1809.05979) · [Paper](https://doi.org/10.48550/arXiv.1809.05979) |
| <a id="building"></a>Cross-View Image Matching for Geo-localization in Urban Environments | IEEE Conference on Computer Vision and Pattern Recognition 2017 | C1 | [Project](https://www.crcv.ucf.edu/data/Cross-View/) |
| <a id="vo"></a>Localizing and Orienting Street Views Using Overhead Imagery | arXiv:1608.00161 2016 | C1 | [Paper](https://arxiv.org/abs/1608.00161) · [Paper](https://doi.org/10.48550/arXiv.1608.00161) |
| <a id="wherecnn"></a>Learning Deep Representations for Ground-to-Aerial Geolocalization | IEEE Conference on Computer Vision and Pattern Recognition 2015 | C1 | [Paper](https://openaccess.thecvf.com/content_cvpr_2015/html/Lin_Learning_Deep_Representations_2015_CVPR_paper.html) |
| <a id="lin2013"></a>Cross-View Image Geolocalization | CVPR 2013 | C1 | [Paper](https://openaccess.thecvf.com/content_cvpr_2013/html/Lin_Cross-View_Image_Geolocalization_2013_CVPR_paper.html) |

## C2: Navigation and Mission Execution

| Paper | Venue / year | Category | Links |
| --- | --- | --- | --- |
| <a id="airanchor"></a>AirAnchor: Bridging Local and Global Spatial Information for Zero-Shot Aerial Vision-and-Language Navigation | arXiv:2609.08442 2026 | C2 | [Paper](https://arxiv.org/abs/2609.08442) · [Paper](https://doi.org/10.48550/arXiv.2609.08442) |
| <a id="airhunt"></a>AirHunt: Bridging VLM Semantics and Continuous Planning for Efficient Aerial Object Navigation | arXiv:2601.12742 2026 | C2 | [Paper](https://arxiv.org/abs/2601.12742) · [Paper](https://doi.org/10.48550/arXiv.2601.12742) |
| <a id="apex"></a>APEX: A Decoupled Memory-based Explorer for Asynchronous Aerial Object Goal Navigation | arXiv:2602.00551 2026 | C2 | [Paper](https://arxiv.org/abs/2602.00551) · [Paper](https://doi.org/10.48550/arXiv.2602.00551) |
| <a id="autofly"></a>AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild | ICLR 2026 | C2 | [Paper](https://openreview.net/pdf/1a99a8c26a0bf879894a517257af43defc03d88a.pdf) |
| <a id="dynfly"></a>DynFly: Dynamic-Aware Continuous Trajectory Generation for UAV Vision-Language Navigation in Urban Environments | arXiv:2606.31654 2026 | C2 | [Paper](https://arxiv.org/abs/2606.31654) · [Paper](https://doi.org/10.48550/arXiv.2606.31654) |
| <a id="fly0"></a>Fly0: Persistent Metric Anchoring for Zero-Shot Aerial Vision-Language Navigation | arXiv:2602.15875 2026 | C2 | [Paper](https://arxiv.org/abs/2602.15875) · [Paper](https://doi.org/10.48550/arXiv.2602.15875) |
| <a id="geonav"></a>GeoNav: Empowering MLLMs with dual-scale geospatial reasoning for language-goal aerial navigation | Pattern Recogn. 2026 | C2 | [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320326003304) · [Paper](https://doi.org/10.1016/j.patcog.2026.113365) · [Code](https://github.com/Xhtshr/geonav-official) |
| <a id="onfly"></a>OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency | arXiv:2603.10682 2026 | C2 | [Paper](https://arxiv.org/abs/2603.10682) · [Paper](https://doi.org/10.48550/arXiv.2603.10682) |
| <a id="openfly"></a>OpenFly: A Comprehensive Platform for Aerial Vision-Language Navigation | ICLR 2026 | C2 | [Paper](https://openreview.net/pdf?id=OKm3w71ymP) · [Code](https://github.com/SHAILAB-IPEC/OpenFly-Platform) |
| <a id="gridvln"></a>Aerial Vision-and-Language Navigation with Grid-based View Selection and Map Construction | arXiv:2503.11091 2025 | C2 | [Paper](https://arxiv.org/abs/2503.11091) · [Paper](https://doi.org/10.48550/arXiv.2503.11091) |
| <a id="citynav"></a>CityNav: A Large-Scale Dataset for Real-World Aerial Navigation | ICCV 2025 | C2 | [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Lee_CityNav_A_Large-Scale_Dataset_for_Real-World_Aerial_Navigation_ICCV_2025_paper.html) · [Paper](https://arxiv.org/abs/2406.14240) · [Code](https://github.com/water-cookie/citynav) |
| <a id="citynavagent"></a>CityNavAgent: Aerial Vision-and-Language Navigation with Hierarchical Semantic Planning and Global Memory | 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) 2025 | C2 | [Paper](https://aclanthology.org/2025.acl-long.1511/) · [Paper](https://doi.org/10.18653/v1/2025.acl-long.1511) |
| <a id="flightgpt"></a>FlightGPT: Towards Generalizable and Interpretable UAV Vision-and-Language Navigation with Vision-Language Models | arXiv:2505.12835 2025 | C2 | [Paper](https://arxiv.org/abs/2505.12835) · [Paper](https://doi.org/10.48550/arXiv.2505.12835) |
| <a id="gradnav"></a>GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics | arXiv:2506.14009 2025 | C2 | [Paper](https://arxiv.org/abs/2506.14009) · [Paper](https://doi.org/10.48550/arXiv.2506.14009) |
| <a id="hett"></a>History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation | arXiv:2512.14222 2025 | C2 | [Paper](https://arxiv.org/abs/2512.14222) · [Paper](https://doi.org/10.48550/arXiv.2512.14222) |
| <a id="longfly"></a>LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration | arXiv:2512.22010 2025 | C2 | [Paper](https://arxiv.org/abs/2512.22010) · [Paper](https://doi.org/10.48550/arXiv.2512.22010) |
| <a id="openvln"></a>OpenVLN: Open-world Aerial Vision-Language Navigation | arXiv:2511.06182 2025 | C2 | [Paper](https://arxiv.org/abs/2511.06182) · [Paper](https://doi.org/10.48550/arXiv.2511.06182) |
| <a id="raven"></a>RAVEN: Resilient Aerial Navigation via Open-Set Semantic Memory and Behavior Adaptation | arXiv:2509.23563 2025 | C2 | [Paper](https://arxiv.org/abs/2509.23563) · [Paper](https://doi.org/10.48550/arXiv.2509.23563) |
| <a id="spf"></a>See, Point, Fly: A Learning-Free VLM Framework for Universal Unmanned Aerial Navigation | CoRL 2025 | C2 | [Paper](https://proceedings.mlr.press/v305/hu25e.html) |
| <a id="singer"></a>SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones | arXiv:2509.18610 2025 | C2 | [Paper](https://arxiv.org/abs/2509.18610) · [Paper](https://doi.org/10.48550/arXiv.2509.18610) |
| <a id="skyvln"></a>SkyVLN: Vision-and-Language Navigation and NMPC Control for UAVs in Urban Environments | arXiv:2507.06564 2025 | C2 | [Paper](https://arxiv.org/abs/2507.06564) · [Paper](https://doi.org/10.48550/arXiv.2507.06564) |
| <a id="uavvla"></a>UAV-VLA: Vision-Language-Action System for Large Scale Aerial Mission Generation | arXiv:2501.05014 2025 | C2 | [Paper](https://arxiv.org/abs/2501.05014) · [Paper](https://doi.org/10.48550/arXiv.2501.05014) |
| <a id="uavvln"></a>UAV-VLN: End-to-End Vision Language guided Navigation for UAVs | arXiv:2504.21432 2025 | C2 | [Paper](https://arxiv.org/abs/2504.21432) · [Paper](https://doi.org/10.48550/arXiv.2504.21432) |
| <a id="asma"></a>ASMA: An Adaptive Safety Margin Algorithm for Vision-Language Drone Navigation via Scene-Aware Control Barrier Functions | arXiv:2409.10283 2024 | C2 | [Paper](https://arxiv.org/abs/2409.10283) · [Paper](https://doi.org/10.48550/arXiv.2409.10283) |
| <a id="navagent"></a>NavAgent: Multi-scale Urban Street View Fusion For UAV Embodied Vision-and-Language Navigation | arXiv:2411.08579 2024 | C2 | [Paper](https://arxiv.org/abs/2411.08579) · [Paper](https://doi.org/10.48550/arXiv.2411.08579) |
| <a id="avdn"></a>Aerial Vision-and-Dialog Navigation | ACL Findings 2023 | C2 | [Paper](https://aclanthology.org/2023.findings-acl.190/) · [Paper](https://doi.org/10.18653/v1/2023.findings-acl.190) |
| <a id="aerialvln"></a>AerialVLN: Vision-and-Language Navigation for UAVs | ICCV 2023 | C2 | [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_AerialVLN_Vision-and-Language_Navigation_for_UAVs_ICCV_2023_paper.html) · [Code](https://github.com/AirVLN/AirVLN) · [Paper](https://arxiv.org/abs/2308.06735) |
| <a id="viking"></a>ViKiNG: Vision-Based Kilometer-Scale Navigation with Geographic Hints | RSS 2022 | C2 | [Paper](https://www.roboticsproceedings.org/rss18/p019.html) · [Paper](https://doi.org/10.15607/RSS.2022.XVIII.019) |
| <a id="sureal"></a>Learning to Map Natural Language Instructions to Physical Quadcopter Control using Simulated Flight | CoRL/PMLR 2020 | C2 | [Paper](https://proceedings.mlr.press/v100/blukis20a.html) |
| <a id="visitation"></a>Mapping Navigation Instructions to Continuous Control Actions with Position-Visitation Prediction | CoRL 2018 | C2 | [Paper](https://proceedings.mlr.press/v87/blukis18a.html) |

## C3: Adaptive Acquisition and Mapping

| Paper | Venue / year | Category | Links |
| --- | --- | --- | --- |
| <a id="weedgp"></a>Active Informative Planning for UAV-based Weed Mapping using Discrete Gaussian Process Representations | arXiv preprint arXiv:2601.13196 2026 | C3 | [Paper](https://arxiv.org/abs/2601.13196) · [Paper](https://doi.org/10.48550/arXiv.2601.13196) |
| <a id="aeoslidar"></a>AEOS: Active Environment-aware Optimal Scanning Control for UAV LiDAR-Inertial Odometry in Complex Scenes | ISPRS JPRS 2026 | C3 | [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0924271626000067) · [Paper](https://doi.org/10.1016/j.isprsjprs.2026.01.006) |
| <a id="diffippo"></a>DIFF-IPPO: Diffusion-Based Informative Path Planning with Open-Vocabulary Belief Maps | arXiv:2606.16780 2026 | C3 | [Paper](https://arxiv.org/abs/2606.16780) · [Paper](https://doi.org/10.48550/arXiv.2606.16780) |
| <a id="iatigris"></a>IA-TIGRIS: An Incremental and Adaptive Sampling-Based Planner for Online Informative Path Planning | IEEE T-RO 2026 | C3 | [Paper](https://arxiv.org/abs/2502.15961) · [Paper](https://doi.org/10.1109/TRO.2026.3672542) |
| <a id="activegeo"></a>Towards Active Cross-View Object Geo-Localization | arXiv 2026 | C3 | [Paper](https://arxiv.org/abs/2609.19662) · [Paper](https://doi.org/10.48550/arXiv.2609.19662) |
| <a id="aeos"></a>An energy-efficient learning solution for the Agile Earth Observation Satellite Scheduling Problem | IEEE International Conference on Machine Learning for Communication and Networking 2025 | C3 | [Paper](https://arxiv.org/abs/2503.04803) |
| <a id="searchtta"></a>Search-TTA: A Multi-Modal Test-Time Adaptation Framework for Visual Search in the Wild | CoRL 2025 | C3 | [Paper](https://proceedings.mlr.press/v305/tan25a.html) |
| <a id="mapagnostic"></a>Towards Map-Agnostic Policies for Adaptive Informative Path Planning | IEEE Robotics and Automation Letters 2025 | C3 | [Paper](https://arxiv.org/abs/2410.17166) · [Paper](https://doi.org/10.1109/LRA.2025.3557233) |
| <a id="dynamicgraph"></a>Deep Reinforcement Learning with Dynamic Graphs for Adaptive Informative Path Planning | IEEE Robotics and Automation Letters 2024 | C3 | [Paper](https://arxiv.org/abs/2402.04894) · [Paper](https://doi.org/10.1109/LRA.2024.3421188) |
| <a id="gimbal"></a>Informative Sensor Planning for a Single-Axis Gimbaled Camera on a Fixed-Wing UAV | IEEE International Conference on Automation Science and Engineering 2024 | C3 | [Paper](https://arxiv.org/abs/2407.04896) · [Paper](https://doi.org/10.1109/CASE59546.2024.10711697) |
| <a id="overfomo"></a>Overcome the Fear Of Missing Out: Active Sensing UAV Scanning for Precision Agriculture | Robotics and Autonomous Systems 2024 | C3 | [Paper](https://arxiv.org/abs/2312.09730) · [Paper](https://doi.org/10.1016/j.robot.2023.104581) |
| <a id="ippal"></a>An Informative Path Planning Framework for Active Learning in UAV-based Semantic Mapping | IEEE T-RO 2023 | C3 | [Code](https://github.com/dmar-bonn/ipp-al-framework) · [Paper](https://doi.org/10.1109/TRO.2023.3313811) · [Paper](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/rueckin2023tro.pdf) |
| <a id="waterberry"></a>Waterberry Farms: A Novel Benchmark For Informative Path Planning | arXiv preprint arXiv:2305.06243 2023 | C3 | [Paper](https://arxiv.org/abs/2305.06243) · [Paper](https://doi.org/10.48550/arXiv.2305.06243) · [Code](https://github.com/lboloni/WaterberryFarms) |
| <a id="rlipp"></a>Adaptive Informative Path Planning Using Deep Reinforcement Learning for UAV-based Active Sensing | ICRA 2022 | C3 | [Paper](https://research.tudelft.nl/en/publications/adaptive-informative-path-planning-using-deep-reinforcement-learn/) · [Paper](https://doi.org/10.1109/ICRA46639.2022.9812025) · [Code](https://github.com/dmar-bonn/ipp-rl) · [Paper](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/rueckin2022icra.pdf) |
| <a id="anomaly"></a>Informative path planning for anomaly detection in environment exploration and monitoring | Ocean Engineering 2022 | C3 | [Paper](https://arxiv.org/abs/2005.10040) · [Paper](https://doi.org/10.1016/j.oceaneng.2021.110242) |
| <a id="agilesensing"></a>Reinforcement Learning for Agile Active Target Sensing with a UAV | arXiv:2212.08214 2022 | C3 | [Paper](https://arxiv.org/abs/2212.08214) · [Paper](https://doi.org/10.48550/arXiv.2212.08214) |
| <a id="tigris"></a>TIGRIS: An Informed Sampling-based Algorithm for Informative Path Planning | IEEE/RSJ International Conference on Intelligent Robots and Systems 2022 | C3 | [Paper](https://arxiv.org/abs/2203.12830) · [Paper](https://doi.org/10.1109/IROS47612.2022.9981992) |
| <a id="surfaceipp"></a>Online Informative Path Planning for Active Information Gathering of a 3D Surface | IEEE International Conference on Robotics and Automation 2021 | C3 | [Paper](https://arxiv.org/abs/2103.09556) · [Paper](https://doi.org/10.1109/ICRA48506.2021.9561963) |
| <a id="radiovisual"></a>Probabilistic Radio-Visual Active Sensing for Search and Tracking | European Control Conference 2021 | C3 | [Paper](https://arxiv.org/abs/2011.10474) |
| <a id="goalcoverage"></a>Search-based Planning for Active Sensing in Goal-Directed Coverage Tasks | IEEE International Conference on Robotics and Automation 2021 | C3 | [Paper](https://arxiv.org/abs/2011.07383) |
| <a id="ipp"></a>An informative path planning framework for UAV-based terrain monitoring | Auton. Robots 2020 | C3 | [Paper](https://arxiv.org/abs/1809.03870) · [Paper](https://doi.org/10.1007/s10514-020-09903-2) · [Code](https://github.com/ethz-asl/tmplanner) |
| <a id="almap"></a>Active Learning for UAV-based Semantic Mapping | arXiv preprint arXiv:1908.11157 2019 | C3 | [Paper](https://arxiv.org/abs/1908.11157) · [Paper](https://doi.org/10.48550/arXiv.1908.11157) |
| <a id="oaipp"></a>Obstacle-aware Adaptive Informative Path Planning for UAV-based Target Search | ICRA 2019 | C3 | [Paper](https://arxiv.org/abs/1902.10182) · [Paper](https://doi.org/10.1109/ICRA.2019.8794345) · [Code](https://github.com/ajitham123/IPP-SaR) |
| <a id="eoa"></a>An Onboard Autonomous Response Prototype for an Earth Observing Spacecraft | IJCAI Workshop on Artificial Intelligence in Space 2015 | C3 | [Paper](https://ai.jpl.nasa.gov/public/documents/papers/chien-ijcai2015-autonomous.pdf) |
| <a id="hollinger"></a>Sampling-based robotic information gathering algorithms | Int J Robot Res 2014 | C3 | [Paper](https://doi.org/10.1177/0278364914533443) |
| <a id="ase"></a>Using Autonomy Flight Software to Improve Science Return on Earth Observing One | JACIC 2005 | C3 | [Paper](https://ai.jpl.nasa.gov/public/documents/papers/chien-JACIC2005-UsingAutonomy.pdf) · [Paper](https://doi.org/10.2514/1.12923) |

## C4: Predictive Models for Observation and Action

| Paper | Venue / year | Category | Links |
| --- | --- | --- | --- |
| <a id="aeroworld"></a>Aero-World: Action-Conditioned Aerial Video Generation from Inertial Controls | arXiv:2605.19728 2026 | C4 | [Paper](https://arxiv.org/abs/2605.19728) · [Paper](https://doi.org/10.48550/arXiv.2605.19728) |
| <a id="airdreamer"></a>AirDreamer: Generalist Drone Navigation with World Models | arXiv 2026 | C4 | [Paper](https://arxiv.org/abs/2606.03252) · [Paper](https://doi.org/10.48550/arXiv.2606.03252) |
| <a id="imagineuav"></a>ImagineUAV: Aerial Vision-Language Navigation via World-Action Modeling and Kinodynamic Planning | arXiv:2606.01205 2026 | C4 | [Paper](https://arxiv.org/abs/2606.01205) · [Paper](https://doi.org/10.48550/arXiv.2606.01205) |
| <a id="mad"></a>MAD: Mapping-Aware World Models for Agile Quadrotor Flight | arXiv:2606.04534 2026 | C4 | [Paper](https://arxiv.org/abs/2606.04534) · [Paper](https://doi.org/10.48550/arXiv.2606.04534) |
| <a id="navdreamer"></a>NavDreamer: Video Models as Zero-Shot 3D Navigators | arXiv 2026 | C4 | [Paper](https://arxiv.org/abs/2602.09765) · [Paper](https://doi.org/10.48550/arXiv.2602.09765) |
| <a id="tadreamer"></a>TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination | arXiv:2609.19824 2026 | C4 | [Paper](https://arxiv.org/abs/2609.19824) · [Paper](https://doi.org/10.48550/arXiv.2609.19824) |
| <a id="uanwm"></a>Uncertainty-Aware World Model for Aerial Image-Goal Navigation | arXiv:2608.05597 2026 | C4 | [Paper](https://arxiv.org/abs/2608.05597) · [Paper](https://doi.org/10.48550/arXiv.2608.05597) |
| <a id="worldfly"></a>WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation | arXiv:2606.06147 2026 | C4 | [Paper](https://arxiv.org/abs/2606.06147) · [Paper](https://doi.org/10.48550/arXiv.2606.06147) |
| <a id="worldvln"></a>WorldVLN: Autoregressive World Action Model for Aerial Vision-Language Navigation | arXiv 2026 | C4 | [Paper](https://arxiv.org/abs/2605.15964) · [Paper](https://doi.org/10.48550/arXiv.2605.15964) · [Code](https://github.com/EmbodiedCity/WorldVLN.code) |
| <a id="anwm"></a>Aerial World Model for Long-horizon Visual Generation and Navigation in 3D Space | arXiv 2025 | C4 | [Paper](https://arxiv.org/abs/2512.21887) · [Paper](https://doi.org/10.48550/arXiv.2512.21887) · [Code](https://github.com/EmbodiedCity/ANWM.code) |
| <a id="airscape"></a>AirScape: An Aerial Generative World Model with Motion Controllability | arXiv:2507.08885 2025 | C4 | [Paper](https://arxiv.org/abs/2507.08885) · [Paper](https://doi.org/10.48550/arXiv.2507.08885) |

## C5: Coordinated Sensing and Information Sharing

| Paper | Venue / year | Category | Links |
| --- | --- | --- | --- |
| <a id="agcvln"></a>Air-Ground Collaborative Vision-and-Language Navigation via Shared Bird's-Eye Maps | arXiv 2026 | C5 | [Paper](https://arxiv.org/abs/2609.03483) · [Paper](https://doi.org/10.48550/arXiv.2609.03483) |
| <a id="gpkalman"></a>Multi-robot Learning-based Informative Path Planning Using Spatio-Temporal Gaussian Process Kalman Filter | arXiv 2026 | C5 | [Paper](https://arxiv.org/abs/2609.05515) · [Paper](https://doi.org/10.48550/arXiv.2609.05515) |
| <a id="belieffusion"></a>Multi-UAV Active Sensing with Information Gain-based Planning and Belief Fusion | arXiv preprint arXiv:2606.10986 2026 | C5 | [Paper](https://arxiv.org/abs/2606.10986) · [Paper](https://doi.org/10.48550/arXiv.2606.10986) |
| <a id="ugvbelief"></a>UGV-Conditioned Multi-UAV Informative Planning on a Shared Exposure Belief | arXiv preprint arXiv:2606.12306 2026 | C5 | [Paper](https://arxiv.org/abs/2606.12306) · [Paper](https://doi.org/10.48550/arXiv.2606.12306) |
| <a id="smoke"></a>Multi-Agent Ergodic Exploration under Smoke-Based, Time-Varying Sensor Visibility Constraints | IEEE International Conference on Robotics and Automation 2025 | C5 | [Paper](https://arxiv.org/abs/2503.04998) |
| <a id="satmarl"></a>Multi-Agent Reinforcement Learning for Autonomous Multi-Satellite Earth Observation: A Realistic Case Study | arXiv 2025 | C5 | [Paper](https://arxiv.org/abs/2506.15207) · [Paper](https://doi.org/10.48550/arXiv.2506.15207) |
| <a id="scoutipp"></a>Traversing Mars: Cooperative Informative Path Planning to Efficiently Navigate Unknown Scenes | IEEE RA-L 2025 | C5 | [Paper](https://arxiv.org/abs/2406.05313) · [Paper](https://doi.org/10.1109/LRA.2024.3513036) |
| <a id="quantile"></a>A Study on Multirobot Quantile Estimation in Natural Environments | arXiv preprint arXiv:2303.03539 2023 | C5 | [Paper](https://arxiv.org/abs/2303.03539) · [Paper](https://doi.org/10.48550/arXiv.2303.03539) |
| <a id="multiipp"></a>Multi-UAV Adaptive Path Planning Using Deep Reinforcement Learning | IROS 2023 | C5 | [Paper](https://ieeexplore.ieee.org/abstract/document/10342516/) · [Paper](https://doi.org/10.1109/IROS55552.2023.10342516) · [Code](https://github.com/dlrudco/multi-UAV-path-planning-rl) |
| <a id="dshield"></a>Planning Satellite Swarm Measurements for Climate Models: Comparing Dynamic Constraint Processing and MILP Methods | NASA Technical Reports Server 2021 | C5 | [Paper](https://ntrs.nasa.gov/citations/20210025802) |
| <a id="wildfire"></a>Coordinated Control of UAVs for Human-Centered Active Sensing of Wildfires | American Control Conference 2020 | C5 | [Paper](https://arxiv.org/abs/2006.07969) · [Paper](https://doi.org/10.23919/ACC45564.2020.9147613) |
| <a id="heteroteam"></a>Heterogeneous Robot Teams for Informative Sampling | arXiv preprint arXiv:1906.07208 2019 | C5 | [Paper](https://arxiv.org/abs/1906.07208) · [Paper](https://doi.org/10.48550/arXiv.1906.07208) |
| <a id="wind"></a>Informative Path Planning and Mapping with Multiple UAVs in Wind Fields | Distributed Autonomous Robotic Systems: The 13th International Symposium 2018 | C5 | [Paper](https://arxiv.org/abs/1610.01303) · [Paper](https://doi.org/10.1007/978-3-319-73008-0_19) |
| <a id="multirobot"></a>Efficient Informative Sensing using Multiple Robots | J Artif Intell Res 2009 | C5 | [Paper](https://arxiv.org/abs/1401.3462) · [Paper](https://doi.org/10.1613/jair.2674) |

## resources: Datasets, benchmarks, platforms and imagery resources

| Paper | Venue / year | Category | Links |
| --- | --- | --- | --- |
| <a id="spatialsky"></a>Is your VLM Sky-Ready? A Comprehensive Spatial Intelligence Benchmark for UAV Navigation | IEEE/CVF Conference on Computer Vision and Pattern Recognition 2026 | resources | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Is_your_VLM_Sky-Ready_A_Comprehensive_Spatial_Intelligence_Benchmark_for_CVPR_2026_paper.html) |
| <a id="aeroduo"></a>AeroDuo: Aerial Duo for UAV-based Vision and Language Navigation | ACM International Conference on Multimedia 2025 | resources | [Paper](https://arxiv.org/abs/2508.15232) · [Paper](https://doi.org/10.1145/3746027.3754498) |
| <a id="bedi"></a>BEDI: A Comprehensive Benchmark for Evaluating Embodied Agents on UAVs | arXiv:2505.18229 2025 | resources | [Paper](https://arxiv.org/abs/2505.18229) · [Paper](https://doi.org/10.48550/arXiv.2505.18229) |
| <a id="claravid"></a>ClaraVid: A Holistic Scene Reconstruction Benchmark From Aerial Perspective With Delentropy-Based Complexity Profiling | IEEE/CVF International Conference on Computer Vision 2025 | resources | [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Beche_ClaraVid_A_Holistic_Scene_Reconstruction_Benchmark_From_Aerial_Perspective_With_ICCV_2025_paper.html) |
| <a id="game4loc"></a>Game4Loc: A UAV Geo-Localization Benchmark from Game Data | AAAI Conference on Artificial Intelligence 2025 | resources | [Paper](https://arxiv.org/abs/2409.16925) |
| <a id="mmgeo"></a>MMGeo: Multimodal Compositional Geo-Localization for UAVs | IEEE/CVF International Conference on Computer Vision 2025 | resources | [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ji_MMGeo_Multimodal_Compositional_Geo-Localization_for_UAVs_ICCV_2025_paper.html) |
| <a id="ortholoc"></a>OrthoLoC: UAV 6-DoF Localization and Calibration Using Orthographic Geodata | arXiv:2509.18350; NeurIPS 2025 Datasets and Benchmarks 2025 | resources | [Paper](https://arxiv.org/abs/2509.18350) · [Paper](https://doi.org/10.48550/arXiv.2509.18350) |
| <a id="refdrone"></a>RefDrone: A Challenging Benchmark for Referring Expression Comprehension in Drone Scenes | arXiv:2502.00392 2025 | resources | [Paper](https://arxiv.org/abs/2502.00392) · [Paper](https://doi.org/10.48550/arXiv.2502.00392) |
| <a id="traveluav"></a>Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology | International Conference on Learning Representations 2025 | resources | [Paper](https://openreview.net/forum?id=rUvCIvI4eB) |
| <a id="uavon"></a>UAV-ON: A Benchmark for Open-World Object Goal Navigation with Aerial Agents | arXiv:2508.00288 2025 | resources | [Paper](https://arxiv.org/abs/2508.00288) · [Paper](https://doi.org/10.48550/arXiv.2508.00288) · [Code](https://github.com/iLearn-Lab/ACMMM25-UAV_ON) |
| <a id="uavscenes"></a>UAVScenes: A Multi-Modal Dataset for UAVs | arXiv:2507.22412 2025 | resources | [Paper](https://arxiv.org/abs/2507.22412) · [Paper](https://doi.org/10.48550/arXiv.2507.22412) |
| <a id="urbanvideo"></a>UrbanVideo-Bench: Benchmarking Vision-Language Models on Embodied Intelligence with Video Data in Urban Spaces | Annual Meeting of the Association for Computational Linguistics 2025 | resources | [Paper](https://aclanthology.org/2025.acl-long.1558/) · [Paper](https://doi.org/10.18653/v1/2025.acl-long.1558) |
| <a id="aeroverse"></a>AeroVerse: UAV-Agent Benchmark Suite for Simulating, Pre-training, Finetuning, and Evaluating Aerospace Embodied World Models | arXiv:2408.15511 2024 | resources | [Paper](https://arxiv.org/abs/2408.15511) · [Paper](https://doi.org/10.48550/arXiv.2408.15511) |
| <a id="embodiedcity"></a>EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-world City Environment | arXiv:2410.09604 2024 | resources | [Paper](https://arxiv.org/abs/2410.09604) · [Paper](https://doi.org/10.48550/arXiv.2410.09604) |
| <a id="uavvisloc"></a>UAV-VisLoc: A Large-scale Dataset for UAV Visual Localization | arXiv:2405.11936 2024 | resources | [Paper](https://arxiv.org/abs/2405.11936) · [Paper](https://doi.org/10.48550/arXiv.2405.11936) |
| <a id="uavd4l"></a>UAVD4L: A Large-Scale Dataset for UAV 6-DoF Localization | arXiv:2401.05971 2024 | resources | [Paper](https://arxiv.org/abs/2401.05971) · [Paper](https://doi.org/10.48550/arXiv.2401.05971) |
| <a id="denseuav"></a>Vision-Based UAV Self-Positioning in Low-Altitude Urban Environments | IEEE Transactions on Image Processing 2024 | resources | [Project](https://github.com/Dmmm1997/DenseUAV) · [Paper](https://doi.org/10.1109/TIP.2023.3346279) |
| <a id="dronescapes"></a>Self-Supervised Hypergraphs for Learning Multiple World Interpretations | IEEE/CVF International Conference on Computer Vision Workshops 2023 | resources | [Paper](https://arxiv.org/abs/2308.07615) |
| <a id="crossloc"></a>CrossLoc: Scalable Aerial Localization Assisted by Multimodal Synthetic Data | IEEE/CVF Conference on Computer Vision and Pattern Recognition 2022 | resources | [Project](https://crossloc.github.io/) |
| <a id="sues"></a>SUES-200: A Multi-height Multi-scene Cross-view Image Benchmark Across Drone and Satellite | arXiv:2204.10704 2022 | resources | [Paper](https://arxiv.org/abs/2204.10704) · [Paper](https://doi.org/10.48550/arXiv.2204.10704) · [Code](https://github.com/Reza-Zhu/SUES-200-Benchmark) |
| <a id="vpair"></a>VPAIR — Aerial Visual Place Recognition and Localization in Large-scale Outdoor Environments | arXiv:2205.11567 2022 | resources | [Paper](https://arxiv.org/abs/2205.11567) · [Paper](https://doi.org/10.48550/arXiv.2205.11567) |
| <a id="agriculture"></a>Agriculture-Vision: A Large Aerial Image Database for Agricultural Pattern Analysis | arXiv:2001.01306 2020 | resources | [Paper](https://arxiv.org/abs/2001.01306) · [Paper](https://doi.org/10.48550/arXiv.2001.01306) |
| <a id="floodnet"></a>FloodNet: A High Resolution Aerial Imagery Dataset for Post Flood Scene Understanding | arXiv:2012.02951 2020 | resources | [Paper](https://arxiv.org/abs/2012.02951) · [Paper](https://doi.org/10.48550/arXiv.2012.02951) |
| <a id="sen1"></a>Sen1Floods11: A georeferenced dataset to train and test deep learning flood algorithms for Sentinel-1 | IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops 2020 | resources | [Project](https://github.com/cloudtostreet/Sen1Floods11) · [Paper](https://doi.org/10.1109/CVPRW50498.2020.00113) |
| <a id="university"></a>University-1652: A Multi-view Multi-source Benchmark for Drone-based Geo-localization | arXiv:2002.12186 2020 | resources | [Paper](https://arxiv.org/abs/2002.12186) · [Paper](https://doi.org/10.48550/arXiv.2002.12186) · [Code](https://github.com/layumi/University1652-Baseline) · [Code](https://github.com/wtyhub/LPN) |
| <a id="midair"></a>Mid-Air: A Multi-Modal Dataset for Extremely Low Altitude Drone Flights | IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops 2019 | resources | [Project](https://midair.ulg.ac.be/) |
| <a id="cvusa"></a>Predicting Ground-Level Scene Layout From Aerial Imagery | IEEE Conference on Computer Vision and Pattern Recognition 2017 | resources | [Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Zhai_Predicting_Ground-Level_Scene_CVPR_2017_paper.html) · [Paper](https://doi.org/10.1109/CVPR.2017.440) |

## background: Background concepts and enabling interfaces

| Paper | Venue / year | Category | Links |
| --- | --- | --- | --- |
| <a id="zhou"></a>Aerial embodied intelligence: from commands to measurements to actions | Natl Sci Rev 2026 | background | [Paper](https://doi.org/10.1093/nsr/nwag404) |
| <a id="wang"></a>From Passive Observation to Active Multi-Agent Sensing in Earth Observation | OpenReview 2026 | background | [Paper](https://openreview.net/pdf?id=cuMVfP3wnp) |
| <a id="rsagent"></a>RS-Agent: Automating Remote Sensing Tasks through Intelligent Agent | arXiv:2406.07089 2024 | background | [Paper](https://arxiv.org/abs/2406.07089) · [Paper](https://doi.org/10.48550/arXiv.2406.07089) |
| <a id="gaussians"></a>3D Gaussian Splatting for Real-Time Radiance Field Rendering | arXiv:2308.04079 2023 | background | [Paper](https://arxiv.org/abs/2308.04079) · [Paper](https://doi.org/10.48550/arXiv.2308.04079) |
| <a id="conceptgraphs"></a>ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning | arXiv:2309.16650 2023 | background | [Paper](https://arxiv.org/abs/2309.16650) · [Paper](https://doi.org/10.48550/arXiv.2309.16650) |
| <a id="semexp"></a>Learning to Explore using Active Neural SLAM | arXiv:2004.05155 2020 | background | [Paper](https://arxiv.org/abs/2004.05155) · [Paper](https://doi.org/10.48550/arXiv.2004.05155) |
| <a id="pomdp"></a>Planning and acting in partially observable stochastic domains | Artif Intell 1998 | background | [Paper](https://doi.org/10.1016/S0004-3702(98)00023-X) |

## related_surveys: Related surveys

| Paper | Venue / year | Category | Links |
| --- | --- | --- | --- |
| <a id="agenticreview"></a>Agentic AI in Remote Sensing: Foundations, Taxonomy, and Emerging Systems | arXiv:2601.01891 2026 | related_surveys | [Paper](https://arxiv.org/abs/2601.01891) · [Paper](https://doi.org/10.48550/arXiv.2601.01891) |
| <a id="uavreview"></a>UAVs Meet Embodied Intelligence: Bridging Human Intents and Flying Dynamics Via Harnessing Physical-Digital AI Agents | arXiv:2609.18326 2026 | related_surveys | [Paper](https://arxiv.org/abs/2609.18326) · [Paper](https://doi.org/10.48550/arXiv.2609.18326) |
| <a id="vlnreview"></a>Vision-and-Language Navigation for UAVs: Progress, Challenges, and a Research Roadmap | arXiv:2604.13654 2026 | related_surveys | [Paper](https://arxiv.org/abs/2604.13654) · [Paper](https://doi.org/10.48550/arXiv.2604.13654) |
| <a id="aerialsurvey"></a>Vision-Language Navigation for Aerial Robots: Towards the Era of Large Language Models | arXiv:2604.07705 2026 | related_surveys | [Paper](https://arxiv.org/abs/2604.07705) · [Paper](https://doi.org/10.48550/arXiv.2604.07705) |
| <a id="spatialreview"></a>A Survey of Large Language Model-Powered Spatial Intelligence Across Scales: Advances in Embodied Agents, Smart Cities, and Earth Science | arXiv:2504.09848 2025 | related_surveys | [Paper](https://arxiv.org/abs/2504.09848) · [Paper](https://doi.org/10.48550/arXiv.2504.09848) |
| <a id="cvglreview"></a>Cross-view geo-localization: a survey | arXiv:2406.09722 2024 | related_surveys | [Paper](https://arxiv.org/abs/2406.09722) · [Paper](https://doi.org/10.48550/arXiv.2406.09722) |
