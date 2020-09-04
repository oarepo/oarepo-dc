import json


def test_mapping(app):
    """Test of mapping."""
    search = app.extensions['invenio-search']
    with open(search.mappings['test-test-v1.0.0']) as f:
        data = json.load(f)
    assert data == {
  "mappings": {
    "properties": {

  "DCObject": {
    "properties": {
      "identifier": {
        "type": "keyword"
      },
      "abstract": {'type': 'object', 'properties':
                    {
                        'cs': {'type': 'text',
                               'fields': {
                                   "keywords": {
                                       "type": "keyword"
                                   }
                               }},
                        'en': {'type': 'text',
                               'fields': {
                                   "keywords": {
                                       "type": "keyword"
                                   }
                               }
                               }
                    }
                          },
      "title": {'type': 'object', 'properties':
                    {
                        'cs': {'type': 'text',
                               'fields': {
                                   "keywords": {
                                       "type": "keyword"
                                   }
                               }},
                        'en': {'type': 'text',
                               'fields': {
                                   "keywords": {
                                       "type": "keyword"
                                   }
                               }
                               }
                    }
                          },
      "alternative": {'type': 'object', 'properties':
                    {
                        'cs': {'type': 'text',
                               'fields': {
                                   "keywords": {
                                       "type": "keyword"
                                   }
                               }},
                        'en': {'type': 'text',
                               'fields': {
                                   "keywords": {
                                       "type": "keyword"
                                   }
                               }
                               }
                    }
                          },
      "description": {'type': 'object', 'properties':
                    {
                        'cs': {'type': 'text',
                               'fields': {
                                   "keywords": {
                                       "type": "keyword"
                                   }
                               }},
                        'en': {'type': 'text',
                               'fields': {
                                   "keywords": {
                                       "type": "keyword"
                                   }
                               }
                               }
                    }
                          },
      "created": {
        "type": "date",
        "format": "date"
      },
      "available": {
        "type": "date",
        "format": "date"
      },
      "dateSubmitted": {
        "type": "date",
        "format": "date"
      },
      "modified": {
        "type": "date",
        "format": "date"
      },
      "creator": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 100
          }
        }
      },
      "contributor": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 100
          }
        }
      },
      "language": {
        "type": "keyword"
      }
    }
  }
}
    }
  }