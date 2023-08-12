from abc import ABC, abstractmethod
import json


class Caller(ABC):
    @abstractmethod
    def get_response(self, service_obj, message_data):
        pass


class OpenAiRes(Caller):
    @classmethod
    def get_response(self, service_obj, message_data):
        data = service_obj.get_response(
            prompts=json.loads(message_data["prompts"]),
            model=message_data["model"],
            variation_count=message_data["variation_count"],
            max_tokens=message_data["max_tokens"],
            temperature=message_data["temperature"],
            output_format=message_data["output_format"],
            format_structure=message_data["format_structure"],
        )
        return data


class OpenAiImageRes(Caller):
    @classmethod
    def get_response(self, service_obj, message_data):
        data = service_obj.get_response(
            prompts=json.loads(message_data["prompts"]),
            image_data=json.loads(message_data["image_data"]),
            mask_image=json.loads(message_data["mask_image"]),
            variation_count=message_data["variation_count"],
            size=message_data["size"],
            process_type=message_data["process_type"],
        )
        return data
