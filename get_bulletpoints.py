def get_bulletpoints(file_name):
    """ get bulletpoints from file"""
    bulletpoints = []
    with open(file_name, "r") as file:
        data = file.read()
        paragraphs = data.split("SPLIT_HERE")
        [bulletpoints.append(p) for p in paragraphs]
    return bulletpoints

