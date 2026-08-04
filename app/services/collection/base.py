"""
Provider-independent base interface for all job collectors.

This module defines the Template Method contract used by the Job Collection
subsystem. Every collector follows the same lifecycle while allowing
protocol-specific retrieval and provider-specific normalization.

Architecture:

    BaseCollector
        ├── APICollector
        │     └── ATSCollector
        ├── FeedCollector
        └── HTMLCollector
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.services.collection.models import RawJobCapture

T_RawData = TypeVar("T_RawData")


class BaseCollector(ABC, Generic[T_RawData]):
    """
    Provider-independent abstract base class for all job collectors.

    This class implements both the Strategy Pattern and the Template Method
    Pattern.

    Downstream services interact only with the public ``fetch()`` method,
    while subclasses implement protocol-specific retrieval and
    provider-specific normalization.

    Responsibilities:
        - Define the collector contract.
        - Orchestrate the collection lifecycle.
        - Remain provider-independent.
        - Return standardized RawJobCapture models.
        - Support deterministic duplicate detection.
    """

    def __init__(self) -> None:
        """Initialize shared collector infrastructure."""
        self.logger = logging.getLogger(self.__class__.__name__)

    @property
    @abstractmethod
    def source_name(self) -> str:
        """
        Return the unique identifier of the provider.

        Examples:
            - "jooble"
            - "euraxess"
            - "greenhouse"
        """

    @property
    @abstractmethod
    def source_type(self) -> str:
        """
        Return the category of the collector.

        Examples:
            - "public_api"
            - "career_page"
            - "web_scraper"

        This value should correspond to the project's source type
        classification.
        """

    @property
    def identity(self) -> str:
        """
        Return the User-Agent presented to external providers.

        Concrete collectors may override this when provider-specific
        identification is required.
        """
        return "AI-Career-Agent"

    async def fetch(self) -> list[RawJobCapture]:
        """
        Execute the standard collection workflow.

        Template Method workflow:

            1. Retrieve raw provider data.
            2. Normalize provider-specific data.
            3. Return validated RawJobCapture models.
        """
        raw_data = await self.fetch_raw_data()
        return self.normalize_to_schema(raw_data)

    @abstractmethod
    async def fetch_raw_data(self) -> T_RawData:
        """
        Retrieve unprocessed data from the external provider.

        Retrieval is protocol-specific and is typically implemented by
        protocol collectors such as APICollector or FeedCollector.
        """

    @abstractmethod
    def normalize_to_schema(
        self,
        raw_data: T_RawData,
    ) -> list[RawJobCapture]:
        """
        Transform provider-specific data into RawJobCapture models.

        Every concrete provider is responsible for mapping its own
        response format into the subsystem's standard representation.
        """

    @abstractmethod
    def fingerprint(self, job: RawJobCapture) -> str:
        """
        Generate a deterministic fingerprint for a captured job.

        The fingerprint is used for duplicate detection (FR-005) and
        must remain consistent across all collector implementations.
        """
