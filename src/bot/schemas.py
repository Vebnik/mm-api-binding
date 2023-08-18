from pydantic import BaseModel


class BotConfig(BaseModel):
    token: str
    endpoint: str


class Event:
    added_to_team = 'added_to_team'
    authentication_challenge = 'authentication_challenge'
    channel_converted = 'channel_converted'
    channel_created = 'channel_created'
    channel_deleted = 'channel_deleted'
    channel_member_updated = 'channel_member_updated'
    channel_updated = 'channel_updated'
    channel_viewed = 'channel_viewed'
    config_changed = 'config_changed'
    delete_team = 'delete_team'
    direct_added = 'direct_added'
    emoji_added = 'emoji_added'
    ephemeral_message = 'ephemeral_message'
    group_added = 'group_added'
    hello = 'hello'
    leave_team = 'leave_team'
    license_changed = 'license_changed'
    memberrole_updated = 'memberrole_updated'
    new_user = 'new_user'
    plugin_disabled = 'plugin_disabled'
    plugin_enabled = 'plugin_enabled'
    plugin_statuses_changed = 'plugin_statuses_changed'
    post_deleted = 'post_deleted'
    post_edited = 'post_edited'
    post_unread = 'post_unread'
    posted = 'posted'
    preference_changed = 'preference_changed'
    preferences_changed = 'preferences_changed'
    preferences_deleted = 'preferences_deleted'
    reaction_added = 'reaction_added'
    reaction_removed = 'reaction_removed'
    response = 'response'
    role_updated = 'role_updated'
    status_change = 'status_change'
    typing = 'typing'
    update_team = 'update_team'
    user_added = 'user_added'
    user_removed = 'user_removed'
    user_role_updated = 'user_role_updated'
    user_updated = 'user_updated'
    dialog_opened = 'dialog_opened'
    thread_updated = 'thread_updated'
    thread_follow_changed = 'thread_follow_changed'
    thread_read_changed = 'thread_read_changed'

