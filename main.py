import cv2
import numpy as np


def extract_roll_no_region():
    # Read the images
    img = cv2.imread('omr.jpg')

    # Define the region of interest coordinates
    # These coordinates represent the first column of circles
    x = 30  # Approximate x-coordinate
    y = 140  # Approximate y-coordinate
    w = 130  # Approximate width
    h = 270  # Approximate height

    # Extract the region
    roi = img[y:y + h, x:x + w]

    # Save the extracted region
    cv2.imwrite('extracted_region.jpg', roi)

    return roi


def extract_registration_no_region():
    # Read the images
    img = cv2.imread('omr.jpg')

    # Coordinates for রেজিস্ট্রেশন নম্বর area
    x = 160  # Adjusted x-coordinate for registration area
    y = 140  # Y-coordinate
    w = 200  # Width to cover full registration number bubbles
    h = 270  # Height to cover all rows of bubbles

    # Extract the region
    roi = img[y:y + h, x:x + w]

    # Save the extracted region
    cv2.imwrite('registration_region.jpg', roi)

    return roi


def extract_subject_code_region():
    img = cv2.imread('omr.jpg')

    # Coordinates for বিষয় কোড area (rightmost column of bubbles)
    x = 360  # Adjusted for subject code area
    y = 140
    w = 80  # Narrower width for subject code
    h = 270

    roi = img[y:y + h, x:x + w]
    cv2.imwrite('subject_code_region.jpg', roi)

    return roi


def extract_class_region():
    img = cv2.imread('omr.jpg')

    x = 440  # Rightmost section
    y = 140
    w = 65  # Narrow width for class bubbles
    h = 270

    roi = img[y:y + h, x:x + w]
    cv2.imwrite('class_region.jpg', roi)

    return roi


def extract_mcq_grid():
    img = cv2.imread('omr.jpg')

    # Coordinates for MCQ answer grid area
    x = 30  # Left position
    y = 430  # Top position
    w = 410  # Width to cover all 30 questions
    h = 300  # Height to cover all rows

    roi = img[y:y + h, x:x + w]
    cv2.imwrite('mcq_grid.jpg', roi)

    return roi

def extract_mcq_grid_1():
    img = cv2.imread('omr.jpg')

    # Coordinates for MCQ answer grid area
    x = 30  # Left position
    y = 430  # Top position
    w = 140  # Width to cover all 30 questions
    h = 300  # Height to cover all rows

    roi = img[y:y + h, x:x + w]
    cv2.imwrite('mcq_grid_1.jpg', roi)

    return roi

def extract_mcq_grid_2():
    img = cv2.imread('omr.jpg')

    # Coordinates for MCQ answer grid area
    x = 165  # Left position
    y = 430  # Top position
    w = 140  # Width to cover all 30 questions
    h = 300  # Height to cover all rows

    roi = img[y:y + h, x:x + w]
    cv2.imwrite('mcq_grid_2.jpg', roi)

    return roi

def extract_mcq_grid_3():
    img = cv2.imread('omr.jpg')

    # Coordinates for MCQ answer grid area
    x = 295  # Left position
    y = 430  # Top position
    w = 140  # Width to cover all 30 questions
    h = 300  # Height to cover all rows

    roi = img[y:y + h, x:x + w]
    cv2.imwrite('mcq_grid_3.jpg', roi)

    return roi

if __name__ == "__main__":
    extracted_region = extract_mcq_grid_3()