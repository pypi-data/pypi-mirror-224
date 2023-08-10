import json

from io import BytesIO
from PIL import Image
from typing import Union, List, Any

from openxlab.model import Inference
from openxlab.model.clients.modelapi_client import Result 

from .type import ImageType
from .result import PoseEstimationResult, OCRResult, DetectionResult, ImageCaptioningResult
from .util import save_image_base64


class Input():

    @staticmethod
    def input(img_path: str) -> Image.Image:
        return Image.open(img_path).convert("RGB")


class Output():
    
    def __init__(self, content, content_type: str="application/json") -> None:
        self._content_type = content_type
        self._content = content

        self._result_attribute = []

    
    def result(self, save_path: str=None) -> Union[Image.Image, Any]:
        if self._content_type == "application/json":
            return self._content

        if self._content_type.startswith("image"):
            img = Image.open(BytesIO(self._content))
            if save_path:
                img.save(save_path)

            return img

    def visual(self, img_path: str=None) -> Image.Image:
        if hasattr(self, 'visualization'):
            visual = self.__getattribute__('visualization')
            return save_image_base64(visual, img_path)


    @property
    def metric(self):
        """返回推理指标"""
        return self._result_attribute if self._result_attribute else []

    
    def __getattribute__(self, __name: str) -> Any:
        """支持根据属性名称，查询预测结果"""
        try:
            return object.__getattribute__(self, __name)
        except AttributeError as err:
            # 查找支持的预测指标
            if self._result_attribute and __name in self._result_attribute:
                pred_json = self.result()
                if pred_json and __name in pred_json.keys():
                    return pred_json[__name]
                
                return None
            
            raise err


class InstanceSegmentationInference(Inference, Input):

    def __init__(self, model_repo):
        super().__init__(model_repo)


    def __call__(self, img: ImageType, 
                       return_visualization: bool=False, 
                       **kwargs) -> Output:
        if return_visualization:
            kwargs["return_visualization"] = True

        result = super().inference([img], **kwargs)

        return Output(result.original, result.content_type)


class SematicSegmentationOutput(Output):

    def __init__(self, content, content_type: str="application/json") -> None:
        super().__init__(content, content_type)


class SematicSegmentationInference(Inference, Input):

    def __init__(self, model_repo):
        super().__init__(model_repo)


    def __call__(self, img: ImageType, 
                       return_visualization: bool=False, 
                       **kwargs) -> Output:
        if return_visualization:
            kwargs["return_visualization"] = True

        result = super().inference([img], **kwargs)

        return SematicSegmentationOutput(result.original, result.content_type)


class ImageCaptioningOutput(Output, ImageCaptioningResult):

    def __init__(self, content, content_type: str="application/json") -> None:
        super().__init__(content, content_type)
        self._result_attribute = list(ImageCaptioningResult.__dataclass_fields__.keys())


class ImageCaptioningInference(Inference, Input):

    def __init__(self, model_repo):
        super().__init__(model_repo)


    def __call__(self, img: ImageType, 
                       return_visualization: bool=False, 
                       **kwargs) -> Output:
        if return_visualization:
            kwargs["return_visualization"] = True

        result = super().inference([img], **kwargs)

        return ImageCaptioningOutput(result.original, result.content_type)



class PoseEstimationOutput(Output, PoseEstimationResult):

    def __init__(self, raw_result: Result) -> None:
        super().__init__(raw_result)

        self._result_attribute = list(PoseEstimationResult.__dataclass_fields__.keys())


class PoseEstimationInference(Inference, Input):

    def __init__(self, model_repo):
        super().__init__(model_repo)


    def __call__(self, img: ImageType, 
                       return_visualization: bool=False, 
                       **kwargs) -> List[PoseEstimationOutput]:
        if return_visualization:
            kwargs["return_visualization"] = True

        result = super().inference([img], **kwargs)

        result = json.loads(result.original)
        if isinstance(result, list):
            return [ PoseEstimationOutput(item) for item in result ]

        return [ PoseEstimationOutput(result) ]


class OCROutput(Output, OCRResult):
    def __init__(self, raw_result: Result) -> None:
        super().__init__(raw_result)

        self._result_attribute = list(OCRResult.__dataclass_fields__.keys())


class OCRInference(Inference, Input):

    def __init__(self, model_repo):
        super().__init__(model_repo)


    def __call__(self, img: ImageType, 
                       return_visualization: bool=False, 
                       **kwargs) -> List[OCROutput]:
        if return_visualization:
            kwargs["return_visualization"] = True

        result = super().inference([img], **kwargs)

        result = json.loads(result.original)
        if isinstance(result, list):
            return [ OCROutput(item) for item in result ]

        return [ OCROutput(result) ]


class DetectionOutput(Output, DetectionResult):
    def __init__(self, raw_result: Result) -> None:
        super().__init__(raw_result)

        self._result_attribute = list(DetectionResult.__dataclass_fields__.keys())


class DetectionInference(Inference, Input):

    def __init__(self, model_repo):
        super().__init__(model_repo)


    def __call__(self, img: ImageType, 
                       return_visualization: bool=False, 
                       **kwargs) -> List[DetectionResult]:
        if return_visualization:
            kwargs["return_visualization"] = True

        result = super().inference([img], **kwargs)

        result = json.loads(result.original)
        if isinstance(result, list):
            return [ DetectionOutput(item) for item in result ]

        return [ DetectionOutput(result) ]


class Text2BoxOutput(Output, DetectionResult):
    def __init__(self, raw_result: Result) -> None:
        super().__init__(raw_result)

        self._result_attribute = list(DetectionResult.__dataclass_fields__.keys())


class Text2BoxInference(Inference, Input):

    def __init__(self, model_repo):
        super().__init__(model_repo)


    def __call__(self, img: ImageType, 
                       prompt: str,
                       return_visualization: bool=False, 
                       **kwargs) -> List[DetectionResult]:
        if return_visualization:
            kwargs["return_visualization"] = True

        result = super().inference([img, prompt], **kwargs)

        result = json.loads(result.original)
        if isinstance(result, list):
            return [ DetectionOutput(item) for item in result ]

        return [ DetectionOutput(result) ]


class RemoteInference():

    def from_remote(model_repo: str, 
                    task_type: str="instance-seg"):
        if "instance-seg" == task_type:
            return InstanceSegInference(model_repo)
        elif "pose-estimation" == task_type:
            return PoseEstimationInference(model_repo)
        
        


