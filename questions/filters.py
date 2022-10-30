def set_if_not_none(mapping: dict, key: str, value: str, new_key: str):
    if key:
        mapping[new_key] = value


def filter_questions(qs: "Queryset", filter_query: dict = None) -> "Queryset":

    if filter_query is None:
        return qs

    # Convert query parameters to ORM filters
    name_mapping = {
        "questioner__id": "questioner_id",
        "question_title": "question_title",
        "question": "question",
        "start_date": "created_at__gte",
        "end_date": "created_at__lte",
    }

    filter_query_dict = {}
    for key, value in filter_query.items():
        new_key = name_mapping.get(key)
        if new_key is None:
            continue
        set_if_not_none(filter_query_dict, key, value, new_key)

    return qs.filter(**filter_query_dict)


def convert_query_params_to_dict(query_params: dict) -> dict:

    new_dict = {}
    for key in query_params.keys():
        if "uuid" in key:
            new_dict[key] = query_params.getlist(key)
        else:
            new_dict[key] = query_params.get(key)
    return new_dict
