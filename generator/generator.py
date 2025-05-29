import math
import json

# Edit this variable to change the sword length!
SWORD_LENGTH = 2048

ONE_PLUS_SQRT_2 = 2.41421356237


def calculate_pivot(offset):
    return -ONE_PLUS_SQRT_2 * offset


def make_tip(offset):
    return {
        "name": "tip",
        "from": [10, 0, 5],
        "to": [13.53553, 0, 12.07107],
        "rotation": {"angle": 0, "axis": "y", "origin": [10 + calculate_pivot(offset), 4, 5  + calculate_pivot(offset)], "rescale": True},
        "faces": {
            "up": {"uv": [16, 0, 11, 10], "rotation": 180, "texture": "#sword"},
            "down": {"uv": [11, 0, 16, 10], "texture": "#sword"}
        }
    }


def make_segment(offset):
    return {
        "name": f"segment.{offset}",
        "from": [10, 0, 6],
        "to": [10.70711, 0, 13.07107],
        "rotation": {"angle": 0, "axis": "y", "origin": [10 + calculate_pivot(offset), 4, 6 + calculate_pivot(offset)], "rescale": True},
        "faces": {
            "up": {"uv": [11, 0, 10, 10], "rotation": 180, "texture": "#sword"},
            "down": {"uv": [10, 0, 11, 10], "texture": "#sword"}
        }
    }


def main():
    with open('sword_base.json') as f:
        model = json.load(f)

    for offset in range(SWORD_LENGTH):
        model['elements'].append(make_segment(offset))
    model['elements'].append(make_tip(SWORD_LENGTH))

    with open('../Swooooooords/assets/minecraft/models/item/sword.json', 'w+') as f:
        json.dump(model, f)


if __name__ == "__main__":
    main()
