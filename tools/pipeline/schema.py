from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SchemaRule:
    required: list[str]
    allow_unknown: bool = True


CORE_FIELDS = {
    "core_identity": ["name"],
    "core_summary": ["summary"],
    "core_time": [],
    "core_place": [],
    "core_people": [],
    "core_media": [],
    "core_relations": [],
    "core_culture": [],
    "core_status": [],
}


TYPE_TIME_FIELDS = {
    "person": ["birth_date", "death_date"],
    "dynasty": ["founded"],
    "polity": ["established", "dissolved"],
    "artifact": ["created", "discovered"],
    "historical_period": ["start_date", "end_date"],
    "event": ["date"],
    "settlement": ["founded"],
    "institution": ["founded"],
    "military_unit": ["formed", "disbanded"],
    "ordinance": ["issued"],
    "law": ["enacted"],
    "treaty": ["signed"],
    "book": ["publication_date"],
    "currency": ["introduced"],
    "deity": [],
    "species": [],
    "technical_concept": [],
    "belief_regime": [],
    "character": [],
    "structure": ["constructed"],
    "administrative_division": ["established", "dissolved"],
    "historical_region": [],
}

TYPE_PLACE_FIELDS = {
    "person": ["birth_place", "death_place"],
    "dynasty": ["realm"],
    "polity": ["capital"],
    "artifact": ["current_location"],
    "event": ["location"],
    "settlement": ["location"],
    "institution": ["location"],
    "military_unit": ["base"],
    "structure": ["location"],
    "administrative_division": ["region"],
    "historical_region": ["region"],
}

TYPE_PEOPLE_FIELDS = {
    "dynasty": ["founder"],
    "polity": ["leader"],
    "institution": ["founder"],
    "military_unit": ["commander"],
    "ordinance": ["issuer"],
    "law": ["author"],
    "treaty": ["parties"],
    "event": ["participants"],
}

TYPE_MEDIA_FIELDS = {
    "dynasty": ["coat_of_arms"],
    "polity": ["map"],
    "structure": ["image"],
    "artifact": ["image"],
    "settlement": ["map"],
}

TYPE_RELATION_FIELDS = {
    "historical_period": ["preceded_by", "followed_by"],
    "polity": ["predecessor", "successor"],
    "event": ["predecessor", "successor"],
    "dynasty": ["parent_house"],
}

TYPE_CULTURE_FIELDS = {
    "polity": ["official_languages", "religion"],
    "dynasty": ["religion"],
    "belief_regime": ["rituals"],
    "deity": ["mythology"],
    "currency": ["symbol"],
    "book": ["language"],
    "character": ["species"],
}

TYPE_STATUS_FIELDS = {
    "polity": ["status", "government_type"],
    "administrative_division": ["status"],
    "institution": ["status"],
    "military_unit": ["allegiance"],
    "technical_concept": ["definition"],
}


def _type_required_fields(article_type: str) -> list[str]:
    required = []
    required += CORE_FIELDS["core_identity"]
    required += CORE_FIELDS["core_summary"]
    required += TYPE_TIME_FIELDS.get(article_type, [])
    required += TYPE_PLACE_FIELDS.get(article_type, [])
    required += TYPE_PEOPLE_FIELDS.get(article_type, [])
    required += TYPE_MEDIA_FIELDS.get(article_type, [])
    required += TYPE_RELATION_FIELDS.get(article_type, [])
    required += TYPE_CULTURE_FIELDS.get(article_type, [])
    required += TYPE_STATUS_FIELDS.get(article_type, [])
    return required


SCHEMAS: dict[str, SchemaRule] = {
    "person": SchemaRule(required=_type_required_fields("person")),
    "dynasty": SchemaRule(required=_type_required_fields("dynasty")),
    "polity": SchemaRule(required=_type_required_fields("polity")),
    "administrative_division": SchemaRule(required=_type_required_fields("administrative_division")),
    "artifact": SchemaRule(required=_type_required_fields("artifact")),
    "belief_regime": SchemaRule(required=_type_required_fields("belief_regime")),
    "book": SchemaRule(required=_type_required_fields("book")),
    "character": SchemaRule(required=_type_required_fields("character")),
    "currency": SchemaRule(required=_type_required_fields("currency")),
    "deity": SchemaRule(required=_type_required_fields("deity")),
    "event": SchemaRule(required=_type_required_fields("event")),
    "historical_period": SchemaRule(required=_type_required_fields("historical_period")),
    "historical_region": SchemaRule(required=_type_required_fields("historical_region")),
    "institution": SchemaRule(required=_type_required_fields("institution")),
    "law": SchemaRule(required=_type_required_fields("law")),
    "military_unit": SchemaRule(required=_type_required_fields("military_unit")),
    "ordinance": SchemaRule(required=_type_required_fields("ordinance")),
    "settlement": SchemaRule(required=_type_required_fields("settlement")),
    "species": SchemaRule(required=_type_required_fields("species")),
    "structure": SchemaRule(required=_type_required_fields("structure")),
    "technical_concept": SchemaRule(required=_type_required_fields("technical_concept")),
    "treaty": SchemaRule(required=_type_required_fields("treaty")),
}


def apply_name_mapping(frontmatter: dict[str, Any]) -> dict[str, Any]:
    if "name" not in frontmatter or frontmatter.get("name") in (None, ""):
        title = frontmatter.get("title")
        if isinstance(title, str) and title.strip():
            frontmatter["name"] = title.strip()
    return frontmatter


ALLOW_UNKNOWN_FIELDS = {
    "birth_date",
    "death_date",
    "preceded_by",
    "followed_by",
}


def validate_schema(article_type: str, frontmatter: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    rule = SCHEMAS.get(article_type)
    if not rule:
        return errors

    fm = apply_name_mapping(frontmatter)
    for field in rule.required:
        value = fm.get(field)
        if field in ALLOW_UNKNOWN_FIELDS:
            if value in (None, "", "unknown", "none"):
                continue
        if value in (None, ""):
            errors.append(f"Missing required field '{field}' for type '{article_type}'")

    if not rule.allow_unknown:
        for key in fm.keys():
            if key not in rule.required and key not in ("title", "type", "slug"):
                errors.append(f"Unknown field '{key}' for type '{article_type}'")

    return errors
