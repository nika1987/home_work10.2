import json


def load_candidates(filename):
    """
    функция,которая загрузит данные из файла
    """
    with open(filename, encoding= "utf-8") as file:
        return json.load(file)


def get_all(filename):
    """
    функция,которая покажет всех кандитатов
    """
    return load_candidates(filename)

def get_by_pk(pk):
    """
    функция,которая вернет кандита по pk
    """
    for candidate in load_candidates(filename="candidates.json"):
        if candidate["pk"] == pk:
            return candidate


def get_by_skill(skill_name):
    """
    функция,которая вернет кандиторов по навыку
    """
    skill = []
    for candidate in load_candidates(filename="candidates.json"):
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            skill.append(candidate)
    return skill






