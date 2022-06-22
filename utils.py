import json


def load_candidates_from_json() -> list[dict]:
    """Возвращает список всех кандидатов"""
    with open("candidates.json", "r", encoding='utf-8') as file:
        return json.load(file)

#print(load_candidates_from_json())


def get_candidates(candidate_id: int) -> dict:
    """Возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate
#print(get_candidates(3))


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """Возвращает кандидатов по имени"""
    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result

#print(get_candidates_by_name('Adela Hendricks'))



def get_candidates_by_skill(skill_name: str) ->list[dict]:
    """Возвращает кандидатов по навыку"""
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

#print(get_candidates_by_skill('python'))


