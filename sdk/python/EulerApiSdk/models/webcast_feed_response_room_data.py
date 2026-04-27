from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_boolean_or_number import RecordStringBooleanOrNumber
    from ..models.record_string_unknown import RecordStringUnknown
    from ..models.webcast_feed_response_hashtag import WebcastFeedResponseHashtag
    from ..models.webcast_feed_response_image import WebcastFeedResponseImage
    from ..models.webcast_feed_response_room_data_blurred_cover import WebcastFeedResponseRoomDataBlurredCover
    from ..models.webcast_feed_response_room_data_feed_room_label import WebcastFeedResponseRoomDataFeedRoomLabel
    from ..models.webcast_feed_response_room_data_game_tag_detail import WebcastFeedResponseRoomDataGameTagDetail
    from ..models.webcast_feed_response_room_data_rectangle_cover_img import (
        WebcastFeedResponseRoomDataRectangleCoverImg,
    )
    from ..models.webcast_feed_response_room_data_square_cover_img import WebcastFeedResponseRoomDataSquareCoverImg
    from ..models.webcast_feed_response_room_data_stats import WebcastFeedResponseRoomDataStats
    from ..models.webcast_feed_response_room_data_taxonomy_tag_info import WebcastFeedResponseRoomDataTaxonomyTagInfo
    from ..models.webcast_feed_response_stream_url import WebcastFeedResponseStreamUrl
    from ..models.webcast_feed_response_user import WebcastFeedResponseUser


T = TypeVar("T", bound="WebcastFeedResponseRoomData")


