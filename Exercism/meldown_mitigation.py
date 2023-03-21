def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and 500 < neutrons_emitted and (temperature * neutrons_emitted) < 500_000


def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = voltage * current
    print(efficiency)
    efficiency = efficiency / theoretical_max_power
    print(efficiency)
    efficiency = efficiency * 100
    print(efficiency)
    # efficiency = ((voltage * current) / theoretical_max_power) * 100
    print(efficiency)
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if (temperature * neutrons_produced_per_second) < (threshold * 0.9):
        return "LOW"
    elif (threshold * 0.9) <= (temperature * neutrons_produced_per_second) <= (threshold * 1.1):

        return "NORMAL"
    else:
        return "DANGER"

