from .Recognizer import FingerprintsRecognizer

def main():
    recognizer = FingerprintsRecognizer()
    fingerprint_image_1 = r"data/101_1.tif"
    fingerprint_image_2 = r"data/101_2.tif"
    print(recognizer.compare_fingerprints(fingerprint_image_1, fingerprint_image_2))
    print(recognizer.find_in_files(fingerprint_image_2))


if __name__ == "__main__":
    main()