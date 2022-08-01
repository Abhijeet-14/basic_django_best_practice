from rest_framework import status

from exceptions.CustomExceptions import CustomApiException

# from news_api.views import logger
import logging
logger = logging.getLogger(__name__)

def check_serializer(serializer, serializer_name = ""):
    """Checks the validation of input data with respect a serializer"""

    logger.info("Entering Check Serializer()")
    if not serializer.is_valid():
        logger.error(f"{serializer_name} :: Serializer error :: {serializer.errors}")
        logger.info("Exiting Check Serializer()")

        raise CustomApiException(
            f"Inputs value are invalid or few input fields are missing :: {list(serializer.errors.keys())}",
            status.HTTP_400_BAD_REQUEST
        )

    logger.info(f"{serializer_name} Serializer is valid !!")
    logger.info("Exiting Check Serializer()")