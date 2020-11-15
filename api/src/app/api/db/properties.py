properties = {
    # Shared
    "kind": {
        "type": "keyword",
    },
    "state": {
        "type": "keyword",
    },
    "hostname": {
        "type": "keyword",
    },
    "timestamp": {
        "type": "long"
    },
    "utcoffset": {
        "type": "long"
    },
    "pid": {
        "type": "long"
    },
    "clock": {
        "type": "long"
    },
    "app_env": {
        "type": "keyword"
    },
    # Tasks specific
    "uuid": {
        "type": "keyword",
    },
    "root_id": {
        "type": "keyword",
    },
    "parent_id": {
        "type": "keyword",
    },
    "name": {
        "type": "keyword",
    },
    "eta": {
        "type": "date"
    },
    "expires": {
        "type": "double"
    },
    "sent_at": {
        "type": "long"
    },
    "received_at": {
        "type": "long"
    },
    "started_at": {
        "type": "long"
    },
    "succeeded_at": {
        "type": "long"
    },
    "failed_at": {
        "type": "long"
    },
    "rejected_at": {
        "type": "long"
    },
    "revoked_at": {
        "type": "long"
    },
    "retried_at": {
        "type": "long"
    },
    "args": {
        "type": "text",
        "fields": {
            "keyword": {
                "type": "keyword",
                "ignore_above": 256
            }
        }
    },
    "kwargs": {
        "type": "text",
        "fields": {
            "keyword": {
                "type": "keyword",
                "ignore_above": 256
            }
        }
    },
    "result": {
        "type": "text",
        "fields": {
            "keyword": {
                "type": "keyword",
                "ignore_above": 256
            }
        }
    },
    "runtime": {
        "type": "double"
    },
    "retries": {
        "type": "long"
    },
    "exception": {
        "type": "text",
        "fields": {
            "keyword": {
                "type": "keyword",
                "ignore_above": 256
            }
        }
    },
    "traceback": {
        "type": "text",
        "fields": {
            "keyword": {
                "type": "keyword",
                "ignore_above": 256
            }
        }
    },
    # Workers specific
    "online_at": {
        "type": "double"
    },
    "offline_at": {
        "type": "double"
    },
    "last_heartbeat_at": {
        "type": "double"
    },
    "processed": {
        "type": "long"
    },
    "active": {
        "type": "long"
    },
    "loadavg": {
        "type": "float"
    },
    "freq": {
        "type": "float"
    },
    "sw_ident": {
        "type": "keyword"
    },
    "sw_sys": {
        "type": "keyword",
    },
    "sw_ver": {
        "type": "keyword",
    },
    # Broker specific
    "exchange": {
        "type": "keyword",
    },
    "routing_key": {
        "type": "keyword",
    }
}
