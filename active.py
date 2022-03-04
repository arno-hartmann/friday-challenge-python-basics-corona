
def get_active(data):
    active = data[-1]['Active'] - data[-8]['Active']
    print(active)
    return active