@_attrs_define
class WebcastFeedResponseRoomData:
    """
    Attributes:
        id (float):
        id_str (str):
        status (float):
        owner_user_id (float):
        title (str):
        user_count (float):
        client_version (float):
        cover (WebcastFeedResponseImage):
        stream_url (WebcastFeedResponseStreamUrl):
        stats (WebcastFeedResponseRoomDataStats):
        feed_room_label (WebcastFeedResponseRoomDataFeedRoomLabel):
        owner (WebcastFeedResponseUser):
        live_type_third_party (bool):
        room_auth (RecordStringBooleanOrNumber): Construct a type with a set of properties K of type T
        like_count (float):
        anchor_tab_type (float):
        commerce_info (RecordStringUnknown): Construct a type with a set of properties K of type T
        live_room_mode (float):
        stream_url_filtered_info (RecordStringUnknown): Construct a type with a set of properties K of type T
        square_cover_img (WebcastFeedResponseRoomDataSquareCoverImg):
        rectangle_cover_img (WebcastFeedResponseRoomDataRectangleCoverImg):
        blurred_cover (WebcastFeedResponseRoomDataBlurredCover):
        multi_stream_url (RecordStringUnknown): Construct a type with a set of properties K of type T
        game_tag_detail (WebcastFeedResponseRoomDataGameTagDetail):
        taxonomy_tag_info (WebcastFeedResponseRoomDataTaxonomyTagInfo):
        hashtag (WebcastFeedResponseHashtag | Unset):
    """

    id: float
    id_str: str
    status: float
    owner_user_id: float
    title: str
    user_count: float
    client_version: float
    cover: WebcastFeedResponseImage
    stream_url: WebcastFeedResponseStreamUrl
    stats: WebcastFeedResponseRoomDataStats
    feed_room_label: WebcastFeedResponseRoomDataFeedRoomLabel
    owner: WebcastFeedResponseUser
    live_type_third_party: bool
    room_auth: RecordStringBooleanOrNumber
    like_count: float
    anchor_tab_type: float
    commerce_info: RecordStringUnknown
    live_room_mode: float
    stream_url_filtered_info: RecordStringUnknown
    square_cover_img: WebcastFeedResponseRoomDataSquareCoverImg
    rectangle_cover_img: WebcastFeedResponseRoomDataRectangleCoverImg
    blurred_cover: WebcastFeedResponseRoomDataBlurredCover
    multi_stream_url: RecordStringUnknown
    game_tag_detail: WebcastFeedResponseRoomDataGameTagDetail
    taxonomy_tag_info: WebcastFeedResponseRoomDataTaxonomyTagInfo
    hashtag: WebcastFeedResponseHashtag | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        id_str = self.id_str

        status = self.status

        owner_user_id = self.owner_user_id

        title = self.title

        user_count = self.user_count

        client_version = self.client_version

        cover = self.cover.to_dict()

        stream_url = self.stream_url.to_dict()

        stats = self.stats.to_dict()

        feed_room_label = self.feed_room_label.to_dict()

        owner = self.owner.to_dict()

        live_type_third_party = self.live_type_third_party

        room_auth = self.room_auth.to_dict()

        like_count = self.like_count

        anchor_tab_type = self.anchor_tab_type

        commerce_info = self.commerce_info.to_dict()

        live_room_mode = self.live_room_mode

        stream_url_filtered_info = self.stream_url_filtered_info.to_dict()

        square_cover_img = self.square_cover_img.to_dict()

        rectangle_cover_img = self.rectangle_cover_img.to_dict()

        blurred_cover = self.blurred_cover.to_dict()

        multi_stream_url = self.multi_stream_url.to_dict()

        game_tag_detail = self.game_tag_detail.to_dict()

        taxonomy_tag_info = self.taxonomy_tag_info.to_dict()

        hashtag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hashtag, Unset):
            hashtag = self.hashtag.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "id_str": id_str,
                "status": status,
                "owner_user_id": owner_user_id,
                "title": title,
                "user_count": user_count,
                "client_version": client_version,
                "cover": cover,
                "stream_url": stream_url,
                "stats": stats,
                "feed_room_label": feed_room_label,
                "owner": owner,
                "live_type_third_party": live_type_third_party,
                "room_auth": room_auth,
                "like_count": like_count,
                "anchor_tab_type": anchor_tab_type,
                "commerce_info": commerce_info,
                "live_room_mode": live_room_mode,
                "stream_url_filtered_info": stream_url_filtered_info,
                "square_cover_img": square_cover_img,
                "rectangle_cover_img": rectangle_cover_img,
                "blurred_cover": blurred_cover,
                "multi_stream_url": multi_stream_url,
                "game_tag_detail": game_tag_detail,
                "taxonomy_tag_info": taxonomy_tag_info,
            }
        )
        if hashtag is not UNSET:
            field_dict["hashtag"] = hashtag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_boolean_or_number import RecordStringBooleanOrNumber
        from ..models.record_string_unknown import RecordStringUnknown
        from ..models.webcast_feed_response_hashtag import WebcastFeedResponseHashtag
        from ..models.webcast_feed_response_image import WebcastFeedResponseImage
        from ..models.webcast_feed_response_room_data_blurred_cover import WebcastFeedResponseRoomDataBlurredCover
        from ..models.webcast_feed_response_room_data_feed_room_label import WebcastFeedResponseRoomDataFeedRoomLabel
        from ..models.webcast_feed_response_room_data_game_tag_detail import WebcastFeedResponseRoomDataGameTagDetail
        from ..models.webcast_feed_response_room_data_rectangle_cover_img import (
            WebcastFeedResponseRoomDataRectangleCoverImg,
        )
        from ..models.webcast_feed_response_room_data_square_cover_img import WebcastFeedResponseRoomDataSquareCoverImg
        from ..models.webcast_feed_response_room_data_stats import WebcastFeedResponseRoomDataStats
        from ..models.webcast_feed_response_room_data_taxonomy_tag_info import (
            WebcastFeedResponseRoomDataTaxonomyTagInfo,
        )
        from ..models.webcast_feed_response_stream_url import WebcastFeedResponseStreamUrl
        from ..models.webcast_feed_response_user import WebcastFeedResponseUser

        d = dict(src_dict)
        id = d.pop("id")

        id_str = d.pop("id_str")

        status = d.pop("status")

        owner_user_id = d.pop("owner_user_id")

        title = d.pop("title")

        user_count = d.pop("user_count")

        client_version = d.pop("client_version")

        cover = WebcastFeedResponseImage.from_dict(d.pop("cover"))

        stream_url = WebcastFeedResponseStreamUrl.from_dict(d.pop("stream_url"))

        stats = WebcastFeedResponseRoomDataStats.from_dict(d.pop("stats"))

        feed_room_label = WebcastFeedResponseRoomDataFeedRoomLabel.from_dict(d.pop("feed_room_label"))

        owner = WebcastFeedResponseUser.from_dict(d.pop("owner"))

        live_type_third_party = d.pop("live_type_third_party")

        room_auth = RecordStringBooleanOrNumber.from_dict(d.pop("room_auth"))

        like_count = d.pop("like_count")

        anchor_tab_type = d.pop("anchor_tab_type")

        commerce_info = RecordStringUnknown.from_dict(d.pop("commerce_info"))

        live_room_mode = d.pop("live_room_mode")

        stream_url_filtered_info = RecordStringUnknown.from_dict(d.pop("stream_url_filtered_info"))

        square_cover_img = WebcastFeedResponseRoomDataSquareCoverImg.from_dict(d.pop("square_cover_img"))

        rectangle_cover_img = WebcastFeedResponseRoomDataRectangleCoverImg.from_dict(d.pop("rectangle_cover_img"))

        blurred_cover = WebcastFeedResponseRoomDataBlurredCover.from_dict(d.pop("blurred_cover"))

        multi_stream_url = RecordStringUnknown.from_dict(d.pop("multi_stream_url"))

        game_tag_detail = WebcastFeedResponseRoomDataGameTagDetail.from_dict(d.pop("game_tag_detail"))

        taxonomy_tag_info = WebcastFeedResponseRoomDataTaxonomyTagInfo.from_dict(d.pop("taxonomy_tag_info"))

        _hashtag = d.pop("hashtag", UNSET)
        hashtag: WebcastFeedResponseHashtag | Unset
        if isinstance(_hashtag, Unset):
            hashtag = UNSET
        else:
            hashtag = WebcastFeedResponseHashtag.from_dict(_hashtag)

        webcast_feed_response_room_data = cls(
            id=id,
            id_str=id_str,
            status=status,
            owner_user_id=owner_user_id,
            title=title,
            user_count=user_count,
            client_version=client_version,
            cover=cover,
            stream_url=stream_url,
            stats=stats,
            feed_room_label=feed_room_label,
            owner=owner,
            live_type_third_party=live_type_third_party,
            room_auth=room_auth,
            like_count=like_count,
            anchor_tab_type=anchor_tab_type,
            commerce_info=commerce_info,
            live_room_mode=live_room_mode,
            stream_url_filtered_info=stream_url_filtered_info,
            square_cover_img=square_cover_img,
            rectangle_cover_img=rectangle_cover_img,
            blurred_cover=blurred_cover,
            multi_stream_url=multi_stream_url,
            game_tag_detail=game_tag_detail,
            taxonomy_tag_info=taxonomy_tag_info,
            hashtag=hashtag,
        )

        return webcast_feed_response_room_data
