from AIBridge.queue_integration.response_class import OpenAiImageRes
from AIBridge.ai_services.openai_images import OpenAIImage
from AIBridge.queue_integration.response_class import OpenAiRes
from AIBridge.exceptions import ProcessMQException


class ProcessMQ:
    @classmethod
    def get_process_mq(self, process_name):
        from AIBridge.ai_services.openai_services import OpenAIService

        process_obj = {"open_ai": OpenAIService(), "open_ai_image": OpenAIImage()}
        response_obj = {"open_ai": OpenAiRes(), "open_ai_image": OpenAiImageRes()}
        if process_name not in process_obj:
            raise ProcessMQException(
                f"Process of message queue Not Found process->{process_name}"
            )
        return process_obj[process_name], response_obj[process_name]
