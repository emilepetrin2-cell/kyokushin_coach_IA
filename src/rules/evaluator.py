config_posture = {
    "kumite":{
        "garde": {"min":75, "max":115},
    }
}

def evaluer_angle(angle, posture="kumite", body_part="garde"):
    requirement = config_posture[posture][body_part]
    if requirement["min"] <= angle <= requirement["max"]:
        return "GARDE OK", (0, 255, 0)
    elif angle > requirement["max"]:
        return "GARDE TROP OUVERTE", (0, 0, 255)
    else:
        return "GARDE TROP FERMEE", (0, 0, 255)
