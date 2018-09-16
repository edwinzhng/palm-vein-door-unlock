from processing import process_image

labels = ["ibrahim", "jason", "jun", "justin", "nick", "samir", "thomas", "will"]

for label in labels:     
    for i in range(5):
        file_name = label + "_left_" + str(i) + ".jpg"
        print file_name
        processImage("data/raw/" + file_name, "data/processed/" + file_name)

    for i in range(5):
        file_name = label + "_right_" + str(i) + ".jpg"
        print file_name
        processImage("data/raw/" + file_name, "data/processed/" + file_name)