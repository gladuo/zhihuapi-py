from .. import urls


def answers(data):
    paging = data['paging']
    answer_list = data['data']
    for obj in answer_list:
        question = obj['question']
        author = obj['author']
        obj['url'] = urls.answer(question['id'], obj['id'])
        question['url'] = urls.question(question['id'])
        author['url'] = urls.user(author['url_token'], author['user_type'])
    return data


def detail(data):
    data['url'] = urls.question(data['id'])
    return data


def followers(data):
    data = data['data']
    for obj in data:
        obj['url'] = urls.user(obj['url_token'], obj['user_type'])
    return data
