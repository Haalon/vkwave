from vkwave_types.responses import *
from ._category import Category


class Friends(Category):
    def add(
        self,
        user_id: typing.Optional[int] = None,
        text: typing.Optional[str] = None,
        follow: typing.Optional[bool] = None,
    ) -> FriendsAddResponse:
        """
        :param user_id: - ID of the user whose friend request will be approved or to whom a friend request will be sent.
        :param text: - Text of the message (up to 500 characters) for the friend request, if any.
        :param follow: - '1' to pass an incoming request to followers list.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("add", params)
        result = FriendsAddResponse(**raw_result)
        return result

    def add_list(
        self,
        name: typing.Optional[str] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
    ) -> FriendsAddListResponse:
        """
        :param name: - Name of the friend list.
        :param user_ids: - IDs of users to be added to the friend list.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addList", params)
        result = FriendsAddListResponse(**raw_result)
        return result

    def are_friends(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        need_sign: typing.Optional[bool] = None,
    ) -> FriendsAreFriendsResponse:
        """
        :param user_ids: - IDs of the users whose friendship status to check.
        :param need_sign: - '1' — to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("areFriends", params)
        result = FriendsAreFriendsResponse(**raw_result)
        return result

    def delete(self, user_id: typing.Optional[int] = None,) -> FriendsDeleteResponse:
        """
        :param user_id: - ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("delete", params)
        result = FriendsDeleteResponse(**raw_result)
        return result

    def delete_all_requests(self,) -> OkResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteAllRequests", params)
        result = OkResponse(**raw_result)
        return result

    def delete_list(self, list_id: typing.Optional[int] = None,) -> OkResponse:
        """
        :param list_id: - ID of the friend list to delete.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteList", params)
        result = OkResponse(**raw_result)
        return result

    def edit(
        self,
        user_id: typing.Optional[int] = None,
        list_ids: typing.Optional[typing.List[int]] = None,
    ) -> OkResponse:
        """
        :param user_id: - ID of the user whose friend list is to be edited.
        :param list_ids: - IDs of the friend lists to which to add the user.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    def edit_list(
        self,
        name: typing.Optional[str] = None,
        list_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        add_user_ids: typing.Optional[typing.List[int]] = None,
        delete_user_ids: typing.Optional[typing.List[int]] = None,
    ) -> OkResponse:
        """
        :param name: - Name of the friend list.
        :param list_id: - Friend list ID.
        :param user_ids: - IDs of users in the friend list.
        :param add_user_ids: - (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
        :param delete_user_ids: - (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editList", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        user_id: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        list_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        ref: typing.Optional[str] = None,
    ) -> FriendsGetResponse:
        """
        :param user_id: - User ID. By default, the current user ID.
        :param order: - Sort order: , 'name' — by name (enabled only if the 'fields' parameter is used), 'hints' — by rating, similar to how friends are sorted in My friends section, , This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param list_id: - ID of the friend list returned by the [vk.com/dev/friends.getLists|friends.getLists] method to be used as the source. This parameter is taken into account only when the uid parameter is set to the current user ID. This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param count: - Number of friends to return.
        :param offset: - Offset needed to return a specific subset of friends.
        :param fields: - Profile fields to return. Sample values: 'uid', 'first_name', 'last_name', 'nickname', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'domain', 'has_mobile', 'rate', 'contacts', 'education'.
        :param name_case: - Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param ref:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = FriendsGetResponse(**raw_result)
        return result

    def get_app_users(self,) -> FriendsGetAppUsersResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAppUsers", params)
        result = FriendsGetAppUsersResponse(**raw_result)
        return result

    def get_by_phones(
        self,
        phones: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> FriendsGetByPhonesResponse:
        """
        :param phones: - List of phone numbers in MSISDN format (maximum 1000). Example: "+79219876543,+79111234567"
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online, counters'.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getByPhones", params)
        result = FriendsGetByPhonesResponse(**raw_result)
        return result

    def get_lists(
        self,
        user_id: typing.Optional[int] = None,
        return_system: typing.Optional[bool] = None,
    ) -> FriendsGetListsResponse:
        """
        :param user_id: - User ID.
        :param return_system: - '1' — to return system friend lists. By default: '0'.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLists", params)
        result = FriendsGetListsResponse(**raw_result)
        return result

    def get_mutual(
        self,
        source_uid: typing.Optional[int] = None,
        target_uid: typing.Optional[int] = None,
        target_uids: typing.Optional[typing.List[int]] = None,
        order: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> FriendsGetMutualResponse:
        """
        :param source_uid: - ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
        :param target_uid: - ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param target_uids: - IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param order: - Sort order: 'random' — random order
        :param count: - Number of mutual friends to return.
        :param offset: - Offset needed to return a specific subset of mutual friends.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getMutual", params)
        result = FriendsGetMutualResponse(**raw_result)
        return result

    def get_online(
        self,
        user_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        online_mobile: typing.Optional[bool] = None,
        order: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> FriendsGetOnlineResponse:
        """
        :param user_id: - User ID.
        :param list_id: - Friend list ID. If this parameter is not set, information about all online friends is returned.
        :param online_mobile: - '1' — to return an additional 'online_mobile' field, '0' — (default),
        :param order: - Sort order: 'random' — random order
        :param count: - Number of friends to return.
        :param offset: - Offset needed to return a specific subset of friends.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getOnline", params)
        result = FriendsGetOnlineResponse(**raw_result)
        return result

    def get_recent(
        self, count: typing.Optional[int] = None,
    ) -> FriendsGetRecentResponse:
        """
        :param count: - Number of recently added friends to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getRecent", params)
        result = FriendsGetRecentResponse(**raw_result)
        return result

    def get_requests(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        need_mutual: typing.Optional[bool] = None,
        out: typing.Optional[bool] = None,
        sort: typing.Optional[int] = None,
        need_viewed: typing.Optional[bool] = None,
        suggested: typing.Optional[bool] = None,
        ref: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> FriendsGetRequestsResponse:
        """
        :param offset: - Offset needed to return a specific subset of friend requests.
        :param count: - Number of friend requests to return (default 100, maximum 1000).
        :param extended: - '1' — to return response messages from users who have sent a friend request or, if 'suggested' is set to '1', to return a list of suggested friends
        :param need_mutual: - '1' — to return a list of mutual friends (up to 20), if any
        :param out: - '1' — to return outgoing requests, '0' — to return incoming requests (default)
        :param sort: - Sort order: '1' — by number of mutual friends, '0' — by date
        :param need_viewed:
        :param suggested: - '1' — to return a list of suggested friends, '0' — to return friend requests (default)
        :param ref:
        :param fields:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getRequests", params)
        result = FriendsGetRequestsResponse(**raw_result)
        return result

    def get_suggestions(
        self,
        filter: typing.Optional[typing.List[str]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
    ) -> FriendsGetSuggestionsResponse:
        """
        :param filter: - Types of potential friends to return: 'mutual' — users with many mutual friends , 'contacts' — users found with the [vk.com/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' — users who imported the same contacts as the current user with the [vk.com/dev/account.importContacts|account.importContacts] method
        :param count: - Number of suggestions to return.
        :param offset: - Offset needed to return a specific subset of suggestions.
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: - Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getSuggestions", params)
        result = FriendsGetSuggestionsResponse(**raw_result)
        return result

    def search(
        self,
        user_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> FriendsSearchResponse:
        """
        :param user_id: - User ID.
        :param q: - Search query string (e.g., 'Vasya Babich').
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param offset: - Offset needed to return a specific subset of friends.
        :param count: - Number of friends to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("search", params)
        result = FriendsSearchResponse(**raw_result)
        return result