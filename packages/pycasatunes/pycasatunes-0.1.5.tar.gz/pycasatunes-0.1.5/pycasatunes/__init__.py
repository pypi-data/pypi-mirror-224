"""CasaTunes: Init"""
import logging

import urllib.parse
from aiohttp import ClientResponse
from typing import List

from .const import API_PORT
from .objects.base import CasaBase
from .objects.system import CasaTunesSystem
from .objects.zone import CasaTunesZone
from .objects.media import CasaTunesMedia
from .objects.source import CasaTunesSource
from .objects.nowplaying import CasaTunesNowPlaying
from .client import CasaClient


class CasaTunes(CasaBase):
    """Interacting with CasaTunes API."""

    logger = logging.getLogger(__name__)

    def __init__(self, client: "CasaClient", host: str) -> None:
        """Initialize the appliance."""
        self._client = client
        self._host = host
        self._system: CasaTunesSystem

        self._zones: List[CasaTunesZone] = []
        self._zones_dict: dict = {}

        self._sources: List[CasaTunesSource] = []
        self._sources_dict: dict = {}

        self._nowplaying: List[CasaTunesNowPlaying] = []
        self._nowplaying_dict: dict = {}

    @property
    def host(self) -> str:
        """Host."""
        return self._host

    @property
    def system(self) -> dict:
        """System."""
        return self._system

    @property
    def zones(self) -> dict:
        """Zones."""
        return self._zones

    @property
    def zones_dict(self) -> dict:
        """Zones dict."""
        return self._zones_dict

    @property
    def sources(self) -> dict:
        """Sources."""
        return self._sources

    @property
    def sources_dict(self) -> dict:
        """Sources dict."""
        return self._sources_dict

    @property
    def nowplaying(self) -> dict:
        """Now playing."""
        return self._nowplaying

    @property
    def nowplaying_dict(self) -> dict:
        """Now playing dict."""
        return self._nowplaying_dict

    async def fetch(self) -> None:
        """Fetch data from CasaTunes zone."""
        data: dict = {}
        data["system"] = await self.get_system()
        data["zones"] = await self.get_zones()
        data["sources"] = await self.get_sources()
        data["nowplaying"] = await self.get_nowplaying()

        return data

    async def get_system(self) -> None:
        """Get System."""
        response: ClientResponse = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/system/info"
        )
        json = await response.json()
        self.logger.debug(json)
        system = [CasaTunesSystem(self._client, json)]
        self._system = system[0]

        return self._system

    async def get_zones(self) -> None:
        """Get Zones."""
        response: ClientResponse = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones"
        )
        json = await response.json()
        self.logger.debug(json)
        self._zones = [CasaTunesZone(self._client, ZoneID) for ZoneID in json or []]

        self._zones_dict: dict = {}
        for zone in self._zones:
            self._zones_dict[zone.ZoneID] = zone

    async def get_sources(self) -> CasaTunesSource:
        """Get Sources."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/sources"
        )
        json = await response.json()
        self.logger.debug(json)

        self._sources = [
            CasaTunesSource(self._client, SourceID) for SourceID in json or []
        ]

        self._sources_dict: dict = {}
        for source in self._sources:
            self._sources_dict[source.SourceID] = source

    async def get_nowplaying(self) -> CasaTunesNowPlaying:
        """Returns now playing information."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/sources/nowplaying"
        )
        json = await response.json()
        self.logger.debug(json)
        self._nowplaying = [
            CasaTunesNowPlaying(self._client, SourceID) for SourceID in json or []
        ]

        self._nowplaying_dict: dict = {}
        for item in self._nowplaying:
            self._nowplaying_dict[item.SourceID] = item

    async def get_media(self, opts) -> CasaTunesMedia:
        """Get Zone Media."""
        if "zone_id" in opts:
            if "item_id" in opts:
                response = await self._client.get(
                    f"http://{self._host}:{API_PORT}/api/v1/media/{opts['item_id']}?limit={opts['limit']}"
                )
            else:
                response = await self._client.get(
                    f"http://{self._host}:{API_PORT}/api/v1/media/zones/{opts['zone_id']}?limit={opts['limit']}"
                )

        json = await response.json()
        self.logger.debug(json)

        return json

    async def search_media(self, zone_id, query) -> dict:
        """Search Media and return the best match."""
        artist_query = query.get("artist")
        album_query = query.get("album")
        track_query = query.get("track")

        if not (artist_query or album_query or track_query):
            return None

        # Build the query string dynamically based on available criteria
        search_query = "+".join(
            urllib.parse.quote(query_part)
            for query_part in [artist_query, album_query, track_query]
            if query_part
        )

        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/media/zones/{zone_id}/search/{search_query}"
        )

        try:
            json_data = await response.json()
            media_items = json_data.get("MediaItems", [])
        except (ValueError, KeyError):
            return None

        best_match = None
        best_match_score = 0

        for item in media_items:
            artist_name = item.get("Artists", "").lower()
            album_name = item.get("Title", "").lower()
            track_name = item.get("Title", "").lower()
            group_name = item.get("GroupName", "").lower()

            artist_score = 0
            album_score = 0
            track_score = 0

            if artist_query and artist_query.lower() in artist_name:
                artist_score = 3
            if album_query and album_query.lower() in album_name:
                album_score = 2
            if track_query and track_query.lower() in track_name:
                track_score = 1

            match_score = artist_score + album_score + track_score

            if match_score > best_match_score:
                if (
                    (artist_score and group_name == "artists")
                    or (album_score and group_name == "albums")
                    or (track_score and group_name == "tracks")
                ):
                    best_match_score = match_score
                    best_match = item

        return best_match

    async def play_media(self, zone_id, media_id):
        """Send player action and option."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/media/zones/{zone_id}/play/{media_id}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def queue_media(self, zone_id, media_id, queue):
        """Add media_id to queue in various ways."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/media/zones/{zone_id}/play/{media_id}/addtoqueue/{queue}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def get_image(self, image_id) -> CasaTunesMedia:
        """Get Image."""
        return f"http://{self._host}:{API_PORT}/api/v1/images/{image_id}"

    async def turn_on(self, zone_id):
        """Turn on the zone."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}?Power=on"
        )
        json = await response.json()
        self.logger.debug(json)

    async def turn_off(self, zone_id):
        """Turn off the zone."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}?Power=off"
        )
        json = await response.json()
        self.logger.debug(json)

    async def mute_volume(self, zone_id, mute):
        """Mute the zone."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}?Mute={mute}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def set_volume_level(self, zone_id, volume):
        """Set volume level for the zone."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}?Volume={volume}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def change_source(self, zone_id, source):
        """Send player action and option."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}?SourceID={source}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def clear_playlist(self, source_id):
        """Clear playlist on source."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/sources/{source_id}/queue/delete"
        )
        json = await response.json()
        self.logger.debug(json)

    async def player_action(self, zone_id, action, option=""):
        """Send player action and option."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}/player/{action}/{option}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def zone_master(self, zone_id, mode):
        """Set Zone master flag."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}/?MasterMode={mode}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def zone_join(self, zone_id, client_zone_id):
        """Join a CasaTunes zone with a zone."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}/group/{client_zone_id}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def zone_unjoin(self, zone_id, client_zone_id):
        """Unjoin a CasaTunes zone with a zone."""
        response = await self._client.get(
            f"http://{self._host}:{API_PORT}/api/v1/zones/{zone_id}/ungroup/{client_zone_id}"
        )
        json = await response.json()
        self.logger.debug(json)

    async def tts(self, zone_id, query):
        """Play TTS in a zone."""
        message = query.get("input", "")
        language = query.get("language", "")
        gender = query.get("gender", "")
        voice = query.get("voice", "en-US-Wavenet-G")
        pre_wait = query.get("pre_wait", "")
        post_wait = query.get("post_wait", "")
        volume = query.get("volume", "")

        payload = {
            "languageCode": language,
            "gender": gender,
            "voice": voice,
            "preWait": pre_wait,
            "postWait": post_wait,
            "volume": volume,
        }

        payload_str = "&".join(f"{key}={value}" for key, value in payload.items())

        url = (
            f"http://{self._host}:{API_PORT}/api/v1/system/tts/input/{message}/zones/{zone_id}?"
            f"{payload_str}"
        )

        response = await self._client.get(url)
        json_response = await response.json()
        self.logger.debug(json_response)

    async def doorbell(self, zone_id, query):
        """Play doorbell in a zone."""
        chime = query.get("chime", "CasaBell 7 Seconds NoDelay")
        pre_wait = query.get("pre_wait", "")
        post_wait = query.get("post_wait", "")
        volume = query.get("volume", "")

        payload = {
            "preWait": pre_wait,
            "postWait": post_wait,
            "volume": volume,
        }

        payload_str = "&".join(f"{key}={value}" for key, value in payload.items())

        url = (
            f"http://{self._host}:{API_PORT}/api/v1/system/doorbell/zones/{zone_id}/chimes/{chime}?"
            f"{payload_str}"
        )

        response = await self._client.get(url)
        json_response = await response.json()
        self.logger.debug(json_response)
