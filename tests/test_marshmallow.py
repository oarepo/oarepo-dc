# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# Invenio OpenID Connect is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
from __future__ import absolute_import, print_function

import marshmallow
import pytest
from marshmallow import ValidationError

from oarepo_dc.marshmallow import DCObjectSchemaV2Mixin


class MD(DCObjectSchemaV2Mixin, marshmallow.Schema):
    pass

def test_marshmallow_app(app):
    "Test marshmallow with app"
    app.config.update(SUPPORTED_LANGUAGES=["cs", "en"])
    data = {"title": {"cs": "jej", "en":"yay"},
                 "creator": "Alzbeta Pokorna",
                 "created": "2020-05-12",
                 "modified": "2020-05-12",
                 "identifier": "id"}

    assert data == MD().load(data)

    data = {"title": {"cs": "jej", "en": "yay", "en-us": "ayayay"},
                 "creator": "Alzbeta Pokorna",
                 "created": "2020-05-12",
                 "modified": "2020-05-12",
                 "identifier": "id"}

    with pytest.raises(ValidationError):
        MD().load(data)


def test_marshmallow():
    """Test marshmallow."""


    data = {"title":{"cs": "jej"},
                 "creator": "Alzbeta Pokorna",
                 "created": "2020-05-12",
                 "modified": "2020-05-12",
                 "identifier": "id"}

    assert data == MD().load(data)

    data = {"title": {"cs": "jej"},
                 "alternative": {"en-us": "yay", "cs": "jej"},
                 "abstract": {},
                 "creator": "Alzbeta Pokorna",
                 "contributor": "Miroslav Simek",
                 "dateSubmitted": "2020-05-12",
                 "available": "2020-05-12",
                 "created": "2020-05-12",
                 "modified": "2020-05-12",
                 "description": {"en-us": "yay", "cs": "jej"},
                 "identifier": "id"}


    assert data == MD().load(data)

    data = {"title": {"cs": "jej"},
                 "creator": 1,
                 "created": "2020-05-10",
                 "modified": "2020-05-12",
                 "identifier": "id"}

    with pytest.raises(ValidationError):
        MD().load(data)
    data = {"title": {"cs": "jej"},
                 "creator": "Alzbeta Pokorna",
                 "created": "2020-051",
                 "modified": "2020-05-12",
                 "identifier": "id"}

    with pytest.raises(ValidationError):
        MD().load(data)

    data = {"title": "cs",
                 "creator": "Alzbeta Pokorna",
                 "created": "2020-05-01",
                 "modified": "2020-05-12",
                 "identifier": "id"}

    with pytest.raises(ValidationError):
        MD().load(data)

    data = {"title": {"csss": "jej"},
                 "creator": "Alzbeta Pokorna",
                 "created": "2020-05-01",
                 "modified": "2020-05-12",
                 "identifier": "id"}

    with pytest.raises(ValidationError):
        MD().load(data)