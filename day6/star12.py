with open("input", "r") as signal:
    markers = []
    for i, s in enumerate(signal.read()):
        try:
            markers = markers[markers.index(s) + 1:]
        except ValueError:
            pass

        markers.append(s)
        if len(markers) == 14:
            print(i + 1)
            break
