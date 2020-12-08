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
        "ticks": 2762140,
        "time": {
          "ms": 2762147
        }
      },
      "total": {
        "ticks": 19647090,
        "time": {
          "ms": 19647103
        },
        "value": 19647090
      },
      "user": {
        "ticks": 16884950,
        "time": {
          "ms": 16884956
        }
      }
    },
    "handles": {
      "limit": {
        "hard": 1048576,
        "soft": 1048576
      },
      "open": 33
    },
    "info": {
      "ephemeral_id": "eeebeb1b-efcf-4814-84df-182ef6ce72f8",
      "uptime": {
        "ms": 3156526791
      }
    },
    "memstats": {
      "gc_next": 55251120,
      "memory_alloc": 46403960,
      "memory_total": 2647667624848,
      "rss": 184160256
    },
    "runtime": {
      "goroutines": 1113
    }
  },
  "filebeat": {
    "events": {
      "active": 27,
      "added": 22771346,
      "done": 22771319
    },
    "harvester": {
      "closed": 402,
      "files": {
        "20674173-8dc8-4edd-b11a-6fa90f535e8f": {
          "last_event_published_time": "2020-12-09T01:23:56.442Z",
          "last_event_timestamp": "2020-12-08T22:23:47.474Z",
          "name": "/var/log/containers/mailapi-search-695cd99666-85n7b_mail-preprod_onlineconf-updater-369b6d713f961285277eb01ff7921a615ab5366dde22c1f40f79d66b99a8ef34.log",
          "read_offset": 262847,
          "size": 262730,
          "start_time": "2020-12-07T14:05:36.219Z"
        },
        "29f0ddc6-0ab9-41ae-a254-db60c0c1ba2e": {
          "last_event_published_time": "2020-12-09T01:23:27.884Z",
          "last_event_timestamp": "2020-12-08T22:23:22.373Z",
          "name": "/var/log/containers/lethed-7c9c87c69-rlcfh_mail_donjuan-other-bdcb7af4ca10de3551fb784e08a41f7a0a8e475d8e0be70c62be2316a2ca2c93.log",
          "read_offset": 44536324,
          "size": 44536324,
          "start_time": "2020-11-18T17:17:06.592Z"
        },
        "3f25765b-c1f3-447c-9fb5-eec3fcbc5888": {
          "last_event_published_time": "2020-12-09T01:23:29.880Z",
          "last_event_timestamp": "2020-12-08T22:23:27.372Z",
          "name": "/var/log/containers/mailapi-search-fb54cbcfb-b7wmv_mail_donjuan-other-88e0a30708920cf0c8caf11ae4a91475387f21392f831c20716d36a82e422b06.log",
          "read_offset": 22863654,
          "size": 22863654,
          "start_time": "2020-12-04T13:32:26.581Z"
        },
        "4e2f7ccc-67fa-4c4c-8269-be988bce62fa": {
          "last_event_published_time": "2020-12-09T01:22:31.129Z",
          "last_event_timestamp": "2020-12-08T22:22:23.573Z",
          "name": "/var/log/containers/mailapi-search-fb54cbcfb-b7wmv_mail_zubr-45f7a8c9416b11e492fe24df731c5bd90e4f4baa6de00429cbc0a8b34eaf9960.log",
          "read_offset": 352633,
          "size": 352633,
          "start_time": "2020-12-04T13:32:26.581Z"
        },
        "594a6d83-b9aa-4a91-8ed5-e055fcd475c8": {
          "last_event_published_time": "2020-12-09T01:23:49.045Z",
          "last_event_timestamp": "2020-12-08T22:23:45.553Z",
          "name": "/var/log/containers/mailapi-search-695cd99666-85n7b_mail-preprod_mailapi-search-e2ca8a096e7688ad4fd719888684abe5bface86664442192c1fb772b8b3723cf.log",
          "read_offset": 59846892,
          "size": 59846501,
          "start_time": "2020-12-07T14:05:36.220Z"
        },
        "63272a82-d1ff-41d6-a114-9bedd17afefb": {
          "last_event_published_time": "2020-12-09T01:22:02.111Z",
          "last_event_timestamp": "2020-12-08T22:22:00.145Z",
          "name": "/var/log/containers/lethed-7c9c87c69-rlcfh_mail_zubr-843a5134a01e9b0c3d40e09d191e2498769b6197d1d3ed923413bb2e23c8cecd.log",
          "read_offset": 782936,
          "size": 782936,
          "start_time": "2020-11-18T17:17:06.594Z"
        },
        "634cc704-01b1-4e67-a6b3-9972c109e27c": {
          "last_event_published_time": "2020-12-09T01:24:02.796Z",
          "last_event_timestamp": "2020-12-08T22:24:02.355Z",
          "name": "/var/log/containers/lethed-7c9c87c69-rlcfh_mail_lethed-6d8412a542d6750780f6d2c70fce1e03c0b9e659003035cf5e8c9230e82c75a5.log",
          "read_offset": 216645103,
          "size": 216629124,
          "start_time": "2020-12-05T06:32:15.848Z"
        },
        "68227608-04d0-40d6-a416-e32daf4017a0": {
          "last_event_published_time": "2020-12-09T01:23:11.026Z",
          "last_event_timestamp": "2020-12-08T22:23:07.958Z",
          "name": "/var/log/containers/lethed-7c9c87c69-rlcfh_mail_envoy-284fd138655cbce675286d3df6685432c3cc80e28fabe0d6e852d7622758d3b4.log",
          "read_offset": 51134144,
          "size": 51134144,
          "start_time": "2020-11-18T17:17:06.593Z"
        },
        "7471924b-761f-4500-936c-a5010479fbc1": {
          "last_event_published_time": "2020-12-09T01:20:38.695Z",
          "last_event_timestamp": "2020-12-08T22:20:32.869Z",
          "name": "/var/log/containers/mailapi-search-695cd99666-85n7b_mail-preprod_zubr-d2de470a130cd585c37947a921452954d7dc31e3428087d3b0a588da0e4f94d3.log",
          "read_offset": 115819,
          "size": 115819,
          "start_time": "2020-12-07T14:05:36.220Z"
        },
        "7881acd3-3386-4ff4-b781-97469882a097": {
          "last_event_published_time": "2020-12-09T01:23:53.052Z",
          "last_event_timestamp": "2020-12-08T22:23:52.786Z",
          "name": "/var/log/containers/calico-node-s9tfx_kube-system_calico-node-9d1d812daed51e7e0f808c9a650c6cabe3076f2adfaf5c7721067d166d798d4c.log",
          "read_offset": 463536371,
          "size": 463535464,
          "start_time": "2020-11-02T12:35:17.279Z"
        },
        "86a1f524-5105-46ee-bba7-85b629eda933": {
          "last_event_published_time": "2020-12-09T01:23:29.573Z",
          "last_event_timestamp": "2020-12-08T22:23:26.995Z",
          "name": "/var/log/containers/filebeat-as-r5bh5_kube-system_filebeat-a66b4864b75f416900a1e548cea29a4394bd40e6ebe4bd386341459435899cca.log",
          "read_offset": 165910131,
          "size": 165910131,
          "start_time": "2020-11-02T12:35:17.278Z"
        },
        "8b7b8cbc-327c-4e86-af24-a9f0aab2ccb1": {
          "last_event_published_time": "2020-12-09T01:24:01.639Z",
          "last_event_timestamp": "2020-12-08T22:23:52.995Z",
          "name": "/var/log/containers/mailapi-search-695cd99666-85n7b_mail-preprod_donjuan-other-02be461af71894d28c37523d4c583b4f77a1123bec8a36218d6878284a886dc8.log",
          "read_offset": 8006373,
          "size": 8006036,
          "start_time": "2020-12-07T14:05:36.218Z"
        },
        "9c0cc1cd-809c-45b7-987a-2edf2841ca6c": {
          "last_event_published_time": "2020-12-09T01:23:43.209Z",
          "last_event_timestamp": "2020-12-08T22:23:35.395Z",
          "name": "/var/log/containers/filebeat-kafka-chv97_kube-system_filebeat-81009533dac6803de63b68d09a3a18a08e89b2f058375c76bd7a0cf254231ee8.log",
          "read_offset": 853896,
          "size": 853896,
          "start_time": "2020-12-08T21:25:07.843Z"
        },
        "aac6796e-35da-44f9-964c-0326f9b84a1d": {
          "last_event_published_time": "2020-12-09T01:23:32.993Z",
          "last_event_timestamp": "2020-12-08T22:23:23.205Z",
          "name": "/var/log/containers/mailapi-search-fb54cbcfb-b7wmv_mail_envoy-0568722b5c80f04138ac9cbbcebd0c0341de2a269be63be8b1e5f69ed66624d5.log",
          "read_offset": 9804527,
          "size": 9804527,
          "start_time": "2020-12-04T13:32:26.581Z"
        },
        "b67e63ee-013b-49a2-90df-5c86da886485": {
          "last_event_published_time": "2020-12-09T01:23:58.787Z",
          "last_event_timestamp": "2020-12-08T22:23:52.308Z",
          "name": "/var/log/containers/mailapi-search-fb54cbcfb-b7wmv_mail_mailapi-search-982281d5b0b10e65f933e5c7a2ab65e1fb00bd5dec6e8d01dc15bc3affcdd38a.log",
          "read_offset": 201497511,
          "size": 201497511,
          "start_time": "2020-12-04T13:32:26.582Z"
        },
        "c8e8d3de-4a50-4ffb-a0c0-9090957edab8": {
          "last_event_published_time": "2020-12-09T01:23:37.995Z",
          "last_event_timestamp": "2020-12-08T22:23:36.881Z",
          "name": "/var/log/containers/mailapi-search-695cd99666-85n7b_mail-preprod_envoy-737f9618e2b977dc962926fd207dc6b00bffb1f3065f2c1eb9b9a046924e5272.log",
          "read_offset": 3223965,
          "size": 3223538,
          "start_time": "2020-12-07T14:05:36.220Z"
        },
        "e0b4f4ff-ed0d-4304-b7eb-fafb6effee35": {
          "last_event_published_time": "2020-12-09T01:23:44.445Z",
          "last_event_timestamp": "2020-12-08T22:23:44.276Z",
          "name": "/var/log/containers/mailapi-search-fb54cbcfb-b7wmv_mail_onlineconf-updater-fbd72a55cd22866f184cfdabc0b39b53e62c9f0acf9c125dd13f02e79b146642.log",
          "read_offset": 787287,
          "size": 787287,
          "start_time": "2020-12-04T13:32:26.582Z"
        },
        "ed0303b1-dd65-4ae1-be0c-8aed64fb5413": {
          "last_event_published_time": "2020-12-09T01:23:54.201Z",
          "last_event_timestamp": "2020-12-08T22:23:47.021Z",
          "name": "/var/log/containers/filebeat-main-f5dgn_kube-system_filebeat-ae50212947d762b8fe4f0d26f3da2941771ed6a8059b8418d8a4c60984d2c28b.log",
          "read_offset": 276892822,
          "size": 276892822,
          "start_time": "2020-11-02T12:35:17.279Z"
        }
      },
      "open_files": 18,
      "running": 18,
      "skipped": 0,
      "started": 420
    },
    "input": {
      "log": {
        "files": {
          "renamed": 0,
          "truncated": 7
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
        "running": 1,
        "starts": 1,
        "stops": 0
      },
      "reloads": 1,
      "scans": 1
    },
    "output": {
      "events": {
        "acked": 22770486,
        "active": 0,
        "batches": 1081730,
        "dropped": 0,
        "duplicates": 0,
        "failed": 440,
        "toomany": 0,
        "total": 22770926
      },
      "read": {
        "bytes": 6490236,
        "errors": 2
      },
      "type": "logstash",
      "write": {
        "bytes": 2568240828,
        "errors": 0
      }
    },
    "pipeline": {
      "clients": 1,
      "events": {
        "active": 27,
        "dropped": 0,
        "failed": 0,
        "filtered": 833,
        "published": 22770513,
        "retry": 1038,
        "total": 22771346
      },
      "queue": {
        "acked": 22770486
      }
    }
  },
  "registrar": {
    "states": {
      "cleanup": 268,
      "current": 36,
      "update": 22771319
    },
    "writes": {
      "fail": 0,
      "success": 1082057,
      "total": 1082057
    }
  },
  "system": {
    "cpu": {
      "cores": 80
    },
    "load": {
      "1": 1.34,
      "15": 2.87,
      "5": 2.41,
      "norm": {
        "1": 0.0168,
        "15": 0.0359,
        "5": 0.0301
      }
    }
  }
}
"""
MyServer("127.0.0.1",5066).serve_forever()
