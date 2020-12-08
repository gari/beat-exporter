from apiserve import ApiServer, ApiRoute


class MyServer(ApiServer): 
        @ApiRoute("/popup")
        def addbar(req):
            return {"boo":req["bar"]+1}

        @ApiRoute("/stats")
        def stat(req):
            print("FUCK")
            return fuck

        @ApiRoute("/baz")
        def justret(req):
            if req:
                 raise ApiError(501,"no data in for baz")
            return {"obj":1}


fuck="""{
  "beat": {
    "cpu": {
      "system": {
        "ticks": 1480,
        "time": {
          "ms": 1487
        }
      },
      "total": {
        "ticks": 6860,
        "time": {
          "ms": 6869
        },
        "value": 6860
      },
      "user": {
        "ticks": 5380,
        "time": {
          "ms": 5382
        }
      }
    },
    "handles": {
      "limit": {
        "hard": 1048576,
        "soft": 1048576
      },
      "open": 22
    },
    "info": {
      "ephemeral_id": "d7a5cace-bcee-4690-87ee-f30714d37cfb",
      "uptime": {
        "ms": 2688955
      }
    },
    "memstats": {
      "gc_next": 45991248,
      "memory_alloc": 32188400,
      "memory_total": 575210464,
      "rss": 117874688
    },
    "runtime": {
      "goroutines": 106
    }
  },
  "filebeat": {
    "events": {
      "active": 4,
      "added": 10922,
      "done": 10918
    },
    "harvester": {
      "closed": 0,
      "files": {
        "437e02be-0783-4069-8273-9a7584df6477": {
          "last_event_published_time": "2020-12-08T22:07:05.475Z",
          "last_event_timestamp": "2020-12-08T19:07:00.145Z",
          "name": "/var/log/containers/lethed-7c9c87c69-rlcfh_mail_zubr-843a5134a01e9b0c3d40e09d191e2498769b6197d1d3ed923413bb2e23c8cecd.log",
          "read_offset": 777868,
          "size": 777868,
          "start_time": "2020-12-08T21:27:05.448Z"
        },
        "54fd5061-71e6-4d8e-9ee3-d8b2773d30f6": {
          "last_event_published_time": "2020-12-08T22:09:09.496Z",
          "last_event_timestamp": "2020-12-08T19:09:06.745Z",
          "name": "/var/log/containers/lethed-7c9c87c69-rlcfh_mail_envoy-284fd138655cbce675286d3df6685432c3cc80e28fabe0d6e852d7622758d3b4.log",
          "read_offset": 50794175,
          "size": 50794175,
          "start_time": "2020-12-08T21:25:05.444Z"
        },
        "63712502-b270-4571-a863-4c41525b8427": {
          "last_event_published_time": "2020-12-08T22:09:53.962Z",
          "last_event_timestamp": "2020-12-08T19:09:52.630Z",
          "name": "/var/log/containers/lethed-7c9c87c69-rlcfh_mail_lethed-6d8412a542d6750780f6d2c70fce1e03c0b9e659003035cf5e8c9230e82c75a5.log",
          "read_offset": 209060853,
          "size": 209049953,
          "start_time": "2020-12-08T21:25:05.444Z"
        },
        "db33d27a-125f-4326-904d-8bcd3625f544": {
          "last_event_published_time": "2020-12-08T22:09:15.487Z",
          "last_event_timestamp": "2020-12-08T19:09:11.378Z",
          "name": "/var/log/containers/lethed-7c9c87c69-rlcfh_mail_donjuan-other-bdcb7af4ca10de3551fb784e08a41f7a0a8e475d8e0be70c62be2316a2ca2c93.log",
          "read_offset": 44500441,
          "size": 44500441,
          "start_time": "2020-12-08T21:25:05.444Z"
        }
      },
      "open_files": 4,
      "running": 4,
      "skipped": 0,
      "started": 4
    },
    "input": {
      "log": {
        "files": {
          "renamed": 0,
          "truncated": 0
        }
      },
      "netflow": {
        "flows": 0,
        "packets": {
          "dropped": 0,
          "received": 0
        }
      }
    }
  },
  "libbeat": {
    "config": {
      "module": {
        "running": 2,
        "starts": 2,
        "stops": 0
      },
      "reloads": 1,
      "scans": 1
    },
    "output": {
      "events": {
        "acked": 10908,
        "active": 0,
        "batches": 593,
        "dropped": 0,
        "duplicates": 0,
        "failed": 0,
        "toomany": 0,
        "total": 10908
      },
      "read": {
        "bytes": 0,
        "errors": 0
      },
      "type": "kafka",
      "write": {
        "bytes": 0,
        "errors": 0
      }
    },
    "outputs": {
      "kafka": {
        "bytes_read": 181130,
        "bytes_write": 3928984
      }
    },
    "pipeline": {
      "clients": 2,
      "events": {
        "active": 4,
        "dropped": 0,
        "failed": 0,
        "filtered": 10,
        "published": 10912,
        "retry": 256,
        "total": 10922
      },
      "queue": {
        "acked": 10908
      }
    }
  },
  "registrar": {
    "states": {
      "cleanup": 0,
      "current": 6,
      "update": 10918
    },
    "writes": {
      "fail": 0,
      "success": 602,
      "total": 602
    }
  },
  "system": {
    "cpu": {
      "cores": 80
    },
    "load": {
      "1": 1.9,
      "15": 2.41,
      "5": 1.98,
      "norm": {
        "1": 0.0238,
        "15": 0.0301,
        "5": 0.0248
      }
    }
  }
}
"""
MyServer("127.0.0.1",5066).serve_forever()
