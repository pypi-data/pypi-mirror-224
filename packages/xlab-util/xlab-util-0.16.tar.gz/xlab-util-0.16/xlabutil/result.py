import base64

from PIL import Image
from io import BytesIO
from dataclasses import dataclass, field
from typing import Optional, List, Union

import numpy as np

from .util import array_to_base64


@dataclass
class Visual():

    # visualization
    visualization: Optional[str] = field(default_factory=lambda: "")

    def set_visual(self, input: Union[np.ndarray, Image.Image], format: str="jpeg"):
        """设置可视化结果"""
        if isinstance(input, np.ndarray):
            visual = array_to_base64(input, format=format)
        elif isinstance(input, Image.Image):
            img_byte = BytesIO()
            input.save(img_byte, format="jpeg")
            visual = base64.b64encode(img_byte.getvalue()).decode('utf-8')
        else:
            visual = input if isinstance(input, str) else None

        self.visualization = visual


@dataclass
class ClassificationResult:
    """The result of image classification."""
    # The predicted label (category index)
    label: int
    # The confidence score of the prediction
    score: Optional[float]
    # The predicted category name
    category: Optional[str]
    # The scores of all categories
    full_scores: Optional[np.ndarray]



@dataclass
class InstanceMask:
    """The dataclass of the instance segmentation mask."""
    size: List[int]  # The size of the mask
    counts: str  # The RLE-encoded mask


@dataclass
class InstancePose:
    """The dataclass of the pose (keypoint) information of an object."""
    keypoints: List[List[float]] = field(default_factory=lambda: [])  # The coordinates of all keypoints
    keypoint_scores: Optional[List[float]] = field(default_factory=lambda: [])  # The scores of all keypoints


@dataclass
class DetectionResult(Visual):
    """The result of object detection."""
    # The labels of all detected objects
    labels: Optional[List[int]] = field(default_factory=lambda: [])
    # The bounding boxes of all detected objects
    bboxes: Optional[List[List[int]]] = field(default_factory=lambda: [])
    # The scores of all detected objects
    scores: Optional[List[float]] = field(default_factory=lambda: [])


    def set_all_pred(self, labels, scores, bboxes):
        """设置预测结果"""
        self.labels = labels
        self.scores = scores
        self.bboxes = bboxes


@dataclass
class PoseEstimationResult(Visual):
    """The result of pose estimation."""
    # The bounding boxes of all detected objects
    bboxes: Optional[List[List[int]]] = field(default_factory=lambda: [])
    # The scores of all detected objects
    scores: Optional[List[float]] = field(default_factory=lambda: [])
    # The pose estimation results of all detected objects
    poses: Optional[List[InstancePose]] = field(default_factory=lambda: [])


    def set_pred(self, bbox, score, keypoints, keypoint_scores):
        """设置预测结果"""
        self.bboxes.append(bbox)
        self.scores.append(score)
        self.poses.append(InstancePose(keypoints, keypoint_scores))

    
    def set_all_pred(self, bboxes, scores, poses):
        """设置预测结果"""
        self.bboxes = bboxes
        self.scores = scores
        self.poses = poses


@dataclass
class OCRResult(Visual):
    """The result of OCR."""
    # The recognized texts
    rec_texts: Optional[List[str]] = field(default_factory=lambda: [])
    # The confidence scores of the recognized texts
    rec_scores: Optional[List[float]] = field(default_factory=lambda: [])
    # The polygon coordinates of the texts
    det_polygons: Optional[List[List[float]]] = field(default_factory=lambda: [])
    # The confidence scores of the detected polygons
    det_scores: Optional[List[float]] = field(default_factory=lambda: [])

    def set_all_pred(self, rec_texts, rec_scores, det_polygons, det_scores):
        """设置预测结果"""
        self.rec_texts = rec_texts
        self.rec_scores = rec_scores
        self.det_polygons = det_polygons
        self.det_scores = det_scores

    
    def set_pred(self, rec_text, rec_score, det_polygon, det_score):
        """设置预测结果"""
        self.rec_texts.append(rec_text)
        self.rec_scores.append(rec_score)
        self.det_polygons.append(det_polygon)
        self.det_scores.append(det_score)
