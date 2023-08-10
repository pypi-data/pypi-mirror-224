import re
import segment.analytics as analytics

user_id = None
analytics_client = None
tenant = None
enabled = False
application_name = None


def init(config):
    global analytics_client, enabled
    analytics_client = analytics.Client(config["write_key"])
    enabled = config["enabled"]


def replace_dynamic_value(path):
    regex = re.compile(
        r"(\/\d+\/)|(\/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\/)"
    )
    return regex.sub("/ID/", path)


def identify(user_info):
    global tenant
    tenant = user_info["tenant"]
    global user_id
    user_id = user_info["user_id"]
    global application_name
    application_name = user_info["application_name"]

    if analytics_client and enabled:
        analytics_client.identify(
            user_id,
            {
                "tenant": tenant,
                "domain": user_info["email"].split("@")[1],
                "application_name": application_name,
            },
        )


def page(path_info):
    if analytics_client and enabled:
        analytics_client.page(
            user_id,
            path_info.get("category"),
            path_info.get("name"),
            {
                "path": replace_dynamic_value(path_info["path"]),
                "tenant": tenant,
                "application_name": application_name,
            },
        )


def track(event):
    if analytics_client and enabled:
        properties = event["properties"] if "properties" in event else {}
        analytics_client.track(
            user_id,
            event["name"],
            {"tenant": tenant, "application_name": application_name, **properties},
        )


def reset():
    global tenant, enabled
    tenant = None
    enabled = False

    if analytics_client:
        analytics_client.reset()


__all__ = ["init", "identify", "track", "page", "reset"]
