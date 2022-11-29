def get_student_with_more_classes(student_a, student_b):
    a_class_count = student_a.get_num_classes()
    b_class_count = student_b.get_num_classes()
    return student_a if a_class_count >= b_class_count else student_b