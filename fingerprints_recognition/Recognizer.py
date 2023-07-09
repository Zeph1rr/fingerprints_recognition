import os
import fingerprint_enhancer
import cv2


class FingerprintsRecognizer:
    def __init__(self, data_path: str = "data"):
        self.data_path = data_path
        if not os.path.exists(data_path):
            os.makedirs(data_path)

    def compare_fingerprints(self, fingerprints_image, fingerprint_database_image):
        fingerprints_image = fingerprint_enhancer.enhance_Fingerprint(cv2.imread(fingerprints_image))
        fingerprint_database_image = fingerprint_enhancer.enhance_Fingerprint(
                cv2.imread(fingerprint_database_image)
            )

        sift = cv2.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(fingerprints_image, None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

        matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), 
                dict()).knnMatch(descriptors_1, descriptors_2, k=2)
        match_points = []
    
        for p, q in matches:
            if p.distance < 0.1*q.distance:
                match_points.append(p)

        keypoints = 0
        if len(keypoints_1) <= len(keypoints_2):
            keypoints = len(keypoints_1)            
        else:
            keypoints = len(keypoints_2)
        
        print("% match: ", len(match_points) / keypoints * 100)

        if (len(match_points) / keypoints)>0.95:
            return True


    def find_in_files(self, fingerprint,  files: list = None):
        if not files:
            files = [os.path.join(self.data_path, path) for path in os.listdir(self.data_path)]
        for file in files:
            if self.compare_fingerprints(fingerprint, file):
                return file
            